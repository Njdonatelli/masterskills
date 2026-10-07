---
name: "mcp-server-builder"
description: >-
  D—e—s—i—g—n— —a—n—d— —s—h—i—p— —p—r—o—d—u—c—t—i—o—n—-—r—e—a—d—y— —M—C—P— —(—M—o—d—e—l— —C—o—n—t—e—x—t— —P—r—o—t—o—c—o—l—)— —s—e—r—v—e—r—s— —f—r—o—m— —O—p—e—n—A—P—I— —c—o—n—t—r—a—c—t—s— —i—n—s—t—e—a—d— —o—f— —h—a—n—d—-—w—r—i—t—t—e—n— —t—o—o—l— —w—r—a—p—p—e—r—s—.— —P—y—t—h—o—n— —a—n—d— —T—y—p—e—S—c—r—i—p—t— —s—u—p—p—o—r—t—,— —s—c—h—e—m—a— —v—a—l—i—d—a—t—i—o—n—,— —s—a—f—e— —e—v—o—l—u—t—i—o—n—.— —U—s—e— —w—h—e—n— —e—x—p—o—s—i—n—g— —a—n— —e—x—i—s—t—i—n—g— —A—P—I— —a—s— —a—n— —M—C—P— —s—e—r—v—e—r—,— —b—u—i—l—d—i—n—g— —t—o—o—l— —i—n—t—e—g—r—a—t—i—o—n—s— —f—o—r— —C—l—a—u—d—e— —o—r— —C—o—d—e—x— —o—r— —C—u—r—s—o—r—,— —o—r— —s—c—a—f—f—o—l—d—i—n—g— —a—n— —M—C—P— —p—r—o—j—e—c—t— —f—r—o—m— —s—c—r—a—t—c—h.
---

# MCP Server Builder

**Tier:** POWERFUL · **Category:** Engineering · **Domain:** AI / API Integration

## Overview

Use this skill to design and ship production-ready MCP servers from API contracts instead of hand-written one-off tool wrappers. It focuses on fast scaffolding, schema quality, validation, and safe evolution.

The workflow supports both Python and TypeScript MCP implementations and treats OpenAPI as the source of truth.

## Core Capabilities

- Convert OpenAPI paths/operations into MCP tool definitions
- Generate starter server scaffolds (Python or TypeScript)
- Enforce naming, descriptions, and schema consistency
- Validate MCP tool manifests for common production failures
- Apply versioning and backward-compatibility checks
- Separate transport/runtime decisions from tool contract design

## When to Use

- You need to expose an internal/external REST API to an LLM agent
- You are replacing brittle browser automation with typed tools
- You want one MCP server shared across teams and assistants
- You need repeatable quality checks before publishing MCP tools
- You want to bootstrap an MCP server from existing OpenAPI specs

## Key Workflows

### 1. OpenAPI to MCP Scaffold

1. Start from a valid OpenAPI spec.
2. Generate tool manifest + starter server code.
3. Review naming and auth strategy.
4. Add endpoint-specific runtime logic.

```bash
python3 scripts/openapi_to_mcp.py \
  --input openapi.json \
  --server-name billing-mcp \
  --language python \
  --output-dir ./out \
  --format text
```

Supports stdin as well:

```bash
cat openapi.json | python3 scripts/openapi_to_mcp.py --server-name billing-mcp --language typescript
```

### 2. Validate MCP Tool Definitions

Run validator before integration tests:

```bash
python3 scripts/mcp_validator.py --input out/tool_manifest.json --strict --format text
```

Checks include duplicate names, invalid schema shape, missing descriptions, empty required fields, and naming hygiene.

### 3. Runtime Selection

- Choose **Python** for fast iteration and data-heavy backends.
- Choose **TypeScript** for unified JS stacks and tighter frontend/backend contract reuse.
- Keep tool contracts stable even if transport/runtime changes.

### 4. Harden for Production

Key items before publishing:

- Keep secrets in env vars, not tool schemas
- Prefer outbound host allowlists over open proxies
- Use additive-only changes; never rename tool names in-place

Full hardening guidance: [references/production-hardening-guide.md](references/production-hardening-guide.md).

## Script Interfaces

- `python3 scripts/openapi_to_mcp.py --help`
  - Reads OpenAPI from stdin or `--input`
  - Produces manifest + server scaffold
  - Emits JSON summary or text report
- `python3 scripts/mcp_validator.py --help`
  - Validates manifests and optional runtime config
  - Returns non-zero exit in strict mode when errors exist

## Reference Material

- [references/production-hardening-guide.md](references/production-hardening-guide.md) — auth & safety design, versioning strategy, common pitfalls, best practices, architecture decisions, contract quality gates, testing strategy, deployment practices, security controls
- [references/openapi-extraction-guide.md](references/openapi-extraction-guide.md)
- [references/python-server-template.md](references/python-server-template.md)
- [references/typescript-server-template.md](references/typescript-server-template.md)
- [references/validation-checklist.md](references/validation-checklist.md)
- [README.md](README.md)
