---
name: "agent-designer"
description: >-
  U—s—e— —w—h—e—n— —t—h—e— —u—s—e—r— —a—s—k—s— —t—o— —d—e—s—i—g—n— —a— —m—u—l—t—i—-—a—g—e—n—t— —s—y—s—t—e—m—,— —p—i—c—k— —a—n— —o—r—c—h—e—s—t—r—a—t—i—o—n— —p—a—t—t—e—r—n— —(—s—u—p—e—r—v—i—s—o—r—/—s—w—a—r—m—/—p—i—p—e—l—i—n—e—)—,— —g—e—n—e—r—a—t—e— —t—o—o—l— —s—c—h—e—m—a—s— —f—o—r— —a—g—e—n—t—s—,— —o—r— —e—v—a—l—u—a—t—e— —a—g—e—n—t— —e—x—e—c—u—t—i—o—n— —l—o—g—s— —f—o—r— —c—o—s—t—,— —l—a—t—e—n—c—y—,— —a—n—d— —f—a—i—l—u—r—e— —b—o—t—t—l—e—n—e—c—k—s—.— —E—x—a—m—p—l—e—s—:— —'—d—e—s—i—g—n— —a—n— —a—g—e—n—t— —a—r—c—h—i—t—e—c—t—u—r—e— —f—o—r— —r—e—s—e—a—r—c—h— —a—u—t—o—m—a—t—i—o—n—'—,— —'—g—e—n—e—r—a—t—e— —A—n—t—h—r—o—p—i—c— —t—o—o—l— —s—c—h—e—m—a—s— —f—r—o—m— —t—h—e—s—e— —t—o—o—l— —d—e—s—c—r—i—p—t—i—o—n—s—'—,— —'—a—n—a—l—y—z—e— —t—h—e—s—e— —a—g—e—n—t— —r—u—n— —l—o—g—s— —f—o—r— —b—o—t—t—l—e—n—e—c—k—s—'—.— —N—O—T— —f—o—r— —C—l—a—u—d—e— —C—o—d—e— —w—o—r—k—f—l—o—w— —f—i—l—e—s— —(—u—s—e— —w—o—r—k—f—l—o—w—-—b—u—i—l—d—e—r—)— —o—r— —s—i—n—g—l—e—-—a—g—e—n—t— —p—r—o—m—p—t— —d—e—s—i—g—n— —(—u—s—e— —a—g—e—n—t—-—w—o—r—k—f—l—o—w—-—d—e—s—i—g—n—e—r—).
---

# Agent Designer — Multi-Agent System Architecture

Design, schema-generate, and evaluate multi-agent systems with three deterministic tools. The scripts are the workflow — do not freehand an architecture when the planner can score one from requirements.

## When to use

- Designing a new multi-agent system from requirements (pattern choice, roles, comms)
- Generating provider-ready tool schemas (Anthropic + OpenAI formats) from plain tool descriptions
- Evaluating execution logs: success rate, latency distribution, cost, bottlenecks

**When NOT to use:** Claude Code Workflow-tool automations → `workflow-builder`; single-agent workflow scaffolds → `agent-workflow-designer`; multi-agent fan-out at runtime → `agenthub`.

## Pattern decision table

| Choose | When | Watch out for |
|---|---|---|
| Single agent | One bounded task, < ~5 tools | Don't add agents you don't need |
| Supervisor | Central decomposition, specialists report back | Supervisor becomes the bottleneck |
| Pipeline | Strictly sequential stages with handoffs | Rigid order; slowest stage gates throughput |
| Hierarchical | Multiple org layers, > ~8 agents | Communication overhead per level |
| Swarm | Parallel peers, fault tolerance over predictability | Hard to debug; needs consensus rules |

The planner applies this scoring deterministically — run it rather than picking by feel.

## Workflow

All paths relative to this skill folder. Each step's JSON output is the next step's design input.

### 1. Design the architecture

Write a requirements JSON (copy `assets/sample_system_requirements.json` — keys: `goal`, `tasks[]`, `constraints{max_response_time, budget_per_task, concurrent_tasks}`, `team_size`):

```bash
python3 agent_planner.py requirements.json --format json -o arch
```

Emits `arch.json` with `architecture_design` (pattern, agents, communication links), `mermaid_diagram`, and `implementation_roadmap`. Read `architecture_design.pattern` and the per-agent role list; present the mermaid diagram to the user.

### 2. Generate tool schemas

Describe each agent's tools in plain JSON (copy `assets/sample_tool_descriptions.json`), then:

```bash
python3 tool_schema_generator.py tool_descriptions.json --validate -o tools
```

Emits `tools.json` (`tool_schemas`, `validation_summary`) plus provider-specific `tools_anthropic.json` / `tools_openai.json`. **Gate: every tool must print `✓ Valid`.** Fix any invalid schema before proceeding — never hand an agent an unvalidated schema.

### 3. Evaluate execution logs

Once the system runs (or against `assets/sample_execution_logs.json` for a dry run):

```bash
python3 agent_evaluator.py execution_logs.json --detailed -o eval
```

Emits `eval.json` with `summary`, `agent_metrics`, `bottleneck_analysis`, `error_analysis`, `cost_breakdown`, `sla_compliance`, and `optimization_recommendations`, plus split files (`eval_errors.json`, `eval_recommendations.json`).

### 4. Verification loop

The design is not done until:

1. `tool_schema_generator.py --validate` reports 0 invalid schemas.
2. `agent_evaluator.py` on a pilot run reports **0 critical issues** (the tool prints `CRITICAL: N critical issues` when found). If N > 0, apply the top item in `eval_recommendations.json`, re-run the pilot, and re-evaluate.
3. Compare your outputs against `expected_outputs/` to confirm the schema shape you're consuming hasn't drifted.

## References

- `references/agent_architecture_patterns.md` — pattern trade-offs in depth
- `references/tool_design_best_practices.md` — schema, idempotency, error-handling rules
- `references/evaluation_methodology.md` — metric definitions the evaluator implements
