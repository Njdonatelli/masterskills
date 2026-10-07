---
name: "decide"
description: >-
  /—c—s—:—d—e—c—i—d—e— —<—m—e—m—o—>— ——— —L—o—g— —a— —d—e—c—i—s—i—o—n— —t—o— —t—w—o—-—l—a—y—e—r— —m—e—m—o—r—y— —v—i—a— —d—e—c—i—s—i—o—n—-—l—o—g—g—e—r—.— —A—p—p—r—o—v—e—d— —m—e—m—o— —b—e—c—o—m—e—s— —d—u—r—a—b—l—e—;— —r—a—w— —t—r—a—n—s—c—r—i—p—t—s— —k—e—p—t— —f—o—r— —r—e—f—e—r—e—n—c—e—.— —U—s—e— —w—h—e—n— —t—h—e— —f—o—u—n—d—e—r— —h—a—s— —a—p—p—r—o—v—e—d— —a— —b—o—a—r—d—r—o—o—m— —m—e—m—o— —a—n—d— —t—h—e— —d—e—c—i—s—i—o—n— —m—u—s—t— —b—e—c—o—m—e— —d—u—r—a—b—l—e— —c—o—m—p—a—n—y— —m—e—m—o—r—y— ——— —e—.—g—.— —r—i—g—h—t— —a—f—t—e—r— —/—c—s—:—b—o—a—r—d—r—o—o—m— —c—o—n—c—l—u—d—e—s.
---

# /cs:decide — Log the Decision

**Command:** `/cs:decide <memo-path>`

Logs the founder's decision via the `decision-logger` skill. This is the gate where in-session deliberation becomes durable company memory.

## Pipeline Position

```
/cs:office-hours  →  /cs:brief  →  /cs:boardroom  →  /cs:decide  →  /cs:execute  →  /cs:post-mortem
                                                       ↑ you are here
```

## Two-Layer Memory Model

The `decision-logger` skill maintains two layers:

1. **Raw transcripts** — every boardroom session, every advisor's Phase 2 position, every dissent. Stored under `~/.claude/decisions/raw/`. Reference only, never feeds back automatically.
2. **Approved decisions** — only the founder-signed memos. Stored under `~/.claude/decisions/approved/`. Feeds into future `/cs:office-hours` and `/cs:founder-mode` calls.

This split prevents the system from "remembering" unresolved debates as if they were decisions.

## Input

A board memo file (output of `/cs:boardroom`).

## Workflow

1. Read the memo path
2. Verify it has founder approval (status: APPROVED)
3. Extract structured decision record:
   - Decision title
   - Date decided
   - Option chosen
   - Success + kill criteria
   - Dissent (preserved)
   - Review checkpoint date
4. Append to `~/.claude/decisions/approved/<YYYY-MM-DD>-<slug>.md`
5. Update the raw transcript pointer
6. If llm-wiki bridge configured, write to vault (`~/company-vault/10-decisions/`)
7. Schedule auto-revisit (90 days)

## Output Record Format

```markdown
# Decision: <title>
**Decided:** YYYY-MM-DD
**By:** <founder name>
**Memo:** <link to boardroom memo>
**Brief:** <link to original brief>
**Review checkpoint:** YYYY-MM-DD (90d default)

## Decision
**Chose:** <option>
**Rejected:** <other options + one-line why>

## Success Criteria (binding)
- <metric, threshold, timeframe>

## Kill Criteria (binding)
- <metric, threshold, action>

## Preserved Dissent
- **<dissenter>:** <unresolved concern>
- (preserved verbatim; dissent never erased)

## Next Action
- `/cs:execute` → 90-day plan due <date>

## Status History
- YYYY-MM-DD: APPROVED
```

## Why Preserved Dissent

The biggest risk in approved decisions is forgetting why someone disagreed. When the kill criteria trigger, the dissent often turns out to have been correct. Preserving it verbatim — not summarized — keeps the company honest at post-mortem time.

## Routing

- `/cs:execute <decision>` — build the 90-day plan
- `/cs:freeze <decision> <days>` — lock if irreversible
- (Auto-scheduled) `/cs:post-mortem <decision>` — at 90-day checkpoint

## Stale-Decision Audit

`cs-chief-of-staff` runs a weekly stale audit:
- Decisions > 90 days without revisit → flag for `/cs:post-mortem`
- Decisions with kill criteria triggered → flag immediately
- Decisions whose company-context.md basis has changed → flag for re-examination

## Related

- Skill: [`decision-logger`](../../../skills/decision-logger/SKILL.md)
- Agent: [`cs-chief-of-staff`](../../agents/cs-chief-of-staff.md)
- Bridge: [`../../references/llm-wiki-bridge.md`](../../references/llm-wiki-bridge.md)

---

**Version:** 1.0.0
