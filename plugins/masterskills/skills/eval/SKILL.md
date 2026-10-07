---
name: "eval"
description: >-
  E—v—a—l—u—a—t—e— —a—n—d— —r—a—n—k— —a—g—e—n—t— —r—e—s—u—l—t—s— —b—y— —m—e—t—r—i—c— —o—r— —L—L—M— —j—u—d—g—e— —f—o—r— —a—n— —A—g—e—n—t—H—u—b— —s—e—s—s—i—o—n—.— —U—s—e— —w—h—e—n— —t—h—e— —u—s—e—r— —r—u—n—s— —/—h—u—b—:—e—v—a—l— —o—r— —a—s—k—s— —t—o— —s—c—o—r—e—,— —c—o—m—p—a—r—e—,— —o—r— —p—i—c—k— —a— —w—i—n—n—e—r— —a—m—o—n—g— —c—o—m—p—l—e—t—e—d— —A—g—e—n—t—H—u—b— —a—g—e—n—t—s.
command: /hub:eval
---

# /hub:eval — Evaluate Agent Results

Rank all agent results for a session. Supports metric-based evaluation (run a command), LLM judge (compare diffs), or hybrid.

## Usage

```
/hub:eval                           # Eval latest session using configured criteria
/hub:eval 20260317-143022           # Eval specific session
/hub:eval --judge                   # Force LLM judge mode (ignore metric config)
```

## What It Does

### Metric Mode (eval command configured)

Run the evaluation command in each agent's worktree:

```bash
python {skill_path}/scripts/result_ranker.py \
  --session {session-id} \
  --eval-cmd "{eval_cmd}" \
  --metric {metric} --direction {direction}
```

Output:
```
RANK  AGENT       METRIC      DELTA      FILES
1     agent-2     142ms       -38ms      2
2     agent-1     165ms       -15ms      3
3     agent-3     190ms       +10ms      1

Winner: agent-2 (142ms)
```

### LLM Judge Mode (no eval command, or --judge flag)

For each agent:
1. Get the diff: `git diff {base_branch}...{agent_branch}`
2. Read the agent's result post from `.agenthub/board/results/agent-{i}-result.md`
3. Compare all diffs and rank by:
   - **Correctness** — Does it solve the task?
   - **Simplicity** — Fewer lines changed is better (when equal correctness)
   - **Quality** — Clean execution, good structure, no regressions

Present rankings with justification.

Example LLM judge output for a content task:
```
RANK  AGENT    VERDICT                               WORD COUNT
1     agent-1  Strong narrative, clear CTA            1480
2     agent-3  Good data points, weak intro           1520
3     agent-2  Generic tone, no differentiation       1350

Winner: agent-1 (strongest narrative arc and call-to-action)
```

### Hybrid Mode

1. Run metric evaluation first
2. If top agents are within 10% of each other, use LLM judge to break ties
3. Present both metric and qualitative rankings

## After Eval

1. Update session state:
```bash
python {skill_path}/scripts/session_manager.py --update {session-id} --state evaluating
```

2. Tell the user:
   - Ranked results with winner highlighted
   - Next step: `/hub:merge` to merge the winner
   - Or `/hub:merge {session-id} --agent {winner}` to be explicit
