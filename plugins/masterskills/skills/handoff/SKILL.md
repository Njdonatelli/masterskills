---
name: handoff
description: >-
  C—o—m—p—a—c—t— —t—h—e— —c—u—r—r—e—n—t— —c—o—n—v—e—r—s—a—t—i—o—n— —i—n—t—o— —a— —h—a—n—d—o—f—f— —d—o—c—u—m—e—n—t— —f—o—r— —a—n—o—t—h—e—r— —a—g—e—n—t— —t—o— —p—i—c—k— —u—p—.— —R—e—f—e—r—e—n—c—e—s— —e—x—i—s—t—i—n—g— —a—r—t—i—f—a—c—t—s— —(—P—R—D—s—,— —p—l—a—n—s—,— —A—D—R—s—,— —i—s—s—u—e—s—,— —c—o—m—m—i—t—s—,— —d—i—f—f—s—)— —b—y— —p—a—t—h— —o—r— —U—R—L— —i—n—s—t—e—a—d— —o—f— —d—u—p—l—i—c—a—t—i—n—g— —t—h—e—m—.— —U—s—e— —w—h—e—n— —u—s—e—r— —w—a—n—t—s— —t—o— —h—a—n—d— —o—f—f— —t—h—e— —c—o—n—v—e—r—s—a—t—i—o—n— —t—o— —a— —f—r—e—s—h— —a—g—e—n—t— —o—r— —s—t—a—r—t—s— —a— —n—e—w— —s—e—s—s—i—o—n— —t—h—a—t— —p—i—c—k—s— —u—p— —p—r—i—o—r— —w—o—r—k.
argument-hint: "What will the next session be used for?"
license: MIT
metadata:
  derived_from: "https://github.com/mattpocock/skills/tree/main/skills/productivity/handoff"
  original_author: "Matt Pocock (@mattpocock)"
  original_license: MIT
  voice: "Matt Pocock — no-duplication, reference-existing-artifacts, tailored to next-session focus"
  version: 1.0.0
---

# Handoff

> Derived from [Matt Pocock's handoff](https://github.com/mattpocock/skills/tree/main/skills/productivity/handoff) (MIT). Matt's no-duplication discipline preserved verbatim. Additions: tools + references + cs-* wrapper (see [references/companion_tooling.md](references/companion_tooling.md)).

Write a handoff document summarising the current conversation so a fresh agent can continue the work. Save it to a path produced by `mktemp -t handoff-XXXXXX.md` (read the file before you write to it).

Suggest the skills to be used, if any, by the next session.

Do not duplicate content already captured in other artifacts (PRDs, plans, ADRs, issues, commits, diffs). Reference them by path or URL instead.

If the user passed arguments, treat them as a description of what the next session will focus on and tailor the doc accordingly.

## Sections

- **Goal of next session** (from user argument or inferred)
- **State of play** (what's done, what's blocking)
- **Open decisions** (what the next agent must decide)
- **Skills to use** (concrete list)
- **Artifacts** (paths/URLs to PRDs, plans, ADRs, issues, branches, PRs — do not duplicate)

## Tooling

See [references/companion_tooling.md](references/companion_tooling.md). Tools: template + dedup + recommender. Agent: `cs-handoff-author`. Command: `/cs:handoff`.

---

**Version:** 1.0.0
**Derived:** Matt Pocock (MIT) + this repo's wrapper
