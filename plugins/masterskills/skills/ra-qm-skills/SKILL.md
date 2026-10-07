---
name: "ra-qm-skills"
description: >-
  R—o—u—t—e—r—/—i—n—d—e—x— —f—o—r— —t—h—e— —1—5— —r—e—g—u—l—a—t—o—r—y— —&— —q—u—a—l—i—t—y—-—m—a—n—a—g—e—m—e—n—t— —s—k—i—l—l—s— —b—u—n—d—l—e—d— —i—n— —t—h—i—s— —p—l—u—g—i—n— —(—I—S—O— —1—3—4—8—5— —Q—M—S—,— —E—U— —M—D—R— —2—0—1—7—/—7—4—5—,— —F—D—A— —s—u—b—m—i—s—s—i—o—n—s— —u—n—d—e—r— —Q—M—S—R—,— —I—S—O— —1—4—9—7—1— —r—i—s—k—,— —C—A—P—A—,— —d—o—c—u—m—e—n—t— —c—o—n—t—r—o—l—,— —I—S—O— —2—7—0—0—1—/—I—S—M—S—,— —I—S—O— —4—2—0—0—1— —A—I—M—S—,— —E—U— —A—I— —A—c—t—,— —G—D—P—R—/—D—S—G—V—O—,— —S—O—C— —2—,— —a—u—d—i—t—i—n—g—)—.— —U—s—e— —w—h—e—n— —a— —c—o—m—p—l—i—a—n—c—e— —r—e—q—u—e—s—t— —d—o—e—s—n—'—t— —o—b—v—i—o—u—s—l—y— —m—a—t—c—h— —o—n—e— —s—k—i—l—l— —a—n—d— —y—o—u— —n—e—e—d— —t—o— —p—i—c—k— —t—h—e— —r—i—g—h—t— —o—n—e— —(—e—.—g—.—,— —'—p—r—e—p—a—r—e— —u—s— —f—o—r— —a—n— —I—S—O— —1—3—4—8—5— —a—u—d—i—t—'—,— —'—i—s— —m—y— —A—I— —s—y—s—t—e—m— —h—i—g—h—-—r—i—s—k— —u—n—d—e—r— —t—h—e— —A—I— —A—c—t—'—).
version: 2.9.0
author: Alireza Rezvani
license: MIT
tags:
  - regulatory
  - quality-management
  - iso-13485
  - mdr
  - fda
  - iso-27001
  - gdpr
agents:
  - claude-code
  - codex-cli
  - openclaw
---

# Regulatory Affairs & Quality Management Skills — Router

This plugin bundles **15 compliance skills** for HealthTech/MedTech organizations (this router is the 16th folder under `ra-qm-team/skills/`). Each skill is self-contained.

## Routing table

Match the request, then load `ra-qm-team/skills/<skill>/SKILL.md`. If multiple rows match, ask one clarifying question first.

| Request signals | Skill | Path |
|---|---|---|
| Regulatory strategy, pathway selection, submissions planning | regulatory-affairs-head | `skills/regulatory-affairs-head/` |
| Management review, quality KPIs, QMR governance | quality-manager-qmr | `skills/quality-manager-qmr/` |
| ISO 13485 QMS implementation, process control | quality-manager-qms-iso13485 | `skills/quality-manager-qms-iso13485/` |
| ISO 14971 risk analysis, FMEA, risk files | risk-management-specialist | `skills/risk-management-specialist/` |
| Root cause analysis, corrective/preventive actions | capa-officer | `skills/capa-officer/` |
| Document control, 21 CFR Part 11, DHF/DMR/DHR | quality-documentation-manager | `skills/quality-documentation-manager/` |
| ISO 13485 internal audits, NC classification | qms-audit-expert | `skills/qms-audit-expert/` |
| ISO 27001 audit planning and execution | isms-audit-expert | `skills/isms-audit-expert/` |
| ISMS design, security risk assessment | information-security-manager-iso27001 | `skills/information-security-manager-iso27001/` |
| EU MDR classification, technical files, PSUR | mdr-745-specialist | `skills/mdr-745-specialist/` |
| FDA 510(k)/PMA/De Novo, QMSR | fda-consultant-specialist | `skills/fda-consultant-specialist/` |
| GDPR/DSGVO, DPIA, data subject rights | gdpr-dsgvo-expert | `skills/gdpr-dsgvo-expert/` |
| EU AI Act risk classification, obligations | eu-ai-act-specialist | `skills/eu-ai-act-specialist/` |
| ISO/IEC 42001 AI management system | iso42001-specialist | `skills/iso42001-specialist/` |
| SOC 2 Type I/II readiness, trust criteria | soc2-compliance | `skills/soc2-compliance/` |

## Quick start

```bash
# Example: route a risk-analysis request
cat ra-qm-team/skills/risk-management-specialist/SKILL.md
python3 ra-qm-team/skills/risk-management-specialist/scripts/risk_matrix_calculator.py --help
```

## Rules

- Route to exactly one skill, then follow that skill's workflow. This router ships no tools of its own.
- All outputs are decision support: final compliance determinations route to the named human owner (QMR, DPO, regulatory counsel) — never auto-decide.
- Verify regulatory citations against the current text (e.g., FDA QMSR effective 2026-02-02 replaced the legacy QSR subsections).
