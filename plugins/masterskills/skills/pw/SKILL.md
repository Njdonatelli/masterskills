---
name: "pw"
description: >-
  Playwright end-to-end testing toolkit and router. Use when the user mentions Playwright tests, end-to-end testing, a test suite, or flaky tests. Routes to pw-init-project (setup), pw-generate-tests (write tests), pw-review-tests (quality gate), and pw-fix-flaky-tests (repair). 55 test templates.
---

# Playwright Pro

Production-grade Playwright testing toolkit for AI coding agents.

## Sub-skills

| Skill | What it does |
|---|---|
| `pw-init-project` | Set up Playwright: detects the framework, writes the config and CI, adds a first test |
| `pw-generate-tests` | Generates tests from a user story, a URL, or a component |
| `pw-review-tests` | Reviews tests for anti-patterns and coverage gaps |
| `pw-fix-flaky-tests` | Diagnoses and fixes failing or flaky tests |

## Quick Start Workflow

The recommended sequence for most projects:

```
1. pw-init-project     → scaffolds config, CI pipeline, and a first smoke test
2. pw-generate-tests   → generates tests from your spec or URL
3. pw-review-tests     → validates quality and flags anti-patterns      ← always run after generate
4. pw-fix-flaky-tests  → diagnoses and repairs any failing/flaky tests  ← run when CI turns red
```

**Validation checkpoints:**
- After `pw-generate-tests`, always run `pw-review-tests` before you commit. It catches locator anti-patterns and missing assertions.
- After `pw-fix-flaky-tests`, run the full suite locally (`npx playwright test`). Make sure that the fix does not cause regressions.

### Example: Generate → Review → Fix

```bash
# 1. Generate tests from a user story (pw-generate-tests)
"As a user I can log in with email and password"

# Generated: tests/auth/login.spec.ts
# → Playwright Pro creates the file using the auth template.

# 2. Review the generated tests (pw-review-tests)
tests/auth/login.spec.ts

# → Flags: one test used page.locator('input[type=password]') — suggests getByLabel('Password')
# → Fix applied automatically.

# 3. Run locally to confirm
npx playwright test tests/auth/login.spec.ts --headed

# 4. If a test is flaky in CI, diagnose it (pw-fix-flaky-tests)
tests/auth/login.spec.ts
# → Identifies missing web-first assertion; replaces waitForTimeout(2000) with expect(locator).toBeVisible()
```

## Golden Rules

1. `getByRole()` over CSS/XPath — resilient to markup changes
2. Never `page.waitForTimeout()` — use web-first assertions
3. `expect(locator)` auto-retries; `expect(await locator.textContent())` does not
4. Isolate every test — no shared state between tests
5. `baseURL` in config — zero hardcoded URLs
6. Retries: `2` in CI, `0` locally
7. Traces: `'on-first-retry'` — rich debugging without slowdown
8. Fixtures over globals — `test.extend()` for shared state
9. One behavior per test — multiple related assertions are fine
10. Mock external services only — never mock your own app

## Locator Priority

```
1. getByRole()        — buttons, links, headings, form elements
2. getByLabel()       — form fields with labels
3. getByText()        — non-interactive text
4. getByPlaceholder() — inputs with placeholder
5. getByTestId()      — when no semantic option exists
6. page.locator()     — CSS/XPath as last resort
```

## What's Included

- **4 sub-skills**: pw-init-project, pw-generate-tests, pw-review-tests, pw-fix-flaky-tests
- **55 test templates**: auth, CRUD, checkout, search, forms, dashboard, settings, onboarding, notifications, API, accessibility
- **6 reference docs**: golden rules, locators, assertions, fixtures, pitfalls, flaky tests

## Quick Reference

See `reference/` directory for:
- `golden-rules.md` — The 10 non-negotiable rules
- `locators.md` — Complete locator priority with cheat sheet
- `assertions.md` — Web-first assertions reference
- `fixtures.md` — Custom fixtures and storageState patterns
- `common-pitfalls.md` — Top 10 mistakes and fixes
- `flaky-tests.md` — Diagnosis commands and quick fixes

See `templates/README.md` for the full template index.
