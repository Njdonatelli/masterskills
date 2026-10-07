---
name: "tech-stack-evaluator"
description: >-
  T—e—c—h—n—o—l—o—g—y— —s—t—a—c—k— —e—v—a—l—u—a—t—i—o—n— —a—n—d— —c—o—m—p—a—r—i—s—o—n— —w—i—t—h— —T—C—O— —a—n—a—l—y—s—i—s—,— —s—e—c—u—r—i—t—y— —a—s—s—e—s—s—m—e—n—t—,— —a—n—d— —e—c—o—s—y—s—t—e—m— —h—e—a—l—t—h— —s—c—o—r—i—n—g—.— —U—s—e— —w—h—e—n— —c—o—m—p—a—r—i—n—g— —f—r—a—m—e—w—o—r—k—s—,— —e—v—a—l—u—a—t—i—n—g— —t—e—c—h—n—o—l—o—g—y— —s—t—a—c—k—s—,— —c—a—l—c—u—l—a—t—i—n—g— —t—o—t—a—l— —c—o—s—t— —o—f— —o—w—n—e—r—s—h—i—p—,— —a—s—s—e—s—s—i—n—g— —m—i—g—r—a—t—i—o—n— —p—a—t—h—s—,— —o—r— —a—n—a—l—y—z—i—n—g— —e—c—o—s—y—s—t—e—m— —v—i—a—b—i—l—i—t—y.
---

# Technology Stack Evaluator

Evaluate and compare technologies, frameworks, and cloud providers with data-driven analysis and actionable recommendations.

## Table of Contents

- [Capabilities](#capabilities)
- [Quick Start](#quick-start)
- [Input Formats](#input-formats)
- [Analysis Types](#analysis-types)
- [Scripts](#scripts)
- [References](#references)

---

## Capabilities

| Capability | Description |
|------------|-------------|
| Technology Comparison | Compare frameworks and libraries with weighted scoring |
| TCO Analysis | Calculate 5-year total cost including hidden costs |
| Ecosystem Health | Assess GitHub metrics, npm adoption, community strength |
| Security Assessment | Evaluate vulnerabilities and compliance readiness |
| Migration Analysis | Estimate effort, risks, and timeline for migrations |
| Cloud Comparison | Compare AWS, Azure, GCP for specific workloads |

---

## Quick Start

### Compare Two Technologies

```
Compare React vs Vue for a SaaS dashboard.
Priorities: developer productivity (40%), ecosystem (30%), performance (30%).
```

### Calculate TCO

```
Calculate 5-year TCO for Next.js on Vercel.
Team: 8 developers. Hosting: $2500/month. Growth: 40%/year.
```

### Assess Migration

```
Evaluate migrating from Angular.js to React.
Codebase: 50,000 lines, 200 components. Team: 6 developers.
```

---

## Input Formats

The evaluator accepts three input formats:

**Text** - Natural language queries
```
Compare PostgreSQL vs MongoDB for our e-commerce platform.
```

**YAML** - Structured input for automation
```yaml
comparison:
  technologies: ["React", "Vue"]
  use_case: "SaaS dashboard"
  weights:
    ecosystem: 30
    performance: 25
    developer_experience: 45
```

**JSON** - Programmatic integration
```json
{
  "technologies": ["React", "Vue"],
  "use_case": "SaaS dashboard"
}
```

---

## Analysis Types

### Quick Comparison (200-300 tokens)
- Weighted scores and recommendation
- Top 3 decision factors
- Confidence level

### Standard Analysis (500-800 tokens)
- Comparison matrix
- TCO overview
- Security summary

### Full Report (1200-1500 tokens)
- All metrics and calculations
- Migration analysis
- Detailed recommendations

---

## Scripts

### stack_comparator.py

Compare technologies with customizable weighted criteria.

```bash
python scripts/stack_comparator.py --help
```

### tco_calculator.py

Calculate total cost of ownership over multi-year projections.

```bash
python scripts/tco_calculator.py --input assets/sample_input_tco.json
```

### ecosystem_analyzer.py

Analyze ecosystem health from GitHub, npm, and community metrics.

```bash
python scripts/ecosystem_analyzer.py --technology react
```

### security_assessor.py

Evaluate security posture and compliance readiness.

```bash
python scripts/security_assessor.py --technology express --compliance soc2,gdpr
```

### migration_analyzer.py

Estimate migration complexity, effort, and risks.

```bash
python scripts/migration_analyzer.py --from angular-1.x --to react
```

---

## References

| Document | Content |
|----------|---------|
| `references/metrics.md` | Detailed scoring algorithms and calculation formulas |
| `references/examples.md` | Input/output examples for all analysis types |
| `references/workflows.md` | Step-by-step evaluation workflows |

---

## Confidence Levels

| Level | Score | Interpretation |
|-------|-------|----------------|
| High | 80-100% | Clear winner, strong data |
| Medium | 50-79% | Trade-offs present, moderate uncertainty |
| Low | < 50% | Close call, limited data |

---

## When to Use

- Comparing frontend/backend frameworks for new projects
- Evaluating cloud providers for specific workloads
- Planning technology migrations with risk assessment
- Calculating build vs. buy decisions with TCO
- Assessing open-source library viability

## When NOT to Use

- Trivial decisions between similar tools (use team preference)
- Mandated technology choices (decision already made)
- Emergency production issues (use monitoring tools)
