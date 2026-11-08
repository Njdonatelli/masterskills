# Backend Engineer — Composition Map

**Principle (simplicity first):** do not reimplement scope that a specialist skill owns. This skill is the backend orchestrator. The specialist skills do the detailed work.

## Composition routing table

| User concern | Use skill | When |
|---|---|---|
| Schema design / ERD / normalization / indexing | `database-designer` | After Q1 (read/write ratio) is known |
| Queries, ORM work, migrations | `sql-database-assistant` | When the schema is stable |
| MCP server for LLM agents | `mcp-builder` (design, evals); `mcp-server-builder` (scaffold from OpenAPI) | When the backend exposes tools to LLM agents |
| CI/CD pipeline for the service | `ci-cd-pipeline-builder` | After Q2 (tenancy) and Q5 (pattern) are set |
| Container build and hardening | `docker-development` | Before the first deploy |
| Dependency vulnerability + license risk | `dependency-auditor` | Before every release |
| API test suite + contract tests | `api-test-suite-builder` | After the API contract is stable |
| Security testing / hostile review | `security-pen-testing` + `adversarial-reviewer` | Before public launch; before handling PII |
| Cloud hosting choice | `gcp-cloud-architect` | When infrastructure choice is the bottleneck |
| Pre-production audit | `ship-gate` | Before the first production deploy |
| Pre-flight architecture grill | `grill-me` | Before locking the pattern or the DB choice |

## Composition rules

1. **One specialist at a time.** Finish the DB branch before you open the API branch.
2. **Use specialist outputs as inputs.** If `database-designer` recommends a schema, the API design uses it.
3. **Never reimplement specialist scope.** If the user asks "what's my index strategy?", use `database-designer`.

## Anti-patterns

- ❌ Recommending Kafka before naming a second team that needs it (premature event-driven).
- ❌ Recommending microservices before Q5 (team-size justification) passes.
- ❌ Auto-approving a production schema migration — every migration names the approver.
