---
name: "runbook-generator"
description: >-
  G—e—n—e—r—a—t—e— —o—p—e—r—a—t—i—o—n—a—l— —r—u—n—b—o—o—k—s— —f—r—o—m— —a— —s—e—r—v—i—c—e— —n—a—m—e— ——— —d—e—p—l—o—y—m—e—n—t—,— —i—n—c—i—d—e—n—t— —r—e—s—p—o—n—s—e—,— —m—a—i—n—t—e—n—a—n—c—e—,— —a—n—d— —r—o—l—l—b—a—c—k— —w—o—r—k—f—l—o—w—s—.— —T—e—m—p—l—a—t—e—d— —s—t—r—u—c—t—u—r—e— —c—u—s—t—o—m—i—z—a—b—l—e— —p—e—r— —e—n—v—i—r—o—n—m—e—n—t—.— —U—s—e— —w—h—e—n— —d—o—c—u—m—e—n—t—i—n—g— —o—n—-—c—a—l—l— —p—r—o—c—e—d—u—r—e—s— —f—o—r— —a— —n—e—w— —s—e—r—v—i—c—e—,— —s—t—a—n—d—a—r—d—i—z—i—n—g— —i—n—c—i—d—e—n—t— —r—e—s—p—o—n—s—e— —a—c—r—o—s—s— —t—e—a—m—s—,— —o—r— —p—r—o—d—u—c—i—n—g— —r—u—n—b—o—o—k—s— —b—e—f—o—r—e— —l—a—u—n—c—h—i—n—g— —t—o— —p—r—o—d—u—c—t—i—o—n.
---

# Runbook Generator

**Tier:** POWERFUL  
**Category:** Engineering  
**Domain:** DevOps / Site Reliability Engineering

---

## Overview

Generate operational runbooks quickly from a service name, then customize for deployment, incident response, maintenance, and rollback workflows.

## Core Capabilities

- Runbook skeleton generation from a CLI
- Standard sections for start/stop/health/rollback
- Structured escalation and incident handling placeholders
- Reference templates for deployment and incident playbooks

---

## When to Use

- A service has no runbook and needs a baseline immediately
- Existing runbooks are inconsistent across teams
- On-call onboarding requires standardized operations docs
- You need repeatable runbook scaffolding for new services

---

## Quick Start

```bash
# Print runbook to stdout
python3 scripts/runbook_generator.py payments-api

# Write runbook file
python3 scripts/runbook_generator.py payments-api --owner platform --output docs/runbooks/payments-api.md
```

---

## Recommended Workflow

1. Generate the initial skeleton with `scripts/runbook_generator.py`.
2. Fill in service-specific commands and URLs.
3. Add verification checks and rollback triggers.
4. Dry-run in staging.
5. Store runbook in version control near service code.

---

## Reference Docs

- `references/runbook-templates.md`

---

## Common Pitfalls

- Missing rollback triggers or rollback commands
- Steps without expected output checks
- Stale ownership/escalation contacts
- Runbooks never tested outside of incidents

## Best Practices

1. Keep every command copy-pasteable.
2. Include health checks after every critical step.
3. Validate runbooks on a fixed review cadence.
4. Update runbook content after incidents and postmortems.
