---
name: "prompt-engineer-toolkit"
description: >-
  T—u—r—n—s— —m—a—r—k—e—t—i—n—g— —p—r—o—m—p—t—s— —i—n—t—o— —t—e—s—t—e—d—,— —v—e—r—s—i—o—n—e—d— —p—r—o—d—u—c—t—i—o—n— —a—s—s—e—t—s—:— —A—/—B— —p—r—o—m—p—t— —e—v—a—l—u—a—t—i—o—n— —a—g—a—i—n—s—t— —s—t—r—u—c—t—u—r—e—d— —t—e—s—t— —c—a—s—e—s—,— —i—m—m—u—t—a—b—l—e— —p—r—o—m—p—t— —v—e—r—s—i—o—n— —h—i—s—t—o—r—y— —w—i—t—h— —d—i—f—f—s—,— —r—e—a—d—y—-—t—o—-—u—s—e— —m—a—r—k—e—t—i—n—g— —p—r—o—m—p—t— —t—e—m—p—l—a—t—e—s— —(—a—d— —c—o—p—y—,— —e—m—a—i—l— —c—a—m—p—a—i—g—n—s—,— —s—o—c—i—a—l— —p—o—s—t—s—,— —l—a—n—d—i—n—g— —p—a—g—e—s—,— —S—E—O— —m—e—t—a—)—,— —a—n—d— —a—n— —L—L—M—-—g—o—v—e—r—n—a—n—c—e— —p—l—a—y—b—o—o—k— —f—o—r— —m—a—r—k—e—t—i—n—g— —t—e—a—m—s— —(—c—l—a—i—m— —d—i—s—c—i—p—l—i—n—e—,— —d—i—s—c—l—o—s—u—r—e— —r—u—l—e—s—,— —h—u—m—a—n—-—r—e—v—i—e—w— —g—a—t—e—s—)—.— —U—s—e— —w—h—e—n— —a— —m—a—r—k—e—t—i—n—g— —t—e—a—m— —r—e—l—i—e—s— —o—n— —A—I—-—g—e—n—e—r—a—t—e—d— —c—o—n—t—e—n—t— —a—n—d— —n—e—e—d—s— —p—r—o—m—p—t— —q—u—a—l—i—t—y— —t—o— —b—e— —m—e—a—s—u—r—a—b—l—e— —a—n—d— —s—a—f—e— ——— —o—r— —w—h—e—n— —t—h—e— —u—s—e—r— —m—e—n—t—i—o—n—s— —'—p—r—o—m—p—t— —e—n—g—i—n—e—e—r—i—n—g—,—'— —'—i—m—p—r—o—v—e— —m—y— —p—r—o—m—p—t—s—,—'— —'—p—r—o—m—p—t— —t—e—m—p—l—a—t—e—s—,—'— —'—p—r—o—m—p—t— —v—e—r—s—i—o—n—i—n—g—,—'— —'—A—I— —c—o—n—t—e—n—t— —w—o—r—k—f—l—o—w—,—'— —o—r— —'—A—I— —g—o—v—e—r—n—a—n—c—e— —f—o—r— —m—a—r—k—e—t—i—n—g.
license: MIT
metadata:
  version: 1.0.0
  author: Alireza Rezvani
  category: marketing
  updated: 2026-03-06
---

# Prompt Engineer Toolkit

## Overview

Use this skill to move prompts from ad-hoc drafts to production assets with repeatable testing, versioning, and regression safety. It emphasizes measurable quality over intuition. Apply it when launching a new LLM feature that needs reliable outputs, when prompt quality degrades after model or instruction changes, when multiple team members edit prompts and need history/diffs, when you need evidence-based prompt choice for production rollout, or when you want consistent prompt governance across environments.

## Core Capabilities

- A/B prompt evaluation against structured test cases
- Quantitative scoring for adherence, relevance, and safety checks
- Prompt version tracking with immutable history and changelog
- Prompt diffs to review behavior-impacting edits
- Reusable prompt templates and selection guidance
- Regression-friendly workflows for model/prompt updates

## Key Workflows

### 1. Run Prompt A/B Test

Prepare JSON test cases and run:

```bash
python3 scripts/prompt_tester.py \
  --prompt-a-file prompts/a.txt \
  --prompt-b-file prompts/b.txt \
  --cases-file testcases.json \
  --runner-cmd 'my-llm-cli --prompt {prompt} --input {input}' \
  --format text
```

Input can also come from stdin/`--input` JSON payload.

### 2. Choose Winner With Evidence

The tester scores outputs per case and aggregates:

- expected content coverage
- forbidden content violations
- regex/format compliance
- output length sanity

Use the higher-scoring prompt as candidate baseline, then run regression suite.

### 3. Version Prompts

```bash
# Add version
python3 scripts/prompt_versioner.py add \
  --name support_classifier \
  --prompt-file prompts/support_v3.txt \
  --author alice

# Diff versions
python3 scripts/prompt_versioner.py diff --name support_classifier --from-version 2 --to-version 3

# Changelog
python3 scripts/prompt_versioner.py changelog --name support_classifier
```

### 4. Regression Loop

1. Store baseline version.
2. Propose prompt edits.
3. Re-run A/B test.
4. Promote only if score and safety constraints improve.

## Script Interfaces

- `python3 scripts/prompt_tester.py --help`
  - Reads prompts/cases from stdin or `--input`
  - Optional external runner command
  - Emits text or JSON metrics
- `python3 scripts/prompt_versioner.py --help`
  - Manages prompt history (`add`, `list`, `diff`, `changelog`)
  - Stores metadata and content snapshots locally

## Pitfalls, Best Practices & Review Checklist

**Avoid these mistakes:**
1. Picking prompts from single-case outputs — use a realistic, edge-case-rich test suite.
2. Changing prompt and model simultaneously — always isolate variables.
3. Missing `must_not_contain` (forbidden-content) checks in evaluation criteria.
4. Editing prompts without version metadata, author, or change rationale.
5. Skipping semantic diffs before deploying a new prompt version.
6. Optimizing one benchmark while harming edge cases — track the full suite.
7. Model swap without rerunning the baseline A/B suite.

**Before promoting any prompt, confirm:**
- [ ] Task intent is explicit and unambiguous.
- [ ] Output schema/format is explicit.
- [ ] Safety and exclusion constraints are explicit.
- [ ] No contradictory instructions.
- [ ] No unnecessary verbosity tokens.
- [ ] A/B score improves and violation count stays at zero.

## References

- [references/prompt-templates.md](references/prompt-templates.md) — 6 production marketing templates (ad copy, email sequence, social repurposing, landing sections, SEO meta, brand-voice rewrite) plus generic building blocks; each written to be graded by `prompt_tester.py`
- [references/technique-guide.md](references/technique-guide.md) — technique-selection table for marketing tasks + the LLM-governance stack for marketing teams (claim discipline, disclosure rules, data boundaries, human-review gates)
- [references/evaluation-rubric.md](references/evaluation-rubric.md) — mechanical scoring weights, acceptance gates, marketing quality dimensions, test-suite design, and eval anti-patterns
- [README.md](README.md)

## Evaluation Design

Each test case should define:

- `input`: realistic production-like input
- `expected_contains`: required markers/content
- `forbidden_contains`: disallowed phrases or unsafe content
- `expected_regex`: required structural patterns

This enables deterministic grading across prompt variants.

## Versioning Policy

- Use semantic prompt identifiers per feature (`support_classifier`, `ad_copy_shortform`).
- Record author + change note for every revision.
- Never overwrite historical versions.
- Diff before promoting a new prompt to production.

## Rollout Strategy

1. Create baseline prompt version.
2. Propose candidate prompt.
3. Run A/B suite against same cases.
4. Promote only if winner improves average and keeps violation count at zero.
5. Track post-release feedback and feed new failure cases back into test suite.
