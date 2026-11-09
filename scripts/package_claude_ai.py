#!/usr/bin/env python3
"""Build one upload-ready ZIP per skill for claude.ai (Customize > Skills > Upload).

Skills uploaded to a claude.ai account sync to the web, desktop, and mobile apps,
and to Claude Code (v2.1.273+). Run:  python scripts/package_claude_ai.py
Output: dist/claude-ai/<skill>.zip, each with one top-level <skill>/ folder.
"""
from __future__ import annotations

import sys
import zipfile
from pathlib import Path

from build_manifest import MAX_DESCRIPTION, ROOT, collect

SKILLS = ROOT / "plugins" / "masterskills"
OUT = ROOT / "dist" / "claude-ai"
MAX_FILES = 200  # claude.ai rejects a ZIP with more files
RESERVED = ("claude", "anthropic")  # not allowed in a skill name
# Not uploaded: claude.ai already has its own version under the same name.
SKIP = {
    "skill-creator": "Anthropic ships skill-creator on claude.ai",
    "job-application": "job-screen-mobile is the claude.ai version",
    "asd-ste100": "the account copy is the newer version",
    "brand-guidelines": "claude.ai reserves this name for a built-in skill",
    "deep-research": "claude.ai reserves this name for a built-in skill",
    "mcp-builder": "claude.ai reserves this name for a built-in skill",
}
EXCLUDE_NAMES = {"profile.md", ".DS_Store", "Thumbs.db"}  # profile.md holds private facts
EXCLUDE_DIRS = {"__pycache__", ".git", "node_modules"}


def files_of(skill_dir: Path) -> list[Path]:
    # claude.ai accepts exactly one SKILL.md per ZIP, so a nested sample skill
    # (a test fixture, such as skill-tester/assets/sample-skill) stays out.
    nested = [p.parent for p in skill_dir.rglob("SKILL.md") if p.parent != skill_dir]
    return sorted(
        p
        for p in skill_dir.rglob("*")
        if p.is_file()
        and p.name not in EXCLUDE_NAMES
        and not EXCLUDE_DIRS.intersection(p.relative_to(skill_dir).parts)
        and not any(p.is_relative_to(n) for n in nested)
    )


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    for old in OUT.glob("*.zip"):
        old.unlink()
    built, errors = 0, []
    for skill in collect(SKILLS):
        name = skill["name"]
        if name in SKIP:
            print(f"skip  {name}: {SKIP[name]}")
            continue
        files = files_of(SKILLS / "skills" / skill["dir"])
        if len(files) > MAX_FILES:
            errors.append(f"{name}: {len(files)} files (max {MAX_FILES})")
        if len(skill["description"]) > MAX_DESCRIPTION:
            errors.append(f"{name}: description over {MAX_DESCRIPTION} characters")
        if any(p.parts[-2] == ".claude-plugin" for p in files):
            errors.append(f"{name}: contains .claude-plugin/ (claude.ai rejects a plugin manifest in a skill)")
        if any(word in name for word in RESERVED):
            errors.append(f"{name}: name contains a reserved word {RESERVED}")
        if errors and errors[-1].startswith(f"{name}:"):
            continue
        with zipfile.ZipFile(OUT / f"{name}.zip", "w", zipfile.ZIP_DEFLATED) as zf:
            for f in files:
                zf.write(f, Path(name) / f.relative_to(SKILLS / "skills" / skill["dir"]))
        built += 1
    print(f"built {built} ZIPs in {OUT.relative_to(ROOT)}")
    for error in errors:
        print(f"  error: {error}", file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
