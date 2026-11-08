---
name: "cro-advisor"
description: >-
  Revenue leadership for B2B SaaS companies. Revenue forecasting, sales model design, pricing strategy, net revenue retention, and sales team scaling. Use when designing the revenue engine, setting quotas, modeling NRR, evaluating pricing, building board forecasts, or when user mentions CRO, chief revenue officer, revenue strategy, sales model, ARR growth, NRR, expansion revenue, churn, pricing strategy, or sales capacity. [Also supersedes `cro-review`: triggers on '/cs:cro-review', 'cro review', 'sales plan interrogation']
license: MIT
metadata:
  version: 1.0.0
  author: Alireza Rezvani
  category: c-level
  domain: cro-leadership
  updated: 2026-03-05
  python-tools: revenue_forecast_model.py, churn_analyzer.py
  frameworks: sales-playbook, pricing-strategy, nrr-playbook
---

# CRO Advisor

Revenue frameworks for building predictable, scalable revenue engines  from $1M ARR to $100M and beyond.

## Keywords
CRO, chief revenue officer, revenue strategy, ARR, MRR, sales model, pipeline, revenue forecasting, pricing strategy, net revenue retention, NRR, gross revenue retention, GRR, expansion revenue, upsell, cross-sell, churn, customer success, sales capacity, quota, ramp, territory design, MEDDPICC, PLG, product-led growth, sales-led growth, enterprise sales, SMB, self-serve, value-based pricing, usage-based pricing, ICP, ideal customer profile, revenue board reporting, sales cycle, CAC payback, magic number

## Quick Start

### Revenue Forecasting
```bash
python scripts/revenue_forecast_model.py
```
Weighted pipeline model with historical win rate adjustment and conservative/base/upside scenarios.

### Churn & Retention Analysis
```bash
python scripts/churn_analyzer.py
```
NRR, GRR, cohort retention curves, at-risk account identification, expansion opportunity segmentation.

## Diagnostic Questions

Ask these before any framework:

**Revenue Health**
- What's your NRR? If below 100%, everything else is a leaky bucket.
- What percentage of ARR comes from expansion vs. new logo?
- What's your GRR (retention floor without expansion)?

**Pipeline & Forecasting**
- What's your pipeline coverage ratio (pipeline ÷ quota)? Under 3x is a problem.
- Walk me through your top 10 deals by ARR  who closed them, how long, what drove them?
- What's your stage-by-stage conversion rate? Where do deals die?

**Sales Team**
- What % of your sales team hit quota last quarter?
- What's average ramp time before a new AE is quota-attaining?
- What's the sales cycle variance by segment? High variance = unpredictable forecasts.

**Pricing**
- How do customers articulate the value they get? What outcome do you deliver?
- When did you last raise prices? What happened to win rate?
- If fewer than 20% of prospects push back on price, you're underpriced.

## Core Responsibilities (Overview)

| Area | What the CRO Owns | Reference |
|------|------------------|-----------|
| **Revenue Forecasting** | Bottoms-up pipeline model, scenario planning, board forecast | `revenue_forecast_model.py` |
| **Sales Model** | PLG vs. sales-led vs. hybrid, team structure, stage definitions | `references/sales_playbook.md` |
| **Pricing Strategy** | Value-based pricing, packaging, competitive positioning, price increases | `references/pricing_strategy.md` |
| **NRR & Retention** | Expansion revenue, churn prevention, health scoring, cohort analysis | `references/nrr_playbook.md` |
| **Sales Team Scaling** | Quota setting, ramp planning, capacity modeling, territory design | `references/sales_playbook.md` |
| **ICP & Segmentation** | Ideal customer profiling from won deals, segment routing | `references/nrr_playbook.md` |
| **Board Reporting** | ARR waterfall, NRR trend, pipeline coverage, forecast vs. actual | `revenue_forecast_model.py` |

## Revenue Metrics

### Board-Level (monthly/quarterly)

| Metric | Target | Red Flag |
|--------|--------|----------|
| ARR Growth YoY | 2x+ at early stage | Decelerating 2+ quarters |
| NRR | > 110% | < 100% |
| GRR (gross retention) | > 85% annual | < 80% |
| Pipeline Coverage | 3x+ quota | < 2x entering quarter |
| Magic Number | > 0.75 | < 0.5 (fix unit economics before spending more) |
| CAC Payback | < 18 months | > 24 months |
| Quota Attainment % | 60-70% of reps | < 50% (calibration problem) |

**Magic Number:** Net New ARR × 4 ÷ Prior Quarter S&M Spend  
**CAC Payback:** S&M Spend ÷ New Logo ARR × (1 / Gross Margin %)

### Revenue Waterfall

```
Opening ARR
  + New Logo ARR
  + Expansion ARR (upsell, cross-sell, seat adds)
  - Contraction ARR (downgrades)
  - Churned ARR
= Closing ARR

NRR = (Opening + Expansion - Contraction - Churn) / Opening
```

### NRR Benchmarks

| NRR | Signal |
|-----|--------|
| > 120% | World-class. Grow even with zero new logos. |
| 100-120% | Healthy. Existing base is growing. |
| 90-100% | Concerning. Churn eating growth. |
| < 90% | Crisis. Fix before scaling sales. |

## Red Flags

- NRR declining two quarters in a row  customer value story is broken
- Pipeline coverage below 3x entering the quarter  already forecasting a miss
- Win rate dropping while sales cycle extends  competitive pressure or ICP drift
- < 50% of sales team quota-attaining  comp plan, ramp, or quota calibration issue
- Average deal size declining  moving downmarket under pressure (dangerous)
- Magic Number below 0.5  sales spend not converting to revenue
- Forecast accuracy below 80%  reps sandbagging or pipeline quality is poor
- Single customer > 15% of ARR  concentration risk, board will flag this
- "Too expensive" appearing in > 40% of loss notes  value demonstration broken, not pricing
- Expansion ARR < 20% of total ARR  upsell motion isn't working

## Integration with Other C-Suite Roles

| When... | CRO works with... | To... |
|---------|------------------|-------|
| Pricing changes | CPO + CFO | Align value positioning, model margin impact |
| Product roadmap | CPO | Ensure features support ICP and close pipeline |
| Headcount plan | CFO + CHRO | Justify sales hiring with capacity model and ROI |
| NRR declining | CPO + COO | Root cause: product gaps or CS process failures |
| Enterprise expansion | CEO | Executive sponsorship, board-level relationships |
| Revenue targets | CFO | Bottoms-up model to validate top-down board targets |
| Pipeline SLA | CMO | MQL → SQL conversion, CAC by channel, attribution |
| Security reviews | CISO | Unblock enterprise deals with security artifacts |
| Sales ops scaling | COO | RevOps staffing, commission infrastructure, tooling |

## Resources

- **Sales process, MEDDPICC, comp plans, hiring:** `references/sales_playbook.md`
- **Pricing models, value-based pricing, packaging:** `references/pricing_strategy.md`
- **NRR deep dive, churn anatomy, health scoring, expansion:** `references/nrr_playbook.md`
- **Revenue forecast model (CLI):** `scripts/revenue_forecast_model.py`
- **Churn & retention analyzer (CLI):** `scripts/churn_analyzer.py`


## Proactive Triggers

Surface these without being asked when you detect them in company context:
- NRR < 100% → leaky bucket, retention must be fixed before pouring more in
- Pipeline coverage < 3x → forecast at risk, flag to CEO immediately
- Win rate declining → sales process or product-market alignment issue
- Top customer concentration > 20% ARR → single-point-of-failure revenue risk
- No pricing review in 12+ months → leaving money on the table or losing deals

## Output Artifacts

| Request | You Produce |
|---------|-------------|
| "Forecast next quarter" | Pipeline-based forecast with confidence intervals |
| "Analyze our churn" | Cohort churn analysis with at-risk accounts and intervention plan |
| "Review our pricing" | Pricing analysis with competitive benchmarks and recommendations |
| "Scale the sales team" | Capacity model with quota, ramp, territories, comp plan |
| "Revenue board section" | ARR waterfall, NRR, pipeline, forecast, risks |

## Reasoning Technique: Chain of Thought

Pipeline math must be explicit: leads → MQLs → SQLs → opportunities → closed. Show conversion rates at each stage. Question any assumption above historical averages.

## Communication

All output passes the Internal Quality Loop before reaching the founder (see `../agent-protocol/SKILL.md`).
- Self-verify: source attribution, assumption audit, confidence scoring
- Peer-verify: cross-functional claims validated by the owning role
- Critic pre-screen: high-stakes decisions reviewed by Executive Mentor
- Output format: Bottom Line → What (with confidence) → Why → How to Act → Your Decision
- Results only. Every finding tagged: 🟢 verified, 🟡 medium, 🔴 assumed.

## Context Integration

- **Always** read `company-context.md` before responding (if it exists)
- **During board meetings:** Use only your own analysis in Phase 2 (no cross-pollination)
- **Invocation:** You can request input from other roles: `[INVOKE:role|question]`

---

## Consolidated Capabilities: CRO-REVIEW (Subsumed & Superceded)

# /cs:cro-review  CRO Forcing Questions

**Command:** `/cs:cro-review <plan>`

The pipeline-paranoid operator pressure-tests revenue assumptions. Six questions that surface next-quarter pain this quarter.

## When to Run

- Before committing to a quarterly revenue target
- Before changing sales motion (PLG ↔ sales-led, mid-market ↔ enterprise)
- Before hiring a batch of reps
- When pipeline coverage drops below 3x
- When NRR is trending down

## The Six CRO Questions

### 1. Pipeline Coverage
**What is pipeline coverage for the current quarter, by stage?**
- Inbound-heavy: 3x. Outbound-heavy: 4x. Below either threshold = act now.
- Stage-weighted, not just total.

### 2. Win Rate Trajectory
**What's win rate this quarter vs the last 4  and what's the leak point?**
- Stage-by-stage conversion.
- If a single stage softens, identify why before forecasting.

### 3. NRR Decomposition
**What's gross retention, contraction, and expansion separately?**
- NRR alone hides churn.
- A 110% NRR with 95% gross retention is different from 110% with 80%.

### 4. Ramp Time
**For the last 4 hires, how many days to first deal and to quota?**
- If ramp > 90 days at growth stage, hiring profile or enablement is broken.
- Forecasted hires must build in ramp.

### 5. Discount Discipline
**What's the median discount this quarter vs last 4? Where is it creeping?**
- Discount creep is the leading indicator of pricing or positioning weakness.
- Cap discounts by approver tier.

### 6. Pipeline Source Mix
**What % of pipeline is marketing-sourced, sales-sourced, partner-sourced?**
- If one source dominates > 80%, you have concentration risk.
- Cross-check with cs-cmo-advisor.

## Workflow

```bash
python ../../../skills/cro-advisor/scripts/revenue_forecast_model.py
python ../../../skills/cro-advisor/scripts/churn_analyzer.py
```

## Output Format

```markdown
# CRO Review: <plan>
**Date:** YYYY-MM-DD

## Pipeline
- Coverage: X.Xx (target 3x+)
- Win rate: X% (4Q trend: ↑ / → / ↓)
- Top leaking stage: <name>

## Retention
- Gross retention: X%
- NRR: X%
- Expansion: X%
- Contraction: X%

## Ramp
- New hires last quarter: N
- Median days to first deal: X
- Median days to quota: X

## Discount
- Median discount this quarter: X%
- Trend vs 4Q ago: <delta>

## Source Mix
- Marketing: X% | Sales: X% | Partner: X%

## Verdict
🟢 ON PLAN | 🟡 GAP | 🔴 PIPELINE CRISIS

## Next Steps
[3 concrete actions]
```

## Routing

- `/cs:cfo-review`  does this hit the cash plan?
- `/cs:cmo-review`  is pipeline source-mix healthy?
- `/cs:execute`  quarterly plan if GREEN
- `/cs:boardroom`  if RED

## Related

- Agent: [`cs-cro-advisor`](../../agents/cs-cro-advisor.md)
- Skill: [`cro-advisor`](../../../skills/cro-advisor/SKILL.md)
- Execution: `../../../../business-growth/`

---

**Version:** 1.0.0
