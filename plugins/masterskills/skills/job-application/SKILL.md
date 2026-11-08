---
name: job-application
description: >-
  Screen one job posting against the owner's job-search rules, then draft truthful application materials if it passes. Use when the user pastes a job posting or link, or asks "should I apply", "do I qualify", "tailor my resume for this", "cover letter for this job", or "prep me for this interview".
---

# Job Application

Screen a job posting against the owner's rules first. Draft materials only for a posting that passes. Every claim in a draft must come from a supplied fact.

## Hard rules

1. **Read the full posting.** If you cannot read the duties and the requirements, put the posting in the "Unverified" list. Do not screen it from the title or a snippet.
2. **Check every required qualification.** Mark each one Met, Unmet, or Unconfirmed. Quote the fact that supports each Met.
3. **Apply only when every required qualification is Met.** If one is Unmet, the verdict is Skip. If one is Unconfirmed, the verdict is Confirm first, with one question for each open item.
4. **Never invent.** Do not add or estimate a tool, license, credential, title, date, number, team size, or outcome. A missing fact is a question, not a guess.
5. **Apply the owner's rules from `profile.md`.** These rules cover location, work mode, title, and employer. A posting that fails one rule is Skip, even when the qualifications are Met.
6. **The owner's decisions in `profile.md` override this file.**

## Process

### 1. Load the facts

Read `profile.md` in this skill folder. It holds the owner's career facts and job-search rules. It is private and it does not ship with the skill. If it does not exist, copy `profile.example.md` to `profile.md`. Fill it by interviewing the owner before you screen anything.

### 2. Screen

Return this table for each posting:

| Requirement (required or preferred) | Status | Evidence or question |
|---|---|---|

Then give:

- **Rule checks:** location and commute, work mode, title, employment type, and employer rules from `profile.md`. Give one line each, with Pass or Fail.
- **Verdict:** Apply, Confirm first, or Skip, with one sentence of reason.
- **Interview risks:** gaps and weak spots that an interviewer can ask about. Do not hide them from the owner.

Do not give a match percentage. The verdict comes from the rules, not from a score.

### 3. Draft (only after Apply, and only when the owner asks)

- **Resume:** reorder, reword, and emphasize facts from `profile.md` and the session. Use a keyword from the posting only when a supplied fact supports it. Keep every job title and date as the owner held it.
- **Cover letter:** one page. Three to four short paragraphs. Write an achievement without a number when no supplied fact gives one.
- **Interview prep:** likely questions from the duties and the risks in step 2. Build each STAR story only from supplied facts. If the facts do not give a Situation, Task, Action, or Result detail, ask for it. Give fewer stories rather than pad the set.
- **File format:** if the owner asks for a Word or PDF file, use the `docx` or `pdf` skill from the document-skills plugin.

### 4. Record

If `profile.md` names a tracker, give the owner one row for it: date, employer, title, link, verdict, and next step. Do not write to the tracker unless the owner asks.

## Not in scope

- Searching for postings. A scheduled task or the owner finds them. This skill screens what it receives.
- Salary negotiation and offer comparison.
