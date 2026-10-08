---
name: "cdo-review"
description: >-
  /—c—s—:—c—d—o—-—r—e—v—i—e—w— —<—p—l—a—n—>— ——— —D—e—c—i—s—i—o—n—-—d—r—i—v—e—n— —C—h—i—e—f— —D—a—t—a— —O—f—f—i—c—e—r— —i—n—t—e—r—r—o—g—a—t—i—o—n— —o—f— —a—n—y— —p—l—a—n— —t—h—a—t— —t—o—u—c—h—e—s— —t—r—a—i—n—i—n—g— —d—a—t—a—,— —d—a—t—a— —a—r—c—h—i—t—e—c—t—u—r—e—,— —d—a—t—a— —p—r—o—d—u—c—t—i—z—a—t—i—o—n—,— —o—r— —d—a—t—a— —t—e—a—m— —h—i—r—i—n—g—.— —U—s—e— —w—h—e—n— —v—a—l—i—d—a—t—i—n—g— —t—r—a—i—n—i—n—g—-—d—a—t—a— —r—i—g—h—t—s— —b—e—f—o—r—e— —m—o—d—e—l— —w—o—r—k—,— —c—h—o—o—s—i—n—g— —w—a—r—e—h—o—u—s—e— —v—s— —l—a—k—e—h—o—u—s—e— —v—s— —m—e—s—h—,— —o—r— —v—a—l—u—i—n—g— —d—a—t—a— —a—s—s—e—t—s— —f—o—r— —p—r—o—d—u—c—t—i—z—a—t—i—o—n— —o—r— —M—&—A.
---

# /cs:cdo-review — CDO Forcing Questions

**Command:** `/cs:cdo-review <plan>`

The decision-driven CDO pressure-tests any plan that touches data strategy. Six questions before any commitment to a data architecture, AI training run, data productization, or data team hire.

## When to Run

- Before approving any new ML model training run that uses customer data
- Before signing a multi-year data-infrastructure SaaS contract (Snowflake, Databricks, Fivetran)
- Before productizing any customer data (benchmark report, embedding endpoint, license)
- Before a major data team hire (head of data, CDO, data PM, ML engineer)
- Before M&A diligence — yours or theirs
- When the founder uses the word "monetize" near "data"

## The Six CDO Questions

### 1. What decision does this data drive?
**If no decision is unblocked, why are we collecting / training on / productizing it?**
- "We might need it later" is not a decision.
- "It feels like a moat" is not a decision.
- A real answer names a specific business call that requires this data.

### 2. What's the consent provenance for every source?
**For each data source: origin, consent flow, data class, intended use.**
- 1st-party-TOS-only is weaker than 1st-party-explicit-opt-in.
- Bundled TOS doesn't cover material new purposes (training on PII for foundation models).
- Run `ai_training_data_audit.py` if there's any AI use case in scope.

### 3. Who consumes this internally — and how many distinct functional domains?
**Drives the centralize-vs-embed and warehouse-vs-mesh decisions.**
- <5 consumers: warehouse-only.
- 5-25 consumers: lakehouse.
- 25+ consumers + federated culture: mesh.
- Premature architecture choice is the #1 cause of data-team burnout.

### 4. What's the M&A diligence impact?
**If an acquirer asks about this data corpus tomorrow, are we ready?**
- Is there a documented anonymization process?
- What % of customers have MSA carve-outs?
- Are training-data provenance logs current?
- Run `data_asset_valuator.py` quarterly.

### 5. Can the model / decision / report be retrained / re-run / re-published without this source?
**Tests how much you depend on a specific data source.**
- If yes → low blast radius; you can change consent posture later.
- If no → high blast radius; you've structurally committed to the source. Vet harder.

### 6. What role unblocks this — and is it the right next hire?
**Wrong hire (data scientist) when right answer (analytics engineer) is a 12-month productivity loss.**
- Map the decision being unblocked to the specific role.
- Confirm prerequisite roles are in place (data engineer before ML engineer, analyst before data scientist).

## Workflow

```bash
# 1. AI training audit (if any ML / AI use case)
python ../../../skills/chief-data-officer-advisor/scripts/ai_training_data_audit.py sources.json

# 2. Architecture decision (if changing the stack)
python ../../../skills/chief-data-officer-advisor/scripts/data_product_strategy_picker.py profile.json

# 3. Data asset valuation (if productizing or pre-M&A)
python ../../../skills/chief-data-officer-advisor/scripts/data_asset_valuator.py corpus.json
```

## Output Format

```markdown
# CDO Review: <plan>
**Date:** YYYY-MM-DD

## The Decision Being Made
[one sentence — which of the four CDO decisions: training | architecture | asset | hire]

## Training Audit (if applicable)
- NO-GO sources: N
- MITIGATE sources: N
- GO sources: N
- Top remediation: <one line>

## Architecture (if applicable)
- Recommended: WAREHOUSE / LAKEHOUSE / MESH
- Build-vs-buy summary: <one line>
- Kill criteria: <when to revisit>

## Asset Value (if applicable)
- Strategic value: X/10 | Moat: STRONG / MEDIUM / WEAK
- M&A multiplier: X.Xx – X.Xx ARR
- Recommended productization path: <name>

## Org (if applicable)
- Next hire: <role>
- Why this, not that: <one line>
- Prerequisite hires in place: yes/no

## Verdict
🟢 SHIP | 🟡 SHARPEN | 🔴 BLOCK

## Next Steps
[3 concrete actions]
```

## Routing

- `/cs:gc-review` — for any productization or licensing path
- `/cs:ciso-review` — for any architecture change touching customer data
- `/cs:cfo-review` — for build-vs-buy TCO and M&A valuation math
- `cs-chro-advisor` agent — for data team hires (comp, ladder, leveling)
- `/cs:decide` — log the verdict
- `/cs:freeze 90` — on multi-year infrastructure contracts

## Related

- Agent: [`cs-cdo-advisor`](../../agents/cs-cdo-advisor.md)
- Skill: [`chief-data-officer-advisor`](../../../skills/chief-data-officer-advisor/SKILL.md)
- Adjacent: `../../../skills/general-counsel-advisor/` (contractual constraints), `../../../skills/cto-advisor/` (architecture capacity)

---

**Version:** 1.0.0
