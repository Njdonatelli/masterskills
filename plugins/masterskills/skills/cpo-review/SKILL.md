---
name: "cpo-review"
description: >-
  /—c—s—:—c—p—o—-—r—e—v—i—e—w— —<—p—l—a—n—>— ——— —J—T—B—D—-—d—r—i—v—e—n— —i—n—t—e—r—r—o—g—a—t—i—o—n— —o—f— —p—r—o—d—u—c—t— —r—o—a—d—m—a—p—,— —P—M—F— —s—i—g—n—a—l—,— —a—n—d— —p—o—r—t—f—o—l—i—o— —f—o—c—u—s—.— —U—s—e— —w—h—e—n— —c—o—m—m—i—t—t—i—n—g— —a— —q—u—a—r—t—e—r—'—s— —r—o—a—d—m—a—p—,— —d—e—c—i—d—i—n—g— —w—h—e—t—h—e—r— —t—o— —k—i—l—l— —a— —f—e—a—t—u—r—e—,— —o—r— —c—l—a—i—m—i—n—g— —P—M—F— —w—i—t—h—o—u—t— —a— —r—e—t—e—n—t—i—o—n— —c—u—r—v—e.
---

# /cs:cpo-review — CPO Forcing Questions

**Command:** `/cs:cpo-review <plan>`

The JTBD-driven builder cuts the roadmap in half. Six questions to surface what to ship and what to kill.

## When to Run

- Before quarterly roadmap commitment
- Before launching a new product line
- Before adding > 3 features to a release
- When retention is flat or declining
- When the team is debating "should we build X?"

## The Six CPO Questions

### 1. JTBD
**What job is this feature hired to do, in the user's words?**
- Not "improve onboarding." "Help a new ops manager get their first deal closed within 7 days."
- Job ≠ feature. Hire ≠ try.

### 2. North Star Metric
**What user behavior does this move, and how does that ladder to the North Star?**
- The metric must be leading, behavior-based, and value-correlated.
- If you can't trace the feature to the North Star, don't build it.

### 3. PMF Signal
**What's the retention curve for users who hire this job — is it flat, decaying, or smiling?**
- Flat or smiling = PMF signal. Decaying = no PMF.
- "Users like it in surveys" is not a signal.

### 4. RICE Score
**Reach, Impact, Confidence, Effort — what's the score and where does this rank in the queue?**
```bash
python product-team/skills/product-manager-toolkit/scripts/rice_prioritizer.py
```

### 5. Opportunity Cost
**What gets cut if this ships? Name the specific initiative or feature.**
- Headcount and time are zero-sum. The cut list is the focus list.

### 6. Kill Criteria
**What signal would tell you in 90 days that this was the wrong bet?**
- Define the metric and threshold in writing, before launch.
- If you can't define a kill criterion, you can't ship responsibly.

## Workflow

1. **Run the analyses:**
   ```bash
   python ../../../skills/cpo-advisor/scripts/pmf_scorer.py
   python ../../../skills/cpo-advisor/scripts/portfolio_analyzer.py
   ```
2. **Answer the six questions.**
3. **Apply the verdict.**

## Output Format

```markdown
# CPO Review: <feature/plan>
**Date:** YYYY-MM-DD

## JTBD
> <one sentence in user voice>

## North Star Link
- Metric moved: <name>
- Expected delta: <%>

## PMF Signal
- Retention curve shape: flat / smiling / decaying
- Cohort sample size: N

## Score
- RICE: <number>
- Rank in queue: #N of M

## Cut List
- Cut: <initiative>
- Reason: <why this matters more>

## Kill Criteria (90 days)
- Metric: <name>
- Threshold: <value>
- Action if missed: <kill | iterate>

## Verdict
🟢 SHIP | 🟡 SHARPEN | 🔴 KILL
```

## Routing

- `/cs:cmo-review` — does the positioning support this feature?
- `/cs:execute` — build the 90-day plan
- `/cs:post-mortem` — if kill criteria triggered

## Related

- Agent: [`cs-cpo-advisor`](../../agents/cs-cpo-advisor.md)
- Skill: [`cpo-advisor`](../../../skills/cpo-advisor/SKILL.md)
- Execution: `product-team/skills/product-manager-toolkit/`

---

**Version:** 1.0.0
