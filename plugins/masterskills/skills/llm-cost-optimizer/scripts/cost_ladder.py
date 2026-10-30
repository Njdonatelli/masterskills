#!/usr/bin/env python3
"""Price one LLM workload at each rung of the cost ladder.

    L1 Full     every request carries the whole shared context, synchronous
    L2 Trim     send only the slice of shared context the answer needs
    L3 Cache    write the shared prefix once, re-read it at the cache-hit rate
    L4 Batch    pool non-urgent requests through the Message Batches API (-50%)

The model is held constant on every rung, so the answers are the same; only the
billing path changes. Each rung is the cheapest option available up to that
point, so a rung that would cost more than the one before it is reported as
skipped, with the reason. Rates come from pricing.json next to this file.
Requires Python 3.9+.

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
import re
import sys
from dataclasses import asdict, dataclass, field, fields
from datetime import date
from pathlib import Path
from typing import Any, Optional

PRICING_PATH = Path(__file__).resolve().parent / "pricing.json"
STALE_AFTER_DAYS = 30
TTL_SECONDS = {"5m": 300, "1h": 3600}
BATCH_MAX_HOURS = 24

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
    trimmed_context: Optional[int] = None
    per_request_input: int = 0
    output_tokens: float = 0.0
    interval_seconds: float = 0.0
    ttl: str = "auto"
    batch_size: Optional[int] = None
    batch_hit_rate: float = 1.0
    latency_sensitive: bool = False
    us_only: bool = False
    cache_read_mult: Optional[float] = None
    runs_per_month: Optional[float] = None
    history_growth: int = 0
    trimmed_history_growth: Optional[int] = None
    trim_requests: Optional[int] = None
    current_rung: Optional[int] = None

    @property
    def shared(self) -> int:
        return self.full_context if self.trimmed_context is None else self.trimmed_context


@dataclass
class Rung:
    level: str
    lever: str
    cost: float
    applied: bool = True
    notes: list[str] = field(default_factory=list)


class InputError(ValueError):
    """Bad workload input; reported as a clean message, never a traceback."""


def load_pricing(path: Path) -> dict[str, Any]:
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)


def normalize_model(name: str) -> str:
    """Accept API ids (claude-sonnet-5-5, claude-sonnet-4-5-20250929) as well as
    table keys (sonnet-5.5)."""
    key = re.sub(r"-\d{8}$", "", name.lower().strip())
    key = key[len("claude-"):] if key.startswith("claude-") else key
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
    plain: float = 0.0,
    write: float = 0.0,
    ttl: str = "5m",
    read: float = 0.0,
    output: float = 0.0,
    discount: float = 1.0,
    geo: float = 1.0,
    read_mult: Optional[float] = None,
) -> float:
    """One request: `plain` uncached input, `write` tokens newly cached at `ttl`,
    `read` tokens served from cache, `output` tokens."""
    rates = rates_for(model, plain + write + read)
    read_rate = rates["input"] * read_mult if read_mult is not None else rates["cache_read"]
    dollars = (plain * rates["input"] + write * rates[f"cache_write_{ttl}"]
               + read * read_rate + output * rates["output"])
    return dollars / 1_000_000 * discount * geo


def plain_series(model: dict[str, Any], w: Workload, *, shared: int, n: int, growth: int,
                 discount: float, geo: float) -> float:
    """No caching. With history growth, request i also carries i * growth
    tokens of accumulated history (agent loop / chat)."""
    g = growth
    return sum(request_cost(model, plain=shared + i * g + w.per_request_input,
                            output=w.output_tokens, discount=discount, geo=geo)
               for i in range(n))


def cached_series(model: dict[str, Any], w: Workload, *, n: int, growth: int, ttl: str, writes: int,
                  hit_rate: float, discount: float, geo: float) -> float:
    """Independent requests sharing a prefix: `writes` requests pay the write
    rate, the rest read, except the miss share (1 - hit_rate), priced as a
    re-write because cache_control is still on the request (pessimistic).

    With --history-growth (a sequential loop), the breakpoint moves forward each
    turn: request i reads everything cached by request i-1 and writes only the
    new growth, which is how automatic caching bills a growing conversation."""
    common = dict(ttl=ttl, output=w.output_tokens, discount=discount, geo=geo,
                  read_mult=w.cache_read_mult)
    shared, u, g = w.shared, w.per_request_input, growth
    if g > 0:
        # A prefix below the model minimum is silently not cached, so early
        # turns of a short-prompt loop pay plain input until history grows past it.
        total, cached = 0.0, 0
        for i in range(n):
            prefix = shared + i * g
            if prefix >= model["min_cacheable"]:
                total += request_cost(model, read=cached, write=prefix - cached, plain=u, **common)
                cached = prefix
            else:
                total += request_cost(model, plain=prefix + u, **common)
        return total
    writes = min(writes, n)
    readers = n - writes
    hits = readers * hit_rate
    write = request_cost(model, write=shared, plain=u, **common)
    read = request_cost(model, read=shared, plain=u, **common)
    return (writes + readers - hits) * write + hits * read


def ttl_options(w: Workload) -> list[str]:
    return ["5m", "1h"] if w.ttl == "auto" else [w.ttl]


def cache_blocker(w: Workload, model: dict[str, Any], key: str, n: int, growth: int) -> Optional[str]:
    if w.shared + (n - 1) * growth < model["min_cacheable"]:
        return (f"prefix {w.shared:,} < {model['min_cacheable']:,}-token minimum for {key}; "
                "API silently skips caching")
    if w.shared == 0 and growth == 0:
        return "no shared prefix to cache"
    return None


def climb(w: Workload, pricing: dict[str, Any]) -> tuple[list[Rung], list[str]]:
    key = normalize_model(w.model)
    if key not in pricing["models"]:
        raise InputError(f"unknown model '{w.model}'; known: {', '.join(sorted(pricing['models']))}")
    model = pricing["models"][key]
    if w.us_only and model.get("inference_geo") is False:
        raise InputError(f"{key} does not support inference_geo (API returns 400); drop --us-only")
    geo = pricing["us_inference_geo_multiplier"] if w.us_only else 1.0
    batch = pricing["batch_discount"]
    warnings: list[str] = []
    n1 = w.requests
    n = w.trim_requests if w.trim_requests is not None else n1  # requests from L2 on
    g1 = w.history_growth
    g = w.trimmed_history_growth if w.trimmed_history_growth is not None else g1  # growth from L2 on

    rungs = [Rung("L1 Full", "send all shared context, sync",
                  plain_series(model, w, shared=w.full_context, n=n1, growth=g1, discount=1.0, geo=geo))]

    # --- L2 trim --------------------------------------------------------------
    trimmed_any = w.shared < w.full_context or n < n1 or g < g1
    lever = f"send {w.shared:,} of {w.full_context:,} shared tokens"
    if n < n1:
        lever += f", {n:,} of {n1:,} requests"
    if g < g1:
        lever += f", {g:,} of {g1:,} history/turn"
    trim = Rung("L2 Trim", lever, plain_series(model, w, shared=w.shared, n=n, growth=g, discount=1.0, geo=geo))
    if not trimmed_any:
        trim.applied = False
        trim.notes.append("no trim given; rung is a no-op until you measure what the answer needs")
    else:
        trim.notes.append("savings hold only if answer quality is unchanged; eval before shipping")
    threshold = model.get("long_context_threshold")
    peak = w.shared + w.per_request_input + (n - 1) * g
    if threshold is not None and peak > threshold:
        trim.notes.append(f"requests reach {peak:,} input tokens, past the {threshold:,}-token long-context "
                          "tier (5x rates for the whole request); keep each request under it")
    rungs.append(trim)
    best = trim.cost

    # --- L3 cache (sync) ------------------------------------------------------
    cache = Rung("L3 Cache", "cache shared prefix, re-read at hit rate", best, applied=False)
    blocker = cache_blocker(w, model, key, n, g)
    if blocker:
        cache.notes.append(blocker)
    elif n < 2:
        cache.notes.append("one request: a write premium with nothing to re-read")
    else:
        spanning = [t for t in ttl_options(w) if w.interval_seconds <= TTL_SECONDS[t]]
        if not spanning:
            if w.ttl == "5m" and w.interval_seconds <= TTL_SECONDS["1h"]:
                cache.notes.append(f"requests {w.interval_seconds:,.0f}s apart outlive the forced 5m TTL; "
                                   "use --ttl 1h (or auto)")
            else:
                cache.notes.append(f"requests {w.interval_seconds:,.0f}s apart outlive every TTL "
                                   "(max 1h); each request would re-write")
        else:
            options = {t: cached_series(model, w, n=n, growth=g, ttl=t, writes=1, hit_rate=1.0,
                                        discount=1.0, geo=geo)
                       for t in spanning}
            ttl = min(options, key=options.get)
            if options[ttl] < best:
                cache.cost, cache.applied = options[ttl], True
                cache.lever = (f"moving breakpoint ({ttl} TTL): re-read history, write only new turns"
                               if g else
                               f"cache prefix ({ttl} TTL, refreshed on each hit), re-read at hit rate")
                if w.interval_seconds == 0 and not g:
                    cache.notes.append("send the first request and wait for its response to START before "
                                       "firing the rest; parallel cold requests all miss")
            else:
                cache.notes.append("write premium exceeds read savings at this volume")
    rungs.append(cache)
    best = min(best, cache.cost)

    # --- L4 batch -------------------------------------------------------------
    batch_rung = Rung("L4 Batch", "Message Batches API, -50% on every token", best, applied=False)
    if w.latency_sensitive:
        batch_rung.notes.append("latency-sensitive: batch results can take up to 24h")
    elif g:
        batch_rung.notes.append("each turn depends on the previous one; batch only across independent "
                                "loops, not within one")
    else:
        size = w.batch_size if w.batch_size is not None else n
        submissions = math.ceil(n / size)
        hold_hours = (size - 1) * w.interval_seconds / 3600
        gap = size * w.interval_seconds  # seconds between consecutive submissions
        candidates: dict[str, tuple[float, str]] = {
            "none": (plain_series(model, w, shared=w.shared, n=n, growth=0, discount=batch, geo=geo),
                     "Message Batches API, -50% on every token"),
        }
        if not blocker and n >= 2:
            # Batches often run 5-60 min, so a 5m entry can expire mid-batch; the
            # docs recommend 1h. Only price 5m when the user forces it.
            for t in (["1h"] if w.ttl == "auto" else [w.ttl]):
                # One warm-up covers every submission while submissions land within
                # the TTL of each other; otherwise each submission re-warms.
                warms = 1 if gap <= TTL_SECONDS[t] else submissions
                cost = cached_series(model, w, n=n, growth=0, ttl=t, writes=warms, hit_rate=w.batch_hit_rate,
                                     discount=batch, geo=geo)
                candidates[t] = (cost, f"batch + {t} cache (warm one request first), -50%")
        choice = min(candidates, key=lambda k: candidates[k][0])
        cost, lever = candidates[choice]
        if cost < best:
            batch_rung.cost, batch_rung.lever, batch_rung.applied = cost, lever, True
            if choice != "none":
                warms = 1 if gap <= TTL_SECONDS[choice] else submissions
                if w.batch_hit_rate < 1.0:
                    batch_rung.notes.append(f"assumes {w.batch_hit_rate:.0%} cache hits (misses priced as "
                                            "re-writes); docs report 30-98% in batches")
                else:
                    batch_rung.notes.append("assumes the warm-up pattern lands every hit; docs call batch "
                                            "hits best-effort (30-98%); try --batch-hit-rate 0.6")
                if warms > 1:
                    batch_rung.notes.append(f"{warms} submissions more than {choice} apart; each re-warms the cache")
                if choice == "5m":
                    batch_rung.notes.append("5m TTL in batches is fragile (batches often run 5-60 min); "
                                            "docs recommend 1h")
        else:
            batch_rung.notes.append(f"best batch option ({fmt(cost, 4)}) does not beat the previous rung; "
                                    "stay synchronous")
        if hold_hours > 0:
            batch_rung.notes.append(f"pooling {size:,} requests holds the earliest up to {hold_hours:,.1f}h "
                                    f"before submission (+ up to {BATCH_MAX_HOURS}h processing); "
                                    "lower --batch-size if that's too stale")
    rungs.append(batch_rung)

    for i, r in enumerate(rungs):
        if not r.applied and i > 0:
            r.lever = f"not used: {r.lever}"
    if w.current_rung is not None:
        here = rungs[w.current_rung - 1]
        if here.applied or w.current_rung == 1:
            here.notes.insert(0, "<- you are here today")
        else:
            here.notes.insert(0, "<- you are here today, but this rung doesn't pay for this workload: "
                                 "today's real cost is above the figure shown; turning it off saves money")
    if w.cache_read_mult is not None:
        warnings.append(f"cache reads priced at {w.cache_read_mult}x input (override), not the live table rate")
    if w.us_only:
        warnings.append("inference_geo=us applies 1.1x to every token category")
    age = (date.today() - date.fromisoformat(pricing["retrieved"])).days
    if age > STALE_AFTER_DAYS:
        warnings.append(f"pricing.json is {age} days old; refresh from {pricing['sources'][0]}")
    return rungs, warnings


def fmt(dollars: float, places: int = 2) -> str:
    return f"${dollars:,.{places}f}"


def precision(costs: list[float]) -> int:
    """One precision for the whole table so columns line up and compare."""
    smallest = min((c for c in costs if c > 0), default=1.0)
    return 2 if smallest >= 1 else 4 if smallest >= 0.0001 else 6


def ratios(base: float, cost: float) -> tuple[Optional[float], Optional[float]]:
    if base <= 0:
        return None, None
    return 1 - cost / base, (base / cost if cost > 0 else None)


def render(w: Workload, rungs: list[Rung], warnings: list[str], pricing: dict[str, Any]) -> str:
    base = rungs[0].cost
    places = precision([r.cost for r in rungs])
    plural = "s" if w.requests != 1 else ""
    growth = f" + {w.history_growth:,} history/turn" if w.history_growth else ""
    if w.trimmed_history_growth is not None and w.trimmed_history_growth != w.history_growth:
        growth += f" (-> {w.trimmed_history_growth:,})"
    lines = [
        f"Model {normalize_model(w.model)} | {w.requests:,} request{plural} | shared context "
        f"{w.full_context:,} -> {w.shared:,}{growth} | {w.per_request_input:,} unique in + "
        f"{w.output_tokens:,.0f} out per request | rates as of {pricing['retrieved']}",
        "",
        f"{'Rung':<9} {'Cost':>12} {'Saved':>6} {'Cheaper':>8}  Lever",
        f"{'-'*9} {'-'*12} {'-'*6} {'-'*8}  {'-'*40}",
    ]
    for i, r in enumerate(rungs):
        saved, times = ratios(base, r.cost)
        saved_s = "base" if i == 0 else ("-" if saved is None else f"{saved:.0%}")
        times_s = "-" if times is None else f"{times:.1f}x"
        lines.append(f"{r.level:<9} {fmt(r.cost, places):>12} {saved_s:>6} {times_s:>8}  {r.lever}")
        for note in r.notes:
            lines.append(f"{'':<39}- {note}")
    if w.runs_per_month is not None:
        monthly = [r.cost * w.runs_per_month for r in rungs]
        mp = precision(monthly)
        parts = [f"{r.level.split()[0]} {fmt(m, mp) if r.applied or i == 0 else '(= previous)'}"
                 for i, (r, m) in enumerate(zip(rungs, monthly))]
        lines += ["", f"Monthly at {w.runs_per_month:g} runs: " + " | ".join(parts)]
    for warn in warnings:
        lines.append(f"! {warn}")
    return "\n".join(lines)


def as_json(w: Workload, rungs: list[Rung], warnings: list[str], pricing: dict[str, Any]) -> str:
    base = rungs[0].cost
    out = []
    for r in rungs:
        saved, times = ratios(base, r.cost)
        row = asdict(r)
        row["cost"] = round(r.cost, 6)
        row["saved_fraction"] = None if saved is None else round(saved, 4)
        row["times_cheaper"] = None if times is None else round(times, 2)
        if w.runs_per_month is not None:
            row["monthly_cost"] = round(r.cost * w.runs_per_month, 4)
        out.append(row)
    return json.dumps({"workload": asdict(w), "pricing_retrieved": pricing["retrieved"],
                       "rungs": out, "warnings": warnings}, indent=2)


FIELD_TYPES: dict[str, type] = {
    "model": str, "requests": int, "full_context": int, "trimmed_context": int,
    "per_request_input": int, "output_tokens": float, "interval_seconds": float,
    "ttl": str, "batch_size": int, "batch_hit_rate": float, "latency_sensitive": bool,
    "us_only": bool, "cache_read_mult": float, "runs_per_month": float,
    "history_growth": int, "trimmed_history_growth": int, "trim_requests": int, "current_rung": int,
}


def coerce(name: str, value: Any) -> Any:
    expected = FIELD_TYPES[name]
    if value is None:
        return None
    if expected is bool:
        if not isinstance(value, bool):
            raise InputError(f"{name} must be true or false")
        return value
    if expected is str:
        if not isinstance(value, str):
            raise InputError(f"{name} must be a string")
        return value
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise InputError(f"{name} must be a number, got {value!r}")
    if expected is int:
        if float(value) != int(value):
            raise InputError(f"{name} must be a whole number, got {value!r}")
        return int(value)
    return float(value)


def read_config(path: str) -> dict[str, Any]:
    try:
        raw = json.loads(Path(path).read_text(encoding="utf-8"))
    except OSError as exc:
        raise InputError(f"cannot read config {path}: {exc.strerror}") from exc
    except json.JSONDecodeError as exc:
        raise InputError(f"config {path} is not valid JSON: {exc}") from exc
    if not isinstance(raw, dict):
        raise InputError(f"config {path} must be a JSON object")
    data = {}
    for k, v in raw.items():
        name = k.replace("-", "_")
        if name not in FIELD_TYPES:
            raise InputError(f"unknown config key '{k}'; valid: {', '.join(FIELD_TYPES)}")
        data[name] = v
    return data


def build_workload(args: argparse.Namespace) -> Workload:
    data: dict[str, Any] = {}
    if args.scenario:
        data.update(SCENARIOS[args.scenario])
    if args.config:
        data.update(read_config(args.config))
    for f in fields(Workload):
        value = getattr(args, f.name, None)
        if value is not None:
            data[f.name] = value
    missing = [k for k in ("model", "requests", "full_context") if data.get(k) is None]
    if missing:
        raise InputError(f"missing required inputs: {', '.join('--' + m.replace('_', '-') for m in missing)}")
    w = Workload(**{k: coerce(k, v) for k, v in data.items()})

    if w.requests < 1:
        raise InputError("requests must be >= 1")
    for name in ("full_context", "per_request_input", "output_tokens", "interval_seconds"):
        if getattr(w, name) < 0:
            raise InputError(f"{name} must be >= 0")
    if w.trimmed_context is not None and not 0 <= w.trimmed_context <= w.full_context:
        raise InputError("trimmed_context must be between 0 and full_context")
    if w.batch_size is not None and w.batch_size < 1:
        raise InputError("batch_size must be >= 1")
    if not 0.0 <= w.batch_hit_rate <= 1.0:
        raise InputError("batch_hit_rate must be between 0 and 1")
    if w.cache_read_mult is not None and w.cache_read_mult < 0:
        raise InputError("cache_read_mult must be >= 0")
    if w.runs_per_month is not None and w.runs_per_month < 0:
        raise InputError("runs_per_month must be >= 0")
    if w.ttl not in ("auto", "5m", "1h"):
        raise InputError("ttl must be auto, 5m or 1h")
    if w.history_growth < 0:
        raise InputError("history_growth must be >= 0")
    if w.trimmed_history_growth is not None and not 0 <= w.trimmed_history_growth <= w.history_growth:
        raise InputError("trimmed_history_growth must be between 0 and history_growth")
    if w.trim_requests is not None and not 1 <= w.trim_requests <= w.requests:
        raise InputError("trim_requests must be between 1 and requests")
    if w.current_rung is not None and w.current_rung not in (1, 2, 3, 4):
        raise InputError("current_rung must be 1, 2, 3 or 4")
    return w


def parse_args(argv: list[str]) -> argparse.Namespace:
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument("--scenario", choices=sorted(SCENARIOS))
    p.add_argument("--config", help="JSON object; keys match the flag names (underscores or dashes)")
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
    p.add_argument("--latency-sensitive", action=argparse.BooleanOptionalAction, default=None,
                   help="a user is waiting; batch rung is skipped")
    p.add_argument("--us-only", action=argparse.BooleanOptionalAction, default=None,
                   help="inference_geo=us (1.1x)")
    p.add_argument("--cache-read-mult", type=float,
                   help="price cache reads as this multiple of input instead of the table rate")
    p.add_argument("--runs-per-month", type=float, help="repeat count for a monthly projection")
    p.add_argument("--history-growth", type=int,
                   help="tokens appended to context per request (agent loop / chat: tool result + assistant turn)")
    p.add_argument("--trimmed-history-growth", type=int,
                   help="history growth per request from L2 on (smaller tool results after the trim)")
    p.add_argument("--trim-requests", type=int,
                   help="request count from L2 on, when trimming also removes calls (e.g. a follow-up fetch)")
    p.add_argument("--current-rung", type=int, choices=[1, 2, 3, 4], help="mark where the workload is today")
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
    try:
        w = build_workload(args)
        rungs, warnings = climb(w, pricing)
    except InputError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    print(as_json(w, rungs, warnings, pricing) if args.json else render(w, rungs, warnings, pricing))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
