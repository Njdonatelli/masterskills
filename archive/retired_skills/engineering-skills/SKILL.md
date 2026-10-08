---
name: "engineering-skills"
description: >-
  I—n—d—e—x— —o—f— —t—h—e— —e—n—g—i—n—e—e—r—i—n—g—-—t—e—a—m— —s—k—i—l—l—s— —b—u—n—d—l—e— —f—o—r— —C—l—a—u—d—e— —C—o—d—e—,— —C—o—d—e—x—,— —G—e—m—i—n—i— —C—L—I—,— —C—u—r—s—o—r—,— —O—p—e—n—C—l—a—w—,— —a—n—d— —6— —m—o—r—e— —t—o—o—l—s—.— —A—r—c—h—i—t—e—c—t—u—r—e—,— —f—r—o—n—t—e—n—d—,— —b—a—c—k—e—n—d—,— —Q—A—,— —D—e—v—O—p—s—,— —s—e—c—u—r—i—t—y—,— —A—I—/—M—L—,— —d—a—t—a— —e—n—g—i—n—e—e—r—i—n—g—,— —P—l—a—y—w—r—i—g—h—t—,— —S—t—r—i—p—e—,— —A—W—S—,— —M—S—3—6—5— —(—s—t—d—l—i—b—-—o—n—l—y— —P—y—t—h—o—n— —t—o—o—l—s—)—.— —U—s—e— —w—h—e—n— —b—r—o—w—s—i—n—g— —o—r— —c—h—o—o—s—i—n—g— —a—m—o—n—g— —e—n—g—i—n—e—e—r—i—n—g—-—t—e—a—m— —r—o—l—e— —s—k—i—l—l—s— ——— —l—o—a—d— —o—n—l—y— —t—h—e— —o—n—e— —s—p—e—c—i—a—l—i—s—t— —S—K—I—L—L—.—m—d— —y—o—u— —n—e—e—d—,— —n—e—v—e—r— —b—u—l—k—-—l—o—a—d— —t—h—e— —b—u—n—d—l—e.
version: 2.9.0
author: Alireza Rezvani
license: MIT
tags:
  - engineering
  - frontend
  - backend
  - devops
  - security
  - ai-ml
  - data-engineering
agents:
  - claude-code
  - codex-cli
  - openclaw
---

# Engineering Team Skills

32 production-ready engineering skills organized into core engineering, security, AI/ML/Data, and specialized tools.

## Quick Start

### Claude Code
```
/read engineering-team/skills/senior-fullstack/SKILL.md
```

### Codex CLI
```bash
npx agent-skills-cli add alirezarezvani/claude-skills/engineering-team
```

## Skills Overview

### Core Engineering (13 skills)

| Skill | Folder | Focus |
|-------|--------|-------|
| Senior Architect | `senior-architect/` | System design, architecture patterns |
| Senior Frontend | `senior-frontend/` | React, Next.js, TypeScript, Tailwind |
| Senior Backend | `senior-backend/` | API design, database optimization |
| Senior Fullstack | `senior-fullstack/` | Project scaffolding, code quality |
| Senior QA | `senior-qa/` | Test generation, coverage analysis |
| Senior DevOps | `senior-devops/` | CI/CD, infrastructure, containers |
| Senior SecOps | `senior-secops/` | Security operations, vulnerability management |
| Code Reviewer | `code-reviewer/` | PR review, code quality analysis |
| Senior Security | `senior-security/` | Threat modeling, STRIDE, penetration testing |
| AWS Solution Architect | `aws-solution-architect/` | Serverless, CloudFormation, cost optimization |
| MS365 Tenant Manager | `ms365-tenant-manager/` | Microsoft 365 administration |
| TDD Guide | `tdd-guide/` | Test-driven development workflows |
| Tech Stack Evaluator | `tech-stack-evaluator/` | Technology comparison, TCO analysis |

### AI/ML/Data (5 skills)

| Skill | Folder | Focus |
|-------|--------|-------|
| Senior Data Scientist | `senior-data-scientist/` | Statistical modeling, experimentation |
| Senior Data Engineer | `senior-data-engineer/` | Pipelines, ETL, data quality |
| Senior ML Engineer | `senior-ml-engineer/` | Model deployment, MLOps, LLM integration |
| Senior Prompt Engineer | `senior-prompt-engineer/` | Prompt optimization, RAG, agents |
| Senior Computer Vision | `senior-computer-vision/` | Object detection, segmentation |

### Specialized Tools (5 skills)

| Skill | Folder | Focus |
|-------|--------|-------|
| Playwright Pro | `playwright-pro/` | E2E testing (9 sub-skills) |
| Self-Improving Agent | `self-improving-agent/` | Memory curation (5 sub-skills) |
| Stripe Integration | `stripe-integration-expert/` | Payment integration, webhooks |
| Incident Commander | `incident-commander/` | Incident response workflows |
| Email Template Builder | `email-template-builder/` | HTML email generation |

## Python Tools

30+ scripts, all stdlib-only. Run directly:

```bash
python3 <skill>/scripts/<tool>.py --help
```

No pip install needed. Scripts include embedded samples for demo mode.

## Rules

- Load only the specific skill SKILL.md you need — don't bulk-load all 32
- Use Python tools for analysis and scaffolding, not manual judgment
- Check CLAUDE.md for tool usage examples and workflows
