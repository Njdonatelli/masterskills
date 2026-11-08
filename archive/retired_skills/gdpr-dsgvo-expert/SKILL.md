---
name: "gdpr-dsgvo-expert"
description: >-
  GDPR and German DSGVO compliance automation. Scans codebases for privacy risks, generates DPIA documentation, tracks data subject rights requests with Art. 12(3) one-month deadlines. Use when running GDPR compliance assessments, privacy audits, data protection planning, DPIA generation, or data subject rights (DSAR) management (e.g., 'check this service for GDPR risks', 'track an access request deadline'). Final compliance determinations route to the DPO or legal counsel. [Also supersedes `gdpr-audit-prep`: triggers on '/cs:gdpr-audit-prep', 'gdpr audit prep', 'GDPR DPO forcing questions']
---

# GDPR/DSGVO Expert

Tools and guidance for EU General Data Protection Regulation (GDPR) and German Bundesdatenschutzgesetz (BDSG) compliance.

---

## Table of Contents

- [Tools](#tools)
  - [GDPR Compliance Checker](#gdpr-compliance-checker)
  - [DPIA Generator](#dpia-generator)
  - [Data Subject Rights Tracker](#data-subject-rights-tracker)
- [Reference Guides](#reference-guides)
- [Workflows](#workflows)

---

## Tools

### GDPR Compliance Checker

Scans codebases for potential GDPR compliance issues including personal data patterns and risky code practices.

```bash
# Scan a project directory
python scripts/gdpr_compliance_checker.py /path/to/project

# JSON output for CI/CD integration
python scripts/gdpr_compliance_checker.py . --json --output report.json
```

**Detects:**
- Personal data patterns (email, phone, IP addresses)
- Special category data (health, biometric, religion)
- Financial data (credit cards, IBAN)
- Risky code patterns:
  - Logging personal data
  - Missing consent mechanisms
  - Indefinite data retention
  - Unencrypted sensitive data
  - Disabled deletion functionality

**Output:**
- Compliance score (0-100)
- Risk categorization (critical, high, medium)
- Prioritized recommendations with GDPR article references

---

### DPIA Generator

Generates Data Protection Impact Assessment documentation following Art. 35 requirements.

```bash
# Get input template
python scripts/dpia_generator.py --template > input.json

# Generate DPIA report
python scripts/dpia_generator.py --input input.json --output dpia_report.md
```

**Features:**
- Automatic DPIA threshold assessment
- Risk identification based on processing characteristics
- Legal basis requirements documentation
- Mitigation recommendations
- Markdown report generation

**DPIA Triggers Assessed:**
- Systematic monitoring (Art. 35(3)(c))
- Large-scale special category data (Art. 35(3)(b))
- Automated decision-making (Art. 35(3)(a))
- EDPB-endorsed high-risk criteria (WP248 rev.01)

---

### Data Subject Rights Tracker

Manages data subject rights requests under GDPR Articles 15-22.

```bash
# Add new request
python scripts/data_subject_rights_tracker.py add \
  --type access --subject "John Doe" --email "john@example.com"

# List all requests
python scripts/data_subject_rights_tracker.py list

# Update status
python scripts/data_subject_rights_tracker.py status --id DSR-202601-0001 --update verified

# Generate compliance report
python scripts/data_subject_rights_tracker.py report --output compliance.json

# Generate response template
python scripts/data_subject_rights_tracker.py template --id DSR-202601-0001
```

**Supported Rights:**

| Right | Article | Deadline |
|-------|---------|----------|
| Access | Art. 15 | One month (Art. 12(3)) |
| Rectification | Art. 16 | One month (Art. 12(3)) |
| Erasure | Art. 17 | One month (Art. 12(3)) |
| Restriction | Art. 18 | One month (Art. 12(3)) |
| Portability | Art. 20 | One month (Art. 12(3)) |
| Objection | Art. 21 | One month (Art. 12(3)) |
| Automated decisions | Art. 22 | One month (Art. 12(3)) |

**Features:**
- Deadline tracking with overdue alerts
- Identity verification workflow
- Response template generation
- Compliance reporting

---

## Reference Guides

### GDPR Compliance Guide
`references/gdpr_compliance_guide.md`

Comprehensive implementation guidance covering:
- Legal bases for processing (Art. 6)
- Special category requirements (Art. 9)
- Data subject rights implementation
- Accountability requirements (Art. 30)
- International transfers (Chapter V)
- Breach notification (Art. 33-34)

### German BDSG Requirements
`references/german_bdsg_requirements.md`

German-specific requirements including:
- DPO appointment threshold (§ 38 BDSG - 20+ employees)
- Employment data processing (§ 26 BDSG)
- Video surveillance rules (§ 4 BDSG)
- Credit scoring requirements (§ 31 BDSG)
- State data protection laws (Landesdatenschutzgesetze)
- Works council co-determination rights

### DPIA Methodology
`references/dpia_methodology.md`

Step-by-step DPIA process:
- Threshold assessment criteria
- EDPB-endorsed high-risk indicators (WP248 rev.01)
- Risk assessment methodology
- Mitigation measure categories
- DPO and supervisory authority consultation
- Templates and checklists

---

## Workflows

### Workflow 1: New Processing Activity Assessment

```
Step 1: Run compliance checker on codebase
        → python scripts/gdpr_compliance_checker.py /path/to/code

Step 2: Review findings and compliance score
        → Address critical and high issues

Step 3: Determine if DPIA required
        → Check references/dpia_methodology.md threshold criteria

Step 4: If DPIA required, generate assessment
        → python scripts/dpia_generator.py --template > input.json
        → Fill in processing details
        → python scripts/dpia_generator.py --input input.json --output dpia.md

Step 5: Document in records of processing activities
```

### Workflow 2: Data Subject Request Handling

```
Step 1: Log request in tracker
        → python scripts/data_subject_rights_tracker.py add --type [type] ...

Step 2: Verify identity (proportionate measures)
        → python scripts/data_subject_rights_tracker.py status --id [ID] --update verified

Step 3: Gather data from systems
        → python scripts/data_subject_rights_tracker.py status --id [ID] --update in_progress

Step 4: Generate response
        → python scripts/data_subject_rights_tracker.py template --id [ID]

Step 5: Send response and complete
        → python scripts/data_subject_rights_tracker.py status --id [ID] --update completed

Step 6: Monitor compliance
        → python scripts/data_subject_rights_tracker.py report
```

### Workflow 3: German BDSG Compliance Check

```
Step 1: Determine if DPO required
        → 20+ employees processing personal data automatically
        → OR processing requires DPIA
        → OR business involves data transfer/market research

Step 2: If employees involved, review § 26 BDSG
        → Document legal basis for employee data
        → Check works council requirements

Step 3: If video surveillance, comply with § 4 BDSG
        → Install signage
        → Document necessity
        → Limit retention

Step 4: Register DPO with supervisory authority
        → See references/german_bdsg_requirements.md for authority list
```

---

## Key GDPR Concepts

### Legal Bases (Art. 6)

- **Consent**: Marketing, newsletters, analytics (must be freely given, specific, informed)
- **Contract**: Order fulfillment, service delivery
- **Legal obligation**: Tax records, employment law
- **Legitimate interests**: Fraud prevention, security (requires balancing test)

### Special Category Data (Art. 9)

Requires explicit consent or Art. 9(2) exception:
- Health data
- Biometric data
- Racial/ethnic origin
- Political opinions
- Religious beliefs
- Trade union membership
- Genetic data
- Sexual orientation

### Data Subject Rights

All rights must be fulfilled within **one month of receipt** (Art. 12(3)). The deadline runs by calendar month, not 30 days, and may be extended by **two further months** for complex or numerous requests  the data subject must be informed of the extension (with reasons) within the first month:
- **Access**: Provide copy of data and processing information
- **Rectification**: Correct inaccurate data
- **Erasure**: Delete data (with exceptions for legal obligations)
- **Restriction**: Limit processing while issues are resolved
- **Portability**: Provide data in machine-readable format
- **Object**: Stop processing based on legitimate interests

### German BDSG Additions

| Topic | BDSG Section | Key Requirement |
|-------|--------------|-----------------|
| DPO threshold | § 38 | 20+ employees = mandatory DPO |
| Employment | § 26 | Detailed employee data rules |
| Video | § 4 | Signage and proportionality |
| Scoring | § 31 | Explainable algorithms |

---

## Consolidated Capabilities: GDPR-AUDIT-PREP (Subsumed & Superceded)

# /cs:gdpr-audit-prep  GDPR DPO Forcing Questions

**Command:** `/cs:gdpr-audit-prep <scope>`

The GDPR DPO auditor pressure-tests any privacy compliance work. Six Article-cited questions before any internal audit, breach response, DPA investigation, or acquisition due diligence.

## When to Run

- Before annual internal GDPR audit
- Before quarterly Article 30 RoPA refresh
- Before launching new high-risk processing (Article 35 DPIA required)
- Post-breach (Articles 33-34)
- Before DPA investigation response or supervisory authority engagement
- During acquisition due diligence (target company privacy posture)
- Quarterly during high-volume new-feature shipping

## The Six DPO Questions

### 1. Show me the Article 30 RoPA  with last-updated date.
**Most-cited finding area.**
- Must include all Article 30(1)(a)-(g) elements for controllers
- Must include all Article 30(2)(a)-(d) elements for processors
- Updated within reasonable time of changes (90 days expected)
- Joint controller arrangements documented per Article 26

### 2. For this processing activity, what's the lawful basis under Article 6?
**Article 6 is exclusive  pick ONE basis per purpose.**
- Six options: consent / contract / legal obligation / vital interests / public task / legitimate interests
- Where "legitimate interests": LIA documented
- Where "consent": records per Article 7; withdrawal mechanism
- Special categories (Article 9) require an Article 9(2) exception

### 3. For high-risk processing, where's the DPIA per Article 35?
**Required for high-risk; sample 3-5 activities.**
- Article 35(7)(a)-(d) required elements:
  - Systematic description of processing
  - Necessity + proportionality assessment
  - Risks to rights + freedoms
  - Measures to address risks
- DPO consulted per Article 35(2)
- Article 36 prior consultation triggered for residual high risk
- For AI systems: integrates with EU AI Act Article 27 FRIA (cross-check with cs-ai-act-compliance)

### 4. Show me a DSAR from the last 30 days  and the response timing.
**Articles 15-22 operational workflow.**
- Response within 1 month (Article 12(3)); extension up to 2 months for complex requests
- Identity verification process documented
- Right of access response includes all Article 15 information
- Right to erasure (Article 17) workflow covers backups + processors

### 5. Show me Transfer Impact Assessments for the largest non-EU transfers.
**Schrems II discipline.**
- Adequacy decision OR SCCs (Article 46) OR derogation (Article 49)
- TIA per EDPB Recommendations 01/2020 + 02/2020
- Supplementary measures where TIA flagged risk
- US transfers covered by EU-US Data Privacy Framework adequacy (Jul 2023)  verify list of certified entities

### 6. Show me the breach log per Article 33(5)  all breaches, not just notifiable ones.
**Article 33(5) requires logging ALL breaches.**
- Internal breach detection mechanism documented
- Article 33 DPA notification within 72 hours (where required)
- Article 34 data subject notification (where high risk)
- Root cause + corrective action via CAPA system
- Cross-check with cs-ciso-iso27001 for A.5.24-27 incident management alignment

## Workflow

```bash
# 1. Compliance posture
python ra-qm-team/skills/gdpr-dsgvo-expert/scripts/gdpr_compliance_checker.py compliance_state.json

# 2. DPIA for high-risk activities
python ra-qm-team/skills/gdpr-dsgvo-expert/scripts/dpia_generator.py processing_activity.json

# 3. DSAR workflow validation
python ra-qm-team/skills/gdpr-dsgvo-expert/scripts/data_subject_rights_tracker.py dsar_log.json

# 4. Cross-framework reuse with ISO 27001 + SOC 2 + ISO 42001
python ../../skills/compliance-os/scripts/cross_framework_mapper.py program.json
```

## Output Format

```markdown
# GDPR Audit Prep: <scope>
**Date:** YYYY-MM-DD
**Article Citations:** Every finding cites Article + paragraph; no paraphrase.

## The Decision Being Made
[RoPA-refresh | DPIA-required | DSAR-workflow | transfer-risk | breach-followup | DPA-readiness]

## Article 30 RoPA Status
- Last refresh: YYYY-MM-DD
- Required elements present: yes/no per processing activity
- Joint controller arrangements: documented/missing

## Article 6 Lawful Basis Discipline
- Activities reviewed: N
- Legitimate-interests claims without LIA: <list>
- Article 9 special categories with documented exception: yes/no

## Article 35 DPIA Quality
- High-risk activities requiring DPIA: <list>
- DPIAs complete per Article 35(7): pass/fail per activity
- Article 36 prior consultation triggered: <list>

## Data Subject Rights (Articles 12-22)
- DSARs in last 90 days: N
- Average response time: X days (target: ≤ 30)
- Right to erasure backup-processor flow: complete/incomplete

## Article 28 Processor Management
- Processors reviewed: N
- Contracts with all Article 28(3)(a)-(j) clauses: % complete
- Sub-processor flow-down notification mechanism: yes/no

## Schrems II Transfer Status
- Non-EU transfers: <list>
- Mechanism per transfer: adequacy / SCCs / derogation
- TIA on file: yes/no per transfer
- Supplementary measures where needed: <list>

## Article 33-34 Breach Discipline
- Breach log last 12 months: N
- Article 33 notification timing: ≤ 72h ratio
- Article 34 data subject notification (where high risk): on-time ratio

## Cross-Framework Impact
- ISO 27001 Article 32 alignment: clean / gaps
- EU AI Act Article 27 FRIA integration: applicable / not
- SOC 2 Privacy TSC alignment (if scope): clean / gaps

## Verdict
🟢 DPA-READY | 🟡 GAPS-IDENTIFIED | 🔴 NOT-READY

## Top 3 Actions
[3 concrete next steps with owner + Article-cited timeline]

## Outside Counsel Required
[Article-level ambiguities flagged: Schrems II supplementary measure adequacy, EU AI Act ↔ GDPR interaction, sectoral derogation interpretation, novel DPA enforcement]
```

## Routing

- `/cs:compliance-readiness`  for multi-framework view
- `/cs:iso27001-audit-prep`  for Article 32 organizational measures
- `/cs:ai-act-readiness`  for EU AI Act Article 27 FRIA integration
- `/cs:soc2-audit-prep`  for SOC 2 Privacy TSC overlap
- `/cs:gc-review`  for novel-case legal review

## Related

- Agent: [`cs-dpo-gdpr`](../../agents/cs-dpo-gdpr.md)
- Skill: [`gdpr-dsgvo-expert`](../../../ra-qm-team/skills/gdpr-dsgvo-expert/SKILL.md)
- Playbook: [gdpr_audit_playbook.md](../../../ra-qm-team/skills/gdpr-dsgvo-expert/references/gdpr_audit_playbook.md)
- Adjacent: `../iso27001-audit-prep/`, `../ai-act-readiness/`, `../soc2-audit-prep/`, `../compliance-readiness/`

---

**Version:** 1.0.0
