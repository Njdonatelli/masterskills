---
name: "monorepo-navigator"
description: >-
  N—a—v—i—g—a—t—e—,— —m—a—n—a—g—e—,— —a—n—d— —o—p—t—i—m—i—z—e— —m—o—n—o—r—e—p—o—s—.— —C—o—v—e—r—s— —T—u—r—b—o—r—e—p—o—,— —N—x—,— —p—n—p—m— —w—o—r—k—s—p—a—c—e—s—,— —a—n—d— —L—e—r—n—a—.— —C—r—o—s—s—-—p—a—c—k—a—g—e— —i—m—p—a—c—t— —a—n—a—l—y—s—i—s—,— —s—e—l—e—c—t—i—v—e— —b—u—i—l—d—s—/—t—e—s—t—s— —o—n— —a—f—f—e—c—t—e—d— —p—a—c—k—a—g—e—s—,— —r—e—m—o—t—e— —c—a—c—h—i—n—g—,— —d—e—p—e—n—d—e—n—c—y— —g—r—a—p—h— —v—i—s—u—a—l—i—z—a—t—i—o—n—,— —a—n—d— —s—t—r—u—c—t—u—r—e—d— —m—u—l—t—i—-—r—e—p—o— —t—o— —m—o—n—o—r—e—p—o— —m—i—g—r—a—t—i—o—n—s—.— —U—s—e— —w—h—e—n— —s—e—t—t—i—n—g— —u—p— —a— —n—e—w— —m—o—n—o—r—e—p—o—,— —o—p—t—i—m—i—z—i—n—g— —C—I— —f—o—r— —a— —l—a—r—g—e— —w—o—r—k—s—p—a—c—e—,— —d—e—b—u—g—g—i—n—g— —c—r—o—s—s—-—p—a—c—k—a—g—e— —d—e—p—e—n—d—e—n—c—y— —i—s—s—u—e—s—,— —o—r— —p—l—a—n—n—i—n—g— —a— —m—u—l—t—i—-—r—e—p—o— —c—o—n—s—o—l—i—d—a—t—i—o—n.
---

# Monorepo Navigator

**Tier:** POWERFUL  
**Category:** Engineering  
**Domain:** Monorepo Architecture / Build Systems  

---

## Overview

Navigate, manage, and optimize monorepos. Covers Turborepo, Nx, pnpm workspaces, and Lerna. Enables cross-package impact analysis, selective builds/tests on affected packages only, remote caching, dependency graph visualization, and structured migrations from multi-repo to monorepo. Includes Claude Code configuration for workspace-aware development.

---

## Core Capabilities

- **Cross-package impact analysis** — determine which apps break when a shared package changes
- **Selective commands** — run tests/builds only for affected packages (not everything)
- **Dependency graph** — visualize package relationships as Mermaid diagrams
- **Build optimization** — remote caching, incremental builds, parallel execution
- **Migration** — step-by-step multi-repo → monorepo with zero history loss
- **Publishing** — changesets for versioning, pre-release channels, npm publish workflows
- **Claude Code config** — workspace-aware CLAUDE.md with per-package instructions

---

## When to Use

Use when:
- Multiple packages/apps share code (UI components, utils, types, API clients)
- Build times are slow because everything rebuilds when anything changes
- Migrating from multiple repos to a single repo
- Need to publish packages to npm with coordinated versioning
- Teams work across multiple packages and need unified tooling

Skip when:
- Single-app project with no shared packages
- Team/project boundaries are completely isolated (polyrepo is fine)
- Shared code is minimal and copy-paste overhead is acceptable

---

## Tool Selection

| Tool | Best For | Key Feature |
|---|---|---|
| **Turborepo** | JS/TS monorepos, simple pipeline config | Best-in-class remote caching, minimal config |
| **Nx** | Large enterprises, plugin ecosystem | Project graph, code generation, affected commands |
| **pnpm workspaces** | Workspace protocol, disk efficiency | `workspace:*` for local package refs |
| **Lerna** | npm publishing, versioning | Batch publishing, conventional commits |
| **Changesets** | Modern versioning (preferred over Lerna) | Changelog generation, pre-release channels |

Most modern setups: **pnpm workspaces + Turborepo + Changesets**

---

## Turborepo
→ See references/monorepo-tooling-reference.md for details

## Workspace Analyzer

```bash
python3 scripts/monorepo_analyzer.py /path/to/monorepo
python3 scripts/monorepo_analyzer.py /path/to/monorepo --json
```

Also see `references/monorepo-patterns.md` for common architecture and CI patterns.

## Common Pitfalls

| Pitfall | Fix |
|---|---|
| Running `turbo run build` without `--filter` on every PR | Always use `--filter=...[origin/main]` in CI |
| `workspace:*` refs cause publish failures | Use `pnpm changeset publish` — it replaces `workspace:*` with real versions automatically |
| All packages rebuild when unrelated file changes | Tune `inputs` in turbo.json to exclude docs, config files from cache keys |
| Shared tsconfig causes one package to break all type-checks | Use `extends` properly — each package extends root but overrides `rootDir` / `outDir` |
| git history lost during migration | Use `git filter-repo --to-subdirectory-filter` before merging — never move files manually |
| Remote cache not working in CI | Check TURBO_TOKEN and TURBO_TEAM env vars; verify with `turbo run build --summarize` |
| CLAUDE.md too generic — Claude modifies wrong package | Add explicit "When working on X, only touch files in apps/X" rules per package CLAUDE.md |

---

## Best Practices

1. **Root CLAUDE.md defines the map** — document every package, its purpose, and dependency rules
2. **Per-package CLAUDE.md defines the rules** — what's allowed, what's forbidden, testing commands
3. **Always scope commands with --filter** — running everything on every change defeats the purpose
4. **Remote cache is not optional** — without it, monorepo CI is slower than multi-repo CI
5. **Changesets over manual versioning** — never hand-edit package.json versions in a monorepo
6. **Shared configs in root, extended in packages** — tsconfig.base.json, .eslintrc.base.js, jest.base.config.js
7. **Impact analysis before merging shared package changes** — run affected check, communicate blast radius
8. **Keep packages/types as pure TypeScript** — no runtime code, no dependencies, fast to build and type-check
