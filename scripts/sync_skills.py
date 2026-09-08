#!/usr/bin/env python3
"""Move skills between this repo and the local ~/.claude/skills directory.

    python scripts/sync_skills.py pull    # ~/.claude/skills  ->  repo   (authoring machine)
    python scripts/sync_skills.py push    # repo  ->  ~/.claude/skills   (bypasses the marketplace)
    python scripts/sync_skills.py status  # report differences, change nothing

`pull` is the normal direction: you edit skills where Claude Code already loads
them, then bring the result into the repo. `push` exists for testing an unreleased
skill locally; the supported install path for other machines is the marketplace.

Add --apply to actually write. Without it, every mode is a dry run.
"""
from __future__ import annotations

import argparse
import filecmp
import shutil
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REPO_SKILLS = ROOT / "plugins" / "masterskills" / "skills"
LOCAL_SKILLS = Path.home() / ".claude" / "skills"


def names(directory: Path) -> set[str]:
    if not directory.is_dir():
        return set()
    return {p.name for p in directory.iterdir() if p.is_dir() and (p / "SKILL.md").is_file()}


def differs(a: Path, b: Path) -> bool:
    comparison = filecmp.dircmp(a, b)
    if comparison.left_only or comparison.right_only or comparison.diff_files:
        return True
    return any(differs(a / sub, b / sub) for sub in comparison.common_dirs)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=["pull", "push", "status"])
    parser.add_argument("--apply", action="store_true", help="write changes instead of dry-running")
    parser.add_argument(
        "--prune",
        action="store_true",
        help="also delete skills at the destination that no longer exist at the source",
    )
    args = parser.parse_args()

    source, dest = (LOCAL_SKILLS, REPO_SKILLS) if args.mode != "push" else (REPO_SKILLS, LOCAL_SKILLS)
    if not source.is_dir():
        print(f"source does not exist: {source}")
        return 1

    src_names, dst_names = names(source), names(dest)
    added = sorted(src_names - dst_names)
    removed = sorted(dst_names - src_names)
    changed = sorted(n for n in src_names & dst_names if differs(source / n, dest / n))

    print(f"source      {source}")
    print(f"destination {dest}")
    for label, items in (("new", added), ("changed", changed), ("only at destination", removed)):
        print(f"  {label}: {len(items)}")
        for name in items:
            print(f"    {name}")

    if args.mode == "status":
        return 0
    if not (added or changed or (removed and args.prune)):
        print("\nnothing to do")
        return 0
    if not args.apply:
        print("\ndry run - re-run with --apply to write")
        return 0

    dest.mkdir(parents=True, exist_ok=True)
    for name in added + changed:
        target = dest / name
        if target.exists():
            shutil.rmtree(target)
        shutil.copytree(source / name, target)
    if args.prune:
        for name in removed:
            shutil.rmtree(dest / name)

    print(f"\napplied: {len(added)} new, {len(changed)} updated, "
          f"{len(removed) if args.prune else 0} removed")
    if args.mode == "pull":
        print("next: python scripts/build_manifest.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
