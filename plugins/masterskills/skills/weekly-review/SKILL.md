---
name: weekly-review
description: >-
  U—s—e— —w—h—e—n— —s—o—m—e—o—n—e— —w—a—n—t—s— —t—o— —r—u—n— —a— —w—e—e—k—l—y— —r—e—v—i—e—w—,— —c—l—o—s—e— —o—p—e—n— —l—o—o—p—s—,— —a—u—d—i—t— —s—t—a—l—l—e—d— —p—r—o—j—e—c—t—s— —a—n—d— —c—o—m—m—i—t—m—e—n—t—s—,— —g—e—t— —t—h—e—i—r— —s—y—s—t—e—m— —b—a—c—k— —t—o— —t—r—u—s—t—e—d—,— —r—e—s—t—a—r—t— —a— —l—a—p—s—e—d— —r—e—v—i—e—w— —h—a—b—i—t—,— —o—r— —s—a—y—s— —"—/—c—s—:—w—e—e—k—l—y—-—r—e—v—i—e—w—"—.— —W—a—l—k—s— —D—a—v—i—d— —A—l—l—e—n—'—s— —t—h—r—e—e—-—p—h—a—s—e— —l—o—o—p— ——— —G—E—T— —C—L—E—A—R—,— —G—E—T— —C—U—R—R—E—N—T—,— —G—E—T— —C—R—E—A—T—I—V—E— ——— —w—i—t—h— —d—e—t—e—r—m—i—n—i—s—t—i—c— —s—c—r—i—p—t—s— —t—h—a—t— —i—n—v—e—n—t—o—r—y— —o—p—e—n— —l—o—o—p—s—,— —g—a—t—e— —t—h—e— —c—h—e—c—k—l—i—s—t— —w—i—t—h— —n—a—m—e—d— —g—a—p—s—,— —a—n—d— —s—c—o—r—e— —c—o—m—m—i—t—m—e—n—t— —h—e—a—l—t—h— —0—-—1—0—0.
argument-hint: "[optional: directory or notes to review]"
license: MIT
metadata:
  version: 1.0.0
  build_pattern: "Path-B ritual skill — GTD weekly-review loop preserved + deterministic scanner/gate/auditor scripts added"
  distinct_from: "reflect (per-conversation reflection, not a recurring cadence); capture (intake that feeds the system, not the review that maintains it); project-management sprint retros (team ceremony, not a personal trusted-system audit)"
---

# Weekly Review — GTD Loop → Trusted System

> **Portability:** Reasoning-led skill with 3 stdlib Python scripts. No external APIs, no LLM calls
> in scripts. Works in Claude Code CLI and Claude.ai web. The scripts do the inventory and the
> gating; Claude and the user do the thinking.

## What this does

A personal system is only trustworthy if it gets reviewed — David Allen calls the weekly review
the critical success factor of the whole method. This skill walks the three phases in order and
refuses to call the review COMPLETE while any of the five mandatory GET CURRENT steps is
unaccounted for. Evidence first: scan the workspace for open loops before asking the user to
recall anything, because their memory is exactly what the method says not to trust.

## Phase 1 — GET CLEAR (steps 1-3)

Collect loose inputs, process every inbox to zero (clarify, don't do — anything over two minutes
becomes a next action), then a mind sweep to empty the head. Start with evidence:

```bash
# Inventory open loops: unchecked checkboxes, TODO/FIXME markers, stale files
python scripts/open_loop_scanner.py --dir ~/notes --stale-days 14
```

Route every loop found to a list — next action, waiting-for, someday/maybe, or trash.

## Phase 2 — GET CURRENT (steps 4-8, all mandatory)

Review the next-action lists (mark done, prune dead), the previous calendar (missed commitments
become actions), the upcoming calendar (prepare, don't react), the waiting-for list (chase or
drop), and every project for exactly one next action. Then gate honestly:

```bash
python scripts/weekly_review_gate.py --list   # show the numbered ten-step checklist
python scripts/weekly_review_gate.py --done "1,2,3,4,5,6,7,8" --skip "9:no someday list yet"
```

The gate computes completion %, names every missing step, and exits 0 (COMPLETE) or 2
(INCOMPLETE). An unskipped missing GET CURRENT step **always** forces INCOMPLETE.

## Phase 3 — GET CREATIVE (steps 9-10)

Review someday/maybe (activate, keep, or kill), capture new ideas while the head is clear, then
audit the whole commitment portfolio:

```bash
python scripts/commitment_auditor.py --input commitments.json
```

Flags STALLED / NO-NEXT-ACTION / SOMEDAY-CANDIDATE, prints the health formula with the score, and
issues HEALTHY / DRIFTING / OVERCOMMITTED. End the review with one named next action.

## Scripts

| Script | Role |
|---|---|
| `scripts/open_loop_scanner.py` | Inventories unchecked checkboxes, TODO/FIXME markers, and stale files across a directory; grouped counts + per-file locations; `--json`. |
| `scripts/weekly_review_gate.py` | The ten-step three-phase checklist; `--done`/`--skip`/`--list`; completion % + named gaps → COMPLETE (exit 0) / INCOMPLETE (exit 2). |
| `scripts/commitment_auditor.py` | Flags stalled and actionless commitments, computes the 0-100 health score with the formula shown → HEALTHY / DRIFTING / OVERCOMMITTED. |

## References

- [`references/gtd_weekly_review_canon.md`](references/gtd_weekly_review_canon.md) — why the weekly review is the critical success factor; the three-phase structure; cadence discipline (7 sources)
- [`references/open_loop_psychology.md`](references/open_loop_psychology.md) — Zeigarnik effect, plan-making research, attention residue: why open loops tax attention (6 sources)
- [`references/review_cadence_design.md`](references/review_cadence_design.md) — horizons of focus, habit anchoring, timeboxing, failure modes, restart-after-lapse (7 sources)

## Assets

- [`assets/weekly_review_checklist.md`](assets/weekly_review_checklist.md) — fillable three-phase checklist
- [`assets/example_weekly_review.md`](assets/example_weekly_review.md) — a full worked review (scan → checklist → gate → audit → next action)

## Rules

- All five GET CURRENT steps are mandatory; skip only with a stated reason, and the gate still names it.
- Never self-certify — the gate issues the verdict; relay its exit code, don't soften it.
- Process, don't do: during the review, anything over two minutes becomes a next action, not a detour.
- Timebox 60-90 minutes; past two hours, gate what's done honestly and schedule the remainder.
- A lapsed habit restarts with a shorter pass and zero guilt — a review is maintenance, not judgment.

## Distinct From (don't reach for the wrong sibling)

- **`productivity/reflect`** — reflects on one conversation or piece of work, once. The weekly review is a recurring cadence over the whole system.
- **`productivity/capture`** — the intake funnel (brain dump → actions). Capture feeds the system; this review keeps it trusted.
- **`project-management` sprint retros** — a team ceremony about a shared iteration. This is a personal trusted-system audit.

---

**Version:** 1.0.0 · **Build pattern:** Path-B ritual skill — GTD weekly-review loop preserved + deterministic gate/scanner/auditor scripts added.
