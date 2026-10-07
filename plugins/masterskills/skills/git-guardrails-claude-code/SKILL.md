---
name: git-guardrails-claude-code
description: >-
  S—e—t— —u—p— —C—l—a—u—d—e— —C—o—d—e— —h—o—o—k—s— —t—o— —b—l—o—c—k— —d—a—n—g—e—r—o—u—s— —g—i—t— —c—o—m—m—a—n—d—s— —(—p—u—s—h—,— —r—e—s—e—t— —-—-—h—a—r—d—,— —c—l—e—a—n—,— —b—r—a—n—c—h— —-—D—,— —e—t—c—.—)— —b—e—f—o—r—e— —t—h—e—y— —e—x—e—c—u—t—e—.— —U—s—e— —w—h—e—n— —u—s—e—r— —w—a—n—t—s— —t—o— —p—r—e—v—e—n—t— —d—e—s—t—r—u—c—t—i—v—e— —g—i—t— —o—p—e—r—a—t—i—o—n—s—,— —a—d—d— —g—i—t— —s—a—f—e—t—y— —h—o—o—k—s—,— —o—r— —b—l—o—c—k— —g—i—t— —p—u—s—h—/—r—e—s—e—t— —i—n— —C—l—a—u—d—e— —C—o—d—e.
---

# Setup Git Guardrails

Sets up a PreToolUse hook that intercepts and blocks dangerous git commands before Claude executes them.

## What Gets Blocked

- `git push` (all variants including `--force`)
- `git reset --hard`
- `git clean -f` / `git clean -fd`
- `git branch -D`
- `git checkout .` / `git restore .`

When blocked, Claude sees a message telling it that it does not have authority to access these commands.

## Steps

### 1. Ask scope

Ask the user: install for **this project only** (`.claude/settings.json`) or **all projects** (`~/.claude/settings.json`)?

### 2. Copy the hook script

The bundled script is at: [scripts/block-dangerous-git.sh](scripts/block-dangerous-git.sh)

Copy it to the target location based on scope:

- **Project**: `.claude/hooks/block-dangerous-git.sh`
- **Global**: `~/.claude/hooks/block-dangerous-git.sh`

Make it executable with `chmod +x`.

### 3. Add hook to settings

Add to the appropriate settings file:

**Project** (`.claude/settings.json`):

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/block-dangerous-git.sh"
          }
        ]
      }
    ]
  }
}
```

**Global** (`~/.claude/settings.json`):

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "~/.claude/hooks/block-dangerous-git.sh"
          }
        ]
      }
    ]
  }
}
```

If the settings file already exists, merge the hook into existing `hooks.PreToolUse` array — don't overwrite other settings.

### 4. Ask about customization

Ask if user wants to add or remove any patterns from the blocked list. Edit the copied script accordingly.

### 5. Verify

Run a quick test:

```bash
echo '{"tool_input":{"command":"git push origin main"}}' | <path-to-script>
```

Should exit with code 2 and print a BLOCKED message to stderr.
