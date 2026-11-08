---
name: "information-security-manager-iso27001"
description: >-
  ISO 27001 ISMS implementation and cybersecurity governance for HealthTech and MedTech companies. Use when designing an ISMS, running security risk assessments, implementing controls, pursuing ISO 27001 certification, preparing security audits, responding to security incidents, or verifying compliance. Covers ISO 27001, ISO 27002, healthcare security, and medical device cybersecurity. [Also supersedes `iso27001-audit-prep`: triggers on '/cs:iso27001-audit-prep', 'iso27001 audit prep', 'ISO 27001 forcing questions'] [Also supersedes `isms-audit-expert`: triggers on 'isms audit expert', 'ISMS internal audit', 'Annex A audit']
---

# Information Security Manager - ISO 27001

Implement and manage Information Security Management Systems (ISMS) aligned with ISO 27001:2022 and healthcare regulatory requirements.

---

## Table of Contents

- [Trigger Phrases](#trigger-phrases)
- [Quick Start](#quick-start)
- [Tools](#tools)
- [Workflows](#workflows)
- [Reference Guides](#reference-guides)
- [Validation Checkpoints](#validation-checkpoints)

---

## Trigger Phrases

Use this skill when you hear:
- "implement ISO 27001"
- "ISMS implementation"
- "security risk assessment"
- "information security policy"
- "ISO 27001 certification"
- "security controls implementation"
- "incident response plan"
- "healthcare data security"
- "medical device cybersecurity"
- "security compliance audit"

---

## Quick Start

### Run Security Risk Assessment

```bash
python scripts/risk_assessment.py --scope "patient-data-system" --output risk_register.json
```

### Check Compliance Status

```bash
python scripts/compliance_checker.py --standard iso27001 --controls-file controls.csv
```

### Generate Gap Analysis Report

```bash
python scripts/compliance_checker.py --standard iso27001 --gap-analysis --output gaps.md
```

---

## Tools

### risk_assessment.py

Automated security risk assessment following ISO 27001 Clause 6.1.2 methodology.

**Usage:**

```bash
# Full risk assessment
python scripts/risk_assessment.py --scope "cloud-infrastructure" --output risks.json

# Healthcare-specific assessment
python scripts/risk_assessment.py --scope "ehr-system" --template healthcare --output risks.json

# Quick asset-based assessment
python scripts/risk_assessment.py --assets assets.csv --output risks.json
```

**Parameters:**

| Parameter | Required | Description |
|-----------|----------|-------------|
| `--scope` | Yes | System or area to assess |
| `--template` | No | Assessment template: `general`, `healthcare`, `cloud` |
| `--assets` | No | CSV file with asset inventory |
| `--output` | No | Output file (default: stdout) |
| `--format` | No | Output format: `json`, `csv`, `markdown` |

**Output:**
- Asset inventory with classification
- Threat and vulnerability mapping
- Risk scores (likelihood × impact)
- Treatment recommendations
- Residual risk calculations

### compliance_checker.py

Verify ISO 27001/27002 control implementation status.

**Usage:**

```bash
# Check all ISO 27001 controls
python scripts/compliance_checker.py --standard iso27001

# Gap analysis with recommendations
python scripts/compliance_checker.py --standard iso27001 --gap-analysis

# Check specific control domains
python scripts/compliance_checker.py --standard iso27001 --domains "access-control,cryptography"

# Export compliance report
python scripts/compliance_checker.py --standard iso27001 --output compliance_report.md
```

**Parameters:**

| Parameter | Required | Description |
|-----------|----------|-------------|
| `--standard` | Yes | Standard to check: `iso27001`, `iso27002`, `hipaa` |
| `--controls-file` | No | CSV with current control status |
| `--gap-analysis` | No | Include remediation recommendations |
| `--domains` | No | Specific control domains to check |
| `--output` | No | Output file path |

**Output:**
- Control implementation status
- Compliance percentage by domain
- Gap analysis with priorities
- Remediation recommendations

---

## Workflows

### Workflow 1: ISMS Implementation

**Step 1: Define Scope and Context**

Document organizational context and ISMS boundaries:
- Identify interested parties and requirements
- Define ISMS scope and boundaries
- Document internal/external issues

**Validation:** Scope statement reviewed and approved by management.

**Step 2: Conduct Risk Assessment**

```bash
python scripts/risk_assessment.py --scope "full-organization" --template general --output initial_risks.json
```

- Identify information assets
- Assess threats and vulnerabilities
- Calculate risk levels
- Determine risk treatment options

**Validation:** Risk register contains all critical assets with assigned owners.

**Step 3: Select and Implement Controls**

Map risks to ISO 27002 controls:

```bash
python scripts/compliance_checker.py --standard iso27002 --gap-analysis --output control_gaps.md
```

Control categories:
- Organizational (policies, roles, responsibilities)
- People (screening, awareness, training)
- Physical (perimeters, equipment, media)
- Technological (access, crypto, network, application)

**Validation:** Statement of Applicability (SoA) documents all controls with justification.

**Step 4: Establish Monitoring**

Define security metrics:
- Incident count and severity trends
- Control effectiveness scores
- Training completion rates
- Audit findings closure rate

**Validation:** Dashboard shows real-time compliance status.

### Workflow 2: Security Risk Assessment

**Step 1: Asset Identification**

Create asset inventory:

| Asset Type | Examples | Classification |
|------------|----------|----------------|
| Information | Patient records, source code | Confidential |
| Software | EHR system, APIs | Critical |
| Hardware | Servers, medical devices | High |
| Services | Cloud hosting, backup | High |
| People | Admin accounts, developers | Varies |

**Validation:** All assets have assigned owners and classifications.

**Step 2: Threat Analysis**

Identify threats per asset category:

| Asset | Threats | Likelihood |
|-------|---------|------------|
| Patient data | Unauthorized access, breach | High |
| Medical devices | Malware, tampering | Medium |
| Cloud services | Misconfiguration, outage | Medium |
| Credentials | Phishing, brute force | High |

**Validation:** Threat model covers top-10 industry threats.

**Step 3: Vulnerability Assessment**

```bash
python scripts/risk_assessment.py --scope "network-infrastructure" --output vuln_risks.json
```

Document vulnerabilities:
- Technical (unpatched systems, weak configs)
- Process (missing procedures, gaps)
- People (lack of training, insider risk)

**Validation:** Vulnerability scan results mapped to risk register.

**Step 4: Risk Evaluation and Treatment**

Calculate risk: `Risk = Likelihood × Impact`

| Risk Level | Score | Treatment |
|------------|-------|-----------|
| Critical | 20-25 | Immediate action required |
| High | 15-19 | Treatment plan within 30 days |
| Medium | 10-14 | Treatment plan within 90 days |
| Low | 5-9 | Accept or monitor |
| Minimal | 1-4 | Accept |

**Validation:** All high/critical risks have approved treatment plans.

### Workflow 3: Incident Response

**Step 1: Detection and Reporting**

Incident categories:
- Security breach (unauthorized access)
- Malware infection
- Data leakage
- System compromise
- Policy violation

**Validation:** Incident logged within 15 minutes of detection.

**Step 2: Triage and Classification**

| Severity | Criteria | Response Time |
|----------|----------|---------------|
| Critical | Data breach, system down | Immediate |
| High | Active threat, significant risk | 1 hour |
| Medium | Contained threat, limited impact | 4 hours |
| Low | Minor violation, no impact | 24 hours |

**Validation:** Severity assigned and escalation triggered if needed.

**Step 3: Containment and Eradication**

Immediate actions:
1. Isolate affected systems
2. Preserve evidence
3. Block threat vectors
4. Remove malicious artifacts

**Validation:** Containment confirmed, no ongoing compromise.

**Step 4: Recovery and Lessons Learned**

Post-incident activities:
1. Restore systems from clean backups
2. Verify integrity before reconnection
3. Document timeline and actions
4. Conduct post-incident review
5. Update controls and procedures

**Validation:** Post-incident report completed within 5 business days.

---

## Reference Guides

### When to Use Each Reference

**references/iso27001-controls.md**
- Control selection for SoA
- Implementation guidance
- Evidence requirements
- Audit preparation

**references/risk-assessment-guide.md**
- Risk methodology selection
- Asset classification criteria
- Threat modeling approaches
- Risk calculation methods

**references/incident-response.md**
- Response procedures
- Escalation matrices
- Communication templates
- Recovery checklists

---

## Validation Checkpoints

### ISMS Implementation Validation

| Phase | Checkpoint | Evidence Required |
|-------|------------|-------------------|
| Scope | Scope approved | Signed scope document |
| Risk | Register complete | Risk register with owners |
| Controls | SoA approved | Statement of Applicability |
| Operation | Metrics active | Dashboard screenshots |
| Audit | Internal audit done | Audit report |

### Certification Readiness

Before Stage 1 audit:
- [ ] ISMS scope documented and approved
- [ ] Information security policy published
- [ ] Risk assessment completed
- [ ] Statement of Applicability finalized
- [ ] Internal audit conducted
- [ ] Management review completed
- [ ] Nonconformities addressed

Before Stage 2 audit:
- [ ] Controls implemented and operational
- [ ] Evidence of effectiveness available
- [ ] Staff trained and aware
- [ ] Incidents logged and managed
- [ ] Metrics collected for 3+ months

### Compliance Verification

Run periodic checks:

```bash
# Monthly compliance check
python scripts/compliance_checker.py --standard iso27001 --output monthly_$(date +%Y%m).md

# Quarterly gap analysis
python scripts/compliance_checker.py --standard iso27001 --gap-analysis --output quarterly_gaps.md
```

---

## Worked Example: Healthcare Risk Assessment

**Scenario:** Assess security risks for a patient data management system.

### Step 1: Define Assets

```bash
python scripts/risk_assessment.py --scope "patient-data-system" --template healthcare
```

**Asset inventory output:**

| Asset ID | Asset | Type | Owner | Classification |
|----------|-------|------|-------|----------------|
| A001 | Patient database | Information | DBA Team | Confidential |
| A002 | EHR application | Software | App Team | Critical |
| A003 | Database server | Hardware | Infra Team | High |
| A004 | Admin credentials | Access | Security | Critical |

### Step 2: Identify Risks

**Risk register output:**

| Risk ID | Asset | Threat | Vulnerability | L | I | Score |
|---------|-------|--------|---------------|---|---|-------|
| R001 | A001 | Data breach | Weak encryption | 3 | 5 | 15 |
| R002 | A002 | SQL injection | Input validation | 4 | 4 | 16 |
| R003 | A004 | Credential theft | No MFA | 4 | 5 | 20 |

### Step 3: Determine Treatment

| Risk | Treatment | Control | Timeline |
|------|-----------|---------|----------|
| R001 | Mitigate | Implement AES-256 encryption | 30 days |
| R002 | Mitigate | Add input validation, WAF | 14 days |
| R003 | Mitigate | Enforce MFA for all admins | 7 days |

### Step 4: Verify Implementation

```bash
python scripts/compliance_checker.py --controls-file implemented_controls.csv
```

**Verification output:**

```
Control Implementation Status
=============================
Cryptography (A.8.24): IMPLEMENTED
  - AES-256 at rest: YES
  - TLS 1.3 in transit: YES

Access Control (A.8.5): IMPLEMENTED
  - MFA enabled: YES
  - Admin accounts: 100% coverage

Application Security (A.8.26): PARTIAL
  - Input validation: YES
  - WAF deployed: PENDING

Overall Compliance: 87%
```

---

## Consolidated Capabilities: ISO27001-AUDIT-PREP (Subsumed & Superceded)

# /cs:iso27001-audit-prep  ISO 27001 ISMS Audit Forcing Questions

**Command:** `/cs:iso27001-audit-prep <scope>`

The ISO 27001 ISMS auditor pressure-tests any ISMS work. Six sample-driven questions before any internal audit, stage 1 readiness, or surveillance audit.

## When to Run

- Before annual Clause 9.2 internal audit
- Before stage 1 / stage 2 ISO 27001 certification audit
- Before surveillance audit (year 2 / year 3)
- After material change to ISMS scope (new business unit, new product line, new SaaS adoption)
- Post-incident (breach triggers ad-hoc ISMS audit)
- Quarterly during high-growth phase

## The Six ISMS Questions

### 1. What's the audit scope, and is rolling 3-year coverage on track?
**No 3-year coverage discipline, no defensible programme.**
- Every Clause 4-10 + every applicable Annex A control must be audited at least once per 3-year cycle
- Run `isms_audit_scheduler.py` in `ra-qm-team/skills/isms-audit-expert/`
- Confirm auditor independence  no self-audit on any sample

### 2. When was the risk register last refreshed, and are treatments linked to Annex A controls?
**Stale risk register = certification finding.**
- Quarterly refresh expected; annual minimum
- Every high/critical risk must link to ≥ 1 Annex A control treating it
- Residual risk acceptance documented + signed
- Review against `iso27001_audit_playbook.md` for stage 1 expectations

### 3. Show me the access review records  quarterly cadence, the last 4 quarters.
**Most-cited finding area.**
- Annex A.5.15 + A.8.2 + A.8.3 access controls
- Sample real records pulled from Okta / IAM, not curated audit-prep packs
- For each terminated employee in last 90 days: deprovisioning evidence within 24-hour SLA
- Privileged access reviewed at finer granularity

### 4. What's the supplier inventory + last review evidence?
**Second-most-cited finding area.**
- Annex A.5.19-A.5.21 supplier management
- Critical SaaS suppliers reviewed at least annually
- DPAs signed for personal-data sub-processors (cross-check with cs-dpo-gdpr)
- AI-specific contract clauses where third-party AI services in use (cross-check with cs-aims-iso42001)

### 5. Where's the incident response evidence + post-incident review?
**A.5.24-27 + A.6.8  high-stakes audit area.**
- Severity definitions documented + consistently applied
- Last 5 incidents have post-incident review (PIR) within 30-day SLA
- GDPR Article 33 / 34 notification timing aligned with A.5.24 (cross-check with cs-dpo-gdpr)
- Blameless retro culture; not punitive

### 6. What's the management review cadence + inputs?
**Clause 9.3 required inputs are prescriptive  easy to miss.**
- Required inputs: audit results, risks, performance, nonconformities, opportunities
- Schedule: annual minimum; quarterly preferred for mature programs
- Outputs documented + tracked to closure
- Integrated review across frameworks (per `multi_framework_audit_playbook.md`) preferred to separate reviews

## Workflow

```bash
# 1. Audit programme planning
python ra-qm-team/skills/isms-audit-expert/scripts/isms_audit_scheduler.py audit_scope.json

# 2. Mock audit for readiness check
python ../../skills/compliance-os/scripts/audit_simulator.py iso27001_scope.json

# 3. Cross-framework reuse (SOC 2 = 75% overlap; ISO 42001 = 60% reuse)
python ../../skills/compliance-os/scripts/cross_framework_mapper.py program.json
```

## Output Format

```markdown
# ISO 27001 Audit Prep: <scope>
**Date:** YYYY-MM-DD

## The Decision Being Made
[programme-plan | finding-severity | cert-readiness | incident-followup]

## Audit Programme Status
- Clauses scheduled this year: <list>
- Annex A controls scheduled: <count>
- Rolling 3-year coverage: clean | gaps in <list>
- Auditor independence: clean | issues in <list>

## Risk Register Health
- Last refresh: YYYY-MM-DD
- High/critical risks without Annex A control link: N
- Residual risk acceptance documentation: complete | gaps

## High-Stakes Controls Status
- A.5.15 + A.8.2 + A.8.3 access control: pass/fail with sample
- A.5.19-A.5.21 supplier mgmt: pass/fail with sample
- A.5.24-27 + A.6.8 incident response: pass/fail with sample
- A.8.15-16 logging: pass/fail with sample

## Management Review Status
- Last review date: YYYY-MM-DD
- Required Article 9.3 inputs present: yes/no
- Open action items past due: N

## Cross-Framework Impact
- SOC 2 controls affected: <list>
- ISO 42001 controls affected (if applicable): <list>
- GDPR Article 32 controls affected: <list>

## Verdict
🟢 READY | 🟡 CLOSE-CRITICALS-FIRST | 🔴 NOT-READY

## Top 3 Actions
[3 concrete next steps with owner + corrective-action timeline]
```

## Routing

- `/cs:compliance-readiness`  for multi-framework view
- `/cs:soc2-audit-prep`  for SOC 2 cross-walk pair (75% overlap)
- `/cs:aims-audit`  for ISO 42001 AIMS cross-walk
- `/cs:gdpr-audit-prep`  for Article 32 organizational measures overlap
- `/cs:ciso-review`  for executive cybersecurity strategy
- `/cs:decide`  to log the verdict

## Related

- Agent: [`cs-ciso-iso27001`](../../agents/cs-ciso-iso27001.md)
- Skill: [`isms-audit-expert`](../../../ra-qm-team/skills/isms-audit-expert/SKILL.md)
- Playbook: [iso27001_audit_playbook.md](../../../ra-qm-team/skills/isms-audit-expert/references/iso27001_audit_playbook.md)
- Adjacent: `../soc2-audit-prep/`, `../aims-audit/`, `../gdpr-audit-prep/`, `../compliance-readiness/`

---

**Version:** 1.0.0

---

## Consolidated Capabilities: ISMS-AUDIT-EXPERT (Subsumed & Superceded)

# ISMS Audit Expert

Internal and external ISMS audit management for ISO 27001 compliance verification, security control assessment, and certification support.

## Table of Contents

- [Audit Program Management](#audit-program-management)
- [Audit Execution](#audit-execution)
- [Control Assessment](#control-assessment)
- [Finding Management](#finding-management)
- [Certification Support](#certification-support)
- [Tools](#tools)
- [References](#references)

---

## Audit Program Management

### Risk-Based Audit Schedule

| Risk Level | Audit Frequency | Examples |
|------------|-----------------|----------|
| Critical | Quarterly | Privileged access, vulnerability management, logging |
| High | Semi-annual | Access control, incident response, encryption |
| Medium | Annual | Policies, awareness training, physical security |
| Low | Annual | Documentation, asset inventory |

### Annual Audit Planning Workflow

1. Review previous audit findings and risk assessment results
2. Identify high-risk controls and recent security incidents
3. Determine audit scope based on ISMS boundaries
4. Assign auditors ensuring independence from audited areas
5. Create audit schedule with resource allocation
6. Obtain management approval for audit plan
7. **Validation:** Audit plan covers all Annex A controls within certification cycle

### Auditor Competency Requirements

- ISO 27001 Lead Auditor certification (preferred)
- No operational responsibility for audited processes
- Understanding of technical security controls
- Knowledge of applicable regulations (GDPR, HIPAA)

---

## Audit Execution

### Pre-Audit Preparation

1. Review ISMS documentation (policies, SoA, risk assessment)
2. Analyze previous audit reports and open findings
3. Prepare audit plan with interview schedule
4. Notify auditees of audit scope and timing
5. Prepare checklists for controls in scope
6. **Validation:** All documentation received and reviewed before opening meeting

### Audit Conduct Steps

1. **Opening Meeting**
   - Confirm audit scope and objectives
   - Introduce audit team and methodology
   - Agree on communication channels and logistics

2. **Evidence Collection**
   - Interview control owners and operators
   - Review documentation and records
   - Observe processes in operation
   - Inspect technical configurations

3. **Control Verification**
   - Test control design (does it address the risk?)
   - Test control operation (is it working as intended?)
   - Sample transactions and records
   - Document all evidence collected

4. **Closing Meeting**
   - Present preliminary findings
   - Clarify any factual inaccuracies
   - Agree on finding classification
   - Confirm corrective action timelines

5. **Validation:** All controls in scope assessed with documented evidence

---

## Control Assessment

### Control Testing Approach

1. Identify control objective from ISO 27002
2. Determine testing method (inquiry, observation, inspection, re-performance)
3. Define sample size based on population and risk
4. Execute test and document results
5. Evaluate control effectiveness
6. **Validation:** Evidence supports conclusion about control status

For detailed technical verification procedures by Annex A control, see [security-control-testing.md](references/security-control-testing.md).

---

## Finding Management

### Finding Classification

| Severity | Definition | Response Time |
|----------|------------|---------------|
| Major Nonconformity | Control failure creating significant risk | 30 days |
| Minor Nonconformity | Isolated deviation with limited impact | 90 days |
| Observation | Improvement opportunity | Next audit cycle |

### Finding Documentation Template

```
Finding ID: ISMS-[YEAR]-[NUMBER]
Control Reference: A.X.X - [Control Name]
Severity: [Major/Minor/Observation]

Evidence:
- [Specific evidence observed]
- [Records reviewed]
- [Interview statements]

Risk Impact:
- [Potential consequences if not addressed]

Root Cause:
- [Why the nonconformity occurred]

Recommendation:
- [Specific corrective action steps]
```

### Corrective Action Workflow

1. Auditee acknowledges finding and severity
2. Root cause analysis completed within 10 days
3. Corrective action plan submitted with target dates
4. Actions implemented by responsible parties
5. Auditor verifies effectiveness of corrections
6. Finding closed with evidence of resolution
7. **Validation:** Root cause addressed, recurrence prevented

---

## Certification Support

### Stage 1 Audit Preparation

Ensure documentation is complete:
- [ ] ISMS scope statement
- [ ] Information security policy (management signed)
- [ ] Statement of Applicability
- [ ] Risk assessment methodology and results
- [ ] Risk treatment plan
- [ ] Internal audit results (past 12 months)
- [ ] Management review minutes

### Stage 2 Audit Preparation

Verify operational readiness:
- [ ] All Stage 1 findings addressed
- [ ] ISMS operational for minimum 3 months
- [ ] Evidence of control implementation
- [ ] Security awareness training records
- [ ] Incident response evidence (if applicable)
- [ ] Access review documentation

### Surveillance Audit Cycle

| Period | Focus |
|--------|-------|
| Year 1, Q2 | High-risk controls, Stage 2 findings follow-up |
| Year 1, Q4 | Continual improvement, control sample |
| Year 2, Q2 | Full surveillance |
| Year 2, Q4 | Re-certification preparation |

**Validation:** No major nonconformities at surveillance audits.

---

## Tools

### scripts/

| Script | Purpose | Usage |
|--------|---------|-------|
| `isms_audit_scheduler.py` | Generate risk-based audit plans | `python scripts/isms_audit_scheduler.py --year 2025 --format markdown` |

### Audit Planning Example

```bash
# Generate annual audit plan
python scripts/isms_audit_scheduler.py --year 2025 --output audit_plan.json

# With custom control risk ratings
python scripts/isms_audit_scheduler.py --controls controls.csv --format markdown
```

---

## References

| File | Content |
|------|---------|
| [iso27001-audit-methodology.md](references/iso27001-audit-methodology.md) | Audit program structure, pre-audit phase, certification support |
| [security-control-testing.md](references/security-control-testing.md) | Technical verification procedures for ISO 27002 controls |
| [cloud-security-audit.md](references/cloud-security-audit.md) | Cloud provider assessment, configuration security, IAM review |

---

## Audit Performance Metrics

| KPI | Target | Measurement |
|-----|--------|-------------|
| Audit plan completion | 100% | Audits completed vs. planned |
| Finding closure rate | >90% within SLA | Closed on time vs. total |
| Major nonconformities | 0 at certification | Count per certification cycle |
| Audit effectiveness | Incidents prevented | Security improvements implemented |
