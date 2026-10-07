---
name: team-communications
description: >-
  W—r—i—t—e— —i—n—t—e—r—n—a—l— —c—o—m—p—a—n—y— —c—o—m—m—u—n—i—c—a—t—i—o—n—s— ——— —3—P— —u—p—d—a—t—e—s— —(—P—r—o—g—r—e—s—s—/—P—l—a—n—s—/—P—r—o—b—l—e—m—s—)—,— —c—o—m—p—a—n—y—-—w—i—d—e— —n—e—w—s—l—e—t—t—e—r—s—,— —F—A—Q— —r—o—u—n—d—u—p—s—,— —i—n—c—i—d—e—n—t— —r—e—p—o—r—t—s—,— —l—e—a—d—e—r—s—h—i—p— —u—p—d—a—t—e—s—,— —s—t—a—t—u—s— —r—e—p—o—r—t—s—,— —p—r—o—j—e—c—t— —u—p—d—a—t—e—s—,— —a—n—d— —g—e—n—e—r—a—l— —i—n—t—e—r—n—a—l— —c—o—m—m—s—.— —U—s—e— —t—h—i—s— —s—k—i—l—l— —a—n—y— —t—i—m—e— —t—h—e— —u—s—e—r— —a—s—k—s— —t—o— —d—r—a—f—t—,— —e—d—i—t—,— —o—r— —f—o—r—m—a—t— —s—o—m—e—t—h—i—n—g— —m—e—a—n—t— —f—o—r— —i—n—t—e—r—n—a—l— —a—u—d—i—e—n—c—e—s—.— —T—r—i—g—g—e—r— —o—n— —k—e—y—w—o—r—d—s— —l—i—k—e— —"—3—P—"—,— —"—w—e—e—k—l—y— —u—p—d—a—t—e—"—,— —"—n—e—w—s—l—e—t—t—e—r—"—,— —"—F—A—Q—"—,— —"—i—n—t—e—r—n—a—l— —c—o—m—m—s—"—,— —"—s—t—a—t—u—s— —r—e—p—o—r—t—"—,— —"—c—o—m—p—a—n—y— —u—p—d—a—t—e—"—,— —"—t—e—a—m— —u—p—d—a—t—e—"—,— —"—i—n—c—i—d—e—n—t— —r—e—p—o—r—t—"—,— —o—r— —a—n—y— —r—e—q—u—e—s—t— —t—o— —s—u—m—m—a—r—i—z—e— —w—o—r—k— —f—o—r— —l—e—a—d—e—r—s—h—i—p—,— —t—e—a—m—m—a—t—e—s—,— —o—r— —t—h—e— —b—r—o—a—d—e—r— —c—o—m—p—a—n—y—.— —E—v—e—n— —c—a—s—u—a—l— —r—e—q—u—e—s—t—s— —l—i—k—e— —"—w—r—i—t—e— —m—y— —u—p—d—a—t—e—"— —o—r— —"—s—u—m—m—a—r—i—z—e— —w—h—a—t— —m—y— —t—e—a—m— —d—i—d— —t—h—i—s— —w—e—e—k—"— —s—h—o—u—l—d— —t—r—i—g—g—e—r— —t—h—i—s— —s—k—i—l—l.
---

# Internal Comms

> Originally contributed by [maximcoding](https://github.com/maximcoding) — enhanced and integrated by the claude-skills team.

Write polished internal communications by loading the right reference file, gathering context, and outputting in the company's exact format.

## Routing

Identify the communication type from the user's request, then read the matching reference file before writing anything:

| Type | Trigger phrases | Reference file |
|---|---|---|
| **3P Update** | "3P", "progress plans problems", "weekly team update", "what did we ship" | `references/3p-updates.md` |
| **Newsletter** | "newsletter", "company update", "weekly/monthly roundup", "all-hands summary" | `references/company-newsletter.md` |
| **FAQ** | "FAQ", "common questions", "what people are asking", "confusion around" | `references/faq-answers.md` |
| **General** | anything internal that doesn't match above | `references/general-comms.md` |

If the type is ambiguous, ask one clarifying question — don't guess.

## Workflow

1. **Read the reference file** for the matched type. Follow its formatting exactly.
2. **Gather inputs.** Use available MCP tools (Slack, Gmail, Google Drive, Calendar) to pull real data. If no tools are connected, ask the user to provide bullet points or raw context.
3. **Clarify scope.** Confirm: team name (for 3Ps), time period, audience, and any specific items the user wants included or excluded.
4. **Draft.** Follow the format, tone, and length constraints from the reference file precisely. Do not invent a new format.
5. **Present the draft** and ask if anything needs to be added, removed, or reworded.

## Tone & Style (applies to all types)

- Use "we" — you are part of the company.
- Active voice, present tense for progress, future tense for plans.
- Concise. Every sentence should carry information. Cut filler.
- Include metrics and links wherever possible.
- Professional but approachable — not corporate-speak.
- Put the most important information first.

## When tools are unavailable

If the user hasn't connected Slack, Gmail, Drive, or Calendar, don't stall. Ask them to paste or describe what they want covered. You're formatting and sharpening — that's still valuable. Mention which tools would improve future drafts so they can connect them later.

---

## Anti-Patterns

| Anti-Pattern | Why It Fails | Better Approach |
|---|---|---|
| Writing updates without reading the reference template first | Output won't match company format — user has to reformat | Always load the matching reference file before drafting |
| Inventing metrics or accomplishments | Internal comms must be factual — fabrication destroys trust | Only include data the user provided or MCP tools retrieved |
| Using passive voice for accomplishments | "The feature was shipped" hides who did the work | "Team X shipped the feature" — active voice credits the team |
| Writing walls of text for status updates | Leadership scans, doesn't read — key info gets buried | Lead with the headline, follow with 3-5 bullet points |
| Sending without confirming audience | A team update reads differently from a company-wide newsletter | Always confirm: who will read this? |

---

## Related Skills

| Skill | Relationship |
|-------|-------------|
| `project-management/senior-pm` | Broader PM scope — status reports feed into PM reporting |
| `project-management/meeting-analyzer` | Meeting insights can feed into 3P updates and status reports |
| `project-management/confluence-expert` | Publish comms as Confluence pages for permanent record |
| `marketing-skill/content-production` | External comms — use for public-facing content, not internal |
