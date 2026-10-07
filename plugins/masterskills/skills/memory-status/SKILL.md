---
name: "memory-status"
description: >-
  M—e—m—o—r—y— —h—e—a—l—t—h— —d—a—s—h—b—o—a—r—d— —s—h—o—w—i—n—g— —l—i—n—e— —c—o—u—n—t—s—,— —t—o—p—i—c— —f—i—l—e—s—,— —c—a—p—a—c—i—t—y—,— —s—t—a—l—e— —e—n—t—r—i—e—s—,— —a—n—d— —r—e—c—o—m—m—e—n—d—a—t—i—o—n—s—.— —U—s—e— —w—h—e—n— —t—h—e— —u—s—e—r— —r—u—n—s— —/—s—i—:—m—e—m—o—r—y—-—s—t—a—t—u—s— —o—r— —a—s—k—s— —h—o—w— —f—u—l—l— —o—r— —h—e—a—l—t—h—y— —t—h—e— —a—g—e—n—t— —m—e—m—o—r—y— —i—s.
---

# /si:memory-status — Memory Health Dashboard

Quick overview of your project's memory state across all memory systems.

## Usage

```
/si:memory-status                    # Full dashboard
/si:memory-status --brief            # One-line summary
```

## What It Reports

### Step 1: Locate all memory files

```bash
# Auto-memory directory
MEMORY_DIR="$HOME/.claude/projects/$(pwd | sed 's|/|%2F|g; s|%2F|/|; s|^/||')/memory"

# Count lines in MEMORY.md
wc -l "$MEMORY_DIR/MEMORY.md" 2>/dev/null || echo "0"

# List topic files
ls "$MEMORY_DIR/"*.md 2>/dev/null | grep -v MEMORY.md

# CLAUDE.md
wc -l ./CLAUDE.md 2>/dev/null || echo "0"
wc -l ~/.claude/CLAUDE.md 2>/dev/null || echo "0"

# Rules directory
ls .claude/rules/*.md 2>/dev/null | wc -l
```

### Step 2: Analyze capacity

| Metric | Healthy | Warning | Critical |
|--------|---------|---------|----------|
| MEMORY.md lines | < 120 | 120-180 | > 180 |
| CLAUDE.md lines | < 150 | 150-200 | > 200 |
| Topic files | 0-3 | 4-6 | > 6 |
| Stale entries | 0 | 1-3 | > 3 |

### Step 3: Quick stale check

For each MEMORY.md entry that references a file path:
```bash
# Verify referenced files still exist
grep -oE '[a-zA-Z0-9_/.-]+\.(ts|js|py|md|json|yaml|yml)' "$MEMORY_DIR/MEMORY.md" | while read f; do
  [ ! -f "$f" ] && echo "STALE: $f"
done
```

### Step 4: Output

```
📊 Memory Status

  Auto-Memory (MEMORY.md):
    Lines:        {{n}}/200 ({{bar}}) {{emoji}}
    Topic files:  {{count}} ({{names}})
    Last updated: {{date}}

  Project Rules:
    CLAUDE.md:    {{n}} lines
    Rules:        {{count}} files in .claude/rules/
    User global:  {{n}} lines (~/.claude/CLAUDE.md)

  Health:
    Capacity:     {{healthy/warning/critical}}
    Stale refs:   {{count}} (files no longer exist)
    Duplicates:   {{count}} (entries repeated across files)

  {{if recommendations}}
  💡 Recommendations:
    - {{recommendation}}
  {{endif}}
```

### Brief mode

```
/si:memory-status --brief
```

Output: `📊 Memory: {{n}}/200 lines | {{count}} rules | {{status_emoji}} {{status_word}}`

## Interpretation

- **Green (< 60%)**: Plenty of room. Auto-memory is working well.
- **Yellow (60-90%)**: Getting full. Consider running `/si:memory-review` to promote or clean up.
- **Red (> 90%)**: Near capacity. Auto-memory may start dropping older entries. Run `/si:memory-review` now.

## Tips

- Run `/si:memory-status --brief` as a quick check anytime
- If capacity is yellow+, run `/si:memory-review` to identify promotion candidates
- Stale entries waste space — delete references to files that no longer exist
- Topic files are fine — Claude creates them to keep MEMORY.md under 200 lines
