---
name: "engineering-advanced-skills"
description: >-
  I—n—d—e—x— —o—f— —3—7— —a—d—v—a—n—c—e—d— —e—n—g—i—n—e—e—r—i—n—g— —a—g—e—n—t— —s—k—i—l—l—s— —f—o—r— —C—l—a—u—d—e— —C—o—d—e—,— —C—o—d—e—x—,— —G—e—m—i—n—i— —C—L—I—,— —C—u—r—s—o—r—,— —O—p—e—n—C—l—a—w—.— —U—s—e— —w—h—e—n— —b—r—o—w—s—i—n—g— —o—r— —c—h—o—o—s—i—n—g— —a—m—o—n—g— —t—h—e— —P—O—W—E—R—F—U—L—-—t—i—e—r— —e—n—g—i—n—e—e—r—i—n—g— —s—k—i—l—l—s—:— —a—g—e—n—t— —d—e—s—i—g—n—,— —R—A—G—,— —M—C—P— —s—e—r—v—e—r—s—,— —C—I—/—C—D—,— —d—a—t—a—b—a—s—e— —d—e—s—i—g—n—,— —o—b—s—e—r—v—a—b—i—l—i—t—y—,— —s—e—c—u—r—i—t—y— —a—u—d—i—t—i—n—g—,— —c—h—a—n—g—e—l—o—g—/—r—e—l—e—a—s—e— —a—u—t—o—m—a—t—i—o—n—,— —r—e—l—i—a—b—i—l—i—t—y— —(—S—L—O—/—c—h—a—o—s—/—f—l—a—g—s—/—o—p—e—r—a—t—o—r—s—)—,— —p—l—a—t—f—o—r—m— —o—p—s.
version: 2.9.0
author: Alireza Rezvani
license: MIT
tags:
  - engineering
  - architecture
  - agents
  - rag
  - mcp
  - ci-cd
  - observability
agents:
  - claude-code
  - codex-cli
  - openclaw
---

# Engineering Advanced Skills (POWERFUL Tier)

37 advanced engineering skills for complex architecture, automation, reliability, and platform operations.

## Quick Start

### Claude Code
```
/read engineering/skills/agent-designer/SKILL.md
```

### Codex CLI
```bash
npx agent-skills-cli add alirezarezvani/claude-skills/engineering
```

## Skills Overview

| Skill | Folder | Focus |
|-------|--------|-------|
| Agent Designer | `agent-designer/` | Multi-agent architecture: plan, schema-generate, evaluate |
| Agent Workflow Designer | `agent-workflow-designer/` | Workflow orchestration scaffolds |
| API Design Reviewer | `api-design-reviewer/` | REST/GraphQL linting, breaking changes |
| API Test Suite Builder | `api-test-suite-builder/` | API test generation |
| Browser Automation | `browser-automation/` | Playwright/Selenium automation patterns |
| Changelog Generator | `changelog-generator/` | Changelogs, semantic version bumps, hotfix/rollback discipline |
| Chaos Engineering | `chaos-engineering/` | Experiment design, blast-radius, postmortems |
| CI/CD Pipeline Builder | `ci-cd-pipeline-builder/` | Pipeline generation |
| Codebase Onboarding | `codebase-onboarding/` | New dev onboarding guides |
| Database Designer | `database-designer/` | Schema analysis, index optimization, migrations |
| Database Schema Designer | `database-schema-designer/` | ERD, normalization |
| Dependency Auditor | `dependency-auditor/` | Dependency security scanning |
| Env Secrets Manager | `env-secrets-manager/` | Secrets rotation, vault |
| Feature Flags Architect | `feature-flags-architect/` | Flag debt, rollout plans, kill switches |
| Focused Fix | `focused-fix/` | Systematic feature/module repair |
| Full Page Screenshot | `full-page-screenshot/` | Full-page capture tooling |
| Git Worktree Manager | `git-worktree-manager/` | Parallel branch workflows |
| Interview System Designer | `interview-system-designer/` | Hiring pipeline design |
| Kubernetes Operator | `kubernetes-operator/` | CRD validation, reconcile linting |
| MCP Server Builder | `mcp-server-builder/` | MCP tool creation |
| Migration Architect | `migration-architect/` | System migration planning |
| Monorepo Navigator | `monorepo-navigator/` | Monorepo tooling |
| Observability Designer | `observability-designer/` | Dashboards, alert noise (SLOs → slo-architect) |
| Performance Profiler | `performance-profiler/` | CPU, memory, load profiling |
| PR Review Expert | `pr-review-expert/` | Pull request analysis |
| RAG Architect | `rag-architect/` | RAG design, chunking, retrieval evaluation |
| Runbook Generator | `runbook-generator/` | Operational runbooks |
| Secrets Vault Manager | `secrets-vault-manager/` | Vault patterns, HCL |
| Self-Eval | `self-eval/` | Honest work-quality scoring |
| Ship Gate | `ship-gate/` | Pre-production audit (89 checks) |
| Skill Security Auditor | `skill-security-auditor/` | Skill vulnerability scanning |
| Skill Tester | `skill-tester/` | Skill quality evaluation |
| SLO Architect | `slo-architect/` | SLO/SLI design, error budgets, burn-rate alerts |
| Spec-Driven Workflow | `spec-driven-workflow/` | Spec-first development gates |
| SQL Database Assistant | `sql-database-assistant/` | Query optimization, 4 dialects |
| TC Tracker | `tc-tracker/` | Task context lifecycle + handoffs |
| Tech Debt Tracker | `tech-debt-tracker/` | Debt scan → prioritize → dashboard |

Note: release management merged into `changelog-generator/` (version bumper + hotfix/rollback procedures live there now).

## Rules

- Load only the specific skill SKILL.md you need
- These are advanced skills — combine with engineering-team/ core skills as needed
