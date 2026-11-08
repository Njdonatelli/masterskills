# Frontend Engineer — Composition Map

**Principle (simplicity first):** do not reimplement scope that a specialist skill owns. This skill is the frontend orchestrator. The specialist skills do the detailed work.

## Composition routing table

| User concern | Use skill | When |
|---|---|---|
| WCAG audit, contrast checks, screen-reader gaps | `a11y-audit` | After Q7 (WCAG target) is set |
| Single-file HTML landing page | `landing-page-html` | When the `marketing-site` or `landing-page` profile applies and no framework is needed |
| Visual design build, critique, or polish | `impeccable`, `ui-craft`, `improve-ui` | Before and after the first build |
| Dependency vulnerability sweep | `dependency-auditor` | Before every major release |
| End-to-end and visual-regression tests | `pw` | After Q7 (WCAG target) is set |
| AEO (answer-engine visibility) | `aeo` | After Q5 (SEO-dependent surface) is confirmed |
| SEO crawlability + meta + structured data | `seo-audit`, `schema-markup` | After Q5 (SEO-dependent surface) |
| Pre-flight architecture grill | `grill-me` | Before locking the framework or rendering model |

## Composition rules

1. **One specialist at a time.** Finish the a11y branch before you open the next branch.
2. **Never reimplement specialist scope.** If the user asks for a contrast audit, use `a11y-audit`.
3. **Document the chain.** Every artifact lists the specialist skills that it used, in order.

## Anti-patterns

- ❌ Adding a third-party perf monitoring lib without checking it against the bundle budget from Q4.
- ❌ Implementing what `a11y-audit` would have caught (e.g., missing alt text, color contrast, focus traps).
- ❌ Treating shipped UI as a final product without a `pw` visual-regression baseline.
