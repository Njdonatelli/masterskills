---
name: md-document
description: >-
  C—o—n—v—e—r—t—s— —l—o—n—g—-—f—o—r—m— —m—a—r—k—d—o—w—n— —(—s—p—e—c—s—,— —R—F—C—s—,— —r—e—p—o—r—t—s—,— —p—l—a—n—s—,— —e—x—p—l—a—i—n—e—r—s—)— —i—n—t—o— —a— —s—i—n—g—l—e—-—f—i—l—e—,— —l—i—g—h—t—l—y—-—i—n—t—e—r—a—c—t—i—v—e— —H—T—M—L— —d—o—c—u—m—e—n—t— —w—i—t—h— —s—t—i—c—k—y— —T—O—C—,— —s—c—r—o—l—l—s—p—y—,— —s—e—a—r—c—h— —f—i—l—t—e—r—,— —c—o—d—e—-—c—o—p—y— —b—u—t—t—o—n—s—,— —a—n—d— —d—e—s—i—g—n—-—s—y—s—t—e—m—-—d—r—i—v—e—n— —b—r—a—n—d— —t—o—k—e—n—s—.— —T—r—i—g—g—e—r—s— —w—h—e—n— —t—h—e— —m—a—r—k—d—o—w—n—-—h—t—m—l—-—o—r—c—h—e—s—t—r—a—t—o—r— —c—l—a—s—s—i—f—i—e—s— —a—n— —i—n—p—u—t— —a—s— —D—O—C—U—M—E—N—T—,— —o—r— —w—h—e—n— —i—n—v—o—k—e—d— —d—i—r—e—c—t—l—y— —v—i—a— —/—c—s—:—m—d—-—d—o—c—u—m—e—n—t—.— —R—e—a—d—s— —t—h—e— —d—e—s—i—g—n—-—s—y—s—t—e—m— —c—o—n—f—i—g— —v—i—a— —c—o—n—f—i—g—_—l—o—a—d—e—r—.—p—y— —a—n—d— —i—n—l—i—n—e—s— —t—h—e— —u—s—e—r—'—s— —1—2— —d—e—r—i—v—e—d— —C—S—S— —c—u—s—t—o—m— —p—r—o—p—e—r—t—i—e—s—;— —r—e—f—u—s—e—s— —t—o— —r—e—n—d—e—r— —i—f— —o—n—b—o—a—r—d—i—n—g— —h—a—s—n—'—t— —r—u—n—.— —S—i—n—g—l—e—-—f—i—l—e— —o—u—t—p—u—t— ——— —G—o—o—g—l—e— —F—o—n—t—s— —+— —P—r—i—s—m—.—j—s— —C—D—N— —a—r—e— —t—h—e— —o—n—l—y— —e—x—t—e—r—n—a—l—s—;— —n—o— —f—r—a—m—e—w—o—r—k— —r—u—n—t—i—m—e—,— —n—o— —b—u—i—l—d— —s—t—e—p—.— —U—s—e— —a—f—t—e—r— —o—r—c—h—e—s—t—r—a—t—o—r— —r—o—u—t—i—n—g— —o—r— —a—f—t—e—r— —d—e—s—i—g—n—-—s—y—s—t—e—m— —o—n—b—o—a—r—d—i—n—g— —i—s— —c—o—n—f—i—r—m—e—d.
version: 2.10.1
author: Alireza Rezvani
license: MIT
tags: [markdown, html, documentation, single-file, toc, scrollspy, search, code-copy, design-system]
compatible_tools: [claude-code, codex-cli, cursor, antigravity, opencode, gemini-cli]
---

# md-document — Long-form Markdown to HTML

The general-purpose converter — handles the 90% case Shihipar describes (specs, plans, RFCs, reports, explainers). Three stdlib tools pipeline together:

```
markdown_parser.py  →  html_renderer.py  →  interactivity_injector.py
   (md → JSON AST)    (AST + tokens → HTML)    (HTML + JS behavior)
```

Output is one `.html` file with sticky TOC, search filter, scrollspy, code-copy buttons, and the user's 12 derived brand tokens. Externals limited to Google Fonts CSS + Prism.js CDN.

## When to invoke

| Symptom | Action |
|---|---|
| `markdown-html-orchestrator` routes input as DOCUMENT | Invoke this skill |
| User runs `/cs:md-document <path>.md` directly | Invoke this skill |
| User says "convert this spec/report/RFC/plan to HTML" | Invoke this skill |
| Input is a code review (has ` ```diff ` blocks) | Route to `md-review` instead |
| Input is a slide deck (clear `---` boundaries) | Route to `md-slides` instead |
| Input is < 100 lines | Refuse (Shihipar threshold — markdown still wins) |
| Design-system not onboarded | Refuse, surface `/cs:design-system` |

## Pipeline

```bash
# 1. Parse markdown → JSON AST
python3 markdown-html/skills/md-document/scripts/markdown_parser.py \
    --input <path>.md --output sections.json

# 2. Render AST + design-system config → single-file HTML
python3 markdown-html/skills/md-document/scripts/html_renderer.py \
    --sections sections.json --output document.html

# 3. Inject lightweight JS (search, copycode, smoothscroll, scrollspy)
python3 markdown-html/skills/md-document/scripts/interactivity_injector.py \
    --file document.html \
    --features search,copycode,smoothscroll,scrollspy
```

Or all-in-one (sample render):

```bash
python3 markdown-html/skills/md-document/scripts/html_renderer.py --sample \
  | python3 markdown-html/skills/md-document/scripts/interactivity_injector.py \
      --file /dev/stdin --output document.html
```

## What gets rendered

CommonMark subset sufficient for agent-generated artifacts:
- Headings H1-H6 (every H2+ gets an anchor id and TOC entry)
- Paragraphs with inline **bold** / *italic* / `code` / [links](url) / ![images](url)
- Fenced code blocks (` ```python `) with Prism.js highlighting on demand
- GFM tables with per-column alignment
- GFM callouts (`> [!NOTE]`, `> [!TIP]`, `> [!IMPORTANT]`, `> [!WARNING]`, `> [!CAUTION]`)
- Blockquotes, ordered + unordered lists (single-level), horizontal rules

Out of scope: nested lists, HTML inlines, footnotes, definition lists, task list checkboxes (rendered as plain text), reference-style links.

## Hard rules

1. **Refuses input < 100 lines.** Markdown wins below the threshold (Shihipar).
2. **Refuses without onboarding.** `config_loader.setup_completed()` must return `True`. Otherwise surface `/cs:design-system`.
3. **Single-file output.** All CSS + JS inline. Only externals are `fonts.googleapis.com` and `cdn.jsdelivr.net` (Prism). Anything else is a regression.
4. **Customization must change behavior.** `design_style=editorial` produces 720px-wide layout with 1.75 line-height; `playful` rounds the callouts and adds shadow; `technical` is dense with 0.875rem code. Smoke-tested.
5. **WCAG-compliant tokens.** Inherits the design-system's WCAG AA palette — body text ≥ 4.5:1 contrast, links iteratively walked to 4.5:1.
6. **Idempotent injection.** Re-injecting interactivity is a no-op (marker check). Re-rendering with a different design_style works cleanly.

## Forcing-question library (Matt Pocock grill discipline)

1. **What's the document for — skim, decide, or deep-read?** Recommended: name it; density follows. Canon: Shihipar; Tufte *Envisioning Information*.
2. **Sticky-sidebar TOC or collapsible-top?** Recommended: sticky-sidebar for > 800 words / 4+ H2s; collapsible-top for shorter mobile-first docs. Canon: NN/g *TOC Best Practices* (2023).
3. **All four interactive features, or a subset?** Recommended: all four — none of them cost more than ~1 KB. Canon: Wattenberger *Why React isn't great for actually building websites*.
4. **Code theme — light, dark, or auto?** Recommended: auto (follows OS `prefers-color-scheme`). Canon: WCAG 2.2 §1.4.3.
5. **Does the document have a clear H1 title?** Recommended: yes — H1 becomes the page `<title>` and is excluded from the TOC.

## Distinct from

- **`md-review`** — that converter renders diff blocks + severity-tagged margin annotations. This one renders prose + tables + code + callouts.
- **`md-slides`** — that converter splits on `---` boundaries into slides. This one renders one continuous document.
- **`marketing/landing/`** — that generates landing pages from scratch (no markdown input). This converts existing markdown.

## Output artifact

`{default_output_dir}/doc-{slug}.html` (path resolved by orchestrator's `output_path_resolver.py`; collision suffix `-2`, `-3`, … by default).

## References

- Shihipar — *Claude Code HTML output* (Medium, 2026)
- Tufte — *Envisioning Information* (1990), ch. 2 "Micro/Macro Readings"
- NN/g — *Table of Contents Best Practices* (2023)
- WCAG 2.2 — §1.4.3 contrast, §2.4.5 multiple ways
- Wattenberger — *Why React isn't great for actually building websites*
- See `references/` for full citations
