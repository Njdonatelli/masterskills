---
name: market-research
description: >-
  U—s—e— —w—h—e—n— —d—o—i—n—g— —u—p—s—t—r—e—a—m— —m—a—r—k—e—t—-—r—e—s—e—a—r—c—h— —m—e—t—h—o—d—o—l—o—g—y— ——— —s—i—z—i—n—g— —a— —m—a—r—k—e—t— —a—s— —T—A—M—/—S—A—M—/—S—O—M— —c—o—m—p—u—t—e—d— —B—O—T—H— —t—o—p—-—d—o—w—n— —a—n—d— —b—o—t—t—o—m—s—-—u—p— —(—n—e—v—e—r— —a— —s—i—n—g—l—e— —u—n—s—o—u—r—c—e—d— —n—u—m—b—e—r—)—,— —p—l—a—n—n—i—n—g— —a— —s—u—r—v—e—y— —s—a—m—p—l—e— —s—i—z—e— —w—i—t—h— —f—i—n—i—t—e—-—p—o—p—u—l—a—t—i—o—n— —c—o—r—r—e—c—t—i—o—n— —a—n—d— —p—e—r—-—s—e—g—m—e—n—t— —m—i—n—i—m—u—m—s—,— —o—r— —s—c—o—r—i—n—g— —c—a—n—d—i—d—a—t—e— —m—a—r—k—e—t— —s—e—g—m—e—n—t—s— —a—g—a—i—n—s—t— —K—o—t—l—e—r—'—s— —m—e—a—s—u—r—a—b—l—e—/—s—u—b—s—t—a—n—t—i—a—l—/—a—c—c—e—s—s—i—b—l—e—/—d—i—f—f—e—r—e—n—t—i—a—b—l—e—/—a—c—t—i—o—n—a—b—l—e— —c—r—i—t—e—r—i—a—.— —O—u—t—p—u—t—s— —a—l—w—a—y—s— —s—h—o—w— —t—h—e— —m—e—t—h—o—d— —a—n—d— —t—h—e— —a—s—s—u—m—p—t—i—o—n—s—.— —F—o—r— —m—a—r—k—e—t—-—r—e—s—e—a—r—c—h— —a—n—a—l—y—s—t—s— —a—n—d— —p—r—o—d—u—c—t—-—m—a—r—k—e—t—i—n—g— —a—t— —t—h—e— —s—i—z—i—n—g—/—s—u—r—v—e—y—/—s—e—g—m—e—n—t—a—t—i—o—n— —m—o—m—e—n—t—.— —D—i—s—t—i—n—c—t— —f—r—o—m— —m—a—r—k—e—t—i—n—g—-—s—k—i—l—l— —(—c—a—m—p—a—i—g—n— —a—n—a—l—y—t—i—c—s—,— —a—t—t—r—i—b—u—t—i—o—n—,— —d—e—m—a—n—d—-—g—e—n—)— ——— —t—h—i—s— —i—s— —t—h—e— —e—v—i—d—e—n—c—e—-—b—u—i—l—d—i—n—g— —m—e—t—h—o—d—o—l—o—g—y—,— —n—o—t— —l—i—v—e—-—c—a—m—p—a—i—g—n— —o—p—t—i—m—i—z—a—t—i—o—n.
version: 2.9.0
author: claude-code-skills
license: MIT
tags: [research-ops, market-research, tam-sam-som, market-sizing, survey, sampling, segmentation, competitive-intelligence]
compatible_tools: [claude-code, codex-cli, cursor, antigravity, opencode, gemini-cli]
---

# market-research

Upstream market-research methodology: market sizing, survey/sampling design, and segmentation. The discipline here is **method + assumptions**: a TAM is never a single number, a survey is never powered only in aggregate, and a segment is never a demographic slice.

## Purpose

Market-research analysts, product marketers, and strategy teams need rigorous evidence *before* anyone optimizes a campaign or sets a strategy. This skill structures three methodology decisions:

Three deterministic tools:

1. `market_sizer.py` — Computes TAM/SAM/SOM by **both** top-down and bottoms-up methods side-by-side, reports the divergence, and flags failed triangulation. Never returns a single number.
2. `sample_size_planner.py` — Survey sample size from confidence, margin of error, and expected proportion, with the finite-population correction and **per-segment minimums** (a survey powered overall is not powered per reported segment).
3. `segmentation_scorer.py` — Scores candidate segments against Kotler's five criteria and enforces a substantiality + accessibility gate; a slice that is too small or unreachable is dropped.

## When to use

Invoke this skill when:

- A board or exec asks "how big is this market?" and you need a defensible, triangulated answer.
- You are fielding a survey and need a sample size that holds up per segment, not just overall.
- You have a list of candidate segments and need to know which are real markets vs demographic slices.
- You are synthesizing competitive intelligence and need a methodological backbone.

**Do NOT use this skill to**: measure a live campaign (attribution, ROAS, CPA → `marketing-skill/campaign-analytics`), build demand-gen / paid-media plans (`marketing-skill/marketing-demand-acquisition`), set positioning / GTM strategy (`marketing-skill/marketing-strategy-pmm`), or set pricing (`commercial/pricing-strategist`).

## Workflow

1. **Write the brief** — Fill `assets/market_research_brief_template.md` (objective, the decision this informs, sizing approach, sampling plan, assumptions register).
2. **Size the market** — Run `market_sizer.py --input market.json --method both --profile {b2b-saas|consumer|enterprise|marketplace|hardware|services}`. Reconcile the top-down/bottoms-up delta before quoting anything.
3. **Plan the survey** — Run `sample_size_planner.py --input survey.json`. Fund the per-segment floors, not just the overall n.
4. **Score the segments** — Run `segmentation_scorer.py --input segments.json --profile <same>`. Drop segments failing the substantiality/accessibility gate.
5. **Assemble the evidence pack** — Combine into a brief. Every number carries its method + assumptions + confidence.

## Scripts

| Script | Purpose | Profiles |
|---|---|---|
| `scripts/market_sizer.py` | TAM/SAM/SOM top-down AND bottoms-up + triangulation flag | b2b-saas, consumer, enterprise, marketplace, hardware, services |
| `scripts/sample_size_planner.py` | Survey n + FPC + per-segment minima | n/a (parameter-driven) |
| `scripts/segmentation_scorer.py` | Kotler 5-criteria scoring + gate | b2b-saas, consumer, enterprise, marketplace, hardware, services |

All three: stdlib-only, `--help`, `--sample`, `--output {human,json}`.

## Onboarding & customization

Run the onboarding questionnaire **once before you start** — it captures your defaults so every tool in this skill is pre-configured. Customization is the point: the answers actually change tool behavior.

```bash
python3 scripts/onboard.py            # interactive (also: --defaults, --set key=value, --reset)
python3 scripts/onboard.py --show     # see the questions + current effective config
```

Answers are saved to `~/.config/research-ops/market-research.json` (global) or `./.research-ops/market-research.json` (`--scope project`) and are read automatically by `config_loader.py`. They set the default market **profile**, the default survey **confidence** and **margin of error**, and the default **sizing method**. CLI flags always override saved config; `RESEARCH_OPS_NO_CONFIG=1` ignores it.

**The four questions:** market profile · survey confidence · margin of error · sizing method.

## Optimize with autoresearch (opt-in)

This skill ships an **isolated, opt-in** bridge to `engineering/autoresearch-agent`. Only when you ask to "optimize" / "reconcile the sizing" / "run a loop" does an autoresearch experiment iteratively reconcile your market model so top-down and bottoms-up triangulate. `scripts/ar_evaluator.py` is the ground-truth evaluator; it prints `tam_divergence: <fraction>` (**lower** is better).

```bash
/ar:setup --domain custom --name tam-triangulation \
  --target market.json \
  --eval "python3 ar_evaluator.py --target market.json" \
  --metric tam_divergence --direction lower
/ar:loop custom/tam-triangulation
```

Isolated: no hard dependency — autoresearch runs only on demand, and the loop edits `market.json`, never the evaluator.

## References

- `references/market_sizing_canon.md` — TAM/SAM/SOM frameworks (Bessemer, a16z); top-down vs bottoms-up; Fermi estimation; market-model conventions; common sizing fallacies.
- `references/survey_methodology.md` — Cochran *Sampling Techniques*; Dillman *Tailored Design Method*; Groves *Survey Methodology*; question-wording bias (Schuman & Presser); AAPOR standards.
- `references/segmentation_and_ci.md` — Kotler segmentation criteria; needs-based vs firmographic; Porter Five Forces; SCIP ethics; Christensen JTBD; conjoint/MaxDiff primer.

## Assumptions

- The sizer reports both methods but cannot validate your inputs — a top-down "1% of a $40B market" is only as good as the cited source and the serviceable fraction.
- Sample-size uses the conservative p=0.5 (maximum variance) unless you supply an expected proportion.
- Segment scores are inputs you provide; the tool enforces the gates and the weighting, it does not gather the underlying evidence.
- Competitive intelligence must follow the SCIP code of ethics — no misrepresentation, no protected information.

## Anti-patterns

- **A single TAM number with no method.** Always triangulate top-down against bottoms-up.
- **Spurious precision.** Size to the decision's tolerance; "$3.7142B" implies a confidence you do not have.
- **Powering only the total.** Each reported segment needs its own sample floor.
- **Leading or double-barreled survey questions.** Pre-test wording against the bias literature.
- **Calling a demographic slice a segment.** It must be substantial AND accessible.

## Distinct from

| Neighbor | Scope | Difference |
|---|---|---|
| `marketing-skill/campaign-analytics` | Attribution, ROAS, CPA, funnel of a live campaign | That **measures spend deployed**; this is **upstream methodology** |
| `marketing-skill/marketing-demand-acquisition` | Demand-gen, paid media, channel mix | That **runs acquisition**; this **builds the evidence** |
| `marketing-skill/marketing-strategy-pmm` | Positioning, GTM, category | That **sets strategy**; this **sizes and segments the market** |
| `commercial/pricing-strategist` | Pricing model + WTP + packaging | That **sets price**; this **sizes the market** |
| `product-research` (sibling) | User/product discovery methods | That studies **users**; this studies **the market** |

## Quick examples

```bash
python3 scripts/market_sizer.py --sample
python3 scripts/sample_size_planner.py --population 62000 --confidence 0.95 --moe 0.05
python3 scripts/segmentation_scorer.py --sample --output json
```

The sample market triangulates a ~$1.47B top-down SAM against the bottoms-up figure and flags the divergence; the segmentation sample drops the "solopreneurs who might want analytics" slice for failing the substantiality and accessibility gates.

## Forcing-question library (Matt Pocock grill discipline)

Walked one at a time by `/cs:grill-research-ops` or the orchestrator. Recommended answer + canon citation per question. Never bundled.

1. **"Is your TAM top-down or bottoms-up — and have you computed it both ways to triangulate?"**
   Recommended: both; reconcile the delta before quoting a number.
   Canon: Bessemer / a16z market-sizing; Fermi estimation.

2. **"What decision will this market size actually drive — and at what precision does it matter?"**
   Recommended: size to the decision's tolerance, not to a spurious-precision number.
   Canon: market-model conventions (Gartner/Forrester); decision-driven analysis.

3. **"What's your target margin of error and confidence — and does your sample clear it per segment, not just overall?"**
   Recommended: power each reported segment, not only the total.
   Canon: Cochran *Sampling Techniques*; AAPOR standards.

4. **"Are your survey questions free of leading and double-barreled wording?"**
   Recommended: pre-test the wording; cite the bias source.
   Canon: Schuman & Presser; Dillman *Tailored Design Method*.

5. **"Do your segments pass measurable / substantial / accessible / actionable — or are they just demographic slices?"**
   Recommended: drop segments that fail substantiality or accessibility.
   Canon: Kotler segmentation criteria.

Walk depth-first. Lock 1-2 before opening 3-5. After all are answered, invoke `market_sizer.py` → `sample_size_planner.py` → `segmentation_scorer.py`.
