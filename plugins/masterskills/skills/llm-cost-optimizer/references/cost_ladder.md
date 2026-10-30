# Cost Ladder: implementation patterns

Rates and rules below were checked against the Claude docs on 2026-10-30 (pricing, prompt-caching, and batch-processing pages; URLs in `scripts/pricing.json`). Re-check before quoting numbers.

## Contents

- [Finding the shared context](#finding-the-shared-context)
- [L2 Trim](#l2-trim)
- [L3 Cache](#l3-cache)
- [L4 Batch](#l4-batch)
- [Verifying the savings](#verifying-the-savings)
- [Getting calculator inputs from code](#getting-calculator-inputs-from-code)

---

## Finding the shared context

The ladder only matters where the same tokens ride along on many requests. Grep the codebase or workflow for:

| Look for | Typical shared context |
|---|---|
| `messages.create`, `client.messages`, `anthropic.`, `ChatAnthropic`, n8n "Anthropic Chat Model" / HTTP nodes to `/v1/messages` | The call sites themselves |
| Long `system=` strings, prompt template files, `.md` instructions loaded at runtime | System prompt |
| `open(...).read()`, `glob`, "load all docs", `"\n\n".join(docs)` before a call | Stuffed documents (L2 + L3) |
| `top_k`, `k=`, `limit=`, `max_results`, chunk size constants | Retrieval width (L2) |
| `tools=[...]` definitions, MCP server tool schemas | Tool definitions (L3, cached first in prefix order) |
| Loops over items, cron schedules, `schedule`, `@daily`, n8n Schedule Trigger, Zapier Schedule | Batch candidates (L4) |
| `history`, `messages.append`, conversation memory | Growing history (L2 windowing, L3 automatic caching) |

Record per call site: requests per run, runs per month, shared tokens, unique tokens per request, output tokens, the gap between requests, and whether a human is waiting.

---

## L2 Trim

Trim is the only rung that can change answers. Every trim needs a before/after check on real questions.

| Pattern | Typical cut |
|---|---|
| Retrieve top-k chunks instead of stuffing whole documents | 60-95% |
| Return excerpts or matched sections from tools instead of full articles | 50-90% of tool-result tokens |
| Cap tool results (`max_chars`, `top_k`) and let the agent ask for more | Bounded worst case |
| Window or summarize chat history past N turns | Linear -> roughly flat growth |
| Strip HTML, navigation, boilerplate, and base64 before sending | 10-40% |
| Address documents by section ID, and send the index first and sections on demand | 50-90% |

Size the trim from evidence. Log which chunks or sections the answers cite, then set `--trimmed-context` to the p95 of what was actually used, plus headroom.

---

## L3 Cache

**Prefix order is tools -> system -> messages.** A change at one level invalidates that level and everything after it. Changing tool definitions invalidates everything.

**Breakpoint rule:** put `cache_control` on the **last block that is identical across requests**. A block that varies (a timestamp, the user question, per-request context) writes a new entry every call and is never read.

```python
import anthropic

client = anthropic.Anthropic()

def ask(question: str, docs_text: str) -> anthropic.types.Message:
    return client.messages.create(
        model="claude-sonnet-5-5",
        max_tokens=800,
        system=[
            {"type": "text", "text": "Answer only from the provided documents. Cite section titles."},
            {
                "type": "text",
                "text": docs_text,  # identical on every call
                "cache_control": {"type": "ephemeral"},  # 5m TTL; add "ttl": "1h" for sparse traffic
            },
        ],
        messages=[{"role": "user", "content": question}],  # varies, so it goes after the breakpoint
    )
```

For multi-turn agents, the top-level `cache_control={"type": "ephemeral"}` (automatic caching) moves the breakpoint as the conversation grows. It uses one of the 4 breakpoint slots.

**Rules that decide whether caching pays:**

| Rule | Value (2026-10-30) |
|---|---|
| Minimum cacheable prefix | 512 tokens on Fable/Mythos 5.1, Opus 5.5, Opus 5, Sonnet 5.5, Haiku 5.5; 1,024 on Sonnet 5, Opus 4.8, Sonnet 4.6/4.5; 2,048 on Opus 4.7; 4,096 on Opus 4.6/4.5 and Haiku 4.5 |
| Below minimum | Silently not cached; no error. Both cache usage fields read 0 |
| 5m write | 1.25x input. The TTL refreshes free on each hit and is measured from request start |
| 1h write | 2x input. Use when requests are 5-60 min apart, or in batches |
| Read | 0.05x on Sonnet/Opus 5.5, 0.025x on Fable/Mythos 5.1, 0.1x on everything else |
| Breakpoints | Max 4 per request. A 1h entry must come before any 5m entry. 20-block lookback |
| Concurrency | An entry is usable only after the first response starts. Send one, then fan out |
| Silent invalidators | Tool definitions, web-search or citations toggles, `tool_choice`, images added or removed, thinking/effort settings, unstable JSON key order (Go, Swift) |

**Break-even:** at 5m TTL, any second request inside the window pays for the write. Writes cost +0.25x and each read saves about 0.9-0.975x. With the 1h TTL (+1.0x write) you need at least 2 reads. Let the calculator decide.

---

## L4 Batch

Flat 50% off input and output, including cache reads and writes. Usually done in under 1 hour, guaranteed within 24h; results kept 29 days. Up to 100,000 requests or 256 MB per batch. No streaming, no fast mode, not ZDR/HIPAA eligible.

**Fit test:** would anyone notice if this result arrived 1-24 hours later? If not, batch it. Nightly digests, scheduled agents, evals, bulk tagging or classification, backfills, and forecast or report generation all fit.

**Cache inside batches is best-effort** (30-98% hit rates reported). To land hits, warm a 1h entry with one request, wait for it, then submit the rest with identical `cache_control` blocks.

```python
import time
import anthropic

client = anthropic.Anthropic()
SYSTEM = [
    {"type": "text", "text": "Classify each permit by project type."},
    {"type": "text", "text": REFERENCE_TEXT, "cache_control": {"type": "ephemeral", "ttl": "1h"}},
]

def params(item_text: str) -> dict:
    return {
        "model": "claude-sonnet-5-5",
        "max_tokens": 200,
        "system": SYSTEM,
        "messages": [{"role": "user", "content": item_text}],
    }

def wait(batch_id: str) -> None:
    while client.messages.batches.retrieve(batch_id).processing_status != "ended":
        time.sleep(30)

def run(items: dict[str, str]) -> dict[str, str]:
    first_id, *rest = items
    # Warm the 1h cache so the bulk submission reads instead of racing to write.
    warm = client.messages.batches.create(requests=[{"custom_id": first_id, "params": params(items[first_id])}])
    wait(warm.id)
    bulk = client.messages.batches.create(
        requests=[{"custom_id": cid, "params": params(items[cid])} for cid in rest]
    )
    wait(bulk.id)
    out: dict[str, str] = {}
    for batch_id in (warm.id, bulk.id):
        for result in client.messages.batches.results(batch_id):  # unordered: always key by custom_id
            if result.result.type == "succeeded":
                out[result.custom_id] = result.result.message.content[0].text
    return out
```

`custom_id` must match `^[a-zA-Z0-9_-]{1,64}$`. Errored, canceled, and expired requests aren't billed. Retry server errors, and fix `invalid_request_error` before resending.

**No-code platforms:** n8n and Zapier "chat model" nodes call the sync endpoint. To batch, use HTTP Request nodes against `/v1/messages/batches`, with a second scheduled workflow that polls and collects results. Verify the platform's current node options before promising this.

---

## Verifying the savings

1. Pick a fixed question set (at least 10 real questions, or the 6-question video replica).
2. Run it at the current rung and the target rung. Log the `usage` fields from each response.
3. **Cost check:** `cache_read_input_tokens > 0` on requests 2..n means L3 is working. Batch line items show at 50%.
4. **Answer check (L2 and routing only):** compare answers side by side or with an LLM judge. Caching and batching must give identical prompts, so any answer difference points to a bug in the prompt assembly.
5. Compare measured spend with the calculator's prediction. A gap over 15% usually means a wrong per-request token estimate or a cache miss.

---

## Getting calculator inputs from code

| Input | How to get it |
|---|---|
| `--full-context` | Count tokens of the shared block with `client.messages.count_tokens(...)`, or estimate at about 4 chars/token for English prose (newer Claude tokenizers produce ~30% more tokens than older ones) |
| `--trimmed-context` | Top-k x chunk tokens, or the measured cited span |
| `--per-request-input` | User question + per-request variables |
| `--output-tokens` | `max_tokens` is the ceiling; use measured p50 when logs exist |
| `--interval-seconds` | Request rate inside one run (0 = burst) |
| `--runs-per-month` | Cron frequency x days, or monthly sessions |
