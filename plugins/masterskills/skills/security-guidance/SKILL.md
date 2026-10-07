---
name: security-guidance
description: >-
  P—r—e—T—o—o—l—U—s—e— —s—e—c—u—r—i—t—y—-—a—n—t—i—-—p—a—t—t—e—r—n— —h—o—o—k— —f—o—r— —C—l—a—u—d—e— —C—o—d—e—.— —C—a—t—c—h—e—s— —1—2— —c—o—m—m—o—n— —s—e—c—u—r—i—t—y— —r—i—s—k—s— —(—c—o—m—m—a—n—d— —i—n—j—e—c—t—i—o—n—,— —X—S—S—,— —S—Q—L— —i—n—j—e—c—t—i—o—n—,— —u—n—s—a—f—e— —d—e—s—e—r—i—a—l—i—z—a—t—i—o—n—,— —G—i—t—H—u—b— —A—c—t—i—o—n—s— —w—o—r—k—f—l—o—w— —i—n—j—e—c—t—i—o—n—,— —e—v—a—l—/—n—e—w— —F—u—n—c—t—i—o—n— —c—o—d—e— —i—n—j—e—c—t—i—o—n—)— —B—E—F—O—R—E— —t—h—e— —E—d—i—t—/—W—r—i—t—e—/—M—u—l—t—i—E—d—i—t— —o—p—e—r—a—t—i—o—n— —c—o—m—p—l—e—t—e—s—.— —S—e—s—s—i—o—n—-—s—t—a—t—e— —c—a—c—h—i—n—g— —p—r—e—v—e—n—t—s— —d—u—p—l—i—c—a—t—e— —w—a—r—n—i—n—g—s— —o—n— —t—h—e— —s—a—m—e— —f—i—l—e—+—r—u—l—e— —c—o—m—b—o—.— —S—t—d—l—i—b— —o—n—l—y— ——— —n—o— —d—e—p—e—n—d—e—n—c—i—e—s—.— —U—s—e— —w—h—e—n— —y—o—u— —w—a—n—t— —a— —s—a—f—e—t—y— —n—e—t— —d—u—r—i—n—g— —C—l—a—u—d—e— —C—o—d—e— —s—e—s—s—i—o—n—s— —t—h—a—t— —t—o—u—c—h— —s—e—c—u—r—i—t—y—-—s—e—n—s—i—t—i—v—e— —c—o—d—e— —(—a—u—t—h—,— —p—a—y—m—e—n—t—s—,— —u—s—e—r— —i—n—p—u—t— —h—a—n—d—l—i—n—g—,— —I—a—C—)—.— —D—i—s—a—b—l—e— —w—i—t—h— —E—N—A—B—L—E—_—S—E—C—U—R—I—T—Y—_—R—E—M—I—N—D—E—R—=—0— —i—f— —y—o—u— —n—e—e—d— —t—o— —p—e—r—f—o—r—m— —a— —v—e—r—i—f—i—e—d—-—s—a—f—e— —o—p—e—r—a—t—i—o—n— —t—h—a—t— —w—o—u—l—d— —o—t—h—e—r—w—i—s—e— —t—r—i—p— —a— —p—a—t—t—e—r—n—.— —T—r—i—g—g—e—r—s— ——— —"—a—d—d— —s—e—c—u—r—i—t—y— —h—o—o—k—"—,— —"—b—l—o—c—k— —u—n—s—a—f—e— —c—o—d—e—"—,— —"—d—e—t—e—c—t— —c—o—m—m—a—n—d— —i—n—j—e—c—t—i—o—n— —b—e—f—o—r—e— —w—r—i—t—e—"—,— —"—p—r—e—v—e—n—t— —S—Q—L— —i—n—j—e—c—t—i—o—n— —p—a—t—t—e—r—n—s—"—,— —"—s—e—c—u—r—i—t—y— —w—a—r—n—i—n—g— —h—o—o—k—".
---

# Security Guidance Hook

**A PreToolUse hook that blocks 12 common security anti-patterns before Claude Code writes them.**

This skill is a **hook**, not a slash command. Once installed, it runs automatically before every `Edit`, `Write`, or `MultiEdit` operation and warns + blocks if it detects a known dangerous pattern.

## What It Catches

The hook scans both:

- **The file path being edited** — flags GitHub Actions workflow files with risky `${{ }}` patterns
- **The content being written** — substring matches against 11 anti-patterns

| Pattern | Category | Risk |
|---|---|---|
| GitHub Actions workflow expressions | Path-based | Workflow command injection via untrusted inputs |
| `child_process.exec`, `exec(`, `execSync(` | Substring | Node.js command injection |
| `new Function` | Substring | JS code injection |
| `eval(` | Substring | JS code injection |
| `dangerouslySetInnerHTML` | Substring | React XSS |
| `document.write` | Substring | DOM XSS |
| `.innerHTML =` | Substring | DOM XSS |
| `pickle` | Substring | Python deserialization RCE |
| `os.system`, `from os import system` | Substring | Python command injection |
| `shell=True` (subprocess) | Substring | Python command injection |
| f-string SQL or `.format` SQL | Substring | SQL injection |
| `yaml.load(`, `yaml.unsafe_load` | Substring | YAML deserialization RCE |

## How It Works

1. Claude Code is about to run `Edit`, `Write`, or `MultiEdit`
2. PreToolUse hook fires → invokes `security_reminder_hook.py` with the tool input as JSON on stdin
3. The hook extracts file_path + content + checks against the pattern table
4. If a pattern matches AND this warning hasn't been shown for this file+rule in this session:
   - Print the warning to stderr (Claude sees it)
   - Exit code 2 → blocks the tool call
   - Save the warning key to `~/.claude/security_warnings_state_<session>.json`
5. If a pattern matches BUT the warning was already shown this session:
   - Allow the tool call (exit code 0) — Claude already saw the warning once
6. If no pattern matches:
   - Allow the tool call (exit code 0)

## Installation

This plugin ships as a Claude Code plugin with `hooks.json` wiring:

```bash
# In Claude Code:
/plugin marketplace add alirezarezvani/claude-skills
/plugin install security-guidance@claude-code-skills
```

Once installed, no further configuration needed — the hook runs automatically.

## Configuration

Disable per-session via environment variable:

```bash
ENABLE_SECURITY_REMINDER=0 claude
# Hook is bypassed for this session
```

Use sparingly — the hook is most useful exactly when you're tempted to disable it (because you're under deadline pressure to ship something you know is sketchy).

## Per-File Override Pattern

If a specific file legitimately needs `eval()` or `pickle` (e.g., a sandboxed REPL, a deliberately unsafe parser for a fuzzer), document it in the file with a comment:

```python
# SAFETY: pickle is the required serialization format for this internal tool.
# This file does NOT accept untrusted input. See SECURITY.md for boundary analysis.
import pickle
```

The hook will still warn on first edit per session. After acknowledging, subsequent edits in the same session are allowed (session-state caching).

## Why The Patterns Are Substring-Based (Not AST-Based)

Trade-off: AST-based detection would be more precise (no false positives on string literals containing "eval("). Substring-based is:

- **Faster** — runs in ms, doesn't parse the file
- **Cross-language** — same hook works for JS/TS/Python/YAML/etc.
- **Conservative** — false positives are easy to dismiss (one keystroke); false negatives are dangerous

For 90%+ of cases, substring detection is sufficient. If you need stricter detection, layer in a proper SAST tool (semgrep, CodeQL) as a CI step.

## State Files

The hook caches "warning shown" state in `~/.claude/security_warnings_state_<session_id>.json`. These files:

- Are auto-cleaned after 30 days (10% chance per hook invocation)
- Are session-scoped (each Claude session gets its own)
- Contain a JSON list of `<file_path>-<rule_name>` keys

You can safely delete `~/.claude/security_warnings_state_*.json` files at any time — the hook regenerates them on next run.

## Debug Log

The hook writes to `~/.claude/security-warnings-log.txt` for debugging hook misfires:

```bash
tail -f ~/.claude/security-warnings-log.txt
# Shows JSON decode errors, state-file save failures, etc.
```

(Upstream version wrote to `/tmp/security-warnings-log.txt` — we moved it to `~/.claude/` for persistence across reboots.)

## Source + Attribution

This plugin is ported from David Dworken's MIT-licensed implementation in [`alirezarezvani/aeo-box`](https://github.com/alirezarezvani/aeo-box/tree/main/.claude/plugins/security-guidance).

**Verbatim:** the original 9 patterns (GitHub Actions, child_process.exec, new Function, eval, dangerouslySetInnerHTML, document.write, innerHTML, pickle, os.system) are preserved with their exact warning text.

**Modifications:**
- Added 3 patterns: `subprocess shell=True`, SQL injection via f-string or `.format`, `yaml.unsafe_load`
- Debug log moved from `/tmp/security-warnings-log.txt` → `~/.claude/security-warnings-log.txt`
- Restructured as a claude-skills plugin with `attribution` block in `plugin.json`

## Anti-Patterns

### Disabling the hook by default

Defeats the purpose. If `ENABLE_SECURITY_REMINDER=0` becomes your default, you've trained yourself to ignore the safety net. Use it only for specific verified-safe operations.

### Modifying the pattern list without security review

Anyone can add a pattern. Removing one requires a security review — patterns exist because they map to real CVE classes.

### Treating session-state as immutable security policy

The cache prevents nag-spam but is per-session. Don't rely on "I dismissed this once" as long-term policy — use the per-file documentation pattern instead (comment justifying the use).

## Related Skills

- `engineering-team/skills/red-team` — adversarial pen-testing
- `engineering-team/skills/threat-detection` — threat modeling + detection design
- `engineering-team/skills/ai-security` — AI-specific security (prompt injection, etc.)
- `engineering/ship-gate` — pre-production audit (8-category, ~89 checks)
- `engineering/skill-security-auditor` — security scan for skill packages

## Trigger Phrases

- "add security hook"
- "block unsafe code before write"
- "detect command injection"
- "prevent SQL injection patterns"
- "warn on eval / pickle / os.system"
- "GitHub Actions security hook"

---

**Version:** 2.7.3
**Source:** Ported from [`alirezarezvani/aeo-box`](https://github.com/alirezarezvani/aeo-box) `.claude/plugins/security-guidance/` (originally by David Dworken at Anthropic, MIT)
**License:** MIT
