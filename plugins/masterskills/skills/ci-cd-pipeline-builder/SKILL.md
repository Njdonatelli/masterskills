---
name: "ci-cd-pipeline-builder"
description: >-
  G—e—n—e—r—a—t—e— —p—r—a—g—m—a—t—i—c— —C—I—/—C—D— —p—i—p—e—l—i—n—e—s— —f—r—o—m— —d—e—t—e—c—t—e—d— —p—r—o—j—e—c—t— —s—t—a—c—k— —s—i—g—n—a—l—s— ——— —f—a—s—t— —b—a—s—e—l—i—n—e— —g—e—n—e—r—a—t—i—o—n—,— —r—e—p—e—a—t—a—b—l—e— —c—h—e—c—k—s—,— —e—n—v—i—r—o—n—m—e—n—t—-—a—w—a—r—e— —d—e—p—l—o—y—m—e—n—t— —s—t—a—g—e—s—.— —U—s—e— —w—h—e—n— —s—e—t—t—i—n—g— —u—p— —C—I— —f—o—r— —a— —n—e—w— —p—r—o—j—e—c—t—,— —r—e—f—a—c—t—o—r—i—n—g— —e—x—i—s—t—i—n—g— —p—i—p—e—l—i—n—e—s—,— —o—r— —s—t—a—n—d—a—r—d—i—z—i—n—g— —d—e—p—l—o—y—m—e—n—t— —w—o—r—k—f—l—o—w—s— —a—c—r—o—s—s— —m—u—l—t—i—p—l—e— —r—e—p—o—s.
---

# CI/CD Pipeline Builder

**Tier:** POWERFUL  
**Category:** Engineering  
**Domain:** DevOps / Automation

## Overview

Use this skill to generate pragmatic CI/CD pipelines from detected project stack signals, not guesswork. It focuses on fast baseline generation, repeatable checks, and environment-aware deployment stages.

## Core Capabilities

- Detect language/runtime/tooling from repository files
- Recommend CI stages (`lint`, `test`, `build`, `deploy`)
- Generate GitHub Actions or GitLab CI starter pipelines
- Include caching and matrix strategy based on detected stack
- Emit machine-readable detection output for automation
- Keep pipeline logic aligned with project lockfiles and build commands

## When to Use

- Bootstrapping CI for a new repository
- Replacing brittle copied pipeline files
- Migrating between GitHub Actions and GitLab CI
- Auditing whether pipeline steps match actual stack
- Creating a reproducible baseline before custom hardening

## Key Workflows

### 1. Detect Stack

```bash
python3 scripts/stack_detector.py --repo . --format text
python3 scripts/stack_detector.py --repo . --format json > detected-stack.json
```

Supports input via stdin or `--input` file for offline analysis payloads.

### 2. Generate Pipeline From Detection

```bash
python3 scripts/pipeline_generator.py \
  --input detected-stack.json \
  --platform github \
  --output .github/workflows/ci.yml \
  --format text
```

Or end-to-end from repo directly:

```bash
python3 scripts/pipeline_generator.py --repo . --platform gitlab --output .gitlab-ci.yml
```

### 3. Validate Before Merge

1. Confirm commands exist in project (`test`, `lint`, `build`).
2. Run generated pipeline locally where possible.
3. Ensure required secrets/env vars are documented.
4. Keep deploy jobs gated by protected branches/environments.

### 4. Add Deployment Stages Safely

- Start with CI-only (`lint/test/build`).
- Add staging deploy with explicit environment context.
- Add production deploy with manual gate/approval.
- Keep rollout/rollback commands explicit and auditable.

## Script Interfaces

- `python3 scripts/stack_detector.py --help`
  - Detects stack signals from repository files
  - Reads optional JSON input from stdin/`--input`
- `python3 scripts/pipeline_generator.py --help`
  - Generates GitHub/GitLab YAML from detection payload
  - Writes to stdout or `--output`

## References

- [references/pipeline-design-notes.md](references/pipeline-design-notes.md) — common pitfalls, best practices, detection heuristics, generation strategy, platform decision notes, pre-merge validation checklist, and scaling guidance
- [references/github-actions-templates.md](references/github-actions-templates.md)
- [references/gitlab-ci-templates.md](references/gitlab-ci-templates.md)
- [references/deployment-gates.md](references/deployment-gates.md)
- [README.md](README.md)
