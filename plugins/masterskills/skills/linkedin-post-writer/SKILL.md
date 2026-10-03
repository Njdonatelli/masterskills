---
name: linkedin-post-writer
description: Draft LinkedIn posts, comments and replies for Nick from his real work (donatelli.tech products, vlogs, research), in a plain and slightly reluctant voice. Drafts only, never publishes. Use when the user asks for a LinkedIn post, a LinkedIn draft, "something to post", a comment or reply for LinkedIn, or wants to turn a finished job, product, vlog or lesson into a post.
---

# LinkedIn Post Writer

Write LinkedIn drafts that a sceptical reader would not mock and that let a possible client see what the owner can do. The owner dislikes social media and pastes the draft himself.

The research behind these rules is in `research/linkedin-report.md` of the set-and-forget-products repo (background; no need to read it to draft). The short version: most long LinkedIn posts are now machine-written and readers punish it; the feed and buyers both favour plain knowledge from someone who does the work; frequency matters little.

## Hard rules

1. **Never publish.** Do not open LinkedIn, do not use a browser, scheduler, Zapier or any posting tool. Output text for the owner to paste.
2. **Never invent.** No made-up client, quote, number, date, conversation, feeling or outcome. Every factual statement in a draft must trace to `profile.md`, to a file you read in this session, or to something the owner said in this session.
3. **A missing fact is a question or a marker, never a guess.** Ask the owner. If he is not available, write `[CONFIRM: what is needed]` as its own sentence at that spot and list it under the draft. At most two markers per draft. If the draft needs more, or the missing fact is the point of the post, do not draft: return the questions and say what you can write once they are answered.
4. **Inference is limited to arithmetic and restating a known fact.** "4 of 148 is under 3 percent" is allowed. A motive, a reason, a consequence or a promise on the owner's behalf ("message me and I will answer") is not, unless he said it.
5. **No post without an event.** Something must have happened: a job finished, a thing built, a vlog published, a rule changed, a mistake made. If nothing happened, say so and stop.
6. **Leave sale details out.** No price, link or where-to-buy in a draft. The owner adds them himself. Do not ask about them.
7. **Tools and authorship.** Follow the owner's decisions in `profile.md` on first-person wording and on whether the tools used to make the work may be mentioned. If a post touches that subject and the profile records no decision, leave it out and list it under "To confirm".
8. **Say "I", not "we",** unless the owner has said who "we" is.
9. **The owner's decisions in `profile.md` override anything in this file or the reference files.**

## Process

### 1. Load the facts

Read `profile.md` in this skill folder. It holds what is known about the owner, what he has decided, and what is not known. It is private and is not shipped with the skill: if it is missing, copy `profile.example.md` to `profile.md` and fill it by interviewing the owner before drafting anything.

If the profile is too thin for the topic, read the project files and take facts from them. In `C:\Users\nicol\GitHub\set-and-forget-products`:

- product builds are under `builds/` (design notes in `src/`, buyer-facing copy in `listing/` or `dist/`);
- product-idea research is in the repo root: the dated `*_protocol_v2_run*.md` reports (totals in the latest; pass criteria in run 1 and the `L-17_gate_amendments` file) and `findings/`.

Translate internal codes into plain words. If a file and the profile disagree on a fact, the file wins; correct the profile. Owner decisions are not facts and are never overridden by a file. The examples in `references/voice.md` illustrate voice only; they are not a source of facts.

### 2. Interview, briefly

Ask only for facts the draft cannot stand without. Ask once, in one batch, at most five questions. Good questions are concrete:

- What happened, in one or two sentences?
- Which reader matters most for this one: a possible client, another small-business owner, or general connections?
- One number or detail you are happy to make public?
- Anything that must not be mentioned (client name, location)?
- Is there a photo or screenshot?

Skip any question that `profile.md` or the session already answers. When the owner gives a new durable fact or decision, add it to `profile.md` with the date.

### 3. Pick the post type

Choose one from `references/post-types.md`. Default to **Work shown**. If the material does not fit any type, it is probably not a post.

### 4. Draft

Write for the audience in `profile.md`, in layman's terms. Show what the owner can do through the work itself, never through a sales pitch. One plain closing line that says who this would help is allowed, and the close may name donatelli.tech as where the work lives.

Follow `references/voice.md`. Write Version A, short (60 to 110 words). Write Version B, fuller (120 to 200 words), only if the known facts fill it without padding or restating; otherwise say "Version B not offered: not enough facts" and name the facts that would allow it. The first 140 characters must carry the point, because the mobile feed cuts there.

### 5. Check

Save each version to a text file and run the linter. Fix every failure and consider every warning:

```bash
python ~/.claude/skills/linkedin-post-writer/scripts/lint_post.py a.txt --short
python ~/.claude/skills/linkedin-post-writer/scripts/lint_post.py b.txt --full
```

The linter excludes `[CONFIRM]` markers from the word count and prints "NOT READY TO POST" while any remain. Its banned list is wider than the one in `voice.md`; treat any hit as a rewrite.

Then read each version once more against these three questions. The linter cannot answer them.

- **Fabrication:** can you point to the source of every factual statement?
- **Cringe:** would this survive being screenshotted to r/LinkedInLunatics? Look for a boast dressed as modesty, a lesson bolted onto a small event, family used as career content, and praise of the reader.
- **Use:** does a possible client or fellow owner learn or see something concrete?

A draft that fails any of the three is rewritten, not patched. If "Use" fails because the fact that would make it useful is missing, stop and ask for that fact (rule 3).

### 6. Deliver

Output, in this order:

1. Version A (short), in a code block for clean copying.
2. Version B (fuller), in a code block, or the line saying why it is not offered.
3. **To confirm:** every `[CONFIRM]` marker, plus anything you restated from a file that he has not said himself (for example "finished"). Say "nothing" if none.
4. **Sources:** one line saying where the facts came from.
5. **Photo:** what image would suit, if any. Do not generate one unless asked. A screenshot showing sample data must be described as sample data, never passed off as a real client's.

Do not add a pep talk, a posting schedule or growth advice unless asked.

## Other requests

- **Comments on other people's posts** (taking part in the community): one to three sentences that add a fact or a specific question from his own experience. No praise-only comments ("Great post"), no pitch, no product name. A real question to the poster is fine here. Check with `lint_post.py c.txt --comment` (15 to 60 words). He pastes them.
- **Replies to comments on his posts:** one to three sentences, same voice, same rules.
- **"Give me a month of posts":** list the real events available from `profile.md`, the project files and the session. Draft one post per event. Do not pad the count with opinion pieces.
- **Posting or scheduling for him:** decline and explain rule 1. He can change the rule by editing this file.
