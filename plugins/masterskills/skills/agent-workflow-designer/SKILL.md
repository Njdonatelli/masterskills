---
name: "agent-workflow-designer"
description: >-
  D—e—s—i—g—n— —p—r—o—d—u—c—t—i—o—n—-—g—r—a—d—e— —m—u—l—t—i—-—a—g—e—n—t— —w—o—r—k—f—l—o—w—s— —w—i—t—h— —c—l—e—a—r— —p—a—t—t—e—r—n— —c—h—o—i—c—e— —(—s—e—q—u—e—n—t—i—a—l—,— —p—a—r—a—l—l—e—l—,— —h—i—e—r—a—r—c—h—i—c—a—l—)—,— —h—a—n—d—o—f—f— —c—o—n—t—r—a—c—t—s—,— —f—a—i—l—u—r—e— —h—a—n—d—l—i—n—g—,— —a—n—d— —c—o—s—t—/—c—o—n—t—e—x—t— —c—o—n—t—r—o—l—s—.— —U—s—e— —w—h—e—n— —a—r—c—h—i—t—e—c—t—i—n—g— —a— —m—u—l—t—i—-—s—t—e—p— —a—g—e—n—t— —p—i—p—e—l—i—n—e—,— —c—h—o—o—s—i—n—g— —b—e—t—w—e—e—n— —s—i—n—g—l—e—-—a—g—e—n—t— —v—s— —m—u—l—t—i—-—a—g—e—n—t— —a—p—p—r—o—a—c—h—e—s—,— —o—r— —r—e—f—a—c—t—o—r—i—n—g— —a—n— —L—L—M— —w—o—r—k—f—l—o—w— —t—h—a—t— —s—u—f—f—e—r—s— —f—r—o—m— —c—o—n—t—e—x—t— —b—l—o—a—t— —o—r— —u—n—r—e—l—i—a—b—l—e— —h—a—n—d—o—f—f—s.
---

# Agent Workflow Designer

**Tier:** POWERFUL  
**Category:** Engineering  
**Domain:** Multi-Agent Systems / AI Orchestration

---

## Overview

Design production-grade multi-agent workflows with clear pattern choice, handoff contracts, failure handling, and cost/context controls.

## Core Capabilities

- Workflow pattern selection for multi-step agent systems
- Skeleton config generation for fast workflow bootstrapping
- Context and cost discipline across long-running flows
- Error recovery and retry strategy scaffolding
- Documentation pointers for operational pattern tradeoffs

---

## When to Use

- A single prompt is insufficient for task complexity
- You need specialist agents with explicit boundaries
- You want deterministic workflow structure before implementation
- You need validation loops for quality or safety gates

---

## Quick Start

```bash
# Generate a sequential workflow skeleton
python3 scripts/workflow_scaffolder.py sequential --name content-pipeline

# Generate an orchestrator workflow and save it
python3 scripts/workflow_scaffolder.py orchestrator --name incident-triage --output workflows/incident-triage.json
```

---

## Pattern Map

- `sequential`: strict step-by-step dependency chain
- `parallel`: fan-out/fan-in for independent subtasks
- `router`: dispatch by intent/type with fallback
- `orchestrator`: planner coordinates specialists with dependencies
- `evaluator`: generator + quality gate loop

Detailed templates: `references/workflow-patterns.md`

---

## Recommended Workflow

1. Select pattern based on dependency shape and risk profile.
2. Scaffold config via `scripts/workflow_scaffolder.py`.
3. Define handoff contract fields for every edge.
4. Add retry/timeouts and output validation gates.
5. Dry-run with small context budgets before scaling.

---

## Common Pitfalls

- Over-orchestrating tasks solvable by one well-structured prompt
- Missing timeout/retry policies for external-model calls
- Passing full upstream context instead of targeted artifacts
- Ignoring per-step cost accumulation

## Best Practices

1. Start with the smallest pattern that can satisfy requirements.
2. Keep handoff payloads explicit and bounded.
3. Validate intermediate outputs before fan-in synthesis.
4. Enforce budget and timeout limits in every step.
