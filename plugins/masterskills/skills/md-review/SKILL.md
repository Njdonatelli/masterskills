---
name: md-review
description: >-
  C—o—n—v—e—r—t—s— —a— —m—a—r—k—d—o—w—n— —P—R— —w—r—i—t—e—u—p— —o—r— —c—o—d—e— —r—e—v—i—e—w— —(—o—n—e— —w—i—t—h— —`—`—`—d—i—f—f— —f—e—n—c—e—d— —b—l—o—c—k—s— —a—n—d— —s—e—v—e—r—i—t—y—-—t—a—g—g—e—d— —>— —[—!—B—L—O—C—K—E—R—]—/—[—!—M—A—J—O—R—]—/—[—!—M—I—N—O—R—]—/—[—!—N—I—T—]— —c—a—l—l—o—u—t—s—)— —i—n—t—o— —a— —s—i—n—g—l—e—-—f—i—l—e— —2—-—c—o—l—u—m—n— —H—T—M—L— —r—e—v—i—e—w— ——— —u—n—i—f—i—e—d—-—d—i—f—f— —o—n— —t—h—e— —l—e—f—t—,— —s—e—v—e—r—i—t—y—-—t—a—g—g—e—d— —a—n—n—o—t—a—t—i—o—n— —c—a—r—d—s— —o—n— —t—h—e— —r—i—g—h—t—,— —t—o—p— —j—u—m—p—-—n—a—v— —l—i—s—t—i—n—g— —e—v—e—r—y— —f—i—n—d—i—n—g—,— —m—a—n—d—a—t—o—r—y— —n—a—m—e—d— —r—e—v—i—e—w—e—r— —f—o—o—t—e—r—.— —T—r—i—g—g—e—r—s— —w—h—e—n— —t—h—e— —m—a—r—k—d—o—w—n—-—h—t—m—l—-—o—r—c—h—e—s—t—r—a—t—o—r— —c—l—a—s—s—i—f—i—e—s— —a—n— —i—n—p—u—t— —a—s— —R—E—V—I—E—W—,— —o—r— —w—h—e—n— —i—n—v—o—k—e—d— —d—i—r—e—c—t—l—y— —v—i—a— —/—c—s—:—m—d—-—r—e—v—i—e—w—.— —R—e—f—u—s—e—s— —w—i—t—h—o—u—t— —e—x—p—l—i—c—i—t— —-—-—r—e—v—i—e—w—e—r— —(—a— —c—o—d—e— —r—e—v—i—e—w— —m—u—s—t— —n—a—m—e— —a— —h—u—m—a—n—)—,— —r—e—f—u—s—e—s— —i—f— —n—o— —d—i—f—f— —h—u—n—k—s— —p—r—e—s—e—n—t— —(—r—o—u—t—e— —t—o— —m—d—-—d—o—c—u—m—e—n—t— —i—n—s—t—e—a—d—)—,— —a—n—d— —r—e—f—u—s—e—s— —t—o— —e—n—c—o—d—e— —s—e—v—e—r—i—t—y— —i—n— —c—o—l—o—r— —o—n—l—y— —(—e—v—e—r—y— —b—a—d—g—e— —s—h—i—p—s— —c—o—l—o—r— —+— —i—c—o—n— —+— —a—r—i—a—-—l—a—b—e—l— —p—e—r— —W—C—A—G— —1—.—4—.—1—)—.— —U—s—e— —a—f—t—e—r— —o—r—c—h—e—s—t—r—a—t—o—r— —r—o—u—t—i—n—g.
version: 2.10.2
author: Alireza Rezvani
license: MIT
tags: [markdown, html, code-review, diff, severity, annotations, single-file, design-system, wcag-1.4.1]
compatible_tools: [claude-code, codex-cli, cursor, antigravity, opencode, gemini-cli]
---

# md-review — Code-review markdown → 2-column HTML

The code-review converter from Tier 2 of Shihipar's essay ("Code Review and PR Writeups"). Takes a markdown PR writeup with diff blocks + severity callouts and produces a single-file HTML review with a jump-nav, 2-column diff + annotation layout, and a named reviewer footer.

Three stdlib tools pipeline together:

```
diff_parser.py  →  annotation_extractor.py  →  review_html_renderer.py
   (md → diff hunks)   (md → severity-tagged    (hunks + annotations
                        annotations attached     + tokens → 2-col HTML)
                        to nearest hunk)
```

## When to invoke

| Symptom | Action |
|---|---|
| `markdown-html-orchestrator` routes input as REVIEW | Invoke this skill |
| User runs `/cs:md-review <path>.md` directly | Invoke this skill |
| Input contains ` ```diff ` fenced blocks + `> [!MAJOR]`/`> [!BLOCKER]`/etc. callouts | Invoke this skill |
| Input is a long-form spec / report (no diff blocks) | Route to `md-document` instead |
| Input is a slide deck | Route to `md-slides` instead |
| Input < 100 lines | Refuse (Shihipar threshold) |
| Design-system not onboarded | Refuse; surface `/cs:design-system` |

## Pipeline

```bash
# 1. Parse markdown → diff hunks JSON
python3 markdown-html/skills/md-review/scripts/diff_parser.py \
    --input <path>.md --output hunks.json

# 2. Extract severity-tagged annotations, attach to nearest preceding hunk
python3 markdown-html/skills/md-review/scripts/annotation_extractor.py \
    --input <path>.md --diff-blocks hunks.json --output annotations.json

# 3. Render 2-col HTML (--reviewer is mandatory — refuses without)
python3 markdown-html/skills/md-review/scripts/review_html_renderer.py \
    --diff-blocks hunks.json --annotations annotations.json \
    --reviewer "Jane Doe" --title "PR #123: Add retry logic" \
    --output review.html
```

## What gets rendered

- **Top jump-nav** — every annotation with severity badge + 80-char preview + jump link; severity counts in the heading ("3 BLOCKER · 2 MAJOR · 1 NIT")
- **2-column hunk rows** — unified diff on the left (per-line old/new line numbers, +/− marks, addition/deletion background tint from design-system tokens), annotation cards on the right (color + icon + aria-label per WCAG 1.4.1)
- **Approval bar** — if `LGTM` markers are present and no severity annotations, a success-tinted "LGTM — no findings flagged" bar
- **General comments** — annotations not attached to any hunk render at the bottom in their own section
- **Reviewer footer** — mandatory; refuses to render without `--reviewer`
- **Responsive** — 2-col collapses to stacked on viewports < 900px

## Hard rules

1. **`--reviewer` is mandatory.** A code review must name a human reviewer. Refuses with exit 3 otherwise. Mirrors research-ops's "named owner" discipline.
2. **Refuses if no hunks present.** No `--- a/file` + `@@ ... @@` blocks means this isn't a code review — refuses with exit 4 and recommends `md-document`.
3. **Refuses input < 100 lines.** Markdown wins below the threshold (Shihipar).
4. **Refuses without onboarding.** Same gate as every converter.
5. **Severity is never color-only.** Each badge ships color + icon + `aria-label` + text. WCAG 1.4.1 enforced at the renderer level.
6. **Single-file output.** All CSS inline. Only external is Google Fonts CSS. No Prism in md-review (diff coloring conflicts with syntax highlighting).
7. **Custom severity convention.** `--severity-convention "critical,important,suggestion,nit"` swaps tier names; position 0 is most severe. Default is BLOCKER / MAJOR / MINOR / NIT (Google Code Review Developer Guide).

## Forcing-question library (Matt Pocock grill discipline)

1. **Who is the named reviewer?** Recommended: the user signing off on the review. Canon: research-ops named-owner pattern; *SWE at Google* ch. 9.
2. **Which severity convention applies — default (BLOCKER/MAJOR/MINOR/NIT) or custom?** Recommended: default unless your team has a documented alternative. Canon: Google *Code Review Developer Guide*.
3. **Are annotations anchored to specific hunks, or are some general?** Recommended: anchor everything you can; general goes to the unanchored section. Canon: *SWE at Google* ch. 9 — "Comments must reference a specific line".
4. **What's the PR title for the `<title>` and header?** Recommended: the actual PR / commit title. Canon: docs-as-context-for-readers.
5. **Should `LGTM` markers ship as the approval bar?** Recommended: yes if there are no severity annotations; otherwise the findings take precedence.

## Distinct from

- **`md-document`** — that converter renders prose + tables + code + callouts. This one renders diff hunks + margin annotations.
- **`md-slides`** — that converter splits on `---` boundaries. This one is a single-page artifact.
- **GitHub PR comments** — those are a thread. This is a single-author snapshot artifact.

## Output artifact

`{default_output_dir}/review-{slug}.html` (path resolved by orchestrator's `output_path_resolver.py`; collision suffix `-2`, `-3`, … by default).

## References

- Shihipar — *Claude Code HTML output* (Medium, 2026), Tier 2 use case
- *Software Engineering at Google* (Manshreck & Wright, O'Reilly 2020), ch. 9 "Code Review"
- Google *Code Review Developer Guide* — severity convention source
- WCAG 2.2 §1.4.1 — color-not-sole-signal enforcement
- See `references/` for full citations (diff_rendering_canon, severity_coding, pr_annotation_ux)
