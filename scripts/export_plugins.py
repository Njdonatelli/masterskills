#!/usr/bin/env python3
"""Snapshot the third-party plugins installed on this machine into plugins.lock.json.

    python scripts/export_plugins.py          # write plugins.lock.json
    python scripts/export_plugins.py --check  # exit 1 if the lockfile is stale

Reads ~/.claude/plugins/installed_plugins.json and known_marketplaces.json. The
masterskills plugin itself is skipped - this repo *is* that plugin.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOCK = ROOT / "plugins.lock.json"
PLUGIN_DIR = Path.home() / ".claude" / "plugins"
SELF = "masterskills"


def marketplace_source(entry: dict) -> str:
    src = entry["source"]
    return src.get("repo") or src.get("url") or src.get("path") or ""


def snapshot() -> dict:
    installed = json.loads((PLUGIN_DIR / "installed_plugins.json").read_text("utf-8"))
    known = json.loads((PLUGIN_DIR / "known_marketplaces.json").read_text("utf-8"))

    marketplaces: dict[str, str] = {}
    plugins: list[dict] = []
    for key, entries in sorted(installed["plugins"].items()):
        name, _, market = key.partition("@")
        if market == SELF:
            continue
        info = entries[0]
        plugins.append({"name": name, "marketplace": market, "version": info.get("version", "")})
        if market in known and market not in marketplaces:
            marketplaces[market] = marketplace_source(known[market])

    return {
        "marketplaces": marketplaces,
        "plugins": plugins,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if plugins.lock.json is stale")
    args = parser.parse_args()

    data = snapshot()
    text = json.dumps(data, indent=2) + "\n"
    if args.check:
        current = LOCK.read_text("utf-8") if LOCK.is_file() else ""
        if current != text:
            print("plugins.lock.json is stale - run: python scripts/export_plugins.py")
            return 1
        print("plugins.lock.json up to date")
        return 0

    LOCK.write_bytes(text.encode("utf-8"))
    print(f"wrote {LOCK.relative_to(ROOT)}: {len(data['marketplaces'])} marketplaces, {len(data['plugins'])} plugins")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
