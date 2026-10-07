---
name: "execute"
description: >-
  /—c—s—:—e—x—e—c—u—t—e— —<—d—e—c—i—s—i—o—n—>— ——— —G—e—n—e—r—a—t—e— —a— —9—0—-—d—a—y— —e—x—e—c—u—t—i—o—n— —p—l—a—n— —w—i—t—h— —w—e—e—k—l—y— —m—i—l—e—s—t—o—n—e—s—,— —D—R—I—s—,— —a—n—d— —c—h—e—c—k—-—i—n— —c—a—d—e—n—c—e— —f—r—o—m— —a—n— —a—p—p—r—o—v—e—d— —d—e—c—i—s—i—o—n—.— —U—s—e— —w—h—e—n— —a— —l—o—g—g—e—d— —d—e—c—i—s—i—o—n— —n—e—e—d—s— —t—o— —b—e—c—o—m—e— —a—n— —o—p—e—r—a—t—i—n—g— —p—l—a—n— ——— —e—.—g—.— —t—u—r—n—i—n—g— —a—n— —a—p—p—r—o—v—e—d— —m—a—r—k—e—t—-—e—n—t—r—y— —c—a—l—l— —i—n—t—o— —w—e—e—k—l—y— —m—i—l—e—s—t—o—n—e—s— —w—i—t—h— —D—R—I—s.
---

# /cs:execute — 90-Day Execution Plan

**Command:** `/cs:execute <decision-path>`

Turns an approved decision into a 90-day plan with weekly milestones, named DRIs, and a check-in cadence. Where most decisions die: between "we decided" and "what's next Monday?"

## Pipeline Position

```
/cs:office-hours  →  /cs:brief  →  /cs:boardroom  →  /cs:decide  →  /cs:execute  →  /cs:post-mortem
                                                                       ↑ you are here
```

## Input

An approved decision record (output of `/cs:decide`).

## Output Plan Format

Saved to `~/.claude/execution/YYYY-MM-DD-<slug>.md`:

```markdown
# Execution Plan: <decision title>
**Decision:** <link to /cs:decide record>
**Owner (Sponsor):** <founder or exec>
**Start:** YYYY-MM-DD
**Checkpoint:** YYYY-MM-DD (90d)

## Outcome (binding)
[Copied from decision: success + kill criteria]

## Workstreams
| Workstream | DRI | Success Metric | Status |
|---|---|---|---|
| <e.g., Pricing rollout> | <name> | <metric, threshold> | Not started |
| <e.g., Comms> | <name> | <metric> | Not started |
| <e.g., Eng changes> | <name> | <metric> | Not started |

## Weekly Milestones
| Week | Milestone | DRI | Definition of Done |
|---|---|---|---|
| 1 | <e.g., positioning locked> | <name> | <observable outcome> |
| 2 | <e.g., draft launched> | <name> | <observable> |
| 3 | ... | | |
| 12 | <e.g., checkpoint review> | <name> | <observable> |

## Cadence
- **Weekly:** Owner reviews status (15 min)
- **Bi-weekly:** Cross-functional sync (30 min)
- **Day 30 / 60 / 90:** Checkpoint with cs-chief-of-staff

## Dependencies
- Internal: <list>
- External: <vendors, regulators, customers>

## Risk Register
| Risk | Likelihood | Impact | Owner | Mitigation |
|---|---|---|---|---|
| <e.g., delayed legal review> | M | H | <name> | <plan> |

## Kill Criteria Watch
[Copied from decision; reviewed at every checkpoint]
- <metric, threshold, action>
```

## Workflow

1. Read the decision record
2. Decompose the chosen option into 3-6 workstreams
3. Name a DRI for each workstream
4. Reverse-engineer 12 weekly milestones from the checkpoint date
5. Set the cadence (weekly + bi-weekly + 30/60/90 checkpoints)
6. Build the risk register (cross-reference original Phase 4 devil's-advocate concerns)
7. Save and notify DRIs

## Why 90 Days

- Long enough to show real signal (not just activity)
- Short enough to course-correct before damage compounds
- Matches quarterly OKR cycle, fundraise sprints, and most board cadences

## Routing

- `/cs:post-mortem <decision>` — at day 90 (or earlier if kill criteria trigger)
- `/cs:boardroom` — if a checkpoint reveals a need to re-decide

## Related

- Skills: [`coo-advisor`](../../../skills/coo-advisor/SKILL.md), [`strategic-alignment`](../../../skills/strategic-alignment/SKILL.md), [`change-management`](../../../skills/change-management/SKILL.md)
- Agent: [`cs-coo-advisor`](../../agents/cs-coo-advisor.md)

---

**Version:** 1.0.0
