#!/usr/bin/env python3
"""Install every third-party plugin recorded in plugins.lock.json on this machine.

    python scripts/install_plugins.py            # add marketplaces + install plugins
    python scripts/install_plugins.py --dry-run  # print the commands only

Uses the `claude` CLI. Already-known marketplaces and already-installed plugins
are skipped by the CLI itself, so re-running is safe.
"""
from __future__ import annotations

import argparse
import json
import shutil
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOCK = ROOT / "plugins.lock.json"


def run(cmd: list[str], dry: bool) -> None:
    print("$", " ".join(cmd))
    if dry:
        return
    result = subprocess.run(cmd)
    if result.returncode:
        print(f"  -> exit {result.returncode} (continuing)")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if not LOCK.is_file():
        print(f"missing {LOCK}")
        return 1
    claude = shutil.which("claude")
    if not claude and not args.dry_run:
        print("`claude` CLI not found on PATH")
        return 1
    claude = claude or "claude"

    data = json.loads(LOCK.read_text("utf-8"))
    for name, source in data["marketplaces"].items():
        run([claude, "plugin", "marketplace", "add", source], args.dry_run)
    for plugin in data["plugins"]:
        run([claude, "plugin", "install", f"{plugin['name']}@{plugin['marketplace']}"], args.dry_run)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
