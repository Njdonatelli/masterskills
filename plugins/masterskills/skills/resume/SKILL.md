---
name: "resume"
description: >-
  R—e—s—u—m—e— —a— —p—a—u—s—e—d— —e—x—p—e—r—i—m—e—n—t—.— —C—h—e—c—k—o—u—t— —t—h—e— —e—x—p—e—r—i—m—e—n—t— —b—r—a—n—c—h—,— —r—e—a—d— —r—e—s—u—l—t—s— —h—i—s—t—o—r—y—,— —c—o—n—t—i—n—u—e— —i—t—e—r—a—t—i—n—g—.— —U—s—e— —w—h—e—n— —t—h—e— —u—s—e—r— —r—u—n—s— —/—a—r—:—r—e—s—u—m—e— —o—r— —a—s—k—s— —t—o— —p—i—c—k— —u—p— —a— —p—r—e—v—i—o—u—s—l—y— —s—t—a—r—t—e—d— —a—u—t—o—r—e—s—e—a—r—c—h— —e—x—p—e—r—i—m—e—n—t.
command: /ar:resume
---

# /ar:resume — Resume Experiment

Resume a paused or context-limited experiment. Reads all history and continues where you left off.

## Usage

```
/ar:resume                                  # List experiments, let user pick
/ar:resume engineering/api-speed            # Resume specific experiment
```

## What It Does

### Step 1: List experiments if needed

If no experiment specified:

```bash
python {skill_path}/scripts/setup_experiment.py --list
```

Show status for each (active/paused/done based on results.tsv age). Let user pick.

### Step 2: Load full context

```bash
# Checkout the experiment branch
git checkout autoresearch/{domain}/{name}

# Read config
cat .autoresearch/{domain}/{name}/config.cfg

# Read strategy
cat .autoresearch/{domain}/{name}/program.md

# Read full results history
cat .autoresearch/{domain}/{name}/results.tsv

# Read recent git log for the branch
git log --oneline -20
```

### Step 3: Report current state

Summarize for the user:

```
Resuming: engineering/api-speed
  Target: src/api/search.py
  Metric: p50_ms (lower is better)
  Experiments: 23 total — 8 kept, 12 discarded, 3 crashed
  Best: 185ms (-42% from baseline of 320ms)
  Last experiment: "added response caching" → KEEP (185ms)

  Recent patterns:
  - Caching changes: 3 kept, 1 discarded (consistently helpful)
  - Algorithm changes: 2 discarded, 1 crashed (high risk, low reward so far)
  - I/O optimization: 2 kept (promising direction)
```

### Step 4: Ask next action

```
How would you like to continue?
  1. Single iteration (/ar:run)  — I'll make one change and evaluate
  2. Start a loop (/ar:loop)     — Autonomous with scheduled interval
  3. Just show me the results    — I'll review and decide
```

If the user picks loop, hand off to `/ar:loop` with the experiment pre-selected.
If single, hand off to `/ar:run`.
