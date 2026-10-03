#!/usr/bin/env python3
"""Mechanical checks for a LinkedIn draft. Usage: lint_post.py FILE --short|--full|--comment  (or - for stdin)

Exit 0 = no failures. Warnings do not change the exit code.
The linter cannot judge fabrication or tone; SKILL.md step 5 covers those.
"""
import re
import sys

BANNED = [
    r"\bhumbled\b", r"\bhonou?red\b", r"\bblessed\b", r"\bthrilled\b", r"\bexcited to\b",
    r"\bproud to\b", r"\bgrateful to announce\b", r"\bdelighted to\b",
    r"here'?s what i learned", r"\bthe lesson\?", r"let that sink in", r"read that again",
    r"\bagree\?", r"\bthoughts\?", r"what do you think\?", r"comment below", r"repost if",
    r"\bgame[- ]changer\b", r"\bjourney\b", r"\bpassion(ate)?\b", r"\bhustle\b", r"\bgrind\b",
    r"\bmindset\b", r"\bunlock\w*\b", r"\bleverag\w+\b", r"\belevat\w+\b", r"\bempower\w*\b",
    r"\bsynerg\w+\b", r"thought leader", r"deep dive", r"level up", r"\b10x\b", r"crushing it",
    r"in today'?s world", r"let'?s be honest", r"here'?s the thing", r"i'?ll be honest",
    r"\bnot just\b", r"isn'?t (just|about)\b", r"\bseamless\w*\b", r"\brobust\b", r"\bdelve\b",
    r"\btestament\b", r"\blandscape of\b", r"\bexcited\b",
]
CONTRAST = re.compile(r"\b(it'?s|this is|that'?s) not [^.?!\n]{1,60}[.;,]\s*(it'?s|this is|that'?s)\b", re.I)
EMOJI = re.compile("[\U0001F000-\U0001FAFF☀-➿⬀-⯿️]")
FANCY = re.compile("[\U0001D400-\U0001D7FF]")


def lint(text, mode=None):
    fails, warns = [], []
    body = text.strip()
    confirms = re.findall(r"\[CONFIRM:[^\]]*\]", body)
    # markers are not post text: count and check without them
    body = re.sub(r"\s*\[CONFIRM:[^\]]*\]", "", body).strip()
    words = len(re.findall(r"\b[\w'’-]+\b", body))
    low = body.lower().replace("’", "'")

    if mode == "comment":
        if not 15 <= words <= 60:
            fails.append(f"length {words} words; comment needs 15-60")
    elif mode == "short" and not 60 <= words <= 110:
        fails.append(f"length {words} words; short version needs 60-110")
    elif mode == "full" and not 120 <= words <= 200:
        fails.append(f"length {words} words; full version needs 120-200")
    elif mode is None and not 60 <= words <= 200:
        fails.append(f"length {words} words; needs 60-200")
    if len(body) > 3000:
        fails.append("over LinkedIn's 3,000-character cap")

    for pat in BANNED:
        m = re.search(pat, low)
        if m:
            fails.append(f"banned phrase: '{m.group(0)}'")
    if CONTRAST.search(low):
        fails.append("contrast formula (it's not X, it's Y)")
    if EMOJI.search(body):
        fails.append("emoji present")
    if FANCY.search(body):
        fails.append("Unicode lookalike bold/italic letters")
    if "—" in body or " – " in body or " -- " in body:
        fails.append("em dash")
    if "!" in body:
        fails.append("exclamation mark")
    tags = re.findall(r"(?<!\w)#\w+", body)
    if len(tags) > 2:
        fails.append(f"{len(tags)} hashtags; at most 2, default none")
    elif tags:
        warns.append(f"hashtags present ({', '.join(tags)}); only if the owner asked")
    links = re.findall(r"https?://\S+", body)
    if links:
        fails.append("link present; the owner adds links himself")
    if mode != "comment" and body.rstrip().endswith("?"):
        fails.append("ends with a question to the audience")

    paras = [p for p in re.split(r"\n\s*\n", body) if p.strip()]
    if mode != "comment" and len(paras) < 2:
        fails.append("single block; needs 2 to 5 paragraphs")
    if len(paras) > 5:
        fails.append(f"{len(paras)} paragraphs; at most 5")
    non_list = [p for p in paras if not p.lstrip().startswith("-")]
    one_liners = [p for p in non_list if len(re.findall(r"[.?!](\s|$)", p)) <= 1 and len(p.split()) < 14]
    if len(non_list) >= 3 and len(one_liners) > len(non_list) / 2:
        fails.append("one-line-per-paragraph staircase")
    items = [l for l in body.splitlines() if l.lstrip().startswith("-")]
    if len(items) > 5:
        fails.append("list longer than 5 items")

    first = body[:140]
    if re.match(r"\s*(i'?m|i am|so|well|ever|what if|did you|have you)\b", first.lower()):
        warns.append("opening looks like a teaser or throat-clearing; open with the fact")
    if mode != "comment" and "?" in first:
        warns.append("question inside the first 140 characters")
    if len(confirms) > 2:
        fails.append(f"{len(confirms)} [CONFIRM] markers; more than 2 means stop and ask the owner")
    for c in confirms:
        warns.append(f"unresolved {c}")
    if re.search(r"\b(ai|a\.i\.|chatgpt|claude|llm|artificial intelligence)\b", low):
        warns.append("AI mentioned; check the owner's decisions in profile.md")
    jargon = re.findall(r"\b(WH-347|eCPR|XML|DIR|schema|API|CSV|SaaS|KPI|ROI)\b", body)
    if jargon:
        warns.append(f"jargon for a general reader: {sorted(set(jargon))}; say it in plain words")
    if re.search(r"\b(tested|verified|reviewed|validated) by\b", low):
        warns.append("testing/review claim; profile.md forbids third-party testing claims")

    return words, fails, warns, first, len(confirms)


def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    mode = next((m for m in ("short", "full", "comment") if "--" + m in sys.argv), None)
    if not args:
        print(__doc__)
        return 2
    text = sys.stdin.read() if args[0] == "-" else open(args[0], encoding="utf-8").read()
    words, fails, warns, first, n_confirm = lint(text, mode)
    print(f"words (markers excluded): {words}")
    print(f"first 140 chars: {first!r}")
    for f in fails:
        print(f"FAIL  {f}")
    for w in warns:
        print(f"warn  {w}")
    print("RESULT:", "FAIL" if fails else "PASS, NOT READY TO POST (markers open)" if n_confirm else "PASS")
    if not fails:
        print("note: settle any To confirm items before pasting")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.stdout.reconfigure(encoding="utf-8")
    sys.exit(main())
