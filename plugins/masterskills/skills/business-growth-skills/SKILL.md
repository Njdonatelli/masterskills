---
name: "business-growth-skills"
description: >-
  R—o—u—t—e—r—/—i—n—d—e—x— —f—o—r— —t—h—e— —4— —b—u—s—i—n—e—s—s— —&— —g—r—o—w—t—h— —s—k—i—l—l—s— —b—u—n—d—l—e—d— —i—n— —t—h—i—s— —p—l—u—g—i—n—:— —c—u—s—t—o—m—e—r—-—s—u—c—c—e—s—s—-—m—a—n—a—g—e—r— —(—h—e—a—l—t—h— —s—c—o—r—i—n—g—,— —c—h—u—r—n— —r—i—s—k—,— —e—x—p—a—n—s—i—o—n—)—,— —s—a—l—e—s—-—e—n—g—i—n—e—e—r— —(—R—F—P— —a—n—a—l—y—s—i—s—,— —c—o—m—p—e—t—i—t—i—v—e— —m—a—t—r—i—c—e—s—,— —P—o—C— —p—l—a—n—n—i—n—g—)—,— —r—e—v—e—n—u—e—-—o—p—e—r—a—t—i—o—n—s— —(—p—i—p—e—l—i—n—e—,— —f—o—r—e—c—a—s—t— —a—c—c—u—r—a—c—y—,— —G—T—M— —e—f—f—i—c—i—e—n—c—y—)—,— —a—n—d— —c—o—n—t—r—a—c—t—-—a—n—d—-—p—r—o—p—o—s—a—l—-—w—r—i—t—e—r—.— —U—s—e— —w—h—e—n— —a— —g—r—o—w—t—h—/—r—e—v—e—n—u—e— —r—e—q—u—e—s—t— —d—o—e—s—n—'—t— —o—b—v—i—o—u—s—l—y— —m—a—t—c—h— —o—n—e— —s—k—i—l—l— —a—n—d— —y—o—u— —n—e—e—d— —t—o— —p—i—c—k— —t—h—e— —r—i—g—h—t— —o—n—e— —(—e—.—g—.—,— —'—w—h—i—c—h— —a—c—c—o—u—n—t—s— —a—r—e— —a—t— —r—i—s—k—'—,— —'—s—h—o—u—l—d— —w—e— —b—i—d— —o—n— —t—h—i—s— —R—F—P—'—).
version: 2.9.0
author: Alireza Rezvani
license: MIT
tags:
  - business
  - customer-success
  - sales
  - revenue-operations
  - growth
agents:
  - claude-code
  - codex-cli
  - openclaw
---

# Business & Growth Skills — Router

This plugin bundles **4 skills** (this router is the 5th folder under `business-growth/skills/`). Each skill is self-contained.

## Routing table

Match the request, then load `business-growth/skills/<skill>/SKILL.md`. If multiple rows match, ask one clarifying question first.

| Request signals | Skill | Path |
|---|---|---|
| Customer health scores, churn risk, expansion plays | customer-success-manager | `skills/customer-success-manager/` |
| RFP/RFI coverage, competitive positioning, PoC plans | sales-engineer | `skills/sales-engineer/` |
| Pipeline coverage, forecast accuracy (MAPE), GTM efficiency | revenue-operations | `skills/revenue-operations/` |
| Proposals, contracts, statements of work, DPAs | contract-and-proposal-writer | `skills/contract-and-proposal-writer/` |

## Quick start

```bash
# Example: route an account-health request
cat business-growth/skills/customer-success-manager/SKILL.md
python3 business-growth/skills/customer-success-manager/scripts/health_score_calculator.py --help
```

## Rules

- Route to exactly one skill, then follow that skill's workflow. This router ships no tools of its own.
- Use the skills' Python scorers for metrics, not manual estimates; deal/contract outputs are drafts for human legal/commercial review.
