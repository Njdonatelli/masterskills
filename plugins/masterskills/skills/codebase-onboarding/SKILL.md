---
name: "codebase-onboarding"
description: >-
  A—n—a—l—y—z—e— —a— —c—o—d—e—b—a—s—e— —a—n—d— —g—e—n—e—r—a—t—e— —o—n—b—o—a—r—d—i—n—g— —d—o—c—u—m—e—n—t—a—t—i—o—n— —f—o—r— —e—n—g—i—n—e—e—r—s—,— —t—e—c—h— —l—e—a—d—s—,— —a—n—d— —c—o—n—t—r—a—c—t—o—r—s—.— —F—a—s—t— —f—a—c—t—-—g—a—t—h—e—r—i—n—g— —a—n—d— —r—e—p—e—a—t—a—b—l—e— —o—n—b—o—a—r—d—i—n—g— —o—u—t—p—u—t—s—.— —U—s—e— —w—h—e—n— —o—n—b—o—a—r—d—i—n—g— —a— —n—e—w— —e—n—g—i—n—e—e—r—,— —w—r—i—t—i—n—g— —a—r—c—h—i—t—e—c—t—u—r—e—-—o—v—e—r—v—i—e—w— —d—o—c—s— —f—o—r— —a— —n—e—w— —p—r—o—j—e—c—t—,— —o—r— —p—r—o—d—u—c—i—n—g— —t—e—c—h—-—l—e—a—d— —b—r—i—e—f—i—n—g—s— —f—o—r— —u—n—f—a—m—i—l—i—a—r— —r—e—p—o—s.
---

# Codebase Onboarding

**Tier:** POWERFUL  
**Category:** Engineering  
**Domain:** Documentation / Developer Experience

---

## Overview

Analyze a codebase and generate onboarding documentation for engineers, tech leads, and contractors. This skill is optimized for fast fact-gathering and repeatable onboarding outputs.

## Core Capabilities

- Architecture and stack discovery from repository signals
- Key file and config inventory for new contributors
- Local setup and common-task guidance generation
- Audience-aware documentation framing
- Debugging and contribution checklist scaffolding

---

## When to Use

- Onboarding a new team member or contractor
- Rebuilding stale project docs after large refactors
- Preparing internal handoff documentation
- Creating a standardized onboarding packet for services

---

## Quick Start

```bash
# 1) Gather codebase facts
python3 scripts/codebase_analyzer.py /path/to/repo

# 2) Export machine-readable output
python3 scripts/codebase_analyzer.py /path/to/repo --json

# 3) Use the template to draft onboarding docs
# See references/onboarding-template.md
```

---

## Recommended Workflow

1. Run `scripts/codebase_analyzer.py` against the target repository.
2. Capture key signals: file counts, detected languages, config files, top-level structure.
3. Fill the onboarding template in `references/onboarding-template.md`.
4. Tailor output depth by audience:
   - Junior: setup + guardrails
   - Senior: architecture + operational concerns
   - Contractor: scoped ownership + integration boundaries

---

## Onboarding Document Template

Detailed template and section examples live in:
- `references/onboarding-template.md`
- `references/output-format-templates.md`

---

## Common Pitfalls

- Writing docs without validating setup commands on a clean environment
- Mixing architecture deep-dives into contractor-oriented docs
- Omitting troubleshooting and verification steps
- Letting onboarding docs drift from current repo state

## Best Practices

1. Keep setup instructions executable and time-bounded.
2. Document the "why" for key architectural decisions.
3. Update docs in the same PR as behavior changes.
4. Treat onboarding docs as living operational assets, not one-time deliverables.
