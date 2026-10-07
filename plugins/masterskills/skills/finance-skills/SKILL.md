---
name: "finance-skills"
description: >-
  R—o—u—t—e—r—/—i—n—d—e—x— —f—o—r— —t—h—e— —2— —f—i—n—a—n—c—e— —s—k—i—l—l—s— —b—u—n—d—l—e—d— —i—n— —t—h—i—s— —p—l—u—g—i—n—:— —f—i—n—a—n—c—i—a—l—-—a—n—a—l—y—s—t— —(—r—a—t—i—o— —a—n—a—l—y—s—i—s—,— —D—C—F— —v—a—l—u—a—t—i—o—n—,— —b—u—d—g—e—t— —v—a—r—i—a—n—c—e—,— —r—o—l—l—i—n—g— —f—o—r—e—c—a—s—t—s—)— —a—n—d— —s—a—a—s—-—m—e—t—r—i—c—s—-—c—o—a—c—h— —(—A—R—R—/—M—R—R—,— —c—h—u—r—n—,— —C—A—C—/—L—T—V—,— —N—R—R—,— —q—u—i—c—k— —r—a—t—i—o—)—.— —U—s—e— —w—h—e—n— —a— —f—i—n—a—n—c—e— —r—e—q—u—e—s—t— —d—o—e—s—n—'—t— —o—b—v—i—o—u—s—l—y— —m—a—t—c—h— —o—n—e— —s—k—i—l—l— —a—n—d— —y—o—u— —n—e—e—d— —t—o— —p—i—c—k— —t—h—e— —r—i—g—h—t— —o—n—e— —(—e—.—g—.—,— —'—a—n—a—l—y—z—e— —t—h—e—s—e— —f—i—n—a—n—c—i—a—l—s—'—,— —'—h—o—w— —h—e—a—l—t—h—y— —a—r—e— —m—y— —S—a—a—S— —m—e—t—r—i—c—s—'—).
version: 2.9.0
author: Alireza Rezvani
license: MIT
tags:
  - finance
  - financial-analysis
  - dcf
  - valuation
  - budgeting
agents:
  - claude-code
  - codex-cli
  - openclaw
---

# Finance Skills — Router

This plugin bundles **2 finance skills** (this router is the 3rd folder under `finance/skills/`). Each skill is self-contained.

## Routing table

| Request signals | Skill | Path |
|---|---|---|
| Ratio analysis, DCF valuation, budget variance, driver-based forecasts | financial-analyst | `skills/financial-analyst/` |
| ARR/MRR, churn, CAC/LTV, NRR, quick ratio, SaaS benchmarks | saas-metrics-coach | `skills/saas-metrics-coach/` |

If both match (e.g., "value my SaaS company"), ask whether the user wants statement-level analysis (financial-analyst) or SaaS operating metrics (saas-metrics-coach).

## Quick start

```bash
# Example: route a statement-analysis request
cat finance/skills/financial-analyst/SKILL.md
python3 finance/skills/financial-analyst/scripts/ratio_calculator.py --help

# Or a SaaS metrics request
python3 finance/skills/saas-metrics-coach/scripts/metrics_calculator.py --help
```

## Related (packaged separately, not in this bundle)

- `finance/business-investment-advisor/` — investment thesis evaluation, ROI modeling (prompt-only skill, separate nested plugin)
- Root commands `/financial-health` and `/saas-health` wrap these skills' scripts.

## Rules

- Route to exactly one skill, then follow that skill's workflow. This router ships no tools of its own.
- Always validate financial outputs against the user's source data; outputs are analysis support, not investment advice.
