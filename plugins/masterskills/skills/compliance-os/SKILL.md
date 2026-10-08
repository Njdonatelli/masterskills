---
name: "compliance-os"
description: >-
  Compliance OS  meta-orchestrator that lets compliance teams CONFIGURE which frameworks apply, COMPUTE cross-framework control overlap, SIMULATE internal audits, and CONSOLIDATE evidence across multiple frameworks. Four decisions: (1) Given a company profile, which of the 12 supported frameworks apply (ISO 27001/13485/42001/14971, EU AI Act, MDR 745, GDPR, SOC 2, FDA QSR, NIST CSF 2.0, NIS2, HIPAA)? (2) Across selected frameworks, which controls overlap and how much evidence reuses? (3) For a given framework + scope, what does a realistic mock audit produce  drawing from the 205-scenario library? (4) Across selected frameworks, what's the unified evidence checklist with reuse map? Use when standing up a multi-framework program, planning the annual audit calendar, or preparing for certification stage 1. Does NOT replace per-framework skills (it orchestrates them). [Also supersedes `compliance-readiness`: triggers on '/cs:compliance-readiness', 'compliance readiness', 'multi-framework compliance interrogation']
license: MIT
metadata:
  version: 1.0.0
  author: Alireza Rezvani
  category: compliance-os
  domain: multi-framework-compliance-orchestration
  updated: 2026-05-13
  python-tools: framework_selector.py, cross_framework_mapper.py, audit_simulator.py, evidence_pool_generator.py
  frameworks: iso-27001, iso-13485, iso-42001, iso-14971, eu-ai-act, eu-mdr-745, gdpr, soc-2, fda-qsr, nist-csf, nis2, hipaa
---

# Compliance OS  Meta-Orchestrator

Multi-framework compliance program orchestration. **Four decisions, no per-framework deep-dive:**

1. **Which frameworks apply to this company?**  `framework_selector.py` ranks the 12 supported frameworks against a company profile (industry, geography, AI use, medical, financial, headcount, customers, healthcare-PHI, NIS2 essential/important entity, US gov contractor) and returns applicable ones with dependency graph
2. **How much do selected frameworks overlap?**  `cross_framework_mapper.py` computes control-level overlap with confidence rating; outputs unified control matrix + evidence-reuse opportunities
3. **What does a mock audit produce?**  `audit_simulator.py` generates 8–15 finding scenarios with severity distribution matching IIA expectations + interview questions per control
4. **What's the unified evidence checklist?**  `evidence_pool_generator.py` consolidates evidence across enabled frameworks; outputs which artefact satisfies which controls across which frameworks

This skill is **NOT** a per-framework deep-dive. The per-framework skills (`ra-qm-team/skills/iso42001-specialist/`, `compliance-team-eu-ai-act/`, `ra-qm-team/skills/gdpr-dsgvo-expert/`, etc.) do the operational work. Compliance OS orchestrates them.

This skill is **NOT** a substitute for binding legal advice. Cross-framework mappings reflect published guidance (ISO standards, regulations, EDPB/Commission guidance, IIA / AICPA professional standards). Novel cross-walks should be reviewed with counsel.

## Keywords

compliance orchestration, multi-framework compliance, compliance OS, cross-framework mapping, control overlap, evidence pool, evidence reuse, audit simulation, mock audit, internal audit programme, GRC, governance risk compliance, framework selector, compliance program, integrated compliance, ISO 19011, IIA IPPF, AICPA AT-C, NIST CSF profile, multi-cert program, SOC 2 + ISO 27001, ISO 27001 + ISO 42001, ISO 13485 + MDR 745, AI Act + ISO 42001, GDPR + ISO 27001, compliance officer, compliance team workflow, certification readiness

## Quick Start

```bash
# Decision A: Which frameworks apply for the company?
python scripts/framework_selector.py                          # embedded mid-stage AI SaaS sample
python scripts/framework_selector.py path/to/profile.json

# Decision B: Compute cross-framework overlap
python scripts/cross_framework_mapper.py                      # embedded ISO 27001 + SOC 2 sample
python scripts/cross_framework_mapper.py path/to/control_libs.json

# Decision C: Simulate an audit
python scripts/audit_simulator.py                             # embedded ISO 27001 sample
python scripts/audit_simulator.py path/to/audit_scope.json

# Decision D: Consolidate evidence checklist across frameworks
python scripts/evidence_pool_generator.py                     # embedded 3-framework sample
python scripts/evidence_pool_generator.py path/to/program.json
```

## Key Questions (ask these first)

- **Have you named every applicable framework?** Forgetting one means rebuilding the audit program later. Run `framework_selector.py` with your profile.
- **What's the most certificate / regulation your company already operates?** That's your reuse anchor. Map every new framework against it.
- **What's the audit calendar?** A multi-framework program means surveillance audits stacked through the year  plan auditor independence + capacity.
- **Where is evidence stored?** Multi-framework programs collapse when evidence lives in one team's drive without an index. Run `evidence_pool_generator.py` to surface the reuse opportunities.
- **What's the management-review cadence across frameworks?** Each framework wants its own management review, but a single integrated review (per ISO Annex SL) typically satisfies all of them with one calendar slot.
- **Who owns the meta-program?** If no single accountable role, the program fragments.

## Core Responsibilities

### 1. Framework Selection

**The framework:** company-profile JSON in → applicable-framework list out with dependency graph.

**Deterministic logic:**
- Medical device → ISO 13485 + ISO 14971 + (EU MDR 745 if EU market) + (FDA QSR if US market)
- Customer-facing AI → ISO 42001 + EU AI Act (if EU users) + GDPR (if personal data)
- B2B SaaS with enterprise customers → SOC 2 + ISO 27001 (often required for procurement)
- EU customers + personal data → GDPR mandatory
- Highly regulated industry (financial, health) → additional sectoral overlays

**Run** `framework_selector.py` to apply the decision rules.

### 2. Cross-Framework Control Mapping

**The framework:** for each selected framework, parse its control library; compute overlap with other selected frameworks.

**Per merged-control output:**
- Mapping confidence (HIGH / MEDIUM / LOW)
- Evidence-reuse opportunity (single artefact satisfies N controls)
- Per-framework citation
- Implementation guidance reusable across frameworks

**Densest known overlap:** ISO 27001 Annex A ↔ SOC 2 Trust Services Criteria  historically ~75% control coverage shared. Adding ISO 42001 brings AI-specific controls; adding GDPR brings privacy-specific.

**Run** `cross_framework_mapper.py` with framework control libraries.

### 3. Audit Simulation

**The framework:** generate a realistic mock internal audit per ISO 19011 + IIA IPPF standards.

**Per audit output:**
- 8–15 finding scenarios per ISO 19011 typical depth
- Severity distribution: ≥ 40% observations/OFI, ≤ 15% critical/major (IIA expectation for healthy programs)
- Interview questions per scoped control (3–5 questions per control)
- Document-review request list
- Walk-through requests where applicable

**Run** `audit_simulator.py` with framework + scope.

### 4. Evidence Pool

**The framework:** consolidate evidence requirements across enabled frameworks; identify reuse opportunities.

**Output:**
- Evidence artefact list (e.g., access-review log, supplier risk register, incident log)
- Per artefact: list of (framework, control) tuples it satisfies
- Reuse-leverage score (artefact A satisfies N controls across M frameworks)
- Acquisition cost estimate (effort to produce + maintain)

**Run** `evidence_pool_generator.py` with program config.

## Workflows

### Workflow 1: Program Bootstrap (multi-framework, 4–8 weeks)
**Goal:** stand up a compliance program covering 2–4 frameworks simultaneously.

```bash
# 1. Run framework selector with company profile
python scripts/framework_selector.py profile.json
# 2. For each applicable framework, identify the per-framework skill and run its gap analysis
# 3. Run cross-framework mapper to identify reuse opportunities
python scripts/cross_framework_mapper.py control_libs.json
# 4. Run evidence pool generator to consolidate
python scripts/evidence_pool_generator.py program.json
# 5. Cross-check with cs-compliance-officer agent
# 6. Output: prioritized program backlog with owners + dates
```

### Workflow 2: Annual Audit Calendar (yearly)
**Goal:** plan internal audit cycles covering all applicable frameworks.

```bash
# 1. Refresh framework selector if profile changed
python scripts/framework_selector.py profile.json
# 2. For each framework, run its internal-audit-plan tool
#    (e.g., aims_audit_scheduler.py for ISO 42001; isms_audit_scheduler.py for ISO 27001)
# 3. Coordinate the audit calendar across frameworks (auditor independence + capacity)
# 4. Run audit simulator for each framework to prep auditors
python scripts/audit_simulator.py scope.json
# 5. Output: integrated audit calendar with owners + auditor assignments
```

### Workflow 3: Pre-Certification Readiness (per new framework, 6–12 weeks)
**Goal:** prepare for an external certification audit.

```bash
# 1. Run gap analysis for the new framework
#    (ISO 42001: aims_gap_analyzer.py; ISO 27001: compliance_checker.py; SOC 2: gap_analyzer.py)
# 2. Run cross-framework mapper against already-certified frameworks
python scripts/cross_framework_mapper.py control_libs.json
# 3. Reuse evidence for HIGH-confidence mappings; build new for MEDIUM/LOW
# 4. Run audit simulator to dry-run the certification audit
python scripts/audit_simulator.py scope.json
# 5. Close remaining gaps before external auditor stage 1
```

### Workflow 4: Evidence Pool Consolidation (quarterly)
**Goal:** keep the unified evidence pool fresh + reusable.

```bash
# 1. Refresh evidence pool generator
python scripts/evidence_pool_generator.py program.json
# 2. Identify HIGH-reuse-leverage artefacts (1 evidence -> 5+ controls)
# 3. Confirm evidence freshness (within retention requirement per framework)
# 4. Audit the evidence pool itself (no orphan controls, no stale evidence)
```

## Output Standards

```
**Bottom Line:** [one sentence  what's the multi-framework picture + biggest reuse opportunity]
**The Decision:** [one of: framework-set | overlap-map | audit-plan | evidence-consolidation]
**The Evidence:** [framework names + control IDs from the tool, not adjectives]
**How to Act:** [3 concrete next steps with owners + dates]
**Your Decision:** [the call only the compliance officer can make  which frameworks to pursue, audit cycle priority, evidence-reuse policy]
```

## Adjacent Skills

- `ra-qm-team/skills/iso42001-specialist/`  ISO 42001 deep-dive (paired with compliance-team-iso42001 plugin)
- `ra-qm-team/skills/eu-ai-act-specialist/`  EU AI Act deep-dive (paired with compliance-team-eu-ai-act plugin)
- `ra-qm-team/skills/information-security-manager-iso27001/`  ISO 27001 ISMS deep-dive
- `ra-qm-team/skills/quality-manager-qms-iso13485/`  ISO 13485 QMS deep-dive
- `ra-qm-team/skills/gdpr-dsgvo-expert/`  GDPR deep-dive
- `ra-qm-team/skills/soc2-compliance/`  SOC 2 deep-dive
- `ra-qm-team/skills/fda-consultant-specialist/`  FDA QSR deep-dive
- `ra-qm-team/skills/mdr-745-specialist/`  EU MDR 745 deep-dive
- `ra-qm-team/skills/risk-management-specialist/`  ISO 14971 deep-dive
- `c-level-advisor/chief-ai-officer-advisor/`  Executive AI risk decisions (build-vs-buy, model selection)
- `c-level-advisor/skills/general-counsel-advisor/`  Legal review for novel cases

## References

- [compliance_os_pattern.md](references/compliance_os_pattern.md)  The meta-framework architecture (configure → map → simulate → consolidate → review); when to use vs not
- [cross_framework_overlap.md](references/cross_framework_overlap.md)  The 9-framework × control-family overlap table with mapping confidence (Phase 3 expands to 12 frameworks via `cross_framework_mapper.py`)
- [audit_simulation_methodology.md](references/audit_simulation_methodology.md)  ISO 19011 + IIA IPPF + AICPA AT-C audit-simulation principles + severity distribution heuristics
- [evidence_management.md](references/evidence_management.md)  Evidence pool design + retention + freshness + reuse-leverage scoring
- [multi_framework_audit_playbook.md](references/multi_framework_audit_playbook.md)  Integrated audit programme for 2+ frameworks (Phase 2)
- [evidence_artifact_reuse_index.md](references/evidence_artifact_reuse_index.md)  Empirically-derived reuse-leverage ranking across all 12 frameworks (Phase 3)

## Phase 3 Asset: Mock Audit Scenario Library

`assets/mock_audit_library.json`  205 pre-built finding scenarios spanning 12 frameworks + 26 themes + 4 severity levels (34 critical, 88 major, 54 minor, 29 observation). Each scenario tags applicable frameworks; cross-reference `scripts/cross_framework_mapper.py` merged-controls catalogue to resolve framework-specific control IDs. Use as input to enrich `audit_simulator.py` mock audits, as a training resource for new internal auditors, or as the seed for finding-pattern detection across multi-framework programmes.

---

**Version:** 1.2.0
**Status:** Production Ready

---

## Consolidated Capabilities: COMPLIANCE-READINESS (Subsumed & Superceded)

# /cs:compliance-readiness  Compliance Officer Forcing Questions

**Command:** `/cs:compliance-readiness <program>`

The multi-framework compliance officer pressure-tests any compliance program. Six questions before any new-framework commitment, audit cycle planning, or certification readiness sign-off.

## When to Run

- Before adopting a new compliance framework
- Before annual audit calendar finalization
- Before certification stage 1 readiness sign-off
- Before management review (Clause 9.3 across frameworks)
- When evidence-collection effort has grown 50%+ year-over-year (a smell)
- When an audit produced > 15% critical findings

## The Six Compliance Officer Questions

### 1. Have you named every applicable framework?
**No framework selector run, no defensible scope.**
- Run `framework_selector.py` with company profile
- Forgetting a framework means rebuilding the audit program later
- Pay attention to industry-specific overlays (financial: NYDFS, FINMA; healthcare: HIPAA, ISO 13485; AI: ISO 42001 + EU AI Act)

### 2. Where do the frameworks overlap, and what's the reuse leverage?
**Single evidence -> N controls = the cornerstone of multi-framework efficiency.**
- Run `cross_framework_mapper.py` with enabled frameworks
- HIGH-confidence mappings: same evidence; MEDIUM: existing + overlay; LOW: new artefact
- Without overlap analysis, you'll collect the same access-review records 3 times

### 3. Who owns each artefact, and what's the reuse-leverage score?
**Joint ownership without accountability is the most common cause of stale evidence.**
- Run `evidence_pool_generator.py` for the artefact inventory
- HIGH-leverage artefacts (≥ 5 mappings) get built first
- Each artefact needs one accountable owner
- Stale evidence is an effective gap  even if the artefact existed historically

### 4. What's the audit calendar, and is auditor independence respected?
**Surveillance audits stacking in the same week is a smell.**
- Use per-framework audit-plan tools (aims_audit_scheduler, isms_audit_scheduler, audit_schedule_optimizer)
- Auditor cannot audit their own work (Clause 9.2 across all ISO standards)
- For small teams: rotate auditors + occasional external auditor

### 5. What does a mock audit produce, and is the severity distribution healthy?
**No mock audit, no readiness signal.**
- Run `audit_simulator.py` with framework + scope
- Healthy distribution: ≥ 40% observation, ≤ 15% critical
- All-critical findings = destructive audit OR genuinely failing program
- All-observation findings = audit too superficial

### 6. What's the management review cadence across frameworks?
**Each framework wants its own management review; an integrated review (per Annex SL) saves 5x exec time.**
- Schedule one quarterly cross-framework review covering all enabled frameworks' Clause 9.3 inputs
- Inputs: risk register changes, open nonconformities, audit findings, incidents, drift, KPIs
- Outputs: action items, resource decisions, scope adjustments

## Workflow

```bash
# 1. Framework selection
python ../../skills/compliance-os/scripts/framework_selector.py profile.json

# 2. Cross-framework overlap
python ../../skills/compliance-os/scripts/cross_framework_mapper.py program.json

# 3. Evidence pool consolidation
python ../../skills/compliance-os/scripts/evidence_pool_generator.py program.json

# 4. Mock audit (per framework)
python ../../skills/compliance-os/scripts/audit_simulator.py scope.json
```

## Output Format

```markdown
# Compliance Readiness: <program>
**Date:** YYYY-MM-DD

## The Decision Being Made
[framework-set | audit-calendar | certification-readiness | evidence-consolidation]

## Framework Set
- Applicable: <list>
- Binding (regulations): <count>
- Certifiable: <count>
- Missing dependencies: <list>

## Cross-Framework Overlap
- Total merged controls in scope: N
- High-leverage artefacts (≥ 5 mappings): M
- Top reuse opportunities: <top 5 artefacts>

## Evidence Pool
- Artefacts in catalog: N
- High-leverage count: M
- Stale evidence rate: X%
- Unowned artefacts: K

## Audit Calendar
- Frameworks scheduled this year: <list>
- Auditor independence respected: Y/N
- Conflicts: <list>

## Mock Audit Results (per framework)
- <framework>: total findings N, critical X%, observation Y%, healthy distribution: Y/N

## Verdict
🟢 READY | 🟡 STAGE-2-CANDIDATE | 🔴 NOT-READY

## Top 3 Actions
[3 concrete next steps with owners + dates]
```

## Routing

- `/cs:aims-audit`  for ISO 42001-specific forcing questions
- `/cs:ai-act-readiness`  for EU AI Act-specific forcing questions
- `/cs:ciso-review`  for cybersecurity strategy
- `/cs:caio-review`  for executive AI strategy
- `/cs:gc-review`  for novel-case legal review
- `/cs:decide`  to log the verdict
- `/cs:freeze 30`  on certification commitments (multi-year financial impact)

## Related

- Agent: [`cs-compliance-officer`](../../agents/cs-compliance-officer.md)
- Skill: [`compliance-os`](../compliance-os/SKILL.md)
- Adjacent: `ra-qm-team/skills/iso42001-specialist/`, `ra-qm-team/skills/eu-ai-act-specialist/`, `ra-qm-team/skills/information-security-manager-iso27001/`, `ra-qm-team/skills/soc2-compliance/`, `ra-qm-team/skills/gdpr-dsgvo-expert/`

---

**Version:** 1.0.0
