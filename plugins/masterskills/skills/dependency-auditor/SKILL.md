---
name: "dependency-auditor"
description: >-
  A—u—d—i—t— —a—n—d— —m—a—n—a—g—e— —d—e—p—e—n—d—e—n—c—i—e—s— —a—c—r—o—s—s— —m—u—l—t—i—-—l—a—n—g—u—a—g—e— —p—r—o—j—e—c—t—s—.— —I—d—e—n—t—i—f—i—e—s— —v—u—l—n—e—r—a—b—i—l—i—t—i—e—s—,— —l—i—c—e—n—s—e— —c—o—n—f—l—i—c—t—s—,— —t—r—a—n—s—i—t—i—v—e— —d—e—p—e—n—d—e—n—c—y— —r—i—s—k—s—,— —a—n—d— —s—a—f—e—-—u—p—g—r—a—d—e— —p—a—t—h—s—.— —U—s—e— —w—h—e—n— —a—u—d—i—t—i—n—g— —t—h—i—r—d—-—p—a—r—t—y— —p—a—c—k—a—g—e—s— —b—e—f—o—r—e— —r—e—l—e—a—s—e—,— —i—n—v—e—s—t—i—g—a—t—i—n—g— —a— —C—V—E—,— —p—l—a—n—n—i—n—g— —a— —m—a—j—o—r— —v—e—r—s—i—o—n— —b—u—m—p—,— —o—r— —r—u—n—n—i—n—g— —a— —l—i—c—e—n—s—e—-—c—o—m—p—l—i—a—n—c—e— —r—e—v—i—e—w—.— —E—x—a—m—p—l—e—s—:— —'—a—u—d—i—t— —o—u—r— —n—p—m— —d—e—p—e—n—d—e—n—c—i—e—s—'—,— —'—d—o— —w—e— —h—a—v—e— —G—P—L— —c—o—n—t—a—m—i—n—a—t—i—o—n—'—,— —'—p—l—a—n— —t—h—e— —u—p—g—r—a—d—e— —t—o— —R—e—a—c—t— —1—9—'.
---

# Dependency Auditor

> **Skill Type:** POWERFUL · **Category:** Engineering · **Domain:** Dependency Management & Security

Offline, deterministic dependency auditing across 8+ package ecosystems. The three scripts are pattern-matchers over manifests/lockfiles — they do **not** call live advisory APIs; pair their findings with `npm audit` / `pip-audit` / `cargo audit` for current CVE coverage.

## Quick Start

```bash
# 1. Scan for vulnerabilities (built-in offline CVE pattern set; exit non-zero on high severity)
python3 scripts/dep_scanner.py /path/to/project --format json --fail-on-high -o scan.json

# 2. Check license compliance and conflicts
python3 scripts/license_checker.py /path/to/project --policy strict --format json -o licenses.json

# 3. Plan upgrades from the scanner's inventory
python3 scripts/upgrade_planner.py scan.json --risk-threshold medium --timeline 90 --format json -o plan.json
```

Consume the outputs: `scan.json` findings drive which packages to pin/patch now; `licenses.json` conflicts go to the user as a legal-risk list; `plan.json` orders upgrades by risk with rollback notes. `--quick-scan` skips transitive deps; `--security-only` limits the plan to security fixes.

**Verification loop:** after applying upgrades, re-run step 1 and assert 0 high-severity findings before closing the audit.

## Supported Ecosystems

| Language | Manifests parsed |
|---|---|
| JavaScript/Node | package.json, package-lock.json, yarn.lock |
| Python | requirements.txt, pyproject.toml, Pipfile.lock, poetry.lock |
| Go | go.mod, go.sum |
| Rust | Cargo.toml, Cargo.lock |
| Ruby | Gemfile, Gemfile.lock |
| Java | pom.xml, gradle.lockfile |
| PHP | composer.json, composer.lock |
| C#/.NET | packages.config, project.assets.json |

## License Classification

- **Permissive**: MIT, Apache 2.0, BSD (2/3-clause), ISC
- **Copyleft (strong)**: GPL v2/v3, AGPL v3 — flags contamination risk in permissive projects
- **Copyleft (weak)**: LGPL v2.1/v3, MPL 2.0
- **Proprietary / Dual / Unknown** — unknown licenses are surfaced for manual review

The checker analyzes license inheritance through dependency chains and emits conflict pairs with remediation suggestions.

## Upgrade Risk Matrix

| Risk | Update type | Handling |
|---|---|---|
| Low | Patch, security fixes | Apply immediately |
| Medium | Minor with new features | Batch into scheduled update |
| High | Major version, API changes | Dedicated migration task + tests |
| Critical | Known breaking changes | Planned migration with rollback procedure |

Prioritization: security patches > bug fixes > feature updates > major rewrites; deprecated features get immediate attention.

## Scripts (accurate capability claims)

- **`scripts/dep_scanner.py`** — multi-format parser; built-in offline vulnerability pattern set (~16 CVE patterns — a smoke layer, not a replacement for live advisories); transitive resolution from lockfiles; JSON + text output.
- **`scripts/license_checker.py`** — license detection from package metadata; compatibility matrix across 20+ license types; `--policy permissive|strict`; conflict detection with remediation.
- **`scripts/upgrade_planner.py`** — semver-based breaking-change prediction; risk-ordered migration plan with testing checklist and timeline estimation.

Sample fixtures: `test-project/` and `test-inventory.json` in this folder; expected shapes in `expected_outputs/`.

## CI Integration

```bash
# Security gate in CI
python3 scripts/dep_scanner.py . --format json --fail-on-high
python3 scripts/license_checker.py . --policy strict --format json
```

## Best Practices

1. **Prioritize security**: address high/critical findings immediately; license compliance before functionality.
2. **Gradual updates**: incremental upgrades with thorough testing; feature flags for risky bumps.
3. **Cadence**: security scans per commit; license audits monthly; full audit quarterly.
4. **False positives**: whitelist with documentation; contact maintainers for license ambiguity.

See [README.md](README.md) for detailed usage and `references/` for the vulnerability/license knowledge bases.
