---
name: "chief-ai-officer-advisor"
description: >-
  Chief AI Officer advisory for startups: model build-vs-buy decisions (API vs fine-tune vs in-house), AI risk classification under EU AI Act + US state patchwork, AI cost economics (API-to-self-hosted breakeven), and AI team org evolution. Use when deciding whether to call an API or fine-tune, classifying AI use cases for regulatory risk, calculating when self-hosting pays off, sequencing AI hires, or when user mentions CAIO, AI strategy, model selection, foundation model, fine-tuning, EU AI Act, NIST AI RMF, AI governance, model risk, or AI economics. Strategic only  does not duplicate engineering AI/ML skills. [Also supersedes `caio-review`: triggers on '/cs:caio-review', 'caio review', 'AI governance interrogation']
license: MIT
metadata:
  version: 1.0.0
  author: Alireza Rezvani
  category: c-level
  domain: chief-ai-officer-leadership
  updated: 2026-05-12
  python-tools: model_buildvsbuy_calculator.py, ai_risk_classifier.py, ai_cost_economics.py
  frameworks: model-buildvsbuy, ai-risk-governance, ai-economics, ai-team-org
---

# Chief AI Officer Advisor

Strategic AI leadership for startup CAIOs and founders without one. **Four decisions, no AI hype:**

1. **Should we use an API, fine-tune, or build our own?**  model build-vs-buy with 3-year TCO
2. **Is this AI use case high-risk under regulation, and how do we govern it?**  EU AI Act + NIST AI RMF + US state patchwork
3. **When do we switch from API to self-hosted, and at what cost?**  token economics with breakeven analysis
4. **What AI role do we hire next?**  stage-to-role map (AI engineer ≠ ML engineer ≠ research scientist)

This skill does **not** cover tactical AI/ML engineering. For RAG implementation, agent design, prompt engineering, eval infrastructure, model deployment, or cost optimization, see `engineering/rag-architect/`, `engineering/agent-designer/`, `engineering/prompt-governance/`, `engineering/self-eval/`, `engineering/llm-cost-optimizer/`.

## Keywords

CAIO, chief AI officer, AI strategy, model selection, foundation model, fine-tuning, RLHF, DPO, LoRA, QLoRA, build vs buy, AI build-vs-buy, model risk tier, EU AI Act, AI Act Article 6, Article 9, Article 10, Annex III, prohibited AI, high-risk AI, NIST AI RMF, AI risk management framework, NYC Local Law 144, Colorado SB 21-169, Illinois HB 53, model card, eval set, eval harness, hallucination rate, jailbreak risk, prompt injection, AI red team, AI safety, alignment, model lifecycle, model registry, API-to-self-hosted breakeven, GPU economics, A100, H100, inference cost, fine-tuning cost, AI team, AI engineer, ML engineer, research scientist, MLOps, AI platform

## Quick Start

```bash
# Decision A: API vs fine-tune vs build
python scripts/model_buildvsbuy_calculator.py                          # embedded customer-support sample
python scripts/model_buildvsbuy_calculator.py path/to/use_case.json

# Decision B: Risk classification under EU AI Act + US state laws
python scripts/ai_risk_classifier.py                                   # embedded hiring-AI sample
python scripts/ai_risk_classifier.py path/to/use_case.json

# Decision C: API vs self-hosted economics
python scripts/ai_cost_economics.py                                    # embedded 5M tokens/day sample
python scripts/ai_cost_economics.py path/to/workload.json
```

## Key Questions (ask these first)

- **What does this AI need to be good at, and how would you measure it?** (If no eval set, no ship.)
- **What's the SLO on hallucination / error rate?** (Without one, "AI quality" is a vibe.)
- **What happens when the model is wrong?** (Fallback behavior, human-in-the-loop, blast radius.)
- **What's the risk tier under EU AI Act, and is conformity assessment required?** (Determines product launch timeline.)
- **At what monthly token volume does self-hosting beat API?** (Almost never below 100M tokens/month at frontier quality.)
- **Are we hiring an AI engineer or an ML research scientist?** (Different jobs; founders confuse them.)

## Core Responsibilities

### 1. Model Build-vs-Buy

The decision is not "use AI or not"  it's **API vs fine-tune vs in-house** for each use case. Each path has a different TCO curve, latency profile, and capability ceiling.

**Default path: API (frontier model)**
- Use when: well-served by frontier (Claude, GPT, Gemini), QPS < 100, latency budget > 1s, cost < $50K/month
- Why: frontier APIs are 10-100x more capable than what most teams can fine-tune in-house
- Failure mode: API rate limits at scale, vendor lock-in, capability drift between model versions

**Fine-tune a smaller model**
- Use when: domain-specific behavior the API can't be prompted into (medical coding, legal redlining), high volume reducing API cost, latency budget < 500ms, specific style/format consistency required
- Approaches: full fine-tune (rare), LoRA/QLoRA (common), RLHF/DPO (when alignment matters)
- Failure mode: fine-tuned model lags frontier capability within 6-12 months; ongoing retraining cost

**Build from scratch / pre-train**
- Use when: almost never. You're a foundation-model company, OR you have a unique data corpus, $50M+ funding, and 18+ month patience.
- Failure mode: by the time you ship, frontier models have caught up and your sunk cost is unrecoverable

**Run** `model_buildvsbuy_calculator.py` for a use-case-specific recommendation with 3-year TCO. See `references/model_buildvsbuy_strategy.md` for full decision tree.

### 2. AI Risk Classification & Governance

The 2026 question every founder is facing: **does this AI use case trigger high-risk regulatory obligations?**

**EU AI Act (in force 2026) tiers:**

| Tier | Examples | Obligations |
|---|---|---|
| **Prohibited** | Social scoring, real-time biometric surveillance, manipulative AI | Cannot deploy in EU |
| **High-risk** | Employment screening, credit scoring, education access, critical infrastructure, law enforcement, biometric ID | Conformity assessment, registration, post-market monitoring, transparency, human oversight |
| **Limited-risk** | Chatbots, deepfakes, emotion recognition | Transparency: user must know they're interacting with AI |
| **Minimal-risk** | Recommendation systems, spam filters, most B2B SaaS internals | No specific obligations |

**Run** `ai_risk_classifier.py` to classify a use case and get the required-controls list.

**US state patchwork (non-exhaustive):**

- NYC LL 144  Automated Employment Decision Tools (AEDTs) require annual bias audit + candidate notice
- Colorado AI Act / SB 21-169  AI in consumer decisions (credit, insurance, employment, housing)
- Illinois HB 53  AI in interview/hiring
- California SB 1001  Bot disclosure
- Texas TCPA  Biometric identifier capture
- Federal NIST AI RMF  voluntary; increasingly referenced in contracts

**Industry-specific overlays:**

- Healthcare: FDA AI/ML guidance (2023), MDR (EU) for medical-device AI, 510(k) pathway for AI/ML-enabled medical devices
- Financial: NYDFS Reg 23, FTC Section 5, ECOA for credit decisions
- Insurance: NAIC model bulletin, state insurance commissioner rules

See `references/ai_risk_governance.md` for the full regulatory landscape + governance program checklist.

### 3. AI Cost Economics

**The breakeven question:** at what monthly token volume does self-hosted inference beat API costs?

**Key components:**

- **API cost**  variable, per-token. Frontier models 2026: Claude Sonnet 4.6 ~$3/$15 per M tokens (input/output), GPT-4o ~$2.50/$10, Gemini 2.5 ~$1.25/$5
- **Self-hosted cost**  fixed (GPU commitment) + variable (electricity). H100 spot ~$2-5/hour, A100 spot ~$1-3/hour. Llama 3.1 70B / Qwen 2.5 72B: ~$0.50-2.00 per million output tokens at 70% utilization
- **Hidden costs of self-hosting**  ops on-call, monitoring, model updates, scaling overhead, idle time penalty
- **Hidden costs of API**  rate limits requiring multi-vendor failover, vendor lock-in, capability drift between versions, data residency

**Typical breakeven (frontier-quality):** 100M–500M tokens/month, depending on model size and acceptable quality tradeoff. Below this, API wins. Above this, run the calculator.

**Run** `ai_cost_economics.py` with workload characteristics for a breakeven point + sensitivity to GPU rates and model size.

See `references/ai_cost_economics.md` for the full economics model and operational considerations.

### 4. AI Team Org Evolution

**The wrong question:** "Should we hire an ML engineer or a research scientist?"
**The right question:** "What's the next AI capability we need to ship, and what role unblocks that?"

Stage-to-role map:

| Stage | First AI hire | Then | Then |
|---|---|---|---|
| Pre-PMF | Founder + 1 ML-curious engineer playing with prompts |  |  |
| Series A | **AI engineer** (applied, full-stack; owns prompts/evals/deployment) | Second AI engineer for evals/quality |  |
| Series B | AI/ML platform engineer (inference, evals, observability) | Third AI engineer for production reliability | Data scientist if model is core IP |
| Series C | Manager of AI | ML research scientist (only if model IS the product) | AI safety / red team (if customer-facing AI) |
| Late-stage | Head of AI → CAIO | Multiple research scientists, platform team, safety/red team | Federated AI leads per business unit |

**Critical distinctions:**

- **AI engineer** ≠ **ML engineer** ≠ **research scientist**
  - AI engineer: full-stack + prompts + evals + deployment. Most startups need this, not the others.
  - ML engineer: production deployment, monitoring, retraining infrastructure. Hire after data engineer.
  - Research scientist: model invention, novel architectures. Only at Series C+ if model is core IP.

**Centralize-vs-embed for AI:** AI starts centralized (one team) and stays there longer than data team, because the surface area is smaller. Embed only when AI is being deployed in 4+ product surfaces.

See `references/ai_team_org_evolution.md`.

## Workflows

### Workflow 1: Model Selection Decision (1 hour)
**Goal:** Decide whether a specific use case should use API, fine-tune, or build.

```bash
# 1. Define use_case.json (volume, latency, accuracy, team size, budget)
python scripts/model_buildvsbuy_calculator.py use_case.json
# 2. Review 3-year TCO + breakeven
# 3. Cross-check with cs-cfo-advisor on budget commitment
# 4. Cross-check with cs-cto-advisor on engineering capacity (esp. for fine-tune)
# 5. Log via /cs:decide; consider /cs:freeze 60 on multi-year vendor commitment
```

### Workflow 2: AI Risk Classification (2-4 hours)
**Goal:** Classify a use case under EU AI Act + US state laws, identify required controls.

```bash
# 1. Define use_case.json (decisions affected, users, geography, sector)
python scripts/ai_risk_classifier.py use_case.json
# 2. For HIGH-RISK: budget conformity assessment + registration
# 3. For LIMITED-RISK: implement transparency requirements
# 4. Cross-check with cs-general-counsel-advisor on contractual implications
# 5. Cross-check with cs-ciso-advisor on technical safeguards
# 6. Log via /cs:decide
```

### Workflow 3: API-to-Self-Hosted Breakeven (1 day)
**Goal:** Decide when (and whether) to migrate from API to self-hosted inference.

```bash
# 1. Build workload.json (tokens/day, model size, latency, quality tolerance)
python scripts/ai_cost_economics.py workload.json
# 2. Run sensitivity scenarios (low/mid/high GPU rates)
# 3. Estimate migration cost (engineering time + risk)
# 4. Cross-check with cs-cfo-advisor on capex commitment
# 5. Cross-check with cs-cto-advisor on platform readiness
# 6. Log via /cs:decide; pair with /cs:freeze if signing GPU commitment
```

### Workflow 4: AI Team Roadmap (1 week)
**Goal:** Sequence next 18 months of AI hires aligned to capabilities to ship.

1. List top 5 AI capabilities the product needs in 12 months
2. Map each capability to the role that ships it (see `ai_team_org_evolution.md`)
3. Sequence hires (one role at a time, ramp before next)
4. Cross-check with cs-chro-advisor on comp + leveling
5. Identify the centralize-vs-embed trigger

## Output Standards

```
**Bottom Line:** [one sentence  decision and rationale]
**The Decision:** [one of: model selection | risk classification | economics | next hire]
**The Evidence:** [numbers from the tool, not adjectives]
**How to Act:** [3 concrete next steps]
**Your Decision:** [the call only the founder can make]
```

## Adjacent Skills

- `c-level-advisor/skills/chief-data-officer-advisor/`  Training data rights, data product strategy (chains directly to model decisions)
- `c-level-advisor/skills/cto-advisor/`  Architecture capacity, scaling cliffs (esp. for self-hosted inference)
- `c-level-advisor/skills/ciso-advisor/`  Threat modeling for AI (prompt injection, jailbreak, training data poisoning)
- `c-level-advisor/skills/general-counsel-advisor/`  AI contracts (vendor liability, output ownership, training-data licensing)
- `c-level-advisor/skills/cfo-advisor/`  Build-vs-buy TCO math, multi-year vendor commitments
- `c-level-advisor/skills/chro-advisor/`  AI team hiring + comp
- `engineering/skills/rag-architect/`  Tactical RAG implementation
- `engineering/skills/agent-designer/`  Tactical agent architecture
- `engineering/prompt-governance/`  Tactical prompt management
- `engineering/skills/self-eval/`  Tactical eval infrastructure
- `engineering/llm-cost-optimizer/`  Tactical inference cost optimization

## References

- [model_buildvsbuy_strategy.md](references/model_buildvsbuy_strategy.md)  Full decision tree + 3-year TCO components + when each path fails
- [ai_risk_governance.md](references/ai_risk_governance.md)  EU AI Act + NIST AI RMF + US state patchwork + industry overlays + governance program
- [ai_cost_economics.md](references/ai_cost_economics.md)  API pricing 2026 + GPU rental economics + utilization realities + migration cost
- [ai_team_org_evolution.md](references/ai_team_org_evolution.md)  Stage-to-role map + role definitions (AI engineer ≠ ML engineer ≠ scientist) + anti-patterns

---

**Version:** 1.0.0
**Status:** Production Ready
**Disclaimer:** AI regulation is evolving rapidly. This skill surfaces decisions and tradeoffs as of 2026 but cannot replace qualified AI counsel for binding compliance decisions, especially under EU AI Act conformity assessments.

---

## Consolidated Capabilities: CAIO-REVIEW (Subsumed & Superceded)

# /cs:caio-review  CAIO Forcing Questions

**Command:** `/cs:caio-review <plan>`

The eval-demanding CAIO pressure-tests any plan that involves AI. Six questions before any AI feature ships, any multi-year vendor commitment, or any AI team expansion.

## When to Run

- Before shipping any new AI-powered feature
- Before signing a multi-year AI vendor contract (API or self-hosted infra)
- Before EU launch of any AI feature
- Before a major AI team hire (especially ML engineer or research scientist)
- Before a fine-tuning project commitment
- Before adopting AI in a regulated domain (employment, credit, healthcare, education, etc.)
- When the founder uses the word "AI" near "competitive advantage" or "moat"

## The Six CAIO Questions

### 1. What does this AI need to be good at, and how would you measure it?
**No eval set = no ship.** Before any AI feature deploys, define the eval criteria.
- 50-100 representative inputs minimum
- Expected outputs OR rubric for grading
- Edge cases: ambiguous, adversarial, format-edge
- If you can't write down what "good" looks like, you don't have a feature; you have a vibe.

### 2. What's the SLO on hallucination / error rate, and what's the fallback?
**Every AI feature has a failure mode. Plan for it.**
- Quantified SLO: "<5% hallucination on factual queries"
- Detection mechanism: monitoring, sampling, customer feedback loop
- Fallback: human-in-loop review, lower-risk default response, refuse-to-answer
- Blast radius if SLO breached: how many users affected, what is the cost?

### 3. What's the risk tier under EU AI Act, and is conformity assessment required?
**Run `ai_risk_classifier.py` if any EU residents are affected OR domain is regulated.**
- PROHIBITED → cannot launch in EU; re-scope
- HIGH → conformity assessment + EU DB registration + 10 Articles of obligations (3-12 months, $50-200K)
- LIMITED → transparency obligations (chatbot disclosure, AI-generated content marking)
- MINIMAL → no specific obligations; NIST AI RMF voluntary

### 4. API, fine-tune, or build?
**Run `model_buildvsbuy_calculator.py` for the specific use case.**
- 80% of B2B SaaS use cases: API
- 15%: fine-tune (when domain-specific behavior + labeled data + ML team + high volume)
- <1%: build from scratch
- Decision must consider economic breakeven AND practical feasibility (data, team, compliance)

### 5. What's the 12-month cost trajectory at expected scale?
**Run `ai_cost_economics.py` for the workload.**
- API: variable, scales linearly
- Self-hosted: mostly fixed, breakeven typically 1-10B tokens/month for 70B-class
- Hidden costs of self-hosted: ops, monitoring, model updates, capacity, failover, security
- Hidden costs of API: vendor lock-in, capability drift, rate limits, data residency
- Prompt caching is the most underrated lever; check provider support

### 6. What role unblocks this  and have we hired prerequisites first?
**Map AI capability to specific role. Founders confuse AI engineer / ML engineer / research scientist.**
- AI engineer: applied + full-stack + prompts + evals + deployment (most startups need this)
- ML engineer: fine-tuning + retraining infra (only after platform engineer + labeled data)
- Research scientist: model invention (only if model IS the product)
- Don't hire research scientist as first AI hire  they need infrastructure to be productive

## Workflow

```bash
# 1. Model selection check
python ../../../skills/chief-ai-officer-advisor/scripts/model_buildvsbuy_calculator.py use_case.json

# 2. Regulatory classification
python ../../../skills/chief-ai-officer-advisor/scripts/ai_risk_classifier.py use_case.json

# 3. Cost projection
python ../../../skills/chief-ai-officer-advisor/scripts/ai_cost_economics.py workload.json
```

## Output Format

```markdown
# CAIO Review: <plan>
**Date:** YYYY-MM-DD

## The Decision Being Made
[one sentence  which CAIO decision: model selection | risk classification | economics | next hire]

## Eval Discipline
- Eval set committed: yes/no
- SLO defined: <metric> < <threshold>
- Fallback behavior: <one line>

## Model Selection (if applicable)
- Recommended: API / FINE_TUNE / BUILD
- 3-year TCO: $X (chosen path) vs $Y (alternatives)
- Breakeven: <volume>

## Risk Classification (if applicable)
- EU AI Act tier: PROHIBITED / HIGH / LIMITED / MINIMAL
- Conformity assessment required: yes/no
- US state triggers: [list]
- Required controls open: N

## Cost Economics (if applicable)
- Monthly cost at current volume: $X
- Breakeven for self-hosted migration: <volume>
- Migration cost if applicable: $X (3-6 months)

## Org (if applicable)
- Next hire: <role>
- Why this, not the alternative: <one line>
- Prerequisite hires in place: yes/no

## Verdict
🟢 SHIP | 🟡 SHARPEN | 🔴 BLOCK

## Next Steps
[3 concrete actions]
```

## Routing

- `/cs:cdo-review`  for any training-data implications
- `/cs:gc-review`  for AI vendor contracts, output liability, training-data licensing
- `/cs:ciso-review`  for prompt injection / jailbreak / training-data poisoning threat model
- `/cs:cfo-review`  for multi-year vendor or GPU commitment TCO
- `cs-chro-advisor` agent  for AI team hires (comp, ladder, leveling)
- `/cs:decide`  log the verdict
- `/cs:freeze 60`  on multi-year AI commitments

## Related

- Agent: [`cs-caio-advisor`](../../agents/cs-caio-advisor.md)
- Skill: [`chief-ai-officer-advisor`](../../../skills/chief-ai-officer-advisor/SKILL.md)
- Adjacent: `../../../skills/chief-data-officer-advisor/` (training data rights, data strategy)

---

**Version:** 1.0.0
