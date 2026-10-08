---
name: "quality-manager-qms-iso13485"
description: >-
  ISO 13485 Quality Management System implementation and maintenance for medical device organizations. Provides QMS design, documentation control, internal auditing, CAPA management, and certification support. Use when working with medical device quality systems, preparing for ISO 13485 audits, managing regulatory compliance documentation, setting up corrective actions, or building audit preparation programs. Useful for quality management, audit preparation, regulatory compliance, medical device documentation, and corrective action workflows. [Also supersedes `quality-manager-qmr`: triggers on 'quality manager qmr', 'QMR governance', 'management review ISO 13485 5.5.2'] [Also supersedes `fda-qsr-audit-prep`: triggers on '/cs:fda-qsr-audit-prep', 'fda qsr audit prep', 'FDA 21 CFR 820 QMSR audit'] [Also supersedes `iso13485-audit-prep`: triggers on '/cs:iso13485-audit-prep', 'iso13485 audit prep', 'ISO 13485 audit checklist']
triggers:
  - ISO 13485
  - QMS implementation
  - quality management system
  - document control
  - internal audit
  - management review
  - quality manual
  - CAPA process
  - process validation
  - design control
  - supplier qualification
  - quality records
---

# Quality Manager - QMS ISO 13485 Specialist

ISO 13485:2016 Quality Management System implementation, maintenance, and certification support for medical device organizations.

---

## Table of Contents

- [QMS Implementation Workflow](#qms-implementation-workflow)
- [Document Control Workflow](#document-control-workflow)
- [Internal Audit Workflow](#internal-audit-workflow)
- [Process Validation Workflow](#process-validation-workflow)
- [Supplier Qualification Workflow](#supplier-qualification-workflow)
- [QMS Process Reference](#qms-process-reference)
- [Decision Frameworks](#decision-frameworks)
- [Tools and References](#tools-and-references)

---

## QMS Implementation Workflow

Implement ISO 13485:2016 compliant quality management system from gap analysis through certification.

### Workflow: Initial QMS Implementation

1. Conduct gap analysis against ISO 13485:2016 requirements
2. Document current state vs. required state for each clause
3. Prioritize gaps by:
   - Regulatory criticality
   - Risk to product safety
   - Resource requirements
4. Develop implementation roadmap with milestones
5. Establish Quality Manual per Clause 4.2.2:
   - QMS scope with justified exclusions
   - Process interactions
   - Procedure references
6. Create required documented procedures  see [Mandatory Documented Procedures](#quick-reference-mandatory-documented-procedures) for the full list
7. Deploy processes with training
8. **Validation:** Gap analysis complete; Quality Manual approved; all required procedures documented and trained

> Use the Gap Analysis Matrix template in [qms-process-templates.md](references/qms-process-templates.md) to document clause-by-clause current state, gaps, priority, and actions.

### QMS Structure

| Level | Document Type | Example |
|-------|---------------|---------|
| 1 | Quality Manual | QM-001 |
| 2 | Procedures | SOP-02-001 |
| 3 | Work Instructions | WI-06-012 |
| 4 | Records | Training records |

---

## Document Control Workflow

Establish and maintain document control per ISO 13485 Clause 4.2.3.

### Workflow: Document Creation and Approval

1. Identify need for new document or revision
2. Assign document number per numbering convention:
   - Format: `[TYPE]-[AREA]-[SEQUENCE]-[REV]`
   - Example: `SOP-02-001-01`
3. Draft document using approved template
4. Route for review to subject matter experts
5. Collect and address review comments
6. Obtain required approvals based on document type
7. Update Document Master List
8. **Validation:** Document numbered correctly; all reviewers signed; Master List updated

### Document Numbering Convention

| Prefix | Document Type | Approval Authority |
|--------|---------------|-------------------|
| QM | Quality Manual | Management Rep + CEO |
| POL | Policy | Department Head + QA |
| SOP | Procedure | Process Owner + QA |
| WI | Work Instruction | Supervisor + QA |
| TF | Template/Form | Process Owner |
| SPEC | Specification | Engineering + QA |

### Area Codes

| Code | Area | Examples |
|------|------|----------|
| 01 | Quality Management | Quality Manual, policy |
| 02 | Document Control | This procedure |
| 03 | Training | Competency procedures |
| 04 | Design | Design control |
| 05 | Purchasing | Supplier management |
| 06 | Production | Manufacturing |
| 07 | Quality Control | Inspection, testing |
| 08 | CAPA | Corrective actions |

### Document Change Control

| Change Type | Approval Level | Examples |
|-------------|----------------|----------|
| Administrative | Document Control | Typos, formatting |
| Minor | Process Owner + QA | Clarifications |
| Major | Full review cycle | Process changes |
| Emergency | Expedited + retrospective | Safety issues |

### Document Review Schedule

| Document Type | Review Period | Trigger for Unscheduled Review |
|---------------|---------------|-------------------------------|
| Quality Manual | Annual | Organizational change |
| Procedures | Annual | Audit finding, regulation change |
| Work Instructions | 2 years | Process change |
| Forms | 2 years | User feedback |

---

## Internal Audit Workflow

Plan and execute internal audits per ISO 13485 Clause 8.2.4.

### Workflow: Annual Audit Program

1. Identify processes and areas requiring audit coverage
2. Assess risk factors for audit frequency:
   - Previous audit findings
   - Regulatory changes
   - Process changes
   - Complaint trends
3. Assign qualified auditors (independent of area audited)
4. Develop annual audit schedule
5. Obtain management approval
6. Communicate schedule to process owners
7. Track completion and reschedule as needed
8. **Validation:** All processes covered; auditors qualified and independent; schedule approved

> Use the Audit Program Template in [qms-process-templates.md](references/qms-process-templates.md) to schedule audits by clause and quarter across processes such as Document Control (4.2.3/4.2.4), Management Review (5.6), Design Control (7.3), Production (7.5), and CAPA (8.5.2/8.5.3).

### Workflow: Individual Audit Execution

1. Prepare audit plan with scope, criteria, and schedule
2. Notify auditee minimum 1 week prior
3. Review procedures and previous audit results
4. Prepare audit checklist
5. Conduct opening meeting
6. Collect evidence through:
   - Document review
   - Record sampling
   - Process observation
   - Personnel interviews
7. Classify findings:
   - Major NC: Absence or breakdown of system
   - Minor NC: Single lapse or deviation
   - Observation: Risk of future NC
8. Conduct closing meeting
9. Issue audit report within 5 business days
10. **Validation:** All checklist items addressed; findings supported by evidence; report distributed

### Auditor Qualification Requirements

| Criterion | Requirement |
|-----------|-------------|
| Training | ISO 13485 awareness + auditor training |
| Experience | Minimum 1 audit as observer |
| Independence | Not auditing own work area |
| Competence | Understanding of audited process |

### Finding Classification Guide

| Classification | Criteria | Response Time |
|----------------|----------|---------------|
| Major NC | System absence, total breakdown, regulatory violation | 30 days for CAPA |
| Minor NC | Single instance, partial compliance | 60 days for CAPA |
| Observation | Potential risk, improvement opportunity | Track in next audit |

---

## Process Validation Workflow

Validate special processes per ISO 13485 Clause 7.5.6.

### Workflow: Process Validation Protocol

1. Identify processes requiring validation:
   - Output cannot be verified by inspection
   - Deficiencies appear only in use
   - Sterilization, welding, sealing, software
2. Form validation team with subject matter experts
3. Write validation protocol including:
   - Process description and parameters
   - Equipment and materials
   - Acceptance criteria
   - Statistical approach
4. Execute IQ: verify equipment installed correctly and document specifications
5. Execute OQ: test parameter ranges and verify process control
6. Execute PQ: run production conditions and verify output meets requirements
7. Write validation report with conclusions
8. **Validation:** IQ/OQ/PQ complete; acceptance criteria met; validation report approved

### Validation Documentation Requirements

| Phase | Content | Evidence |
|-------|---------|----------|
| Protocol | Objectives, methods, criteria | Approved protocol |
| IQ | Equipment verification | Installation records |
| OQ | Parameter verification | Test results |
| PQ | Performance verification | Production data |
| Report | Summary, conclusions | Approval signatures |

### Revalidation Triggers

| Trigger | Action Required |
|---------|-----------------|
| Equipment change | Assess impact, revalidate affected phases |
| Parameter change | OQ and PQ minimum |
| Material change | Assess impact, PQ minimum |
| Process failure | Full revalidation |
| Periodic | Per validation schedule (typically 3 years) |

### Special Process Examples

| Process | Validation Standard | Critical Parameters |
|---------|--------------------|--------------------|
| EO Sterilization | ISO 11135 | Temperature, humidity, EO concentration, time |
| Steam Sterilization | ISO 17665 | Temperature, pressure, time |
| Radiation Sterilization | ISO 11137 | Dose, dose uniformity |
| Sealing | Internal | Temperature, pressure, dwell time |
| Welding | ISO 11607 | Heat, pressure, speed |

---

## Supplier Qualification Workflow

Evaluate and approve suppliers per ISO 13485 Clause 7.4.

### Workflow: New Supplier Qualification

1. Identify supplier category:
   - Category A: Critical (affects safety/performance)
   - Category B: Major (affects quality)
   - Category C: Minor (indirect impact)
2. Request supplier information:
   - Quality certifications
   - Product specifications
   - Quality history
3. Evaluate supplier based on:
   - Quality system (ISO certification)
   - Technical capability
   - Quality history
   - Financial stability
4. For Category A suppliers:
   - Conduct on-site audit
   - Require quality agreement
5. Calculate qualification score
6. Make approval decision:
   - >80: Approved
   - 60-80: Conditional approval
   - <60: Not approved
7. Add to Approved Supplier List
8. **Validation:** Evaluation criteria scored; qualification records complete; supplier categorized

### Supplier Evaluation Criteria

| Criterion | Weight | Scoring |
|-----------|--------|---------|
| Quality System | 30% | ISO 13485=30, ISO 9001=20, Documented=10, None=0 |
| Quality History | 25% | Reject rate: <1%=25, 1-3%=15, >3%=0 |
| Delivery | 20% | On-time: >95%=20, 90-95%=10, <90%=0 |
| Technical Capability | 15% | Exceeds=15, Meets=10, Marginal=5 |
| Financial Stability | 10% | Strong=10, Adequate=5, Questionable=0 |

### Supplier Category Requirements

| Category | Qualification | Monitoring | Agreement |
|----------|---------------|------------|-----------|
| A - Critical | On-site audit | Annual review | Quality agreement |
| B - Major | Questionnaire | Semi-annual review | Quality requirements |
| C - Minor | Assessment | Issue-based | Standard terms |

### Supplier Performance Metrics

| Metric | Target | Calculation |
|--------|--------|-------------|
| Accept Rate | >98% | (Accepted lots / Total lots) × 100 |
| On-Time Delivery | >95% | (On-time / Total orders) × 100 |
| Response Time | <5 days | Average days to resolve issues |
| Documentation | 100% | (Complete CoCs / Required CoCs) × 100 |

---

## QMS Process Reference

For detailed requirements and audit questions for each ISO 13485:2016 clause, see [iso13485-clause-requirements.md](references/iso13485-clause-requirements.md).

### Management Review Required Inputs (Clause 5.6.2)

| Input | Source | Prepared By |
|-------|--------|-------------|
| Audit results | Internal and external audits | QA Manager |
| Customer feedback | Complaints, surveys | Customer Quality |
| Process performance | Process metrics | Process Owners |
| Product conformity | Inspection data, NCs | QC Manager |
| CAPA status | CAPA system | CAPA Officer |
| Previous actions | Prior review records | QMR |
| Changes affecting QMS | Regulatory, organizational | RA Manager |
| Recommendations | All sources | All Managers |

### Record Retention Requirements

> **⚠️ STATUS  QMSR transition (effective 2026-02-02):** FDA's Quality Management System Regulation (QMSR) final rule (89 FR 7496) amended 21 CFR Part 820 to **incorporate ISO 13485:2016 by reference** and removed the legacy QSR subsection structure. The section numbers below (820.30/.181/.184/.198) **no longer exist in the CFR**  they are retained only as a familiar index. The current authority for record retention is **ISO 13485:2016 §4.2.5** (retain "for at least the lifetime of the medical device as defined by the organization, but not less than two years"), with records additions in retained **21 CFR 820.35**. Cite the ISO 13485 clauses  not the 820.x numbers  in current compliance documentation.

| Record Type | Minimum Retention | Current authority under QMSR (legacy QSR shown for index) |
|-------------|-------------------|------------------|
| Device Master Record | Life of device + 2 years | ISO 13485 §4.2.3 (medical device file)/§4.2.5 (legacy QSR 820.181, historical) |
| Device History Record | Life of device + 2 years | ISO 13485 §4.2.5 + 21 CFR 820.35 (legacy QSR 820.184, historical) |
| Design History File | Life of device + 2 years | ISO 13485 §7.3.10/§4.2.5 (legacy QSR 820.30, historical) |
| Complaint Records | Life of device + 2 years | ISO 13485 §8.2.2/§4.2.5 + 21 CFR 820.35(b) (legacy QSR 820.198, historical) |
| Training Records | Employment + 3 years | Best practice |
| Audit Records | 7 years | Best practice |
| CAPA Records | 7 years | Best practice |
| Calibration Records | Equipment life + 2 years | Best practice |

> **Decision discipline:** This skill's checklists and tools structure QMS conformity assessment  they do not certify ISO 13485 / QMSR compliance. Final compliance determinations and record-retention decisions are yours to make and must be reviewed and signed off by the named QMR; route FDA-specific regulatory-classification questions to Regulatory Affairs and confirm current 21 CFR 820 / ISO 13485:2016 text at fda.gov before relying on any citation here.

---

## Decision Frameworks

### Exclusion Justification (Clause 4.2.2)

| Clause | Permissible Exclusion | Justification Required |
|--------|----------------------|------------------------|
| 6.4.2 | Contamination control | Product not affected by contamination |
| 7.3 | Design and development | Organization does not design products |
| 7.5.2 | Product cleanliness | No cleanliness requirements |
| 7.5.3 | Installation | No installation activities |
| 7.5.4 | Servicing | No servicing activities |
| 7.5.5 | Sterile products | No sterile products |

### Nonconformity Disposition Decision Tree

```
Nonconforming Product Identified
            │
            ▼
    Can it be reworked?
            │
       Yes──┴──No
        │       │
        ▼       ▼
    Is rework     Can it be used
    procedure     as is?
    available?        │
        │        Yes──┴──No
    Yes─┴─No     │       │
     │    │     ▼       ▼
     ▼    ▼  Concession  Scrap or
  Rework  Create    approval    return to
  per SOP  rework    needed?    supplier
          procedure     │
                    Yes─┴─No
                     │    │
                     ▼    ▼
                 Customer  Use as is
                 approval  with MRB
                          approval
```

### CAPA Initiation Criteria

| Source | Automatic CAPA | Evaluate for CAPA |
|--------|----------------|-------------------|
| Customer complaint | Safety-related | All others |
| External audit | Major NC | Minor NC |
| Internal audit | Major NC | Repeat minor NC |
| Product NC | Field failure | Trend exceeds threshold |
| Process deviation | Safety impact | Repeated deviations |

---

## Tools and References

### Scripts

| Tool | Purpose | Usage |
|------|---------|-------|
| [qms_audit_checklist.py](scripts/qms_audit_checklist.py) | Generate audit checklists by clause or process | `python qms_audit_checklist.py --help` |

**Audit Checklist Generator Features:**
- Generate clause-specific checklists (e.g., `--clause 7.3`)
- Generate process-based checklists (e.g., `--process design-control`)
- Full system audit checklist (`--audit-type system`)
- Text or JSON output formats
- Interactive mode for guided selection

### References

| Document | Content |
|----------|---------|
| [iso13485-clause-requirements.md](references/iso13485-clause-requirements.md) | Detailed requirements for each ISO 13485:2016 clause with audit questions |
| [qms-process-templates.md](references/qms-process-templates.md) | Ready-to-use templates for gap analysis, audit program, document control, CAPA, supplier, training |

### Quick Reference: Mandatory Documented Procedures

| Procedure | Clause | Key Elements |
|-----------|--------|--------------|
| Document Control | 4.2.3 | Approval, distribution, obsolete control |
| Record Control | 4.2.4 | Identification, retention, disposal |
| Internal Audit | 8.2.4 | Program, auditor qualification, reporting |
| NC Product Control | 8.3 | Identification, segregation, disposition |
| Corrective Action | 8.5.2 | Root cause, implementation, verification |
| Preventive Action | 8.5.3 | Risk identification, implementation |

---

## Related Skills

| Skill | Integration Point |
|-------|-------------------|
| [quality-manager-qmr](../quality-manager-qmr/) | Management review, quality policy |
| [capa-officer](../capa-officer/) | CAPA system management |
| [qms-audit-expert](../qms-audit-expert/) | Advanced audit techniques |
| [quality-documentation-manager](../quality-documentation-manager/) | DHF, DMR, DHR management |
| [risk-management-specialist](../risk-management-specialist/) | ISO 14971 integration |

---

## Consolidated Capabilities: QUALITY-MANAGER-QMR (Subsumed & Superceded)

# Senior Quality Manager Responsible Person (QMR)

Quality system accountability, management review leadership, and regulatory compliance oversight per ISO 13485 Clause 5.5.2 requirements.

---

## Table of Contents

- [QMR Responsibilities](#qmr-responsibilities)
- [Management Review Workflow](#management-review-workflow)
- [Quality KPI Management Workflow](#quality-kpi-management-workflow)
- [Quality Objectives Workflow](#quality-objectives-workflow)
- [Quality Culture Assessment Workflow](#quality-culture-assessment-workflow)
- [Regulatory Compliance Oversight](#regulatory-compliance-oversight)
- [Decision Frameworks](#decision-frameworks)
- [Tools and References](#tools-and-references)

---

## QMR Responsibilities

### ISO 13485 Clause 5.5.2 Requirements

| Responsibility | Scope | Evidence |
|----------------|-------|----------|
| QMS effectiveness | Monitor system performance and suitability | Management review records |
| Reporting to management | Communicate QMS performance to top management | Quality reports, dashboards |
| Quality awareness | Promote regulatory and quality requirements | Training records, communications |
| Liaison with external parties | Interface with regulators, Notified Bodies | Meeting records, correspondence |

### QMR Accountability Matrix

| Domain | Accountable For | Reports To | Frequency |
|--------|-----------------|------------|-----------|
| Quality Policy | Policy adequacy and communication | CEO/Board | Annual review |
| Quality Objectives | Objective achievement and relevance | Executive Team | Quarterly |
| QMS Performance | System effectiveness metrics | Management | Monthly |
| Regulatory Compliance | Compliance status across jurisdictions | CEO | Quarterly |
| Audit Program | Audit schedule completion, findings closure | Management | Per audit |
| CAPA Oversight | CAPA effectiveness and timeliness | Executive Team | Monthly |

### Authority Boundaries

| Decision Type | QMR Authority | Escalation Required |
|---------------|---------------|---------------------|
| Process changes within QMS | Approve with owner | Major process redesign |
| Document approval | Final QA approval | Policy-level changes |
| Nonconformity disposition | Accept/reject with MRB | Product release decisions |
| Supplier quality actions | Quality holds, audits | Supplier termination |
| Audit scheduling | Adjust internal audit schedule | External audit timing |
| Training requirements | Define quality training needs | Organization-wide training budget |

---

## Management Review Workflow

Conduct management reviews per ISO 13485 Clause 5.6 requirements.

### Workflow: Prepare and Execute Management Review

1. Schedule management review (minimum annually, typically quarterly or semi-annually)
2. Notify all required attendees minimum 2 weeks prior
3. Collect required inputs from process owners:
   - Audit results (internal and external)
   - Customer feedback (complaints, satisfaction, returns)
   - Process performance and product conformity
   - CAPA status and effectiveness
   - Previous review action items
   - Changes affecting QMS (regulatory, organizational)
   - Recommendations for improvement
4. Compile input summary report with trend analysis
5. Prepare presentation materials with supporting data
6. Distribute agenda and input package 1 week prior
7. Conduct review meeting per agenda
8. **Validation:** All required inputs reviewed; decisions documented with owners and due dates

### Required Attendees

| Role | Requirement | Input Responsibility |
|------|-------------|---------------------|
| CEO/General Manager | Required | Strategic decisions |
| QMR | Chair | Overall QMS status |
| Department Heads | Required | Process performance |
| RA Manager | Required | Regulatory changes |
| Production Manager | Required | Product conformity |
| Customer Quality | Required | Complaint data |

### Management Review Input Template

```
MANAGEMENT REVIEW INPUT SUMMARY

Review Period: [Start Date] to [End Date]
Review Date: [Scheduled Date]
Prepared By: [QMR Name]

1. AUDIT RESULTS
   Internal audits completed: [X] of [X] planned
   External audits completed: [X]
   Total findings: [X] major / [X] minor
   Open findings: [X]
   Finding trends: [Analysis]

2. CUSTOMER FEEDBACK
   Complaints received: [X]
   Complaint rate: [X per 1000 units]
   Customer satisfaction score: [X.X/5.0]
   Returns: [X] units ([X]%)
   Top issues: [Categories]

3. PROCESS PERFORMANCE
   [Process 1]: [Metric] vs [Target] - [Status]
   [Process 2]: [Metric] vs [Target] - [Status]
   Out-of-spec processes: [List]

4. PRODUCT CONFORMITY
   First pass yield: [X]%
   Nonconformance rate: [X]%
   Scrap cost: $[X]
   Top defect categories: [List]

5. CAPA STATUS
   Open CAPAs: [X]
   Overdue: [X]
   Effectiveness rate: [X]%
   Average age: [X] days

6. PREVIOUS ACTIONS
   Total from last review: [X]
   Completed: [X] | In progress: [X] | Overdue: [X]

7. CHANGES AFFECTING QMS
   Regulatory: [List changes]
   Organizational: [List changes]
   Process: [List changes]

8. RECOMMENDATIONS
   [Collected improvement opportunities]
```

### Management Review Output Requirements

| Output | Documentation | Owner |
|--------|---------------|-------|
| QMS improvement decisions | Action items with due dates | Assigned per item |
| Resource needs | Resource plan updates | Department heads |
| Quality objectives changes | Updated objectives document | QMR |
| Process improvement needs | Improvement project charters | Process owners |

See: [references/management-review-guide.md](references/management-review-guide.md)

---

## Quality KPI Management Workflow

Establish, monitor, and report quality performance indicators.

### Workflow: Establish Quality KPI Framework

1. Identify quality objectives requiring measurement
2. Select KPIs per objective using SMART criteria:
   - Specific: Clear definition and calculation
   - Measurable: Quantifiable with available data
   - Actionable: Team can influence results
   - Relevant: Aligned to quality objectives
   - Time-bound: Defined measurement frequency
3. Define target values based on baseline data and benchmarks
4. Assign data source and collection responsibility
5. Establish reporting frequency per KPI category
6. Configure dashboard displays and trend analysis
7. Define escalation thresholds and alert triggers
8. **Validation:** Each KPI has owner, target, data source, and escalation criteria

### Core Quality KPIs

| Category | KPI | Target | Calculation |
|----------|-----|--------|-------------|
| Process | First Pass Yield | >95% | (Units passed first time / Total units) × 100 |
| Process | Nonconformance Rate | <1% | (NC count / Total units) × 100 |
| CAPA | CAPA Closure Rate | >90% | (On-time closures / Due closures) × 100 |
| CAPA | CAPA Effectiveness | >85% | (Effective CAPAs / Verified CAPAs) × 100 |
| Audit | Finding Closure Rate | >90% | (On-time closures / Due closures) × 100 |
| Audit | Repeat Finding Rate | <10% | (Repeat findings / Total findings) × 100 |
| Customer | Complaint Rate | <0.1% | (Complaints / Units sold) × 100 |
| Customer | Satisfaction Score | >4.0/5.0 | Average of survey scores |

### KPI Review Frequency

| KPI Type | Review Frequency | Trend Period | Audience |
|----------|------------------|--------------|----------|
| Safety/Compliance | Daily monitoring | Weekly | Operations |
| Production Quality | Weekly | Monthly | Department heads |
| Customer Quality | Monthly | Quarterly | Executive team |
| Strategic Quality | Quarterly | Annual | Board/C-suite |

### Performance Response Matrix

| Performance Level | Status | Action Required |
|-------------------|--------|-----------------|
| >110% of target | Exceeding | Consider raising target |
| 100-110% of target | Meeting | Maintain current approach |
| 90-100% of target | Approaching | Monitor closely |
| 80-90% of target | Below | Improvement plan required |
| <80% of target | Critical | Immediate intervention |

See: [references/quality-kpi-framework.md](references/quality-kpi-framework.md)

---

## Quality Objectives Workflow

Establish and maintain measurable quality objectives per ISO 13485 Clause 5.4.1.

### Workflow: Annual Quality Objectives Setting

1. Review prior year objective achievement
2. Analyze quality performance trends and gaps
3. Align with organizational strategic plan
4. Draft objectives with measurable targets
5. Validate resource availability for achievement
6. Obtain executive approval
7. Communicate objectives organization-wide
8. **Validation:** Each objective is measurable, has owner, target, and timeline

### Quality Objective Structure

```
QUALITY OBJECTIVE [Number]

Objective Statement: [Clear, measurable statement]
Aligned to Policy Element: [Quality policy section]
Target: [Specific measurable target]
Baseline: [Current performance]
Owner: [Name and title]
Due Date: [Target achievement date]

Success Criteria:
- [Criterion 1]
- [Criterion 2]

Measurement Method: [How progress is tracked]
Reporting Frequency: [Monthly/Quarterly]

Supporting Initiatives:
- [Initiative 1]
- [Initiative 2]

Resource Requirements:
- [Resource 1]
- [Resource 2]
```

### Objective Categories

| Category | Example Objectives | Typical Targets |
|----------|-------------------|-----------------|
| Customer Quality | Reduce complaint rate | <0.1% of units sold |
| Process Quality | Improve first pass yield | >96% |
| Compliance | Maintain certification | Zero major NCs |
| Efficiency | Reduce quality costs | <4% of revenue |
| Culture | Increase training completion | >98% on-time |

### Quarterly Objective Review

| Review Element | Assessment | Action |
|----------------|------------|--------|
| Progress vs. target | On track / Behind / Ahead | Adjust resources if behind |
| Relevance | Still valid / Needs update | Modify if conditions changed |
| Resources | Adequate / Insufficient | Request additional if needed |
| Barriers | Identified obstacles | Escalate for resolution |

---

## Quality Culture Assessment Workflow

Assess and improve organizational quality culture.

### Workflow: Annual Quality Culture Assessment

1. Design or select quality culture survey instrument
2. Define survey population (all employees or sample)
3. Communicate survey purpose and confidentiality
4. Administer survey with 2-week response window
5. Analyze results by department, role, and tenure
6. Identify strengths and improvement areas
7. Develop action plan for culture gaps
8. **Validation:** Response rate >60%; action plan addresses bottom 3 scores

### Quality Culture Dimensions

| Dimension | Indicators | Assessment Method |
|-----------|------------|-------------------|
| Leadership commitment | Management visible support for quality | Survey, observation |
| Quality ownership | Employees feel responsible for quality | Survey |
| Communication | Quality information flows effectively | Survey, audit |
| Continuous improvement | Suggestions submitted and implemented | Metrics |
| Training and competence | Employees feel adequately trained | Survey, records |
| Problem solving | Issues addressed at root cause | CAPA analysis |

### Culture Survey Categories

| Category | Sample Questions |
|----------|------------------|
| Leadership | "Management demonstrates commitment to quality" |
| Resources | "I have the tools and training to do quality work" |
| Communication | "Quality expectations are clearly communicated" |
| Empowerment | "I am encouraged to report quality issues" |
| Recognition | "Quality achievements are recognized" |

### Culture Improvement Actions

| Gap Identified | Potential Actions |
|----------------|-------------------|
| Low leadership visibility | Quality gemba walks, all-hands quality updates |
| Inadequate training | Competency-based training program |
| Poor communication | Quality newsletters, department huddles |
| Low reporting | Anonymous reporting system, no-blame culture |
| Lack of recognition | Quality award program, team celebrations |

---

## Regulatory Compliance Oversight

Monitor and maintain regulatory compliance across jurisdictions.

### Multi-Jurisdictional Compliance Matrix

| Jurisdiction | Regulation | Requirement | Status Tracking |
|--------------|------------|-------------|-----------------|
| EU | MDR 2017/745 | CE marking, Notified Body | Technical file, annual review |
| USA | 21 CFR 820 (QMSR) | FDA registration, QMSR compliance  21 CFR 820 incorporates ISO 13485:2016 by reference (effective 2026-02-02; formerly the QSR) | Annual registration, inspections |
| International | ISO 13485 | QMS certification | Surveillance audits |
| Germany | MPG/MPDG | National implementation | Competent authority filings |

### Compliance Monitoring Workflow

1. Maintain regulatory requirement register
2. Subscribe to regulatory update services
3. Assess impact of regulatory changes monthly
4. Update affected processes within 90 days of effective date
5. Verify training completion for regulatory changes
6. Document compliance status in management review
7. Maintain inspection readiness checklist
8. **Validation:** All applicable requirements mapped; no expired registrations

> **Decision discipline:** This compliance matrix is decision support, not a compliance determination. Final regulatory-status calls are yours to make as QMR and must be signed off by the named owner; route FDA-specific questions to Regulatory Affairs and verify current 21 CFR 820 (QMSR) / ISO 13485:2016 text at fda.gov before relying on any citation here.

### Regulatory Authority Interface

| Activity | QMR Role | Preparation Required |
|----------|----------|---------------------|
| Notified Body audit | Primary contact | Audit package, personnel schedules |
| FDA inspection | Host, escort coordinator | Inspection readiness review |
| Competent Authority inquiry | Response coordinator | Technical file access |
| Regulatory meeting | Attendee or delegate | Briefing materials |

### Inspection Readiness Checklist

| Area | Ready | Action Needed |
|------|-------|---------------|
| Document control system current | ☐ | |
| Training records complete | ☐ | |
| CAPA system current, no overdue items | ☐ | |
| Complaint files complete | ☐ | |
| Equipment calibration current | ☐ | |
| Supplier qualification files complete | ☐ | |
| Management review records available | ☐ | |
| Internal audit program current | ☐ | |

---

## Decision Frameworks

### Escalation Decision Tree

```
Issue Identified
      │
      ▼
Is it a regulatory violation?
      │
  Yes─┴─No
  │      │
  ▼      ▼
Escalate to    Is it a safety issue?
Executive          │
immediately    Yes─┴─No
               │      │
               ▼      ▼
          Escalate to   Does it affect
          Safety Team   multiple departments?
                             │
                         Yes─┴─No
                         │      │
                         ▼      ▼
                    Escalate to  Handle at
                    Executive    department level
```

### Quality Investment Prioritization

| Criteria | Weight | Score Method |
|----------|--------|--------------|
| Regulatory requirement | 30% | Required=10, Recommended=5, Optional=2 |
| Customer impact | 25% | Direct=10, Indirect=5, None=0 |
| Cost savings potential | 20% | >$100K=10, $50-100K=7, <$50K=3 |
| Implementation complexity | 15% | Simple=10, Moderate=5, Complex=2 |
| Strategic alignment | 10% | Core=10, Supporting=5, Peripheral=2 |

### Resource Allocation Matrix

| Resource Type | Allocation Authority | Escalation Threshold |
|---------------|---------------------|---------------------|
| Quality personnel | QMR | >1 FTE addition |
| Quality equipment | QMR | >$25K |
| External consultants | QMR | >$50K or >30 days |
| Quality systems | Executive approval | >$100K |

---

## Tools and References

### Scripts

| Tool | Purpose | Usage |
|------|---------|-------|
| [management_review_tracker.py](scripts/management_review_tracker.py) | Track review inputs, actions, metrics | `python management_review_tracker.py --help` |

**Management Review Tracker Features:**
- Track input collection status from process owners
- Monitor action item completion and aging
- Generate metrics summary for review
- Produce recommendations for review focus areas

### References

| Document | Content |
|----------|---------|
| [management-review-guide.md](references/management-review-guide.md) | ISO 13485 Clause 5.6 requirements, input/output templates, action tracking |
| [quality-kpi-framework.md](references/quality-kpi-framework.md) | KPI categories, targets, calculations, dashboard templates |

### Quick Reference: Management Review Inputs (ISO 13485 Clause 5.6.2)

| Input | Source | Required |
|-------|--------|----------|
| Feedback | Customer complaints, surveys | Yes |
| Audit results | Internal and external audits | Yes |
| Process performance | Process metrics | Yes |
| Product conformity | Inspection, NC data | Yes |
| CAPA status | CAPA system | Yes |
| Previous actions | Prior review records | Yes |
| Changes | Regulatory, organizational | Yes |
| Recommendations | All sources | Yes |

### Quick Reference: Management Review Outputs (ISO 13485 Clause 5.6.3)

| Output | Documentation Required |
|--------|----------------------|
| Improvement to QMS and processes | Action items with owners |
| Improvement to product | Project initiation if needed |
| Resource needs | Resource plan updates |

---

## Related Skills

| Skill | Integration Point |
|-------|-------------------|
| [quality-manager-qms-iso13485](../quality-manager-qms-iso13485/) | QMS process management |
| [capa-officer](../capa-officer/) | CAPA system oversight |
| [qms-audit-expert](../qms-audit-expert/) | Internal audit program |
| [quality-documentation-manager](../quality-documentation-manager/) | Document control oversight |

---

## Consolidated Capabilities: FDA-QSR-AUDIT-PREP (Subsumed & Superceded)

# /cs:fda-qsr-audit-prep  FDA QSR Forcing Questions

**Command:** `/cs:fda-qsr-audit-prep <scope>`

The FDA QSR auditor pressure-tests any US medical-device QSR work. Six questions before any internal audit, FDA inspection, Form 483 response, or recall decision.

## When to Run

- Before annual internal QSR audit
- Before pre-FDA-inspection readiness review (any device commercially distributed in US)
- After receiving Form 483 observations
- After Warning Letter receipt
- After MDR-reportable event
- Before recall decision (voluntary vs FDA-initiated)
- Before submitting 510(k) / PMA (where QSR posture affects approval timeline)

## The Six QSR Questions

### 1. Show me the complaint files from the last quarter  and the corresponding MDR reports.
**21 CFR 820.198 + 21 CFR 803  most-cited FDA inspection area.**
- Complaint log complete: who / what / when / device / batch
- Investigation closure within reasonable timeline
- MDR-reporting decision tree applied: death OR serious injury OR malfunction-that-could-cause = MDR
- 30-day timeline for most MDR reports; 5 days for certain serious events
- Complaint trending input to management review

### 2. When was process validation (IQ/OQ/PQ) last revalidated per 21 CFR 820.75?
**Cross-walks ISO 13485 Clause 7.5.6 (substantially harmonized post-Feb 2026).**
- Initial validation at process introduction
- Revalidation triggers: process / equipment / material change OR periodic schedule
- Statistical techniques per 21 CFR 820.250 where applicable
- Cross-check with cs-cqm-iso13485 for ISO 13485 alignment

### 3. Show me the DHRs for products commercially distributed in last 2 years.
**21 CFR 820.180  2-year retention from commercial distribution; check sampling for completeness.**
- Device History Record (DHR) for each unit/lot/batch
- Must include: dates of manufacture, quantity manufactured, quantity released, acceptance records, primary identification label, device identification, control number
- Sample stratified by product class
- Verify DHR closeness to DHF (design history file)

### 4. Show me CAPAs from the last 6 months with effectiveness verification.
**21 CFR 820.100 = ISO 13485 8.5.2 substantially harmonized.**
- Root cause analysis depth (5 Why minimum)
- Effectiveness verification = measurable evidence, not "we updated the procedure"
- Containment / correction / corrective action distinction documented
- Closure approval by appropriate authority
- Aging CAPAs > 90 days flagged

### 5. Show me labeling (21 CFR 801) review for the most recent product launch.
**FDA-specific overlay not in ISO 13485.**
- Labeling per 21 CFR 801 requirements
- For specific device types: also 21 CFR 800 series sectoral overlays
- UDI (Unique Device Identification) per 21 CFR 830
- Promotional materials reviewed for accuracy + non-misleading

### 6. If a Form 483 was issued in the last 3 years, show me the closure status.
**Form 483 = FDA observation; not equivalent to ISO nonconformity.**
- Response within 15 working days
- Each observation has documented corrective + preventive action with timeline
- Effectiveness verification evidence
- For Warning Letters: separate response track + potentially FDA meeting

## Workflow

```bash
# 1. QSR compliance posture
python ra-qm-team/skills/fda-consultant-specialist/scripts/qsr_compliance_checker.py compliance_state.json

# 2. FDA submission tracking (510(k) / PMA / IDE)
python ra-qm-team/skills/fda-consultant-specialist/scripts/fda_submission_tracker.py submissions.json

# 3. HIPAA overlap (if connected device handles PHI)
python ra-qm-team/skills/fda-consultant-specialist/scripts/hipaa_risk_assessment.py phi_inventory.json

# 4. Mock FDA inspection
python ../../skills/compliance-os/scripts/audit_simulator.py fda_qsr_scope.json
```

## Output Format

```markdown
# FDA QSR Audit Prep: <scope>
**Date:** YYYY-MM-DD

## The Decision Being Made
[programme-plan | inspection-readiness | 483-response | MDR-decision | recall]

## Complaint + MDR Posture
- Complaints last quarter: N
- MDR-reportable events: M
- MDR reports filed within timeline: % (target 100%)
- Complaint trending review at management level: yes/no

## Process Validation Status (21 CFR 820.75)
- Validations on schedule: %
- Stale validations: <list>
- Statistical techniques applied: yes/no per process

## DHR Completeness (21 CFR 820.180)
- DHRs sampled: N
- Completeness rate: %
- 2-year retention compliant: yes/no
- Stratified by product class: yes/no

## CAPA Health (21 CFR 820.100)
- CAPAs sampled: N
- Root cause analysis depth: adequate/inadequate
- Effectiveness verification: complete/incomplete
- Aging CAPAs > 90 days: N

## Labeling (21 CFR 801)
- Recent products reviewed: <list>
- Labeling accurate + non-misleading: yes/no
- UDI compliance per 21 CFR 830: yes/no

## Form 483 / Warning Letter History
- Form 483s last 3 years: N (each: closed/in-progress)
- Warning Letters last 5 years: N (each: closed/in-progress)
- Pattern across observations: <thematic>

## ISO 13485 Cross-Walk (post-Feb 2026 harmonization)
- ISO 13485 audit findings: <link to cs-cqm-iso13485 output>
- FDA-specific overlays remaining: labeling + complaint handling + MDR reporting + recall procedures
- Cross-framework reuse: % of evidence shared

## Verdict
🟢 INSPECTION-READY | 🟡 GAPS-IDENTIFIED | 🔴 NOT-READY

## Top 3 Actions
[3 concrete next steps with owner + FDA-cited timeline (15 days / 30 days / etc.)]

## Outside Counsel Required
[For Warning Letter response, recall decisions, or 510(k) / PMA strategy disputes]
```

## Routing

- `/cs:compliance-readiness`  for multi-framework view
- `/cs:iso13485-audit-prep`  for ISO 13485 cross-walk pair (substantially harmonized)
- `/cs:gdpr-audit-prep`  if connected device handles personal data
- `/cs:gc-review`  for Warning Letter response coordination

## Related

- Agent: [`cs-fda-qsr-auditor`](../../agents/cs-fda-qsr-auditor.md)
- Skill: [`fda-consultant-specialist`](../../../ra-qm-team/skills/fda-consultant-specialist/SKILL.md)
- Adjacent: `../iso13485-audit-prep/`, `../compliance-readiness/`

---

**Version:** 1.0.0

---

## Consolidated Capabilities: ISO13485-AUDIT-PREP (Subsumed & Superceded)

# /cs:iso13485-audit-prep  ISO 13485 QMS Forcing Questions

**Command:** `/cs:iso13485-audit-prep <scope>`

The ISO 13485 QMS auditor pressure-tests any medical-device QMS work. Six traceability-obsessed questions before any internal audit, MDR / FDA QSR review, or product launch.

## When to Run

- Before annual Clause 8.2.4 internal audit
- Before MDR / FDA QSR alignment review (substantially harmonized post Feb 2026)
- Before new-device commercial launch (DHF closure audit)
- After significant CAPA closure event (effectiveness verification audit)
- Post-recall event (root cause + corrective action audit)
- Quarterly during regulatory submission preparation

## The Six QMS Questions

### 1. Pull three random DHFs. Are design verification + validation evidence complete?
**Most-cited finding area.**
- DHF must include: design plan + inputs + outputs + verification + validation + transfer + changes
- Sample stratified by product class (I, IIa, IIb, III per MDR)
- Reference `iso13485_audit_playbook.md` for the per-DHF checklist
- Verify traceability matrix from user needs through clinical evidence

### 2. Show me the last 5 CAPAs with effectiveness verification evidence.
**Second-most-cited finding area.**
- Containment / correction / corrective action distinction documented
- Root cause analysis depth: 5 Why minimum
- Effectiveness verification = measurable evidence, not "we updated the procedure"
- Closure approved by appropriate authority
- Repeat CAPAs across products = systemic issue trigger

### 3. When was process validation (IQ/OQ/PQ) last revalidated?
**Clause 7.5.6  often stale.**
- Initial validation at process introduction
- Revalidation triggers: process change, equipment change, material change, periodic schedule
- Trend monitoring (SPC) where statistical techniques apply per Clause 8.4
- Cross-check with cs-fda-qsr-auditor for 21 CFR 820.75 alignment

### 4. Show me the risk management file for the highest-risk product.
**Clause 7.1 + ISO 14971:2019.**
- Risk management plan exists per product
- Hazard identification covers reasonable foreseeable misuse
- Risk control hierarchy applied: inherent safety > protective measures > information for safety
- Residual risk evaluated + accepted with rationale
- Post-production information feeds back into RMF
- For AI-enabled medical devices: layer ISO 42001 A.5 impact assessment on top

### 5. Show me post-market surveillance evidence  last 6 months.
**Clause 8.2.1  high-stakes for MDR + FDA.**
- Customer complaint log + investigation closure
- Vigilance reports (serious incident / FSCA) submitted per applicable regulation
- Trend analysis evidence + management review input
- Post-market clinical follow-up (PMCF) for MDR high-risk devices
- MDR reports per 21 CFR 803 for US-marketed devices (cross-check with cs-fda-qsr-auditor)

### 6. Where's the management review evidence covering all Clause 5.6 inputs?
**Annual minimum; semi-annual for mature programs.**
- Required inputs per Clause 5.6.2: audit results, customer feedback, process performance, product conformity, status of preventive + corrective actions, follow-up from prior reviews, changes that could affect QMS, recommendations for improvement, regulatory requirements
- Outputs per Clause 5.6.3: improvement decisions, product requirement changes, resource needs
- Integrated review across frameworks (per `multi_framework_audit_playbook.md`) preferred

## Workflow

```bash
# 1. Audit programme optimization
python ra-qm-team/skills/qms-audit-expert/scripts/audit_schedule_optimizer.py audit_scope.json

# 2. Mock audit for readiness check
python ../../skills/compliance-os/scripts/audit_simulator.py iso13485_scope.json

# 3. CAPA system review
# Route to ra-qm-team/skills/capa-officer/ tools

# 4. Risk management file review
# Route to ra-qm-team/skills/risk-management-specialist/ tools
```

## Output Format

```markdown
# ISO 13485 Audit Prep: <scope>
**Date:** YYYY-MM-DD

## The Decision Being Made
[programme-plan | DHF-closure | CAPA-health | post-market-trend | pre-cert | MDR-FDA-alignment]

## Design Control Status (sampled DHFs)
- DHFs sampled: <list product IDs>
- Verification evidence: pass/fail per DHF
- Validation evidence: pass/fail per DHF
- Clinical evidence (per MDR Annex XIV / FDA 510(k)): pass/fail
- Traceability matrix complete: yes/no per DHF

## CAPA Health
- CAPAs sampled: N
- Root cause analysis depth: adequate/inadequate per CAPA
- Effectiveness verification: complete/incomplete per CAPA
- Aging CAPAs > 90 days: N
- Repeat issues across products: <list>

## Process Validation Status
- Validations on schedule: %
- Stale validations (> 12 months since revalidation): <list>
- Statistical techniques applied per Clause 8.4: yes/no

## Risk Management File Status
- Sampled product RMFs: <list>
- Post-production updates in last 12 months: <count per product>
- Residual risk acceptance signed: yes/no

## Post-Market Surveillance
- Complaint trending: stable/rising
- MDR / vigilance reports filed timely: %
- PMCF on schedule (where required): yes/no

## Management Review Status
- Last review date: YYYY-MM-DD
- Required Clause 5.6.2 inputs present: yes/no
- Open action items past due: N

## Cross-Framework Impact
- EU MDR alignment: clean / gaps in <list>
- FDA QSR alignment (post-Feb 2026): substantially harmonized; FDA-specific overlays per cs-fda-qsr-auditor
- ISO 42001 AIMS overlay (if AI-enabled device): pass/fail per Annex A

## Verdict
🟢 READY | 🟡 CLOSE-DHF-GAPS-FIRST | 🔴 NOT-READY

## Top 3 Actions
[3 concrete next steps with owner + corrective-action timeline]
```

## Routing

- `/cs:compliance-readiness`  for multi-framework view
- `/cs:fda-qsr-audit-prep`  for FDA-specific overlay
- `/cs:aims-audit`  for AI-enabled medical device ISO 42001 layer
- `/cs:gdpr-audit-prep`  for personal-data overlap (clinical data, customer data)
- `/cs:cpo-review`  for executive product strategy decisions
- `/cs:decide`  to log the verdict

## Related

- Agent: [`cs-cqm-iso13485`](../../agents/cs-cqm-iso13485.md)
- Skill: [`qms-audit-expert`](../../../ra-qm-team/skills/qms-audit-expert/SKILL.md)
- Playbook: [iso13485_audit_playbook.md](../../../ra-qm-team/skills/qms-audit-expert/references/iso13485_audit_playbook.md)
- Adjacent: `../fda-qsr-audit-prep/`, `../aims-audit/`, `../compliance-readiness/`

---

**Version:** 1.0.0
