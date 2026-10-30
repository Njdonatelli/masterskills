#!/usr/bin/env python3
"""Price one LLM workload at each rung of the cost ladder.

    L1 Full     every request carries the whole shared context, synchronous
    L2 Trim     send only the slice of shared context the answer needs
    L3 Cache    write the shared prefix once, re-read it at the cache-hit rate
    L4 Batch    pool non-urgent requests through the Message Batches API (-50%)

The model is held constant on every rung, so the answers are the same; only the
billing path changes. Rates come from pricing.json next to this file.

Examples (shell: Bash/Zsh or Git Bash):
    python3 scripts/cost_ladder.py --scenario video
    python3 scripts/cost_ladder.py --scenario video --cache-read-mult 0.1
    python3 scripts/cost_ladder.py --model opus-5.5 --requests 400 \
        --full-context 60000 --trimmed-context 12000 --per-request-input 300 \
        --output-tokens 500 --interval-seconds 20 --runs-per-month 30
    python3 scripts/cost_ladder.py --config workload.json --json
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from dataclasses import asdict, dataclass, field
from datetime import date
from pathlib import Path
from typing import Any

PRICING_PATH = Path(__file__).resolve().parent / "pricing.json"
STALE_AFTER_DAYS = 30
TTL_SECONDS = {"5m": 300, "1h": 3600}

# The @donimas "AI Levels EP03" workload: 6 questions over the same 100K docs,
# 40K of which matter. Output total of 4K tokens is back-solved from the
# video's $1.24 baseline ($1.20 input + $0.04 output on Sonnet 5.5).
SCENARIOS: dict[str, dict[str, Any]] = {
    "video": {
        "model": "sonnet-5.5",
        "requests": 6,
        "full_context": 100_000,
        "trimmed_context": 40_000,
        "per_request_input": 0,
        "output_tokens": 4_000 / 6,
    },
}


@dataclass
class Workload:
    model: str
    requests: int
    full_context: int
    trimmed_context: int | None = None
    per_request_input: int = 0
    output_tokens: float = 0.0
    interval_seconds: float = 0.0
    ttl: str = "auto"
    batch_size: int | None = None
    batch_hit_rate: float = 1.0
    latency_sensitive: bool = False
    us_only: bool = False
    cache_read_mult: float | None = None
    runs_per_month: float | None = None


@dataclass
class Rung:
    level: str
    lever: str
    cost: float
    applied: bool = True
    notes: list[str] = field(default_factory=list)


def load_pricing(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)


def normalize_model(name: str) -> str:
    """Accept API ids (claude-sonnet-5-5) as well as table keys (sonnet-5.5)."""
    key = name.lower().removeprefix("claude-")
    parts = key.split("-")
    if len(parts) >= 3 and parts[-1].isdigit() and parts[-2].isdigit():
        key = "-".join(parts[:-2]) + f"-{parts[-2]}.{parts[-1]}"
    return key


def rates_for(model: dict[str, Any], total_input: float) -> dict[str, float]:
    """Haiku 5.5 bills the whole request at long-tier rates once total input
    (cache reads and writes included) crosses the threshold."""
    threshold = model.get("long_context_threshold")
    if threshold is not None and total_input > threshold:
        return model["long"]
    return model


def request_cost(
    model: dict[str, Any],
    *,
    prefix: float,
    prefix_mode: str,
    uncached: float,
    output: float,
    discount: float,
    geo: float,
    read_mult: float | None,
) -> float:
    rates = rates_for(model, prefix + uncached)
    prefix_rate = {
        "plain": rates["input"],
        "write_5m": rates["cache_write_5m"],
        "write_1h": rates["cache_write_1h"],
        "read": rates["input"] * read_mult if read_mult is not None else rates["cache_read"],
    }[prefix_mode]
    dollars = prefix * prefix_rate + uncached * rates["input"] + output * rates["output"]
    return dollars / 1_000_000 * discount * geo


def choose_ttl(w: Workload) -> str | None:
    """Cheapest TTL that still spans the gap between requests; None if no TTL does."""
    if w.ttl != "auto":
        return w.ttl if w.interval_seconds <= TTL_SECONDS[w.ttl] else None
    if w.interval_seconds <= TTL_SECONDS["5m"]:
        return "5m"
    if w.interval_seconds <= TTL_SECONDS["1h"]:
        return "1h"
    return None


def cached_series_cost(
    model: dict[str, Any],
    w: Workload,
    prefix: int,
    *,
    ttl: str,
    writes: int,
    hit_rate: float,
    discount: float,
    geo: float,
) -> float:
    """`writes` requests pay the write rate; the rest read, except the miss
    share (1 - hit_rate), which re-writes because the cache_control block is
    still on the request."""
    common = dict(uncached=w.per_request_input, output=w.output_tokens,
                  discount=discount, geo=geo, read_mult=w.cache_read_mult)
    readers = w.requests - writes
    hits = readers * hit_rate
    misses = readers - hits
    write = request_cost(model, prefix=prefix, prefix_mode=f"write_{ttl}", **common)
    read = request_cost(model, prefix=prefix, prefix_mode="read", **common)
    return (writes + misses) * write + hits * read


def climb(w: Workload, pricing: dict[str, Any]) -> tuple[list[Rung], list[str]]:
    key = normalize_model(w.model)
    if key not in pricing["models"]:
        raise KeyError(f"unknown model '{w.model}'; known: {', '.join(sorted(pricing['models']))}")
    model = pricing["models"][key]
    geo = pricing["us_inference_geo_multiplier"] if w.us_only else 1.0
    batch = pricing["batch_discount"]
    warnings: list[str] = []
    n = w.requests

    def plain(prefix: int, discount: float = 1.0) -> float:
        return n * request_cost(model, prefix=prefix, prefix_mode="plain",
                                uncached=w.per_request_input, output=w.output_tokens,
                                discount=discount, geo=geo, read_mult=None)

    rungs = [Rung("L1 Full", "send all shared context, sync", plain(w.full_context))]

    trimmed = w.trimmed_context if w.trimmed_context is not None else w.full_context
    trim = Rung("L2 Trim", f"send {trimmed:,} of {w.full_context:,} shared tokens", plain(trimmed))
    if trimmed >= w.full_context:
        trim.applied = False
        trim.notes.append("no trim given; rung is a no-op until you measure what the answer needs")
    else:
        trim.notes.append("savings hold only if answer quality is unchanged at this context size; eval before shipping")
    rungs.append(trim)
    best_sync = trim.cost

    # --- L3 cache -------------------------------------------------------------
    ttl = choose_ttl(w)
    cache = Rung("L3 Cache", "cache shared prefix, re-read at hit rate", best_sync, applied=False)
    min_tokens = model["min_cacheable"]
    if trimmed < min_tokens:
        cache.notes.append(f"prefix {trimmed:,} < {min_tokens:,}-token minimum for {key}; API silently skips caching")
    elif n < 2:
        cache.notes.append("one request: a write premium with nothing to re-read")
    elif ttl is None:
        cache.notes.append(f"requests {w.interval_seconds:,.0f}s apart outlive every TTL; each would re-write")
    else:
        cost = cached_series_cost(model, w, trimmed, ttl=ttl, writes=1, hit_rate=1.0, discount=1.0, geo=geo)
        if cost < best_sync:
            cache.cost, cache.applied, cache.lever = cost, True, f"cache prefix ({ttl} TTL), re-read at hit rate"
            if w.interval_seconds == 0:
                cache.notes.append("send the first request and wait for its response to START before firing the rest; parallel cold requests all miss")
        else:
            cache.notes.append("write premium exceeds read savings at this volume")
    rungs.append(cache)
    if cache.applied:
        best_sync = cache.cost

    # --- L4 batch -------------------------------------------------------------
    if w.latency_sensitive:
        rungs.append(Rung("L4 Batch", "Message Batches API, -50%", best_sync, applied=False,
                          notes=["latency-sensitive: batch results can take up to 24h"]))
    else:
        size = w.batch_size or n
        submissions = math.ceil(n / size)
        no_cache = plain(trimmed, discount=batch)
        batch_rung = Rung("L4 Batch", "Message Batches API, -50% on every token", no_cache)
        if cache.applied or (trimmed >= min_tokens and size >= 2):
            # Batches run unordered and can exceed 5 minutes: warm a 1h entry with
            # one request per submission, then submit the rest.
            cached = cached_series_cost(model, w, trimmed, ttl="1h", writes=submissions,
                                        hit_rate=w.batch_hit_rate, discount=batch, geo=geo)
            if cached < no_cache:
                batch_rung.cost = cached
                batch_rung.lever = "batch + 1h cache (warm one request first), -50%"
                if w.batch_hit_rate < 1.0:
                    batch_rung.notes.append(f"assumes {w.batch_hit_rate:.0%} cache hits; docs report 30-98% in batches")
                else:
                    batch_rung.notes.append("assumes the warm-up pattern lands every hit; docs call batch hits best-effort (30-98%)")
        if submissions > 1:
            batch_rung.notes.append(f"{submissions} separate submissions, each re-warms the cache")
        rungs.append(batch_rung)

    if w.cache_read_mult is not None:
        warnings.append(f"cache reads priced at {w.cache_read_mult}x input (override), not the live table rate")
    if w.us_only:
        warnings.append("inference_geo=us applies 1.1x to every token category (Claude 4.6+ only)")
    retrieved = date.fromisoformat(pricing["retrieved"])
    age = (date.today() - retrieved).days
    if age > STALE_AFTER_DAYS:
        warnings.append(f"pricing.json is {age} days old; refresh from {pricing['sources'][0]}")
    return rungs, warnings


def render(w: Workload, rungs: list[Rung], warnings: list[str], pricing: dict[str, Any]) -> str:
    base = rungs[0].cost
    lines = [
        f"Model {normalize_model(w.model)} | {w.requests:,} request{'s' if w.requests != 1 else ''} | shared context "
        f"{w.full_context:,} -> {w.trimmed_context or w.full_context:,} | "
        f"{w.per_request_input:,} unique in + {w.output_tokens:,.0f} out per request | "
        f"rates as of {pricing['retrieved']}",
        "",
        f"{'Rung':<9} {'Cost':>11} {'vs L1':>7} {'Cumulative':>11}  Lever",
        f"{'-'*9} {'-'*11} {'-'*7} {'-'*11}  {'-'*40}",
    ]
    for r in rungs:
        mark = "" if r.applied else "  (skipped)"
        ratio = f"{base / r.cost:.1f}x" if r.cost > 0 else "-"
        saved = f"-{(1 - r.cost / base):.0%}" if base > 0 and r is not rungs[0] else "base"
        lines.append(f"{r.level:<9} {fmt(r.cost):>11} {saved:>7} {ratio:>11}  {r.lever}{mark}")
        for note in r.notes:
            lines.append(f"{'':<42}- {note}")
    if w.runs_per_month:
        lines += ["", f"Monthly at {w.runs_per_month:g} runs: "
                  + " | ".join(f"{r.level.split()[0]} {fmt(r.cost * w.runs_per_month)}" for r in rungs)]
    for warn in warnings:
        lines.append(f"! {warn}")
    return "\n".join(lines)


def fmt(dollars: float) -> str:
    return f"${dollars:,.4f}" if dollars < 1 else f"${dollars:,.2f}"


def build_workload(args: argparse.Namespace) -> Workload:
    data: dict[str, Any] = {}
    if args.scenario:
        data.update(SCENARIOS[args.scenario])
    if args.config:
        data.update(json.loads(Path(args.config).read_text(encoding="utf-8")))
    for name in Workload.__dataclass_fields__:
        value = getattr(args, name, None)
        if value is not None and value is not False:
            data[name] = value
    missing = [k for k in ("model", "requests", "full_context") if k not in data]
    if missing:
        raise SystemExit(f"missing required inputs: {', '.join('--' + m.replace('_', '-') for m in missing)}")
    w = Workload(**data)
    if w.requests < 1 or w.full_context < 0:
        raise SystemExit("--requests must be >= 1 and --full-context >= 0")
    if w.trimmed_context is not None and w.trimmed_context > w.full_context:
        raise SystemExit("--trimmed-context cannot exceed --full-context")
    if not 0.0 <= w.batch_hit_rate <= 1.0:
        raise SystemExit("--batch-hit-rate must be between 0 and 1")
    if w.ttl not in ("auto", "5m", "1h"):
        raise SystemExit("--ttl must be auto, 5m or 1h")
    return w


def parse_args(argv: list[str]) -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--scenario", choices=sorted(SCENARIOS))
    p.add_argument("--config", help="JSON file whose keys match the flag names (underscored)")
    p.add_argument("--pricing", default=str(PRICING_PATH))
    p.add_argument("--model")
    p.add_argument("--requests", type=int)
    p.add_argument("--full-context", type=int, help="shared tokens every request carries today")
    p.add_argument("--trimmed-context", type=int, help="shared tokens the answer actually needs")
    p.add_argument("--per-request-input", type=int, help="unique, uncacheable input tokens per request")
    p.add_argument("--output-tokens", type=float, help="output tokens per request")
    p.add_argument("--interval-seconds", type=float, help="gap between requests (0 = burst)")
    p.add_argument("--ttl", choices=["auto", "5m", "1h"])
    p.add_argument("--batch-size", type=int, help="requests pooled per batch submission (default: all)")
    p.add_argument("--batch-hit-rate", type=float, help="expected cache hit share inside batches (0-1)")
    p.add_argument("--latency-sensitive", action="store_true", help="a user is waiting; batch rung is skipped")
    p.add_argument("--us-only", action="store_true", help="inference_geo=us (1.1x)")
    p.add_argument("--cache-read-mult", type=float, help="price cache reads as this multiple of input instead of the table rate")
    p.add_argument("--runs-per-month", type=float, help="repeat count for a monthly projection")
    p.add_argument("--json", action="store_true")
    p.add_argument("--list-models", action="store_true")
    return p.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    try:
        pricing = load_pricing(Path(args.pricing))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"cannot read pricing file {args.pricing}: {exc}", file=sys.stderr)
        return 2
    if args.list_models:
        print("\n".join(sorted(pricing["models"])))
        return 0
    w = build_workload(args)
    try:
        rungs, warnings = climb(w, pricing)
    except KeyError as exc:
        print(exc.args[0], file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps({"workload": asdict(w), "pricing_retrieved": pricing["retrieved"],
                          "rungs": [asdict(r) for r in rungs], "warnings": warnings}, indent=2))
    else:
        print(render(w, rungs, warnings, pricing))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
