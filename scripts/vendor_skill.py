#!/usr/bin/env python3
"""Vendor a skill from a public git repo into plugins/masterskills/skills/.

    python scripts/vendor_skill.py --repo owner/name --path skills/foo [--path skills/bar ...]
                                   [--ref main] [--name newname] [--force]

For every --path the skill directory is copied verbatim, any nested .git is
stripped, the repo-level LICENSE is copied in when the skill folder has none,
and a SOURCE.json is written next to SKILL.md recording where it came from:

    {"repo": "https://github.com/owner/name", "ref": "main", "commit": "<sha>",
     "path": "skills/foo", "license": "MIT", "vendored_at": "2026-09-21",
     "upstream_name": "foo"}

Clones are shallow, blobless and sparse, cached under --cache (default: the
system temp dir) so vendoring many skills from one repo costs one clone.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILLS = ROOT / "plugins" / "masterskills" / "skills"
LICENSE_NAMES = ("LICENSE", "LICENSE.md", "LICENSE.txt", "LICENCE", "LICENCE.md", "COPYING", "LICENSE-MIT", "LICENSE.MIT")
NAME_RE = re.compile(r"^[a-z0-9][a-z0-9-]{0,63}$")


def run(*cmd: str, cwd: Path | None = None) -> str:
    return subprocess.run(cmd, cwd=cwd, check=True, capture_output=True, text=True, encoding="utf-8", errors="replace").stdout.strip()


def clone(repo: str, ref: str | None, cache: Path) -> Path:
    url = repo if repo.startswith(("http://", "https://", "git@")) else f"https://github.com/{repo}"
    slug = re.sub(r"[^A-Za-z0-9_.-]+", "_", repo)
    dest = cache / slug
    if not (dest / ".git").is_dir():
        cmd = ["git", "clone", "--depth", "1", "--filter=blob:none", "--sparse", "--no-checkout"]
        if ref:
            cmd += ["--branch", ref]
        run(*cmd, url, str(dest))
        # skill trees nest deeply; without this Windows refuses paths over 260 chars
        run("git", "config", "core.longpaths", "true", cwd=dest)
    lock = dest / ".git" / "index.lock"
    if lock.exists():  # left behind by an earlier failed checkout; runs are sequential
        lock.unlink()
    return dest


def checkout(repo_dir: Path, paths: list[str]) -> None:
    run("git", "sparse-checkout", "set", "--no-cone", *paths, *[f"/{n}" for n in LICENSE_NAMES], cwd=repo_dir)
    run("git", "checkout", cwd=repo_dir)


def detect_license(repo_dir: Path, skill_dir: Path) -> tuple[str, Path | None]:
    for base in (skill_dir, repo_dir):
        for name in LICENSE_NAMES:
            candidate = base / name
            if candidate.is_file():
                return spdx_guess(candidate.read_text(encoding="utf-8", errors="replace")), candidate
    return "NONE", None


def spdx_guess(text: str) -> str:
    head = text[:2000]
    if "MIT License" in head or "Permission is hereby granted, free of charge" in head:
        return "MIT"
    if "Apache License" in head:
        return "Apache-2.0"
    if "GNU GENERAL PUBLIC LICENSE" in head:
        return "GPL-3.0" if "Version 3" in head else "GPL-2.0"
    if "GNU AFFERO" in head:
        return "AGPL-3.0"
    if "GNU LESSER" in head:
        return "LGPL-3.0"
    if "Mozilla Public License" in head:
        return "MPL-2.0"
    if "BSD" in head and "Redistribution and use" in head:
        return "BSD-3-Clause" if "Neither the name" in head else "BSD-2-Clause"
    if "Creative Commons" in head or "CC BY" in head:
        return "CC-BY-4.0"
    if "This is free and unencumbered software" in head:
        return "Unlicense"
    if "ISC License" in head:
        return "ISC"
    return "UNKNOWN"


def frontmatter_name(skill_md: Path) -> str | None:
    text = skill_md.read_text(encoding="utf-8", errors="replace")
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    match = re.search(r"^name:\s*[\"']?([^\"'\n]+)[\"']?\s*$", text[3:end], re.M)
    return match.group(1).strip() if match else None


def set_frontmatter_name(skill_md: Path, name: str) -> None:
    text = skill_md.read_text(encoding="utf-8", errors="replace")
    end = text.find("\n---", 3)
    head, tail = text[: end + 4], text[end + 4 :]
    head = re.sub(r"^name:.*$", f"name: {name}", head, count=1, flags=re.M)
    skill_md.write_text(head + tail, encoding="utf-8", newline="")


def vendor(repo: str, ref: str | None, path: str, name: str | None, cache: Path, force: bool) -> Path:
    path = "" if path in (".", "") else path
    repo_dir = clone(repo, ref, cache)
    checkout(repo_dir, [path or "/*"])
    src = repo_dir / path if path else repo_dir
    if not (src / "SKILL.md").is_file():
        raise SystemExit(f"{repo}:{path} has no SKILL.md")
    commit = run("git", "rev-parse", "HEAD", cwd=repo_dir)
    branch = ref or run("git", "rev-parse", "--abbrev-ref", "HEAD", cwd=repo_dir)

    upstream_name = frontmatter_name(src / "SKILL.md") or src.name
    target_name = name or upstream_name
    if not NAME_RE.match(target_name):
        raise SystemExit(f"'{target_name}' is not a valid skill name (lowercase, digits, hyphens, <=64)")
    dest = SKILLS / target_name
    if dest.exists():
        if not force:
            raise SystemExit(f"{dest} already exists (use --force to replace)")
        shutil.rmtree(dest)

    shutil.copytree(src, dest, ignore=shutil.ignore_patterns(".git"))
    for nested in dest.rglob(".git"):
        shutil.rmtree(nested) if nested.is_dir() else nested.unlink()

    license_id, license_file = detect_license(repo_dir, src)
    if license_file and license_file.parent == repo_dir and not any((dest / n).exists() for n in LICENSE_NAMES):
        shutil.copy2(license_file, dest / "LICENSE")

    if frontmatter_name(dest / "SKILL.md") != target_name:
        set_frontmatter_name(dest / "SKILL.md", target_name)

    url = repo if repo.startswith("http") else f"https://github.com/{repo}"
    source = {
        "repo": url,
        "ref": branch,
        "commit": commit,
        "path": path,
        "license": license_id,
        "vendored_at": dt.date.today().isoformat(),
        "upstream_name": upstream_name,
        "tool": "scripts/vendor_skill.py",
    }
    (dest / "SOURCE.json").write_text(json.dumps(source, indent=2) + "\n", encoding="utf-8", newline="\n")
    return dest


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--repo", required=True, help="owner/name or full git URL")
    parser.add_argument("--path", action="append", required=True, help="skill directory inside the repo (repeatable)")
    parser.add_argument("--ref", help="branch or tag (default: repo default branch)")
    parser.add_argument("--name", help="destination skill name (single --path only)")
    parser.add_argument("--force", action="store_true", help="replace an existing destination")
    parser.add_argument("--cache", type=Path, default=Path(tempfile.gettempdir()) / "masterskills-vendor", help="clone cache directory")
    args = parser.parse_args()
    if args.name and len(args.path) > 1:
        parser.error("--name only works with a single --path")
    args.cache.mkdir(parents=True, exist_ok=True)
    for path in args.path:
        dest = vendor(args.repo, args.ref, path.strip("/"), args.name, args.cache, args.force)  # "." = repo root
        print(f"vendored {args.repo}:{path} -> {dest.relative_to(ROOT)}")
    print("next: python scripts/build_manifest.py && python scripts/check_skills.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
