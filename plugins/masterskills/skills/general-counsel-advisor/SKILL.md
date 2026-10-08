---
name: "general-counsel-advisor"
description: >-
  General Counsel advisory for startups: contract review (MSA, SaaS, NDA, DPA, employment), IP strategy, term sheet decoding, and regulatory landscape mapping. Use when reviewing any contract or term sheet, deciding when to engage outside counsel, defining IP strategy, evaluating regulatory exposure (HIPAA, GDPR, FDA, fintech), or when user mentions general counsel, GC, legal review, contract risk, term sheet, IP assignment, or regulatory exposure. NOT a substitute for licensed counsel  surfaces questions to bring to qualified attorneys. [Also supersedes `gc-review`: triggers on '/cs:gc-review', 'gc review', 'legal plan interrogation']
license: MIT
metadata:
  version: 1.0.0
  author: Alireza Rezvani
  category: c-level
  domain: general-counsel-leadership
  updated: 2026-05-12
  python-tools: contract_risk_scanner.py, term_sheet_analyzer.py
  frameworks: contract-review, ip-strategy, term-sheet-decoding, regulatory-mapping
---

# General Counsel Advisor

Strategic legal frameworks for startup General Counsels and founders without one. Contract risk, IP strategy, term sheet decoding, regulatory landscape.

This is **not legal advice**. It surfaces the right questions to bring to qualified outside counsel and catches the obvious traps before they reach a signature. Treat every output as a starting point for a conversation with a licensed attorney, not as a substitute for one.

## Keywords

general counsel, GC, legal review, contract review, MSA, SaaS agreement, NDA, DPA, employment agreement, contractor agreement, IP assignment, invention assignment, open source license, OSS compliance, term sheet, liquidation preference, anti-dilution, option pool, vesting, acceleration, drag-along, pro-rata, board composition, regulatory, HIPAA, GDPR, CCPA, FDA, MDR, fintech, BSA/AML, money transmitter, AI Act, indemnity, liability cap, force majeure, auto-renewal, choice of law, venue, non-compete, non-solicit

## Quick Start

```bash
# Scan a contract for risky clauses (uses bundled sample if no path given)
python scripts/contract_risk_scanner.py
python scripts/contract_risk_scanner.py path/to/contract.txt

# Analyze a term sheet for founder-friendliness
python scripts/term_sheet_analyzer.py
python scripts/term_sheet_analyzer.py path/to/term_sheet.json
```

## Key Questions (ask these first)

- **Who owns the IP being created or shared?** (Founders forget that contractors don't auto-assign IP without a written clause.)
- **What's the liability cap, and what's carved out?** (Standard: 12 months of fees, with carve-outs for IP infringement, data breach, willful misconduct.)
- **Is there a DPA in place if any personal data flows?** (GDPR, CCPA, state laws  non-negotiable if EU/CA data is touched.)
- **What's the termination right, notice period, and auto-renewal trap?** (5-year auto-renew with 60-day notice is a common founder mistake.)
- **Does this contract or product launch trigger a new regulatory regime?** (Healthcare → HIPAA. Fintech → BSA/AML. Medical device → FDA/MDR.)
- **For term sheets: liquidation preference, pre-money option pool, anti-dilution flavor?** (Three places where 5% of founder economics can quietly disappear.)

## Core Responsibilities

### 1. Contract Review

Standard contracts a startup signs in its first 5 years:

- **Vendor MSA**  Master Service Agreement (cloud, tooling, services)
- **Customer SaaS Agreement**  your standard customer paper + customer redlines
- **NDA**  mutual + one-way, with carve-outs for residuals + independent development
- **DPA**  Data Processing Agreement (required when personal data flows)
- **Employment Agreement**  offer letter, IP assignment, non-compete (where enforceable), arbitration
- **Contractor / 1099 Agreement**  IP assignment is critical; misclassification risk
- **Equity Agreements**  option grants, RSU agreements, advisor grants (FAST template, YC SAFE for advisors)

**Run** `contract_risk_scanner.py` on the text. It flags the 12 most common founder-killer clauses.

### 2. IP Strategy

- **Invention assignment**  every employee and contractor signs one. No exceptions.
- **Open source license compliance**  track every OSS dependency's license; AGPL and GPL trigger copyleft obligations.
- **Trade secrets**  define what's protected and how (clean room dev, access controls, NDAs).
- **Patents**  file provisional within 12 months of disclosure; PCT for international.
- **Trademarks**  register the word mark first, design mark second; clear before launch.
- **Copyright**  automatic on creation, but register for statutory damages eligibility.

See `references/ip_and_regulatory.md`.

### 3. Term Sheet Decoding

When a term sheet arrives, the difference between a founder-friendly and founder-hostile sheet often hides in three clauses:

- **Liquidation preference**  1x non-participating is standard; 1x participating or 2x is hostile
- **Pre-money vs post-money option pool**  pre-money pool dilutes founders; post-money dilutes everyone proportionally
- **Anti-dilution**  broad-based weighted average is standard; full ratchet is hostile

**Run** `term_sheet_analyzer.py` to get a 0-100 founder-friendliness score with flags.

### 4. Regulatory Landscape

When to engage outside counsel **before** committing:

| Trigger | Regime | First Step |
|---|---|---|
| Healthcare data | HIPAA, HITECH, state breach laws | Specialist health-tech counsel |
| Cardholder data | PCI DSS (industry standard, not law, but contractually required) | QSA + counsel |
| Money movement | BSA/AML, state money-transmitter (50-state patchwork) | Fintech specialist |
| Medical device claims | FDA 510(k) / De Novo / PMA, MDR (EU), ISO 13485 | Medical-device specialist |
| EU residents' personal data | GDPR + EU AI Act if AI is deployed | EU privacy counsel |
| California residents | CCPA / CPRA | Privacy generalist |
| Securities (tokens, equity crowdfunding) | SEC rules (Reg D, Reg A+, Reg CF) | Securities counsel |
| Defense / aerospace customers | ITAR, EAR, DFARS, CMMC | Export-control counsel |
| AI in EU | EU AI Act (risk-tiered) | EU privacy + product counsel |
| AI for hiring (NYC, CO, IL) | Local bias-audit laws | Employment counsel |

See `references/ip_and_regulatory.md` for sequencing.

## Workflows

### Workflow 1: Contract Review
1. Save the contract as plain text
2. Run `contract_risk_scanner.py path/to/contract.txt`
3. For each HIGH risk finding, draft a counter-proposal
4. Bring the redline + counter-proposals to outside counsel
5. Log the decision via `/cs:decide`

### Workflow 2: Term Sheet Response
1. Save the term sheet as a JSON file matching the schema in `term_sheet_analyzer.py --help`
2. Run `python scripts/term_sheet_analyzer.py path/to/term_sheet.json`
3. Review the founder-friendliness score and per-clause flags
4. Negotiate the worst 3 clauses (don't try to win all 20)
5. Always have a securities/venture attorney review before signing
6. Log via `/cs:decide` with `/cs:freeze 30` to prevent regret-driven re-opening

### Workflow 3: IP Hygiene Audit
1. Confirm every employee and contractor (past 12 months) signed invention assignment
2. Run an OSS license inventory (`pip-licenses`, `license-checker` for npm)
3. Map AGPL/GPL dependencies and confirm compliance (or remove)
4. File provisional patents on novel inventions (12-month deadline from disclosure)
5. Register word-mark trademarks for the product name

### Workflow 4: Regulatory Trigger Assessment
1. List planned product features for the next 12 months
2. Map each feature to the trigger table in this document
3. For any HIPAA / FDA / fintech trigger, engage a specialist counsel **before** building
4. Document the regulatory roadmap and budget alongside the product roadmap
5. Pair with `cs-ciso-advisor` for ISO 27001 / SOC 2 sequencing

## Output Standard (when invoked via `/cs:gc-review`)

```
**Bottom Line:** [sign / negotiate / do not sign]
**The Risks:** [3 highest-severity issues]
**Counter-Proposals:** [specific language]
**Outside Counsel Action Items:** [what to bring to the attorney]
**Your Decision:** [the call only the founder can make]
```

## Adjacent Skills

- `c-level-advisor/skills/ciso-advisor/`  Compliance overlap (SOC 2, ISO 27001, HIPAA technical safeguards)
- `c-level-advisor/skills/cfo-advisor/`  Term sheet → dilution math
- `c-level-advisor/skills/ma-playbook/`  Acquisition agreements, integration playbooks
- `ra-qm-team/`  ISO 13485, MDR, FDA 510(k), GDPR execution
- `c-level-advisor/c-level-agents/skills/gc-review/SKILL.md`  `/cs:gc-review` slash command

## References

- [contracts_playbook.md](references/contracts_playbook.md)  Standard contracts, clause checklist, common founder traps
- [ip_and_regulatory.md](references/ip_and_regulatory.md)  IP protection + regulatory landscape mapping
- [term_sheet_decoder.md](references/term_sheet_decoder.md)  Term sheet glossary + founder-friendly defaults + pushback strategies

---

**Version:** 1.0.0
**Status:** Production Ready
**Disclaimer:** Not legal advice. Always engage qualified counsel for binding decisions.

---

## Consolidated Capabilities: GC-REVIEW (Subsumed & Superceded)

# /cs:gc-review  General Counsel Forcing Questions

**Command:** `/cs:gc-review <plan>`

The General Counsel lens. Six questions before any contract, term sheet, IP move, or regulatory commitment. This is a lane gstack has zero of  and one where a single missed clause costs more than a year of engineering.

> ⚠️ **Not legal advice.** This command surfaces the right questions to ask before talking to outside counsel. Always engage qualified counsel for binding decisions.

## When to Run

- Before signing any contract > $100K or > 1 year
- Before issuing equity (employee grants, advisor grants)
- Before a term sheet response
- Before entering a regulated market (healthcare, fintech, defense)
- Before any open-source license decision in core IP
- Before an M&A LOI

## The Six GC Questions

### 1. IP Ownership
**Who owns the IP being created or shared in this transaction?**
- Work-for-hire vs license vs joint.
- For employees and contractors: written IP assignment in place?
- For OSS: license compatibility checked?

### 2. Liability & Indemnity
**What's the liability cap, and what's carved out from it?**
- Standard cap: 12 months of fees.
- Carve-outs: IP infringement, data breach, willful misconduct.
- Mutual indemnity desirable.

### 3. Data Processing
**What personal data is involved, and is a DPA in place?**
- GDPR / CCPA scope?
- Subprocessor flow-down?
- Data residency requirements?

### 4. Termination & Renewal
**What's the termination right, what's the notice period, and what's auto-renew?**
- Termination for convenience vs cause.
- Notice period (30 / 60 / 90 days).
- Auto-renewal trap?

### 5. Regulatory Surface
**Does this expose the company to a new regulatory regime?**
- Healthcare → HIPAA.
- Fintech → BSA/AML, state money-transmitter.
- Medical device → FDA, MDR, ISO 13485.
- Data → GDPR, CCPA, state breach laws.

### 6. Employment / Equity
**If this is a hire or contractor: jurisdiction, classification, equity grant, IP assignment?**
- Misclassification risk?
- Equity vesting standard (4-year, 1-year cliff)?
- Acceleration triggers?
- 409A current?

## Workflow

1. Read the contract / term sheet end to end
2. Run the six questions
3. Identify the top-3 issues that need outside counsel review
4. Apply the verdict

## Output Format

```markdown
# GC Review: <plan>
**Date:** YYYY-MM-DD

## Document
- Type: <contract / term sheet / grant / DPA>
- Counterparty: <name>
- $ value or scope: <amount>

## Issues
| # | Issue | Risk | Recommendation |
|---|---|---|---|
| 1 | <e.g., uncapped IP indemnity> | HIGH | Cap at fees paid, mutual |
| 2 | <e.g., 5-year auto-renew> | MED | 1-year max, 60-day notice |
| 3 | <e.g., no DPA, EU data> | HIGH | Require DPA before sign |

## Regulatory Trigger
- New regime triggered? <yes/no>
- Specific frameworks: <HIPAA / GDPR / etc.>

## Outside Counsel Action Items
- [ ] <specific item 1>
- [ ] <specific item 2>
- [ ] <specific item 3>

## Verdict
🟢 SIGN AS-IS (rare)
🟡 NEGOTIATE  counter on top-3 issues
🔴 DO NOT SIGN  material risk
```

## Routing

- `/cs:ciso-review`  for any data-touching contract
- `/cs:cfo-review`  for any commitment > 1 year or > 1% of revenue
- `/cs:decide`  log the verdict after outside counsel review

## Workflow Integration with `general-counsel-advisor` skill

Since v2.5.1, this command is backed by a full skill at `../../../skills/general-counsel-advisor/` with two Python tools:

```bash
# Automated contract scan (12 founder-killer patterns)
python ../../../skills/general-counsel-advisor/scripts/contract_risk_scanner.py path/to/contract.txt

# Term sheet scoring (0-100 founder-friendliness)
python ../../../skills/general-counsel-advisor/scripts/term_sheet_analyzer.py path/to/term_sheet.json
```

The `cs-general-counsel-advisor` agent orchestrates both tools plus 3 references (contracts playbook, IP + regulatory, term sheet decoder).

## Related

- Skill: [`general-counsel-advisor`](../../../skills/general-counsel-advisor/SKILL.md)  full skill with Python tools + references
- Agent: [`cs-general-counsel-advisor`](../../agents/cs-general-counsel-advisor.md)
- Compliance execution: `../../../../ra-qm-team/`
- Adjacent: `../../../skills/ma-playbook/`

---

**Version:** 1.0.0
