---
name: "skill-tester"
description: >-
  V—a—l—i—d—a—t—e—,— —t—e—s—t—,— —a—n—d— —s—c—o—r—e— —t—h—e— —q—u—a—l—i—t—y— —o—f— —s—k—i—l—l—s— —w—i—t—h—i—n— —t—h—e— —c—l—a—u—d—e—-—s—k—i—l—l—s— —e—c—o—s—y—s—t—e—m—.— —C—o—m—p—r—e—h—e—n—s—i—v—e— —m—e—t—a—-—s—k—i—l—l—:— —s—t—r—u—c—t—u—r—e— —v—a—l—i—d—a—t—i—o—n—,— —P—y—t—h—o—n— —s—c—r—i—p—t— —t—e—s—t—i—n—g— —(—s—y—n—t—a—x— —+— —i—m—p—o—r—t—s— —+— —r—u—n—t—i—m—e— —+— —o—u—t—p—u—t— —f—o—r—m—a—t—)—,— —m—u—l—t—i—-—d—i—m—e—n—s—i—o—n—a—l— —q—u—a—l—i—t—y— —s—c—o—r—i—n—g— —w—i—t—h— —l—e—t—t—e—r— —g—r—a—d—e—s— —a—n—d— —t—i—e—r— —c—l—a—s—s—i—f—i—c—a—t—i—o—n— —(—B—A—S—I—C—/—S—T—A—N—D—A—R—D—/—P—O—W—E—R—F—U—L—)—.— —U—s—e— —w—h—e—n— —a—u—t—h—o—r—i—n—g— —a— —n—e—w— —s—k—i—l—l—,— —a—u—d—i—t—i—n—g— —e—x—i—s—t—i—n—g— —s—k—i—l—l—s— —f—o—r— —t—i—e—r— —p—r—o—m—o—t—i—o—n—,— —s—e—t—t—i—n—g— —u—p— —p—r—e—-—c—o—m—m—i—t— —h—o—o—k—s— —f—o—r— —s—k—i—l—l— —q—u—a—l—i—t—y—,— —o—r— —i—n—t—e—g—r—a—t—i—n—g— —s—k—i—l—l— —Q—A— —i—n—t—o— —C—I.
---

# Skill Tester

**Tier**: POWERFUL · **Category**: Engineering Quality Assurance · **Dependencies**: None (Python stdlib only)

Meta-skill that validates, tests, and scores skills in this repository. Four tools, run from the **repo root** with full paths:

1. **`scripts/skill_validator.py`** — structure + documentation compliance
2. **`scripts/script_tester.py`** — Python script syntax/imports/runtime/output testing
3. **`scripts/quality_scorer.py`** — multi-dimensional scoring with letter grade
4. **`scripts/security_scorer.py`** — security posture scoring (also available via `quality_scorer.py --include-security`)

> **Scope note:** this skill's tier line-count minimums measure *legacy* skills. For authoring *new* skills, `engineering/write-a-skill` (SKILL.md under ~100 lines, Matt Pocock doctrine) is the binding standard — do not pad a new skill to satisfy a tier minimum here.

## Quick Start (exact, runnable from repo root)

```bash
# 1. Validate structure (exit non-zero on failure — usable as a gate)
python3 engineering/skills/skill-tester/scripts/skill_validator.py engineering/skills/self-eval --json

# 2. Test the skill's Python scripts (30s default timeout per script)
python3 engineering/skills/skill-tester/scripts/script_tester.py engineering/skills/self-eval --json

# 3. Score quality (fail CI below threshold with --minimum-score)
python3 engineering/skills/skill-tester/scripts/quality_scorer.py engineering/skills/self-eval --json --detailed --minimum-score 75
```

Consume the JSON: validator emits `overall_score`, `compliance_level`, per-check `checks{}`; scorer emits `overall_score`, `letter_grade`, `tier_recommendation`, `dimensions`, and an `improvement_roadmap` — work the roadmap top-down, then re-run until the target score is met.

For repo-wide auditing prefer `scripts/audit_skills.py` at the repo root (wraps the write-a-skill checklist runner across all skills).

## What Each Tool Checks

### skill_validator.py
- SKILL.md frontmatter parsing, required sections, minimum line counts per tier (`--tier BASIC|STANDARD|POWERFUL`)
- Required structure: SKILL.md, README.md, scripts/, references/, assets/, expected_outputs/
- Python scripts: argparse present, stdlib-only imports

### script_tester.py
- AST-based syntax validation; import analysis (flags external dependencies)
- Controlled execution with timeout protection (`--timeout`, default 30s)
- `--help` functionality verification; sample-data runs compared against expected_outputs/

### quality_scorer.py
Four dimensions, 25% each: **Documentation** (depth, examples, references), **Code Quality** (complexity, error handling, output consistency), **Completeness** (required dirs, sample data, expected outputs), **Usability** (help text, example clarity). Outputs 0-100 + A-F grade + tier recommendation.

## Tier Classification

| Tier | SKILL.md | Scripts | CLI surface |
|---|---|---|---|
| BASIC | ≥ 100 lines | 1 (100-300 LOC) | basic argparse |
| STANDARD | ≥ 200 lines | 1-2 (300-500 LOC) | subcommands, JSON + text output |
| POWERFUL | ≥ 300 lines | 2-3 (500-800 LOC) | multiple modes, CI integration |

(Advisory for legacy skills; new skills follow write-a-skill — see scope note above.)

## CI Integration

```yaml
# GitHub Actions: gate changed skills
- name: "validate-changed-skills"
  run: |
    for skill in $changed_skills; do
      python3 engineering/skills/skill-tester/scripts/skill_validator.py "$skill" --json
      python3 engineering/skills/skill-tester/scripts/script_tester.py "$skill"
      python3 engineering/skills/skill-tester/scripts/quality_scorer.py "$skill" --minimum-score 75
    done
```

Pre-commit hook: run the validator on the staged skill directory and block the commit on non-zero exit.

## Verification Loop

A skill "passes" when, in one run from repo root:

1. `skill_validator.py <skill> --json` exits 0,
2. `script_tester.py <skill>` reports all scripts passing, and
3. `quality_scorer.py <skill> --minimum-score <target>` exits 0.

If any step fails, apply the top `improvement_roadmap` item and re-run all three — never report a partial pass.

## Troubleshooting

- **Timeout errors** → raise `--timeout` or optimize the script under test
- **Import failures** → external deps detected; stdlib-only is the repo policy
- **Tier misclassification** → check line counts/LOC against the tier table; remember the write-a-skill exception for new skills

References: `references/` holds the structure specification, tier requirements matrix, and scoring rubric the tools implement.
