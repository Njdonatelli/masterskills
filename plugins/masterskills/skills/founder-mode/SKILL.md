---
name: "founder-mode"
description: >-
  /—c—s—:—f—o—u—n—d—e—r—-—m—o—d—e— —<—q—u—e—s—t—i—o—n—>— ——— —A—u—t—o—-—r—o—u—t—e—s— —a—n—y— —f—o—u—n—d—e—r— —q—u—e—s—t—i—o—n— —t—o— —t—h—e— —r—i—g—h—t— —C—-—r—o—l—e— —a—d—v—i—s—o—r— —o—r— —t—o— —/—c—s—:—b—o—a—r—d—r—o—o—m— —f—o—r— —m—u—l—t—i—-—r—o—l—e— —t—o—p—i—c—s—.— —T—h—e— —s—i—n—g—l—e—-—c—o—m—m—a—n—d— —e—n—t—r—y— —p—o—i—n—t—.— —U—s—e— —w—h—e—n— —a— —f—o—u—n—d—e—r— —a—s—k—s— —a—n—y— —s—t—r—a—t—e—g—i—c— —q—u—e—s—t—i—o—n— —w—i—t—h—o—u—t— —k—n—o—w—i—n—g— —w—h—i—c—h— —a—d—v—i—s—o—r— —o—r— —c—o—m—m—a—n—d— —f—i—t—s— ——— —e—.—g—.— —'—r—u—n—w—a—y— —p—r—e—s—s—u—r—e—'— —r—o—u—t—e—s— —t—o— —t—h—e— —C—F—O—,— —'—g—r—o—s—s— —r—e—t—e—n—t—i—o—n— —d—r—o—p—p—e—d—'— —r—o—u—t—e—s— —t—o— —t—h—e— —C—C—O.
---

# /cs:founder-mode — The Auto-Router

**Command:** `/cs:founder-mode <question>`

The single command a founder needs to remember. Routes the question to the right C-role automatically, or triggers `/cs:boardroom` if multi-role.

This is the **killer command** — the answer to "I don't know which slash command to use." Type the question; the system figures out the room.

## Routing Logic

The router (via `cs-chief-of-staff`) does keyword + intent matching:

| Signal in question | Route |
|---|---|
| burn, runway, fundraise, dilution, model, LTV, CAC | `cs-cfo-advisor` |
| pipeline, win rate, forecast, quota, ramp, sales motion | `cs-cro-advisor` |
| positioning, ICP, message, brand, channel, campaign | `cs-cmo-advisor` |
| roadmap, PMF, JTBD, North Star, RICE, kill | `cs-cpo-advisor` |
| cadence, OKR, scorecard, DRI, operating system, rhythm | `cs-coo-advisor` |
| hiring, comp, ladder, level, attrition, eNPS, equity | `cs-chro-advisor` |
| security, threat, breach, compliance, audit, SOC 2 | `cs-ciso-advisor` |
| architecture, scaling, tech debt, SLO, latency | `cs-cto-advisor` |
| contract, IP, term sheet, regulator, license | `cs-general-counsel-advisor` |
| retention, GRR, NRR, churn, customer success, CSM, time-to-value, renewals | `cs-cco-advisor` |
| training data, data rights, consent, data asset, warehouse, lakehouse, data mesh | `cs-cdo-advisor` |
| model selection, eval, hallucination, AI risk, EU AI Act, fine-tune, build vs buy AI | `cs-caio-advisor` |
| DORA, cycle time, deploy frequency, eng hiring funnel, team topology, delivery throughput | `cs-vpe-advisor` |
| strategy, vision, board, M&A, raise, exit | `cs-ceo-advisor` |
| **2+ signals from different roles** | `/cs:boardroom` |
| **ambiguous** | `/cs:office-hours` first, then route |

## Workflow

1. Parse the question for role signals
2. If exactly one role: invoke that cs-* agent directly
3. If 2+ roles: build a brief via `/cs:brief` and trigger `/cs:boardroom`
4. If ambiguous / no signal match: trigger `/cs:office-hours` to force the founder to sharpen
5. Log the routing decision (raw layer) via `decision-logger`

## Output

The router emits one of three responses:

### Single-role route
```
**Routing:** cs-cfo-advisor
**Why:** Question hits burn rate and unit economics.
**Next:** Invoking cs-cfo-advisor with company-context loaded.

[Advisor's response follows]
```

### Multi-role route
```
**Routing:** /cs:boardroom
**Why:** Question touches CFO + CMO + CPO (pricing change has finance, positioning, and product implications).
**Next:** Building brief via /cs:brief, then running boardroom.

Brief saved: ~/.claude/briefs/2026-05-12-pricing-v3.md
Run: /cs:boardroom ~/.claude/briefs/2026-05-12-pricing-v3.md
```

### Ambiguous → office hours
```
**Routing:** /cs:office-hours
**Why:** Question is too broad ("should we grow faster?"). Need framing before any advisor can help.
**Next:** Six-question intake.

[Office hours questions follow]
```

## Why This Is the Killer Command

gstack requires the founder to know all 23 slash commands and pick the right one. That's a cognitive tax. `/cs:founder-mode` collapses that to one — the system picks. This is also where persistent memory pays off: with company-context.md + decision-logger, the router knows what's already been decided and won't re-litigate.

## Examples

```
/cs:founder-mode "should we raise a Series B now or wait 6 months?"
   → boardroom (CFO + CEO + CRO touched)

/cs:founder-mode "the win rate dropped 20% this month"
   → cs-cro-advisor

/cs:founder-mode "gross retention dropped 5 points this quarter"
   → cs-cco-advisor

/cs:founder-mode "let's hire a VP Marketing"
   → boardroom (CHRO + CMO + CFO touched)

/cs:founder-mode "should we be growing faster?"
   → /cs:office-hours (too ambiguous)
```

## Related

- Agent: [`cs-chief-of-staff`](../../agents/cs-chief-of-staff.md) — does the routing
- Skill: [`chief-of-staff`](../../../skills/chief-of-staff/SKILL.md) — routing logic
- Skill: [`context-engine`](../../../skills/context-engine/SKILL.md) — loads context

---

**Version:** 1.0.0
