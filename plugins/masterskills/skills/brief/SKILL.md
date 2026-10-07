---
name: "brief"
description: >-
  /—c—s—:—b—r—i—e—f— —<—t—o—p—i—c—>— ——— —G—e—n—e—r—a—t—e— —a— —o—n—e—-—p—a—g—e— —s—t—r—a—t—e—g—y— —b—r—i—e—f— —f—r—o—m— —a—n— —o—f—f—i—c—e—-—h—o—u—r—s— —i—n—t—a—k—e—.— —F—i—r—s—t— —s—t—e—p— —i—n— —t—h—e— —s—t—r—a—t—e—g—i—c— —s—p—r—i—n—t— —p—i—p—e—l—i—n—e—.— —U—s—e— —w—h—e—n— —a— —s—t—r—a—t—e—g—i—c— —q—u—e—s—t—i—o—n— —n—e—e—d—s— —t—o— —b—e— —f—r—a—m—e—d— —b—e—f—o—r—e— —b—o—a—r—d—r—o—o—m— —d—e—l—i—b—e—r—a—t—i—o—n— ——— —e—.—g—.— —l—o—c—k—i—n—g— —o—p—t—i—o—n—s—,— —a—s—s—u—m—p—t—i—o—n—s—,— —a—n—d— —s—u—c—c—e—s—s— —c—r—i—t—e—r—i—a— —f—o—r— —a— —p—r—i—c—i—n—g— —c—h—a—n—g—e— —o—r— —a— —m—a—r—k—e—t—-—e—n—t—r—y— —d—e—c—i—s—i—o—n.
---

# /cs:brief — One-Page Strategy Brief

**Command:** `/cs:brief <topic>` or `/cs:brief <office-hours-output>`

Turns intake (raw question or office-hours output) into a one-page strategy brief that the boardroom can deliberate on. This is **Step 1** of the strategic sprint pipeline.

## Pipeline Position

```
/cs:office-hours  →  /cs:brief  →  /cs:boardroom  →  /cs:decide  →  /cs:execute  →  /cs:post-mortem
                       ↑ you are here
```

## Inputs

- A topic string, **or**
- An office-hours brief (preferred — more rigor)
- `~/.claude/company-context.md` (loaded automatically)

## Output

A single Markdown file under `~/.claude/briefs/YYYY-MM-DD-<slug>.md` with this structure:

```markdown
# Strategy Brief: <topic>
**Date:** YYYY-MM-DD
**Author:** cs-chief-of-staff
**Status:** DRAFT | UNDER REVIEW | APPROVED | RETIRED

## Context
[1-2 paragraphs: where the company sits today on this topic — pulled from company-context.md]

## Question
[The one sentence question the boardroom must answer]

## Options
1. **Option A:** <name> — <one-sentence summary>
2. **Option B:** <name> — <one-sentence summary>
3. **Option C:** <name> — <one-sentence summary>

(Minimum 2 options. "Do nothing" is always an option.)

## Assumptions
- <assumption 1 — explicit>
- <assumption 2>
- <assumption 3>

## Constraints
- Time: <by when must this decide>
- Money: <budget envelope>
- People: <who can / can't be reallocated>
- Reversibility: <one-way door | two-way door>

## Affected Roles
[Which cs-* advisors should weigh in. Used to route to /cs:boardroom panel composition.]

- [ ] cs-ceo-advisor
- [ ] cs-cfo-advisor
- [ ] cs-cto-advisor
- [ ] cs-cmo-advisor
- [ ] cs-cro-advisor
- [ ] cs-cpo-advisor
- [ ] cs-coo-advisor
- [ ] cs-chro-advisor
- [ ] cs-ciso-advisor
- [ ] cs-general-counsel-advisor
- [ ] cs-cdo-advisor
- [ ] cs-caio-advisor
- [ ] cs-cco-advisor
- [ ] cs-vpe-advisor
- [ ] cs-chief-of-staff

## Success Criteria
[Measurable outcomes that define success — set BEFORE the decision]
- <metric 1, threshold, timeframe>
- <metric 2, threshold, timeframe>

## Kill Criteria
[What signal would tell you in 90 days that this was the wrong call]
- <metric, threshold, action if missed>
```

## Workflow

1. Load company-context.md via context-engine
2. If input is office-hours output, parse the 6 answers
3. If input is a raw topic, prompt the founder for the missing pieces
4. Draft 2-3 options (never just one — every brief needs a counterfactual)
5. Make assumptions and constraints explicit
6. Identify affected roles → drives panel composition for `/cs:boardroom`
7. Write success + kill criteria BEFORE the decision (this is the rigor moment)
8. Save to `~/.claude/briefs/`

## Why This Step Exists

The biggest decision-making failure is debating implementation before agreeing on the question. The brief locks the question, options, and success criteria so the boardroom can deliberate without scope creep.

This is also the **artifact handoff** — the next command consumes this file, not your memory.

## Routing

- `/cs:boardroom <brief>` — multi-role deliberation
- `/cs:cross-eval <brief>` — multi-model sanity check before boardroom (for high-stakes)
- `/cs:freeze <brief>` — cooldown lock for irreversible decisions

## Related

- Agent: [`cs-chief-of-staff`](../../agents/cs-chief-of-staff.md)
- Skills: [`context-engine`](../../../skills/context-engine/SKILL.md), [`board-meeting`](../../../skills/board-meeting/SKILL.md)

---

**Version:** 1.0.0
