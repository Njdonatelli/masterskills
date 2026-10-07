---
name: "product-skills"
description: >-
  U—s—e— —w—h—e—n— —c—o—o—r—d—i—n—a—t—i—n—g— —p—r—o—d—u—c—t— —w—o—r—k— —a—c—r—o—s—s— —t—h—e— —1—2— —b—u—n—d—l—e—d— —p—r—o—d—u—c—t— —s—u—b—-—s—k—i—l—l—s— —(—R—I—C—E—,— —O—K—R—s—,— —U—X— —r—e—s—e—a—r—c—h—,— —d—e—s—i—g—n— —t—o—k—e—n—s—,— —c—o—m—p—e—t—i—t—i—v—e— —t—e—a—r—d—o—w—n—,— —a—n—a—l—y—t—i—c—s—,— —e—x—p—e—r—i—m—e—n—t—s—,— —d—i—s—c—o—v—e—r—y—,— —r—o—a—d—m—a—p—s—,— —s—p—e—c—-—t—o—-—r—e—p—o—,— —l—a—n—d—i—n—g— —p—a—g—e—s—,— —S—a—a—S— —s—c—a—f—f—o—l—d—i—n—g—)— —o—r— —t—h—e— —4— —s—t—a—n—d—a—l—o—n—e— —p—r—o—d—u—c—t—-—t—e—a—m— —p—l—u—g—i—n—s— —(—u—s—e—r— —s—t—o—r—i—e—s—,— —A—p—p—l—e— —H—I—G—,— —c—o—d—e—-—t—o—-—P—R—D—,— —r—e—s—e—a—r—c—h— —s—u—m—m—a—r—i—z—e—r—)—.— —T—r—i—g—g—e—r—s— —o—n— —'—h—e—l—p— —m—e— —p—r—i—o—r—i—t—i—z—e—'—,— —'—p—l—a—n— —a— —p—r—o—d—u—c—t— —e—x—p—e—r—i—m—e—n—t—'—,— —'—w—e— —s—h—i—p— —f—e—a—t—u—r—e—s— —n—o—b—o—d—y— —u—s—e—s—'—,— —'—r—u—n— —t—h—e— —d—i—s—c—o—v—e—r—y— —l—o—o—p—'—,— —'—i—s— —o—u—r— —O—S—T— —s—o—u—n—d—'—.— —F—o—r—k—s— —c—o—n—t—e—x—t— —t—o— —r—o—u—t—e— —t—o— —o—n—e— —s—u—b—-—s—k—i—l—l— —v—i—a— —a— —d—e—t—e—r—m—i—n—i—s—t—i—c— —s—i—g—n—a—l— —r—o—u—t—e—r— —a—n—d— —r—e—t—u—r—n—s— —a— —d—i—g—e—s—t—;— —c—a—n— —a—l—s—o— —d—r—i—v—e— —a— —c—o—n—t—i—n—u—o—u—s—-—d—i—s—c—o—v—e—r—y— —l—o—o—p— —(—T—o—r—r—e—s— —c—a—d—e—n—c—e— —t—r—a—c—k—e—r— —+— —O—S—T— —l—i—n—t—e—r— —a—s— —m—a—c—h—i—n—e— —g—a—t—e—s—)— —o—r— —a— —f—u—l—l— —g—o—a—l—→—p—l—a—n—→—e—x—e—c—u—t—e—→—v—e—r—i—f—y—→—c—l—o—s—e— —r—u—n— —t—h—r—o—u—g—h— —t—h—e— —r—e—p—o—-—w—i—d—e— —a—g—e—n—t—-—h—a—r—n—e—s—s—.— —D—i—s—t—i—n—c—t— —f—r—o—m— —p—r—o—j—e—c—t—-—m—a—n—a—g—e—m—e—n—t— —(—h—o—w— —t—o— —d—e—l—i—v—e—r— —v—s— —w—h—a—t— —t—o— —b—u—i—l—d—)—,— —m—a—r—k—e—t—i—n—g—/—l—a—n—d—i—n—g— —(—f—r—o—m—-—s—c—r—a—t—c—h— —p—a—g—e—s—)—,— —a—n—d— —e—n—g—i—n—e—e—r—i—n—g—/—a—g—e—n—t—-—h—a—r—n—e—s—s— —(—t—h—e— —g—e—n—e—r—i—c— —l—o—o—p— —e—n—g—i—n—e— —t—h—i—s— —o—r—c—h—e—s—t—r—a—t—o—r— —p—l—u—g—s— —i—n—t—o—).
context: fork
version: 2.11.1
author: Alireza Rezvani
license: MIT
tags: [product, product-management, orchestrator, discovery, ux, analytics, agent-harness]
compatible_tools: [claude-code, codex-cli, cursor, antigravity, opencode, gemini-cli]
---

# Product Team — Domain Orchestrator & Discovery Loop

This orchestrator does two jobs. **Routing:** fork context, classify a product inquiry
with `scripts/product_goal_router.py` across all 16 product-team lanes (12 bundled + 4
standalone plugins), run exactly one, return a digest. **Looping:** run product work as
bounded agentic loops with machine-checkable gates — the continuous-discovery loop
(weekly cadence scored by `discovery_cadence_tracker.py`, tree structure enforced by
`ost_linter.py`) and goal-scale runs through the repo-wide agent-harness.

## When to invoke

| Symptom | Sub-skill |
|---|---|
| "Prioritize features / RICE / PRD" | `product-manager-toolkit` |
| "OKRs, strategy cascade" | `product-strategist` |
| "Personas, usability, research synthesis" | `ux-researcher-designer` |
| "Design tokens, WCAG contrast" | `ui-design-system` |
| "Competitor matrix, teardown" | `competitive-teardown` |
| "Retention, cohorts, funnels, KPIs" | `product-analytics` |
| "A/B test, sample size, hypothesis" | `experiment-designer` |
| "Discovery, assumptions, opportunity trees" | `product-discovery` |
| "Roadmap comms, release notes, changelog" | `roadmap-communicator` |
| "Spec → runnable repo" | `spec-to-repo` |
| "Landing page (Next.js/Tailwind)" | `landing-page-generator` |
| "SaaS boilerplate" | `saas-scaffolder` |
| "User stories, sprint capacity" | `agile-product-owner` (standalone) |
| "Apple HIG audit" | `apple-hig-expert` (standalone) |
| "PRD from an existing codebase" | `code-to-prd` (standalone) |
| "Summarize papers/articles" | `research-summarizer` (standalone) |

## Routing logic (deterministic)

```bash
python3 scripts/product_goal_router.py --text "<the goal>" --output json
```

Exit 0 → `route_to` names the skill (with `skill_path`, including the standalone
plugins): load its SKILL.md and follow its workflow. Exit 2 → ask ONE clarifying question
naming the listed candidates, with a recommended answer. Exit 3 → no signal: ask the user
to restate the goal with the deliverable named. Never guess silently; never silently
chain — digest first, confirm, then chain.

## The discovery loop (the domain's recurring agentic loop)

Modern discovery is a weekly habit, not a project phase (Torres). Run it as a bounded
loop with two machine gates:

1. **Observe** — maintain `discovery_log.json` (interviews, assumption tests; shape in
   `assets/sample_discovery_log.json`) and score the cadence:
   ```bash
   python3 scripts/discovery_cadence_tracker.py --input discovery_log.json
   ```
   Refuses on < 2 interviews (exit 5) — there is no cadence to measure yet. Output:
   health 0–100, verdict HEALTHY/AT-RISK/DORMANT, named gaps, and `next_loop_action`.
2. **Choose** — the tracker's `next_loop_action` IS the choice: book the touchpoint,
   re-anchor the guide on the outcome, or test the top untested assumption (route to
   `product-discovery`'s assumption_mapper for prioritization).
3. **Act** — run the interview / assumption test with the routed sub-skill's tools.
4. **Verify** — keep the tree structurally sound before it may drive a roadmap:
   ```bash
   python3 scripts/ost_linter.py --input ost.json    # exit 2 = NEEDS-REWORK, fix before citing the tree
   ```
   Rules: one measurable outcome root (O1), opportunities are needs not features (O2),
   targeted opportunities compare ≥ 2 solutions (O3), every solution has an assumption
   test (O4), no orphan solutions (O5 — the feature-factory tell).
5. **Record / Repeat-or-stop** — update the log, keep the weekly streak alive. Stop
   states: HEALTHY + validated assumption → graduate to `experiment-designer` (build the
   A/B gate) or `product-manager-toolkit` (PRD); DORMANT for 4+ weeks → escalate to the
   product lead by name — do not quietly let discovery die.

For build-scale goals ("turn this validated spec into a repo and verify it"), compile
through the repo-wide harness instead:

```bash
python3 engineering/agent-harness/skills/agent-harness/scripts/goal_compiler.py \
  --goal "<goal>" --manifest engineering/agent-harness/skills/agent-harness/assets/harnesses/product-team.json \
  --out .agent-harness/plan.json
```

The domain's three strongest close-out gates plug in as task verifications:
`../spec-to-repo/scripts/validate_project.py` (exit 0), `code-to-prd`'s golden
`expected_outputs/`, and `research-summarizer`'s citation-count check.

## Hard rules

1. **Evidence before conviction**: no roadmap item cites the OST unless `ost_linter.py`
   exits 0; no insight is asserted from a single participant (anecdote, not insight).
2. **Outcome-first**: every loop hangs from one measurable outcome — the linter's O1 rule
   is the intake gate.
3. **Experiments are gated by math**: sample size from
   `../experiment-designer/scripts/sample_size_calculator.py`, never gut feel; report the
   MDE with the verdict.
4. **Prioritization shows its framework**: RICE for steady-state, WSJF/cost-of-delay when
   time sensitivity dominates, opportunity scoring for underserved needs — name which and
   why (see [references/product_operating_model.md](references/product_operating_model.md)).
5. **AI features ship with evals**: a golden set + rubric is the PRD's quality contract
   for probabilistic features
   ([references/ai_product_evals.md](references/ai_product_evals.md)).
6. **Never modify a gate you are judged by**; exhausted budgets escalate to a named human,
   never report as success.

## Forcing-question library (grill-with-docs pattern)

One per turn, recommended answer, canon citation. Never run a sub-skill or start a loop
until the lane-defining decision is locked:

- **DISCOVERY lane**: "What is the single outcome this discovery serves, stated with a
  number? Recommended: write it as the OST root first — opportunities without an outcome
  are a feature factory. Canon: Torres, *Continuous Discovery Habits*; opportunity
  solution trees (producttalk.org)."
- **PRIORITIZE lane**: "Does time sensitivity change this ranking — would delaying any
  item a quarter erode its value? Recommended: if yes, run WSJF/cost-of-delay alongside
  RICE and compare ranks; flag items whose rank flips on a one-step estimate change.
  Canon: Reinertsen, *Principles of Product Development Flow*; SAFe WSJF false-precision
  critique."
- **EXPERIMENT lane**: "What baseline rate and MDE justify this test's runtime?
  Recommended: compute n first; if you can't reach it in 4 weeks, test a bigger lever.
  Canon: statistical power analysis (experiment-designer)."
- **ANALYTICS lane**: "Is your North Star a leading indicator of value exchange, or
  revenue/vanity? Recommended: leading value metric with an input tree. Canon: Amplitude,
  *The North Star Playbook*."
- **STRATEGY lane**: "Are these OKRs outcomes or shipping lists? Recommended: outcomes —
  output OKRs are the #1 operating-model failure. Canon: Cagan, *Transformed* (SVPG,
  2024)."
- **BUILD lanes (spec-to-repo / saas-scaffolder)**: "Which validated assumption says this
  should be built at all? Recommended: link the OST test that survived; building is the
  most expensive way to test an idea. Canon: Torres; Bland, *Testing Business Ideas*."

## Assumptions

1. The user owns (or advises the owner of) the product decision.
2. Discovery data lives in the workspace as JSON logs — the loop is file-backed and
   resumable; every tool ships `--sample` so the shape is visible first.
3. The four standalone plugins are installed alongside the bundle (the router still
   routes to them by path if not).

## Non-goals

- Not the delivery loop — sprint/flow/Jira work routes to `project-management`.
- Not the generic loop engine — that is `engineering/agent-harness`; this orchestrator is
  the product-domain adapter (router + discovery gates).
- Not campaign marketing — `marketing/landing` builds from-scratch marketing pages;
  `landing-page-generator` here scaffolds product Next.js/TSX pages.

## Output artifacts

| Mode | Artifact |
|---|---|
| Route | Sub-skill's own artifact + ≤ 200-word digest with one canon-cited challenge |
| Discovery loop | `discovery_log.json` + cadence report + linted `ost.json` |
| Harness run | `.agent-harness/plan.json` + `state.json` + close handoff |

## Anti-patterns (do not)

- ❌ Run all 16 lanes "to be thorough" — route to one, digest, chain on confirmation
- ❌ Cite an OST that fails the linter, or promote a single-participant anecdote to insight
- ❌ Ship an AI feature whose PRD has no eval (golden set + rubric)
- ❌ Let the discovery streak die silently — DORMANT escalates by name
- ❌ Treat RICE as the only prioritization lens when deadlines dominate

## References

- [references/continuous_discovery_canon.md](references/continuous_discovery_canon.md) —
  Torres, OST, assumption testing, JTBD switch interviews, story mapping
- [references/product_operating_model.md](references/product_operating_model.md) — Cagan
  *Transformed*, North Star framework, PLG benchmarks, WSJF/ODI vs RICE
- [references/ai_product_evals.md](references/ai_product_evals.md) — evals-as-PRD, model
  cards, evaluator-optimizer loops
- Loop engine: `engineering/agent-harness` · Loop vocabulary: `loop-library`
