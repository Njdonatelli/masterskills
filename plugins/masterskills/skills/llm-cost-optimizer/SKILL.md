---
name: llm-cost-optimizer
description: >-
  Use proactively whenever LLM API costs come up -- or should. Triggers include: 'my AI costs are too high', 'optimize token usage', 'which model should I use', 'LLM spend is out of control', 'implement prompt caching', 'should I use the batch API', 'trim my context', 'how much will this pipeline cost', 'make this 10x cheaper', 'we're about to launch an AI feature', 'build me an AI endpoint'. Don't wait for an explicit cost complaint -- if someone is building an AI feature, an agent, a RAG or MCP retrieval layer, a scheduled LLM job, or choosing between models, cost architecture belongs in the conversation. Apply immediately when any of these are true: the same documents or system prompt ride along on every request, a non-interactive job (nightly, scheduled, eval, backfill) calls the API synchronously, a system prompt exceeds a few hundred tokens, all requests hit the same model, max_tokens is not set, or no per-feature cost logging exists. Ships a runnable four-rung cost-ladder calculator (full -> trim -> cache -> batch) priced from a dated Claude rate table. NOT for RAG retrieval-quality design (use rag-architect). NOT for improving prompt quality or effectiveness (use senior-prompt-engineer).
---

# LLM Cost Optimizer

You are an expert in LLM cost engineering. Your goal is to cut LLM API spend -- routinely by 5-10x on document-heavy workloads -- without degrading user-facing quality, using the cost ladder, model routing, output control, and observability.

AI API costs are engineering costs. Treat them like database query costs: measure first, optimize second, monitor always.

---

## Step 0: Classify Before You Ask

Pull answers from the conversation and the code first -- don't ask for what you can read.

| Mode | When to use |
|---|---|
| **Cost Audit** | Spend exists but no clear picture of where it goes |
| **Optimize Existing System** | A codebase, workflow, or described workload exists; apply the ladder |
| **Design Cost-Efficient Architecture** | Building new AI features; wire in cost controls before launch |

If you were handed a repo, workflow export (n8n, Zapier), or log file, start auditing it -- don't open with questions. Ask only for numbers you cannot measure or reasonably estimate, and label every estimate.

---

## The Cost Ladder (hold the model, change the billing path)

Same model, same answers, four ways to pay. Climb in order; each rung compounds on the one before. Reference workload: 6 questions over the same 100K-token doc set on Sonnet 5.5.

| Rung | Lever | What changes | Video figure | Live rates 2026-10-30 |
|---|---|---|---|---|
| **L1 Full** | none | Every request carries all shared context at full input price, synchronously | $1.24 | $1.24 |
| **L2 Trim** | Send only what the answer needs | Shared context per request shrinks (100K -> 40K) | $0.52 | $0.52 |
| **L3 Cache** | Prompt caching | Shared prefix written once, re-read at the cache-hit rate | $0.18 | $0.16 |
| **L4 Batch** | Message Batches API | Non-urgent requests pooled; every token -50% | $0.12 | $0.11 |

Source: @donimas, "AI Levels EP 03" ("10x cheaper"). The video prices cache reads at 0.1x input. Live Sonnet 5.5 and Opus 5.5 reads are 0.05x, so L3 and L4 are cheaper today. The video's $0.12 matches a **1-hour** cache write (2x) in batch, which is the TTL the batch docs recommend. Both columns reproduce exactly with the calculator (`--scenario video` and `--scenario video --cache-read-mult 0.1`).

**Run the numbers, never estimate them in prose:**

```bash
python3 scripts/cost_ladder.py --model sonnet-5.5 --requests 500 \
  --full-context 80000 --trimmed-context 15000 --per-request-input 400 \
  --output-tokens 600 --interval-seconds 30 --runs-per-month 22
```

Flags: `--latency-sensitive` (skips L4), `--batch-hit-rate 0.6` (batch caching is best-effort), `--batch-size` (requests per submission), `--ttl 5m|1h`, `--us-only` (1.1x), `--config workload.json`, `--json`, `--list-models`. For non-Claude providers, pass `--pricing` a JSON file in the same shape as `scripts/pricing.json`.

**Rates go stale.** `scripts/pricing.json` is a dated snapshot. If it is older than 30 days (the script warns), or the user's model isn't in it, re-fetch the pricing, prompt-caching, and batch pages listed in its `sources` and update the file before quoting dollars. Store absolute prices, not multipliers: cache-read multipliers differ by model (0.025x, 0.05x, 0.1x).

### How to apply each rung

Read [references/cost_ladder.md](references/cost_ladder.md) for implementation patterns, code, and failure modes. Short form:

- **L2 Trim** -- find the shared context (stuffed docs, whole-file reads, full tool outputs, every chunk instead of top-k, full chat history) and size what the answer needs. Trim is the only rung that can change answers, so require an eval or side-by-side check before shipping it. If retrieval quality becomes the question, hand off to `rag-architect`.
- **L3 Cache** -- put stable content first (tools -> system -> messages), mark the **last block that is identical across requests**, and confirm with `cache_read_input_tokens > 0`. It pays when the prefix clears the model's minimum (512 tokens on the 5.x family, up to 4,096 on older models) and the same prefix is re-sent within the TTL. Caching is exact-prefix and answer-neutral.
- **L4 Batch** -- for anything no one is waiting on: nightly jobs, scheduled agents, evals, backfills, bulk classification, embedding-adjacent summarization. Flat 50% off input and output, stacks with caching, results within 24h (usually under 1h). Use a 1h cache and send one warm-up request before the rest. Answer-neutral.

**Workload shapes that hide the ladder:**

| Shape | Where the shared context is | Usual best rung |
|---|---|---|
| Doc Q&A / RAG endpoint | Retrieved chunks + system prompt | L2 (top-k, chunk size) then L3 on the system prompt and tool definitions |
| MCP / tool server consumed by an agent | Tool results returned into the agent's context; tool definitions | L2: cap result size and top-k, return excerpts not full articles. L3 is the client's job; flag it if the user owns the client |
| Agent loop / chat | Growing history + tools + system | L3 (automatic caching or a moving breakpoint) and history trimming |
| Scheduled / nightly job | Same instructions and reference data per item | L4 + L3 (1h TTL), often 10x+ |
| One-off long prompt | None shared | L1 is fine; look at routing and output length instead |

---

## Mode 1: Cost Audit

Use when spend exists but the breakdown is unknown. Instrument first; optimize second.

1. **Instrument every request.** Log model, `input_tokens`, `cache_creation_input_tokens`, `cache_read_input_tokens`, `output_tokens`, latency, endpoint/feature, and calculated cost. Total input = all three input fields; `input_tokens` alone excludes cache traffic.
2. **Find the 20% causing 80% of spend.** Sort by feature x model x tokens. Usually 2-3 endpoints dominate.
3. **Place each hot path on the ladder.** Which rung is it on today? Run the calculator for the next rungs.
4. **Classify requests by complexity** for routing (below).

**If token logging doesn't exist yet**, the logging schema is deliverable #1, but still run the calculator on code-derived estimates so the user sees the size of the prize.

---

## Mode 2: Optimize Existing System

Apply in this order, measuring after each step:

1. **Cost ladder (L2 -> L3 -> L4)** on every path with shared context. Biggest wins for document-heavy and scheduled work, and caching/batching never change answers.
2. **Model routing (60-80% on routed traffic).** The ladder holds the model fixed; routing changes it. Small models for classification, extraction, and formatting; mid models for structured output and summarization; large models for multi-step reasoning, long-context analysis, and agentic work. Routing changes answers, so eval it. Then re-run the ladder on the new model; cache minimums and rates differ.
3. **Output length control (20-40%).** Output costs 5x input on current Claude models. Set `max_tokens` per endpoint from measured p95, use schema-constrained output, and add stop sequences.
4. **Prompt compression (15-30% of input).** Remove filler and duplicated context. Preserve task-critical instructions; over-compression causes retries that erase the savings.
5. **Semantic response caching (30-60% hit rate on repeated queries).** Embedding-keyed response cache (cosine > 0.95). Unlike prompt caching, this can serve a stale or wrong answer, so scope it to stable FAQs.

---

## Mode 3: Design Cost-Efficient Architecture

Wire these in before launch:

- **Prompt layout for caching.** Stable content first, volatile last, breakpoint on the last stable block. Never put timestamps, user names, or request IDs in the system prompt.
- **Sync vs async split.** Decide per feature whether a human is waiting. Everything else goes through the Batch API by default.
- **Context budget per call.** A top-k and token cap for every retrieval or tool result, chosen from an eval, not from "more is safer".
- **Budget envelopes** per feature, user tier, and day, with alerts at 80%.
- **Routing layer.** Classify -> route -> call. Never call the large model by default.
- **Cost observability.** Spend by feature and model, cache hit rate, batch share, cost per active user, and week-over-week trend.
- **Graceful degradation** when a budget is hit: smaller model -> cached response -> async queue.

---

## Proactive Flags

| Signal | Action |
|---|---|
| Same docs/system prompt re-sent on every request with no `cache_control` | L3 target. Run the calculator and show the dollar delta |
| Cron, scheduled task, nightly agent, eval, or backfill calling the sync API | L4 target. 50% off, usually stackable with L3 |
| Whole files, full articles, or all chunks stuffed into context | L2 target. Measure what the answer uses |
| `cache_control` on a block that varies per request | Writes every call, reads never. Move the breakpoint up to the last stable block |
| Parallel cold requests expecting cache hits | Cache exists only after the first response starts. Send one, then fan out |
| Batch jobs using the 5-minute TTL | Batches often run 5-60 min. Use the 1h TTL plus a warm-up request |
| Shared prefix below the model's cache minimum | Caching silently no-ops (both cache usage fields read 0). Don't claim savings |
| No per-feature cost breakdown | Instrument logging, including the cache usage fields |
| All requests hitting one model | Initiate routing design |
| `max_tokens` not set per endpoint | Active cost leak |

---

## Failure Modes and Recovery

| Situation | Response |
|---|---|
| No token logs exist | Ship the logging schema, and give calculator estimates from code-derived token counts, labeled as estimates |
| Cache hit rate near 0 after enabling | Check: prefix below minimum; breakpoint on a varying block; tool/JSON key order changing (Go, Swift); thinking or effort settings changing between calls; requests spaced past the TTL |
| Batch cache hit rate low | Warm one request with the 1h cache first, keep `cache_control` identical across requests, then submit the rest |
| Trim degrades answers | Restore context in steps until the eval passes. Report the quality-bound trim size, not the cheapest one |
| Routing classifier adds unacceptable latency | Fall back to rule-based routing (token thresholds, endpoint tags) |
| Pricing table stale or model missing | Re-fetch the docs in `pricing.json` sources, update the file, and re-run before quoting |

---

## Handoff Triggers

- **Retrieval quality (chunking, embeddings, reranking) becomes the question** -> `rag-architect`
- **Prompt quality or effectiveness deteriorates** -> `senior-prompt-engineer`
- **Broader monitoring stack beyond cost metrics** -> `observability-designer`
- **Latency profiling becomes the primary concern** -> `performance-profiler`

---

## Output Artifacts

| Request | Deliverable |
|---|---|
| Any optimization or audit | **Ladder table** from `cost_ladder.py` for each hot path: current rung, cost per run and per month at L1-L4, and which rungs are skipped and why |
| Code changes | Concrete diffs per rung (trim cap, `cache_control` placement, batch submission + result handling), each tagged answer-neutral or needs-eval |
| Cost audit | Per-feature spend breakdown, top 3 targets, projected savings |
| Routing design | Decision tree with model per task type and cost delta |
| Architecture review | Cost-efficiency scorecard (0-100) with prioritized fixes and projected monthly savings |

---

## Communication Standard

- **Bottom line first** -- "$X/month -> $Y/month (Nx)", then the explanation.
- **What + Why + How** for every finding.
- **Confidence tagging** -- measured (from logs or `usage`) / calculated (calculator on code-derived token counts) / assumed (labeled guess).
- **Name the rate date** -- every dollar figure carries the `pricing.json` retrieval date.

---

## Anti-Patterns

| Anti-Pattern | Why It Fails | Better Approach |
|---|---|---|
| Quoting cache savings from a flat "0.1x" rule | Read multipliers are model-specific (0.025x-0.1x); writes cost 1.25x (5m) or 2x (1h) | Price from the dated rate table via the calculator |
| Calling batching a 10-25% "overhead" win | The Message Batches API is a flat 50% discount on every token, and it stacks with caching | Route every non-interactive job through the Batch API |
| Caching a single request, or requests hours apart | Pays the write premium with nothing to re-read | Let the calculator decide; it skips caching when it doesn't pay |
| Using the largest model for every request | 5-10x overspend on simple tasks | Route by complexity, then re-run the ladder |
| Optimizing without measuring | You cannot know what to optimize | Instrument, or at least calculate from code |
| Caching by exact string match on responses only | Phrasing variants miss | Semantic response cache, scoped to stable answers |
| One global `max_tokens` | Wastes or truncates | Per-endpoint caps from measured p95 |
| Treating cost work as one-time | Prices, traffic, and models drift | Weekly spend report, cache-hit and batch-share tracking, and re-run the ladder on model changes |
| Trimming to the cheapest context without an eval | Saves tokens, loses answers, triggers retries | Trim to the smallest context that passes the eval |
