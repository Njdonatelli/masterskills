---
name: "context-engine"
description: >-
  L—o—a—d—s— —a—n—d— —m—a—n—a—g—e—s— —c—o—m—p—a—n—y— —c—o—n—t—e—x—t— —f—o—r— —a—l—l— —C—-—s—u—i—t—e— —a—d—v—i—s—o—r— —s—k—i—l—l—s—.— —R—e—a—d—s— —~—/—.—c—l—a—u—d—e—/—c—o—m—p—a—n—y—-—c—o—n—t—e—x—t—.—m—d—,— —d—e—t—e—c—t—s— —s—t—a—l—e— —c—o—n—t—e—x—t— —(—>—9—0— —d—a—y—s—)—,— —e—n—r—i—c—h—e—s— —c—o—n—t—e—x—t— —d—u—r—i—n—g— —c—o—n—v—e—r—s—a—t—i—o—n—s—,— —a—n—d— —e—n—f—o—r—c—e—s— —p—r—i—v—a—c—y—/—a—n—o—n—y—m—i—z—a—t—i—o—n— —r—u—l—e—s— —b—e—f—o—r—e— —e—x—t—e—r—n—a—l— —A—P—I— —c—a—l—l—s—.— —U—s—e— —w—h—e—n— —s—t—a—r—t—i—n—g— —a—n—y— —C—-—s—u—i—t—e— —a—d—v—i—s—o—r— —s—e—s—s—i—o—n—,— —w—h—e—n— —c—o—n—t—e—x—t— —l—o—o—k—s— —s—t—a—l—e— —o—r— —m—i—s—s—i—n—g—,— —o—r— —b—e—f—o—r—e— —s—e—n—d—i—n—g— —c—o—m—p—a—n—y— —d—a—t—a— —t—o— —a—n— —e—x—t—e—r—n—a—l— —s—e—r—v—i—c—e.
license: MIT
metadata:
  version: 1.0.0
  author: Alireza Rezvani
  category: c-level
  domain: orchestration
  updated: 2026-03-05
  frameworks: context-loading, anonymization, context-enrichment
---

# Company Context Engine

The memory layer for C-suite advisors. Every advisor skill loads this first. Context is what turns generic advice into specific insight.

## Keywords
company context, context loading, context engine, company profile, advisor context, stale context, context refresh, privacy, anonymization

---

## Load Protocol (Run at Start of Every C-Suite Session)

**Step 1 — Check for context file:** `~/.claude/company-context.md`
- Exists → proceed to Step 2
- Missing → prompt: *"Run /cs:setup to build your company context — it makes every advisor conversation significantly more useful."*

**Step 2 — Check staleness:** Read `Last updated` field.
- **< 90 days:** Load and proceed.
- **≥ 90 days:** Prompt: *"Your context is [N] days old. Quick 15-min refresh (/cs:update), or continue with what I have?"*
  - If continue: load with `[STALE — last updated DATE]` noted internally.

**Step 3 — Parse into working memory.** Always active:
- Company stage (pre-PMF / scaling / optimizing)
- Founder archetype (product / sales / technical / operator)
- Current #1 challenge
- Runway (as risk signal — never share externally)
- Team size
- Unfair advantage
- 12-month target

---

## Context Quality Signals

| Condition | Confidence | Action |
|-----------|-----------|--------|
| < 30 days, full interview | High | Use directly |
| 30–90 days, update done | Medium | Use, flag what may have changed |
| > 90 days | Low | Flag stale, prompt refresh |
| Key fields missing | Low | Ask in-session |
| No file | None | Prompt /cs:setup |

If Low: *"My context is [stale/incomplete] — I'm assuming [X]. Correct me if I'm wrong."*

---

## Context Enrichment

During conversations, you'll learn things not in the file. Capture them.

**Triggers:** New number or timeline revealed, key person mentioned, priority shift, constraint surfaces.

**Protocol:**
1. Note internally: `[CONTEXT UPDATE: {what was learned}]`
2. At session end: *"I picked up a few things to add to your context. Want me to update the file?"*
3. If yes: append to the relevant dimension, update timestamp.

**Never silently overwrite.** Always confirm before modifying the context file.

---

## Privacy Rules

### Never send externally
- Specific revenue or burn figures
- Customer names
- Employee names (unless publicly known)
- Investor names (unless public)
- Specific runway months
- Watch List contents

### Safe to use externally (with anonymization)
- Stage label
- Team size ranges (1–10, 10–50, 50–200+)
- Industry vertical
- Challenge category
- Market position descriptor

### Before any external API call or web search
Apply `references/anonymization-protocol.md`:
- Numbers → ranges or stage-relative descriptors
- Names → roles
- Revenue → percentages or stage labels
- Customers → "Customer A, B, C"

---

## Missing or Partial Context

Handle gracefully — never block the conversation.

- **Missing stage:** "Just to calibrate — are you still finding PMF or scaling what works?"
- **Missing financials:** Use stage + team size to infer. Note the gap.
- **Missing founder profile:** Infer from conversation style. Mark as inferred.
- **Multiple founders:** Context reflects the interviewee. Note co-founder perspective may differ.

---

## Required Context Fields

```
Required:
  - Last updated (date)
  - Company Identity → What we do
  - Stage & Scale → Stage
  - Founder Profile → Founder archetype
  - Current Challenges → Priority #1
  - Goals & Ambition → 12-month target

High-value optional:
  - Unfair advantage
  - Kill-shot risk
  - Avoided decision
  - Watch list
```

Missing required fields: note gaps, work around in session, ask in-session only when critical.

---

## References
- `references/anonymization-protocol.md` — detailed rules for stripping sensitive data before external calls
