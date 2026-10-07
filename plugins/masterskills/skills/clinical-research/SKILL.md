---
name: clinical-research
description: >-
  U—s—e— —w—h—e—n— —d—e—s—i—g—n—i—n—g— —a— —p—r—o—s—p—e—c—t—i—v—e— —c—l—i—n—i—c—a—l— —s—t—u—d—y— —b—e—f—o—r—e— —s—u—b—m—i—s—s—i—o—n— ——— —s—e—l—e—c—t—i—n—g— —a—n—d— —c—l—a—s—s—i—f—y—i—n—g— —e—n—d—p—o—i—n—t—s— —(—p—r—i—m—a—r—y— —/— —k—e—y—-—s—e—c—o—n—d—a—r—y— —/— —e—x—p—l—o—r—a—t—o—r—y—,— —w—i—t—h— —s—u—r—r—o—g—a—t—e—-—e—n—d—p—o—i—n—t— —f—l—a—g—g—i—n—g—)—,— —e—s—t—i—m—a—t—i—n—g— —s—a—m—p—l—e— —s—i—z—e— —a—n—d— —p—o—w—e—r— —f—o—r— —t—w—o—-—a—r—m— —d—e—s—i—g—n—s— —(—m—e—a—n—s— —/— —p—r—o—p—o—r—t—i—o—n—s— —/— —s—u—r—v—i—v—a—l—)—,— —o—r— —s—c—o—r—i—n—g— —a— —s—t—u—d—y— —p—l—a—n— —f—o—r— —f—e—a—s—i—b—i—l—i—t—y— —a—n—d— —a— —G—O— —/— —G—O—-—W—I—T—H—-—C—O—N—D—I—T—I—O—N—S— —/— —R—E—D—E—S—I—G—N— —/— —N—O—-—G—O— —p—h—a—s—e—-—g—a—t—e— —d—e—c—i—s—i—o—n—.— —E—v—e—r—y— —o—u—t—p—u—t— —i—s— —a—n— —E—S—T—I—M—A—T—E— —p—l—u—s— —a— —n—a—m—e—d— —h—u—m—a—n— —o—w—n—e—r— —(—c—l—i—n—i—c—i—a—n— —/— —b—i—o—s—t—a—t—i—s—t—i—c—i—a—n— —/— —r—e—g—u—l—a—t—o—r—y— —o—w—n—e—r—)— ——— —n—e—v—e—r— —c—l—i—n—i—c—a—l— —f—a—c—t—,— —n—e—v—e—r— —a— —f—i—n—i—s—h—e—d— —p—r—o—t—o—c—o—l—.— —D—i—s—t—i—n—c—t— —f—r—o—m— —r—a—-—q—m—-—t—e—a—m—,— —w—h—i—c—h— —h—a—n—d—l—e—s— —t—h—e— —r—e—g—u—l—a—t—o—r—y—/—Q—M— —s—u—b—m—i—s—s—i—o—n— —(—I—S—O— —1—3—4—8—5—,— —E—U— —M—D—R—,— —F—D—A— —5—1—0—(—k—)—/—P—M—A—/—Q—S—R—)—,— —n—o—t— —t—h—e— —s—t—u—d—y— —d—e—s—i—g—n.
version: 2.9.0
author: claude-code-skills
license: MIT
tags: [research-ops, clinical-research, study-design, endpoint, sample-size, power, phase-gate, biostatistics]
compatible_tools: [claude-code, codex-cli, cursor, antigravity, opencode, gemini-cli]
---

# clinical-research

Prospective clinical study DESIGN: endpoints, sample size / power, and phase-gate feasibility. Every output is an **estimate with stated assumptions** routed to a **named human owner**. This skill never gives clinical advice as fact and never substitutes for a biostatistician or regulatory affairs.

## Purpose

R&D clinical teams, medical monitors, and biostatistics functions live at the moment between *we-have-a-hypothesis* and *we-have-a-protocol-ready-for-submission*. This skill structures three of the hardest design decisions:

Three deterministic tools:

1. `sample_size_estimator.py` — Closed-form power / sample-size for two-arm **means** (Cohen's d), **proportions** (normal approximation), and **survival** (Schoenfeld events). Inflates for dropout. Prints an "ESTIMATE — confirm with a biostatistician" banner.
2. `endpoint_selector.py` — Scores candidate endpoints across 5 weighted dimensions (clinical relevance, measurability, regulatory acceptance, sensitivity-to-change, burden) and classifies each as **PRIMARY / KEY-SECONDARY / EXPLORATORY**. Penalizes unvalidated surrogate endpoints.
3. `phase_gate_scorer.py` — Scores a study plan 0-100 across recruitment feasibility, endpoint readiness, statistical power, operational complexity, and budget fit; returns **GO / GO-WITH-CONDITIONS / REDESIGN / NO-GO** plus the named owners who must sign.

## When to use

Invoke this skill when:

- You are choosing a primary endpoint and need to defend it against surrogate-endpoint scrutiny.
- You need a defensible first sample-size estimate for a protocol synopsis.
- A study plan needs a feasibility read before a phase-gate review.
- You are pressure-testing whether the planned enrollment is achievable given the eligible population and sites.

**Do NOT use this skill to**: prepare a regulatory submission or clinical evaluation report (use `ra-qm-team`), find or position a grant (use `research/grants`), design a live product A/B experiment (use `product-team/experiment-designer`), or replace a biostatistician's final sample-size justification.

## Workflow

1. **Draft the synopsis** — Fill `assets/protocol_synopsis_template.md` (objectives, design, population, endpoints, statistical plan placeholder, owners-to-sign).
2. **Select the endpoint** — Run `endpoint_selector.py --input endpoints.json --profile {drug|device|biologic|diagnostic|digital-therapeutic}`. Read the classification + surrogate flags. If >1 primary, plan multiplicity control.
3. **Estimate the sample size** — Run `sample_size_estimator.py --design {means|proportions|survival} ...`. Trace the effect/difference/HR to a published or anchor-based source; inflate for dropout.
4. **Score feasibility** — Run `phase_gate_scorer.py --input study.json --profile <same> --phase {1|2|3|4}`. Read the verdict + blockers + named owners.
5. **Route for sign-off** — Assemble the synopsis + estimates into the gate packet. The packet is **a recommendation**; a biostatistician, medical monitor, and regulatory owner sign.

## Scripts

| Script | Purpose | Profiles |
|---|---|---|
| `scripts/sample_size_estimator.py` | Power / sample-size for means, proportions, survival | n/a (design-driven) |
| `scripts/endpoint_selector.py` | 5-dimension endpoint scoring + classification + surrogate flag | drug, device, biologic, diagnostic, digital-therapeutic |
| `scripts/phase_gate_scorer.py` | Feasibility 0-100 + GO/GO-WITH-CONDITIONS/REDESIGN/NO-GO + owners | drug, device, biologic, diagnostic, digital-therapeutic |

All three: stdlib-only, `--help`, `--sample`, `--output {human,json}`.

## Onboarding & customization

Run the onboarding questionnaire **once before you start** — it captures your defaults and named owners so every tool in this skill is pre-configured. Customization is the point: the answers actually change tool behavior.

```bash
python3 scripts/onboard.py            # interactive (also: --defaults, --set key=value, --reset)
python3 scripts/onboard.py --show     # see the questions + current effective config
```

Answers are saved to `~/.config/research-ops/clinical-research.json` (global) or `./.research-ops/clinical-research.json` (`--scope project`) and are read automatically by `config_loader.py`. They set the default development-area **profile**, default **alpha / power / dropout**, and the named **biostatistician / medical monitor / regulatory owner** printed on outputs. CLI flags always override saved config; `RESEARCH_OPS_NO_CONFIG=1` ignores it entirely.

**The seven questions:** development area · alpha · power · dropout · biostatistician · medical monitor · regulatory owner.

## Optimize with autoresearch (opt-in)

This skill ships an **isolated, opt-in** bridge to `engineering/autoresearch-agent`. Only when you ask to "optimize" / "run a loop" does an autoresearch experiment iteratively improve a study plan against this skill's own feasibility score. `scripts/ar_evaluator.py` is the ground-truth evaluator; it prints `feasibility_composite: <0-100>` (higher is better).

```bash
/ar:setup --domain custom --name trial-feasibility \
  --target study.json \
  --eval "python3 ar_evaluator.py --target study.json" \
  --metric feasibility_composite --direction higher
/ar:loop custom/trial-feasibility
```

Isolated: no hard dependency — autoresearch runs only on demand, and the loop edits `study.json`, never the evaluator (locked ground truth).

## References

- `references/study_design_canon.md` — ICH E8(R1) general considerations; ICH E9 + E9(R1) estimand addendum; CONSORT 2010; SPIRIT 2013; FDA Multiple Endpoints guidance (2022).
- `references/endpoint_and_power.md` — Cohen *Statistical Power Analysis*; Schoenfeld (1983) survival sample size; FDA Surrogate Endpoint Table / BEST glossary; FDA PRO guidance (2009); Chow, Shao & Wang *Sample Size Calculations in Clinical Research*.
- `references/trial_operations.md` — ICH E6(R2/R3) GCP; TransCelerate risk-based monitoring; FDA RBM guidance; CTTI recruitment best practices; site-feasibility scoring literature.

## Assumptions

- Sample-size formulas use normal approximations with a built-in z-table. They are first-pass **estimates**; a biostatistician produces the final justification (and may use simulation, adaptive designs, or exact methods).
- The endpoint scorer applies *customary* regulatory priors per development area via `--profile`. Company- or indication-specific precedent overrides the prior.
- The phase-gate scorer bakes in a profile cost-per-patient benchmark; pass a real budget to override the default.
- An unvalidated surrogate cannot anchor a PRIMARY endpoint — the scorer enforces this with a penalty.

## Anti-patterns

- **Presenting a power estimate as fact.** Every output is an estimate with a named owner who must sign.
- **Powering for a convenience effect size.** The effect must trace to a published or anchor-based MCID, not to the n you can afford.
- **Anchoring a primary on an unvalidated surrogate.** Surrogate endpoints need validation evidence for the indication.
- **Ignoring multiplicity.** More than one primary endpoint requires pre-specified alpha allocation.
- **Skipping dropout inflation.** Raw n undersizes the study; inflate by 1/(1 − dropout).

## Distinct from

| Sibling / neighbor | Scope | Difference |
|---|---|---|
| `ra-qm-team` | ISO 13485 QMS, ISO 14971 risk, EU MDR tech docs + clinical evaluation, FDA 510(k)/PMA/De Novo/QSR submission | That is the **submission**; clinical-research designs the **study** beforehand |
| `research/grants` | NIH funding discovery + positioning | That **finds funding**; this **designs the trial** |
| `product-team/experiment-designer` | Live product A/B hypothesis + sample size | That is a **product experiment**; this is a **clinical trial** |
| `research-finance` (sibling) | R&D program budget + burn | That **funds** the program; this **scopes** the study |

## Quick examples

```bash
python3 scripts/sample_size_estimator.py --sample
python3 scripts/sample_size_estimator.py --design proportions --p1 0.30 --p2 0.45 --dropout 0.15
python3 scripts/endpoint_selector.py --sample
python3 scripts/phase_gate_scorer.py --sample --output json
```

The sample correctly flags an unvalidated serum-cytokine surrogate (cannot be primary) and ranks PASI-75 as the PRIMARY endpoint; the phase-gate sample returns a verdict with a named owner chain.

## Forcing-question library (Matt Pocock grill discipline)

Walked one at a time by `/cs:grill-research-ops` or the orchestrator. Recommended answer + canon citation per question. Never bundled.

1. **"Is your primary endpoint a clinical outcome or a surrogate — and if surrogate, is it on FDA's validated table?"**
   Recommended: clinical outcome unless the surrogate is validated for this indication.
   Canon: FDA Surrogate Endpoint Table; BEST (Biomarkers, EndpointS, and other Tools) glossary.

2. **"What's the minimal clinically important difference you're powering for — and where did that number come from?"**
   Recommended: a published or anchor-based MCID, cited; never a convenience effect size.
   Canon: ICH E9; Cohen *Statistical Power Analysis*.

3. **"What dropout rate are you assuming, and is the sample size inflated for it?"**
   Recommended: inflate n by 1/(1 − dropout) using a justified rate.
   Canon: Chow, Shao & Wang; ICH E9(R1).

4. **"Single primary endpoint or multiple — and if multiple, what's the multiplicity control?"**
   Recommended: pre-specify alpha allocation (hierarchical / Bonferroni).
   Canon: FDA Multiple Endpoints guidance (2022).

5. **"Who is the named biostatistician / medical monitor / regulatory owner signing this synopsis?"**
   Recommended: name them now — this output is a recommendation, not a protocol.
   Canon: ICH E6(R2) GCP roles & responsibilities.

Walk depth-first. Lock 1-2 before opening 3-5. After all are answered, invoke `endpoint_selector.py` → `sample_size_estimator.py` → `phase_gate_scorer.py`.
