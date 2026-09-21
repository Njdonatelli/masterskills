#!/usr/bin/env python3
"""Lint every skill: frontmatter, referenced files, provenance.

    python scripts/check_skills.py                # all skills, offline checks
    python scripts/check_skills.py --network      # also verify SOURCE.json against GitHub via gh
    python scripts/check_skills.py --only a b c   # subset
    python scripts/check_skills.py --json out.json

Checks
  frontmatter  SKILL.md starts with a YAML block that PyYAML parses, has non-empty
               `name` and `description`, `name` equals the directory name and is a
               valid skill name (lowercase letters, digits, hyphens, <= 64 chars).
  references   every relative path mentioned in SKILL.md that points into a skill
               sub-directory (references/, scripts/, assets/, ...) exists on disk.
  source       SOURCE.json (when present) is valid, and with --network the commit
               and path resolve on GitHub. Its optional "lint_ignore" list names
               path-like mentions that are sample output rather than references.
  injection    crude scan for prompt-injection / exfiltration phrases; warnings only.

Exit status is 1 when any skill has an error.
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "plugins" / "masterskills" / "skills"
NAME_RE = re.compile(r"^[a-z0-9][a-z0-9-]{0,63}$")
SUBDIRS = (
    "references", "reference", "scripts", "assets", "templates", "examples", "resources",
    "checklists", "agents", "commands", "hooks", "prompts", "expected_outputs", "workflows",
    "rules", "guides", "playbooks", "frameworks", "knowledge",
)
PATH_RE = re.compile(
    r"(?<![\w/.:-])((?:\./)?(?:%s)/[\w./+@-]*\w\.[A-Za-z0-9]{1,6})(?![\w/])" % "|".join(SUBDIRS)
)
LINK_RE = re.compile(r"\]\(([^)\s#?]+)")
INJECTION = [
    r"ignore (all )?(previous|prior|above) instructions",
    r"disregard (all )?(previous|prior) instructions",
    r"you are now (in )?(developer|dan|jailbreak)",
    r"do not (tell|inform) the user",
    r"without (telling|informing|asking) the user",
    r"curl [^\n]*\|\s*(ba)?sh\b",
    r"wget [^\n]*\|\s*(ba)?sh\b",
    r"~/\.ssh|~/\.aws/credentials|id_rsa",
    r"(post|upload|send|exfiltrate)[^\n.]{0,60}(webhook\.site|pastebin|ngrok|requestbin)",
    "[​‌‍⁠﻿]",  # zero-width characters
]


def parse_frontmatter(text: str) -> tuple[dict | None, str | None]:
    if not text.startswith("---"):
        return None, "SKILL.md does not start with '---'"
    end = text.find("\n---", 3)
    if end == -1:
        return None, "frontmatter block is not closed"
    block = text[text.find("\n", 3) + 1 : end]
    try:
        data = yaml.safe_load(block)
    except yaml.YAMLError as exc:
        return None, f"frontmatter is not valid YAML: {str(exc).splitlines()[0]}"
    if not isinstance(data, dict):
        return None, "frontmatter is not a mapping"
    return data, None


def check_frontmatter(skill: Path, text: str, errors: list[str]) -> None:
    data, problem = parse_frontmatter(text)
    if problem:
        errors.append(problem)
        return
    name = data.get("name")
    description = data.get("description")
    if not isinstance(name, str) or not name.strip():
        errors.append("frontmatter has no name")
    else:
        if name != skill.name:
            errors.append(f"frontmatter name '{name}' != directory '{skill.name}'")
        if not NAME_RE.match(name):
            errors.append(f"name '{name}' is not lowercase-hyphen, <= 64 chars")
    if not isinstance(description, str) or not description.strip():
        errors.append("frontmatter has no description")
    elif len(description) > 1024:
        errors.append(f"description is {len(description)} chars (> 1024)")


def lint_ignores(skill: Path) -> set[str]:
    """Paths listed under "lint_ignore" in SOURCE.json: mentions the checker
    mistakes for references (sample output, paths relative to a sub-folder)."""
    source_file = skill / "SOURCE.json"
    if not source_file.is_file():
        return set()
    try:
        data = json.loads(source_file.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return set()
    return set(data.get("lint_ignore", []))


def check_references(skill: Path, text: str, errors: list[str], warnings: list[str]) -> None:
    ignored = lint_ignores(skill)
    candidates: set[str] = set()
    # markdown links inside fenced code are sample content, not references
    prose = re.sub(r"```.*?```", "", text, flags=re.S)
    for match in LINK_RE.finditer(prose):
        target = match.group(1)
        if re.match(r"^[a-z][a-z0-9+.-]*:", target) or target.startswith(("/", "#", "mailto:")):
            continue
        candidates.add(target)
    for match in PATH_RE.finditer(text):
        candidates.add(match.group(1))
    for raw in sorted(candidates):
        rel = raw.strip().strip("`'\"").rstrip("/.,;:")
        rel = re.sub(r"^\./", "", rel)
        if not rel or any(ch in rel for ch in "*{<$") or rel in ignored:
            continue
        if (skill / rel).exists():
            continue
        if (SKILLS / rel).exists():
            warnings.append(f"reference '{rel}' resolves only relative to the skills root")
            continue
        first = rel.split("/")[0]
        if first in SUBDIRS or "/" in rel:
            errors.append(f"missing referenced file: {rel}")
        else:
            warnings.append(f"unresolved relative link: {rel}")


def check_source(skill: Path, errors: list[str], warnings: list[str], network: bool) -> dict | None:
    source_file = skill / "SOURCE.json"
    if not source_file.is_file():
        return None
    try:
        source = json.loads(source_file.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        errors.append(f"SOURCE.json is not valid JSON: {exc}")
        return None
    missing = [key for key in ("repo", "commit") if not source.get(key)] + (["path"] if "path" not in source else [])
    for key in missing:
        errors.append(f"SOURCE.json missing '{key}'")
    if missing or not network:
        return source
    match = re.match(r"https://github\.com/([^/]+)/([^/]+?)(?:\.git)?/?$", source["repo"])
    if not match:
        warnings.append(f"SOURCE.json repo is not a github.com URL, skipping network check: {source['repo']}")
        return source
    owner, repo = match.groups()
    path = source["path"].strip("/")
    api = f"repos/{owner}/{repo}/contents/{path + '/' if path else ''}SKILL.md?ref={source['commit']}"
    result = subprocess.run(["gh", "api", api, "--jq", ".sha"], capture_output=True, text=True)
    if result.returncode != 0:
        detail = result.stderr.strip().splitlines()[-1] if result.stderr.strip() else "error"
        errors.append(f"SOURCE.json does not resolve on GitHub: {api} -> {detail}")
    return source


def check_injection(skill: Path, warnings: list[str]) -> None:
    for md in skill.rglob("*.md"):
        text = md.read_text(encoding="utf-8", errors="replace")
        for pattern in INJECTION:
            match = re.search(pattern, text, re.I)
            if match:
                line = text.count("\n", 0, match.start()) + 1
                snippet = text[max(0, match.start() - 30) : match.end() + 30].replace("\n", " ")
                warnings.append(f"injection pattern in {md.relative_to(skill)}:{line}: ...{snippet.strip()}...")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--network", action="store_true", help="verify SOURCE.json entries against GitHub with gh")
    parser.add_argument("--only", nargs="*", help="check only these skill names")
    parser.add_argument("--json", type=Path, help="write the full report here")
    parser.add_argument("--quiet", action="store_true", help="print only the summary and errors")
    args = parser.parse_args()

    report: dict[str, dict] = {}
    skills = sorted(p for p in SKILLS.iterdir() if p.is_dir())
    if args.only:
        wanted = set(args.only)
        skills = [p for p in skills if p.name in wanted]
    for skill in skills:
        errors: list[str] = []
        warnings: list[str] = []
        source = None
        skill_md = skill / "SKILL.md"
        if not skill_md.is_file():
            errors.append("no SKILL.md")
        else:
            text = skill_md.read_text(encoding="utf-8", errors="replace")
            check_frontmatter(skill, text, errors)
            check_references(skill, text, errors, warnings)
            check_injection(skill, warnings)
            source = check_source(skill, errors, warnings, args.network)
        report[skill.name] = {"errors": errors, "warnings": warnings, "source": source}

    bad = {k for k, v in report.items() if v["errors"]}
    warned = {k for k, v in report.items() if v["warnings"]}
    for name, entry in report.items():
        if entry["errors"] or (entry["warnings"] and not args.quiet):
            print(name)
            for err in entry["errors"]:
                print(f"  ERROR    {err}")
            if not args.quiet:
                for warn in entry["warnings"]:
                    print(f"  warning  {warn}")
    sourced = sum(1 for v in report.values() if v["source"])
    print(f"\n{len(report)} skills checked: {len(bad)} with errors, {len(warned)} with warnings, {sourced} with SOURCE.json")
    if args.json:
        args.json.write_text(json.dumps(report, indent=2), encoding="utf-8")
    return 1 if bad else 0


if __name__ == "__main__":
    raise SystemExit(main())
