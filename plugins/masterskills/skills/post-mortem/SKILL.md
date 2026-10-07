---
name: "post-mortem"
description: >-
  /—c—s—:—p—o—s—t—-—m—o—r—t—e—m— —<—d—e—c—i—s—i—o—n—>— ——— —H—o—n—e—s—t— —r—e—t—r—o—s—p—e—c—t—i—v—e— —o—n— —a—n— —e—x—e—c—u—t—e—d— —d—e—c—i—s—i—o—n—,— —s—c—o—r—e—d— —a—g—a—i—n—s—t— —o—r—i—g—i—n—a—l— —a—s—s—u—m—p—t—i—o—n—s— —a—n—d— —d—i—s—s—e—n—t—.— —C—l—o—s—e—s— —t—h—e— —s—t—r—a—t—e—g—i—c— —s—p—r—i—n—t— —l—o—o—p—.— —U—s—e— —w—h—e—n— —a— —d—e—c—i—s—i—o—n— —h—i—t—s— —i—t—s— —9—0—-—d—a—y— —r—e—v—i—e—w— —c—h—e—c—k—p—o—i—n—t— —o—r— —i—t—s— —k—i—l—l— —c—r—i—t—e—r—i—a— —t—r—i—g—g—e—r— ——— —e—.—g—.— —s—c—o—r—i—n—g— —l—a—s—t— —q—u—a—r—t—e—r—'—s— —p—r—i—c—i—n—g— —c—h—a—n—g—e— —a—g—a—i—n—s—t— —i—t—s— —p—r—e—-—c—o—m—m—i—t—t—e—d— —s—u—c—c—e—s—s— —m—e—t—r—i—c—s.
---

# /cs:post-mortem — Honest Retrospective

**Command:** `/cs:post-mortem <decision-path>`

Closes the strategic sprint loop. Scores a decision against the success and kill criteria written **before** the decision (not retro-fitted) and revisits the preserved dissent. This is the rigor that compounds over time.

## Pipeline Position

```
/cs:office-hours  →  /cs:brief  →  /cs:boardroom  →  /cs:decide  →  /cs:execute  →  /cs:post-mortem
                                                                                       ↑ you are here
```

## When to Run

- At the 90-day checkpoint (auto-scheduled by `/cs:decide`)
- When a kill criterion triggers
- After a major decision is reversed
- Quarterly on all decisions of the past quarter

## Inputs

- The decision record (output of `/cs:decide`)
- The execution plan (output of `/cs:execute`)
- Actual outcomes (metrics, events, customer signals)

## Output: Post-Mortem Record

Saved to `~/.claude/postmortems/YYYY-MM-DD-<slug>.md`:

```markdown
# Post-Mortem: <decision title>
**Decision date:** YYYY-MM-DD
**Post-mortem date:** YYYY-MM-DD
**Status:** WIN / PARTIAL / LOSS / MIXED

## Outcome Scoring (against pre-committed criteria)

| Success Criterion | Threshold | Actual | Met? |
|---|---|---|---|
| <metric 1> | <threshold> | <actual> | ✅ / ❌ |
| <metric 2> | <threshold> | <actual> | ✅ / ❌ |

| Kill Criterion | Threshold | Actual | Triggered? |
|---|---|---|---|
| <metric> | <threshold> | <actual> | ✅ / ❌ |

**Overall:** WIN / PARTIAL / LOSS / MIXED

## What We Got Right
- <factor 1>
- <factor 2>

## What We Got Wrong
- <factor 1>
- <factor 2>

## Preserved Dissent — Revisited
[Original dissent from the boardroom memo, scored:]

- **<dissenter>:** <original concern>
  - **Did it materialize?** YES / NO / PARTIAL
  - **Cost if YES:** <quantified impact>
  - **Lesson:** <one sentence>

## Assumption Audit
[Original brief's assumptions, scored:]

- **Assumption 1:** <text>
  - **Held?** YES / NO / PARTIAL
  - **Why:** <explanation>

## Process Lessons
- **Phase 2 isolation worked?** YES / NO
- **Devil's advocate concerns played out?** YES / NO / PARTIAL
- **Cadence was right?** YES / TOO LOOSE / TOO TIGHT

## Forward Actions
- [ ] <change to operating system or routing logic>
- [ ] <new decision to make based on this learning>
- [ ] <update company-context.md>

## Status
- WIN → archive, log lesson
- LOSS → schedule follow-up boardroom: `/cs:brief` for the next call
```

## Why Pre-Committed Criteria Matter

The biggest temptation in post-mortems is retroactive justification: "we always knew X, that's why we did Y." Pre-committed criteria, signed at `/cs:decide` time, eliminate that move. The numbers either matched or they didn't.

## Why Revisit Dissent

The dissent column from `/cs:boardroom` is the single most useful piece of organizational memory. Most of the time, the dissenter was directionally right. Revisiting and scoring it builds calibration over years.

## Routing

- `/cs:brief` — if the post-mortem surfaces a new decision
- `/cs:freeze` — if the post-mortem reveals a process gap that needs cooldown enforcement
- Updates to company-context.md via `cs-onboard`

## Related

- Skill: [`decision-logger`](../../../skills/decision-logger/SKILL.md)
- Agent: [`cs-chief-of-staff`](../../agents/cs-chief-of-staff.md)
- Sibling: [`/em:postmortem`](../../../executive-mentor/skills/postmortem/SKILL.md) — adversarial single-decision post-mortem

---

**Version:** 1.0.0
