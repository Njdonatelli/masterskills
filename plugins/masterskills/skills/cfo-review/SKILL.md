---
name: "cfo-review"
description: >-
  /—c—s—:—c—f—o—-—r—e—v—i—e—w— —<—p—l—a—n—>— ——— —N—u—m—e—r—a—t—e—-—s—k—e—p—t—i—c— —i—n—t—e—r—r—o—g—a—t—i—o—n— —o—f— —a—n—y— —p—l—a—n— —t—h—a—t— —t—o—u—c—h—e—s— —m—o—n—e—y—.— —U—n—i—t— —e—c—o—n—o—m—i—c—s—,— —r—u—n—w—a—y—,— —d—i—l—u—t—i—o—n—,— —c—a—p—i—t—a—l— —a—l—l—o—c—a—t—i—o—n—.— —U—s—e— —w—h—e—n— —a— —p—l—a—n— —c—o—m—m—i—t—s— —m—e—a—n—i—n—g—f—u—l— —s—p—e—n—d— ——— —e—.—g—.— —a— —h—i—r—i—n—g— —w—a—v—e—,— —a— —f—u—n—d—r—a—i—s—e— —d—e—c—i—s—i—o—n—,— —o—r— —a— —n—e—w— —c—h—a—n—n—e—l— —b—u—d—g—e—t.
---

# /cs:cfo-review — CFO Forcing Questions

**Command:** `/cs:cfo-review <plan>`

The numerate skeptic stress-tests anything that touches money. Six questions before any spend or fundraise.

## When to Run

- Before approving any spend > 1% of revenue
- Before opening a new hiring requisition
- Before any fundraise conversation
- Before changing pricing or unit economics
- Before signing a multi-year contract

## The Six CFO Questions

### 1. Burn & Runway
**What's the burn multiple and how many months of cash remain at base / bull / bear?**
- Burn multiple = Net burn ÷ Net new ARR. Above 2x is a problem.
- If bear case < 12 months, you're already in fundraising mode.

### 2. Unit Economics
**What is LTV / CAC per channel, and what's the payback period on the top-2 channels?**
- LTV / CAC > 3x is healthy. Payback < 12 months is healthy.
- If either is broken, do not scale that channel.

### 3. Dilution Path
**If this plan requires a raise, what's the dilution at base and bear valuations?**
- Founder dilution per round.
- Cumulative dilution to next 2 rounds.

### 4. Capital Allocation Alternative
**If this dollar wasn't spent here, where else could it go and what's the expected return?**
- Three alternatives: hiring, product, marketing.
- Make the opportunity cost explicit.

### 5. Revenue Quality
**What's the gross margin, and how does it trend at scale?**
- If margin compresses with scale, the model is broken.
- Cost-of-revenue should grow slower than revenue.

### 6. Bear Case Survival
**If revenue is 50% of plan, does the company survive 18 months?**
- Default-alive is non-negotiable.
- If not, identify the cut triggers in advance.

## Workflow

1. **Run the numbers:**
   ```bash
   python ../../../skills/cfo-advisor/scripts/burn_rate_calculator.py
   python ../../../skills/cfo-advisor/scripts/unit_economics_analyzer.py
   python ../../../skills/cfo-advisor/scripts/fundraising_model.py
   ```
2. **Answer all six questions** with numbers, not adjectives.
3. **Apply the verdict:**
   - 🟢 GREEN — fund it
   - 🟡 YELLOW — fund with cut triggers
   - 🔴 RED — kill or revise

## Output Format

```markdown
# CFO Review: <plan>
**Date:** YYYY-MM-DD
**Reviewer:** cs-cfo-advisor

## Numbers
- Burn multiple: X.Xx
- Runway (base/bull/bear): X / X / X months
- LTV/CAC top channel: X.Xx, payback Y months
- Gross margin: X% (trend: Y)
- Dilution this round: X%
- Bear-case survival: PASS / FAIL

## Verdict
🟢 GREEN | 🟡 YELLOW | 🔴 RED

## Conditions (if YELLOW)
- Cut trigger: <metric> < <threshold> → <action>
- Review checkpoint: <date>

## Recommendation
[3 concrete next steps]
```

## Routing

- `/cs:decide` — log the verdict
- `/cs:execute` — build 90-day plan if GREEN
- `/cs:boardroom` — escalate if multi-role implications

## Related

- Agent: [`cs-cfo-advisor`](../../agents/cs-cfo-advisor.md)
- Skill: [`cfo-advisor`](../../../skills/cfo-advisor/SKILL.md)

---

**Version:** 1.0.0
