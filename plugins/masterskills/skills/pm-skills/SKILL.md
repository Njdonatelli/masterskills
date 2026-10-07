---
name: "pm-skills"
description: >-
  U—s—e— —w—h—e—n— —c—o—o—r—d—i—n—a—t—i—n—g— —p—r—o—j—e—c—t—-—d—e—l—i—v—e—r—y— —w—o—r—k— —a—c—r—o—s—s— —t—h—e— —8— —p—r—o—j—e—c—t—-—m—a—n—a—g—e—m—e—n—t— —s—u—b—-—s—k—i—l—l—s— ——— —s—p—r—i—n—t—/—v—e—l—o—c—i—t—y— —a—n—a—l—y—t—i—c—s—,— —p—o—r—t—f—o—l—i—o— —h—e—a—l—t—h—,— —J—i—r—a—/—J—Q—L—,— —C—o—n—f—l—u—e—n—c—e—,— —A—t—l—a—s—s—i—a—n— —a—d—m—i—n—,— —t—e—m—p—l—a—t—e—s—,— —m—e—e—t—i—n—g— —a—n—a—l—y—s—i—s—,— —t—e—a—m— —c—o—m—m—s—.— —T—r—i—g—g—e—r—s— —o—n— —'—o—u—r— —s—p—r—i—n—t—s— —f—e—e—l— —o—f—f—'—,— —'—p—r—o—j—e—c—t— —h—e—a—l—t—h— —r—e—p—o—r—t—'—,— —'—a—u—d—i—t— —o—u—r— —J—i—r—a— —p—e—r—m—i—s—s—i—o—n—s—'—,— —'—w—h—e—n— —w—i—l—l— —i—t— —b—e— —d—o—n—e—'—,— —'—r—u—n— —t—h—e— —d—e—l—i—v—e—r—y— —l—o—o—p—'—.— —F—o—r—k—s— —c—o—n—t—e—x—t— —t—o— —r—o—u—t—e— —t—o— —o—n—e— —s—u—b—-—s—k—i—l—l— —v—i—a— —a— —d—e—t—e—r—m—i—n—i—s—t—i—c— —s—i—g—n—a—l— —r—o—u—t—e—r— —a—n—d— —r—e—t—u—r—n—s— —a— —d—i—g—e—s—t—;— —c—a—n— —a—l—s—o— —d—r—i—v—e— —a— —f—u—l—l— —g—o—a—l—→—p—l—a—n—→—e—x—e—c—u—t—e—→—v—e—r—i—f—y—→—c—l—o—s—e— —d—e—l—i—v—e—r—y— —l—o—o—p— —t—h—r—o—u—g—h— —t—h—e— —r—e—p—o—-—w—i—d—e— —a—g—e—n—t—-—h—a—r—n—e—s—s— —w—i—t—h— —J—i—r—a— —M—C—P— —d—a—t—a— —b—r—i—d—g—e—d— —i—n—t—o— —t—h—e— —d—o—m—a—i—n—'—s— —a—n—a—l—y—t—i—c—s— —t—o—o—l—s—.— —D—i—s—t—i—n—c—t— —f—r—o—m— —p—r—o—d—u—c—t—-—t—e—a—m— —(—w—h—a—t— —t—o— —b—u—i—l—d— —v—s— —h—o—w— —t—o— —d—e—l—i—v—e—r— —i—t—)—,— —b—u—s—i—n—e—s—s—-—o—p—e—r—a—t—i—o—n—s— —(—i—n—t—e—r—n—a—l— —o—p—s—)—,— —a—n—d— —e—n—g—i—n—e—e—r—i—n—g—/—a—g—e—n—t—-—h—a—r—n—e—s—s— —(—t—h—e— —g—e—n—e—r—i—c— —l—o—o—p— —e—n—g—i—n—e— —t—h—i—s— —o—r—c—h—e—s—t—r—a—t—o—r— —p—l—u—g—s— —i—n—t—o—).
context: fork
version: 2.11.1
author: Alireza Rezvani
license: MIT
tags: [project-management, orchestrator, jira, confluence, atlassian, scrum, agile, flow-metrics, agent-harness]
compatible_tools: [claude-code, codex-cli, cursor, antigravity, opencode, gemini-cli]
---

# Project Management — Domain Orchestrator & Delivery Loop

This orchestrator does two jobs. **Routing:** fork context, classify a PM inquiry with
`scripts/pm_goal_router.py`, run exactly one of the 8 sub-skills, return a digest.
**Looping:** turn a delivery goal into a bounded agentic loop — pull live Jira data via the
bundled Atlassian MCP, bridge it into the domain's deterministic analytics tools, verify
every step with machine-run gates, and refuse to close until everything is verified or a
human waives it. The bundled `.mcp.json` wires the Atlassian Remote MCP
(`https://mcp.atlassian.com/v1/sse`, OAuth handled by Claude Code).

## When to invoke

| Symptom | Sub-skill |
|---|---|
| "Project/portfolio health, risk EMV, capacity" | `senior-pm` |
| "Sprint velocity, retro follow-through, ceremony health, when-will-it-be-done" | `scrum-master` |
| "JQL, Jira workflows, boards, automation" | `jira-expert` |
| "Confluence spaces, page trees, content audits" | `confluence-expert` |
| "Users, groups, permissions, SSO" | `atlassian-admin` |
| "Reusable Jira/Confluence templates" | `atlassian-templates` |
| "Meeting transcripts, talk time, action items" | `meeting-analyzer` |
| "Status updates, 3P updates, stakeholder comms" | `team-communications` |

## Routing logic (deterministic)

Run the router — do not eyeball the table when a script can decide:

```bash
python3 scripts/pm_goal_router.py --text "<the goal>" --output json
```

Exit 0 → `route_to` names the sub-skill: load its SKILL.md and follow its workflow.
Exit 2 → ask ONE clarifying question naming the listed candidates, with a recommended
answer. Exit 3 → no signal: ask the user to restate the goal with the deliverable named.
Never guess silently; never silently chain a second sub-skill — digest first, confirm, then
chain.

## The delivery loop (agentic)

For goals (not questions) — "get sprint 14 to a verified close", "produce a portfolio
health report from live Jira", "make our flow metrics visible weekly" — run the
loop-library contract (Observe → Choose → Act → Verify → Record → Repeat-or-stop):

1. **Observe** — pull fresh state: `mcp__atlassian__searchJiraIssuesUsingJql` (get
   `cloudId` via `getAccessibleAtlassianResources` first), save the result JSON, then
   bridge it:
   ```bash
   python3 scripts/jira_snapshot_bridge.py --input snapshot.json --to flow            # WIP, throughput, cycle time p50/85/95, work-item age, SLE, aging alerts
   python3 scripts/jira_snapshot_bridge.py --input snapshot.json --to sprint > s.json # scrum-master schema
   python3 ../scrum-master/scripts/velocity_analyzer.py s.json                        # velocity + volatility + forecast
   ```
   Add `--forecast N` for a seeded Monte Carlo "when will N items be done" answer
   (refuses on < 10 completed items — thin history forecasts are lies).
2. **Choose** — route the next task with `pm_goal_router.py`; one task at a time.
3. **Act** — execute with the routed sub-skill's own tools per its SKILL.md.
4. **Verify** — gate the plan and every close with:
   ```bash
   python3 scripts/delivery_loop_gate.py --plan plan.json --mode plan    # exit 2 = blocked
   python3 scripts/delivery_loop_gate.py --plan plan.json --mode close   # exit 4 = close refused
   ```
   Plus each sub-skill's own gates (scrum-master's ≥ 3-sprints rule, atlassian-admin's
   VERIFY steps). Never adjudicate your own verification.
5. **Record / Repeat-or-stop** — for multi-task goals, run the state through the repo-wide
   harness (it enforces attempt caps, iteration budgets, and evidence logging):
   ```bash
   python3 engineering/agent-harness/skills/agent-harness/scripts/goal_compiler.py \
     --goal "<goal>" --manifest engineering/agent-harness/skills/agent-harness/assets/harnesses/project-management.json \
     --out .agent-harness/plan.json
   python3 engineering/agent-harness/skills/agent-harness/scripts/loop_controller.py init|next|record|verify|close ...
   ```
   Terminal states: success, clean no-op, blocked, approval-required, exhausted,
   stagnated. An exhausted budget is an escalation — never a success report.

## Hard rules (agentic delegation governance)

1. **Agents are contributors, never owners** (Linear model): every loop task carries a
   named human owner; agent-executed tasks also carry a named human reviewer.
   `delivery_loop_gate.py` enforces this (G1/G2).
2. **Acceptance must be machine-checkable** — a command, or a criterion with a threshold.
   "Looks good" is not a gate (G3).
3. **Every Jira/Confluence write is auditable and reversible-first** (Rovo discipline):
   never `transitionJiraIssue` to Done without verify evidence; destructive/irreversible
   actions (deletes, permission changes, org-wide admin) are approval-required terminal
   states, not loop steps.
4. **Never modify a gate you are judged by** — same locked-evaluator invariant as
   autoresearch-agent.
5. **Forecasts are ranges with confidence, never dates** — Monte Carlo percentiles
   (p50/p70/p85/p95), per Vacanti. Single-date promises are the anti-pattern.
6. **Max 3 attempts per task, 12 loop iterations per goal** — then escalate to the named
   human with the evidence log.

## Forcing-question library (grill-with-docs pattern)

One per turn, recommended answer, canon citation. Never run a sub-skill or start a loop
until the lane-defining decision is locked:

- **SPRINT lane**: "Do you want to *measure* flow (cycle time, WIP, throughput, age) or
  *forecast* delivery? Recommended: measure first — a forecast off unmeasured flow is
  noise. Canon: Kanban Guide (May 2025) four mandatory flow measures; Vacanti,
  *Actionable Agile Metrics*."
- **HEALTH lane**: "Is your project status self-reported RAG or derived from signals?
  Recommended: derive it (schedule variance, aging WIP, scope churn) and diff against the
  self-report — that diff finds watermelon projects. Canon: Kanban Guide 2025;
  DORA 2025 (AI amplifies, doesn't fix, weak signals)."
- **JIRA lane**: "Is this configuration change deployable to a test project first?
  Recommended: always stage in a test project; jira-expert's workflow validator must exit
  0 before production. Canon: jira-expert validation workflow."
- **ADMIN lane**: "Is this action reversible, and who approves it? Recommended: name the
  approver before touching permissions — admin actions are approval-required terminal
  states in any loop. Canon: atlassian-admin VERIFY discipline; loop-library stop states."
- **LOOP intake**: "What single observable outcome means DONE, and which command proves
  it? Recommended: a named artifact + a command that exits 0 against it. Canon:
  agent-harness verifier's law; Anthropic, *Building Effective Agents* (evaluator needs
  clear criteria)."
- **MEETINGS/COMMS lanes**: "Could this meeting be an async written update? Recommended:
  status-broadcast meetings convert to async 3P updates; decision meetings keep sync.
  Canon: GitLab async-first handbook."

## Assumptions

1. The user has (or is preparing analysis for someone with) delivery authority.
2. Jira/Confluence access goes through the bundled MCP; capabilities NOT in
   `project-management/references/atlassian-mcp-tools.md` (project/sprint/board/space
   creation, admin config) are done in the web UI — never invent tool names.
3. Inputs may be partial — every tool ships `--sample` so the shape is visible first.

## Non-goals

- Not a replacement for the sub-skills — the orchestrator routes and loops; the
  sub-skills do the work.
- Not the generic loop engine — that is `engineering/agent-harness`; this orchestrator is
  the PM-domain adapter (data bridge + governance gate + lane router).
- Does not decide *what* to build — that's `product-team`.

## Output artifacts

| Mode | Artifact |
|---|---|
| Route | Sub-skill's own artifact + ≤ 200-word digest with one canon-cited challenge |
| Flow report | `flow_metrics.json` (bridge output) with SLE conformance + aging alerts |
| Delivery loop | `.agent-harness/plan.json` + `state.json` + gate verdicts + close handoff |

## Anti-patterns (do not)

- ❌ Run all 8 sub-skills "to be thorough" — route to one, digest, chain on confirmation
- ❌ Report sprint health or forecasts from hand-typed numbers when a Jira snapshot is one
  MCP call away — bridge real data
- ❌ Close a loop with unverified tasks, or report an exhausted budget as success
- ❌ Let an agent be the assignee of record — humans own, agents contribute
- ❌ Auto-transition Jira issues or touch permissions inside a loop without the named
  approver

## References

- [references/flow_forecasting_canon.md](references/flow_forecasting_canon.md) — Kanban
  Guide 2025, Vacanti Monte Carlo, DORA 2025, EBM, SPACE
- [references/agentic_delivery_governance.md](references/agentic_delivery_governance.md) —
  Linear/Rovo delegation models, Anthropic agent patterns, audit discipline
- [references/pm_loop_playbook.md](references/pm_loop_playbook.md) — the five reusable PM
  loops (sprint, health, retro-action, RAID-hygiene, comms) mapped to the loop contract
- Canonical MCP tool list: `project-management/references/atlassian-mcp-tools.md`
- Loop engine: `engineering/agent-harness` · Loop vocabulary: `loop-library`
