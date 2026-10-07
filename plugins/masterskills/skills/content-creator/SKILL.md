---
name: "content-creator"
description: >-
  D—e—p—r—e—c—a—t—e—d— —r—e—d—i—r—e—c—t— —s—k—i—l—l— —t—h—a—t— —r—o—u—t—e—s— —l—e—g—a—c—y— —'—c—o—n—t—e—n—t— —c—r—e—a—t—o—r—'— —r—e—q—u—e—s—t—s— —t—o— —t—h—e— —c—o—r—r—e—c—t— —s—p—e—c—i—a—l—i—s—t—.— —U—s—e— —w—h—e—n— —a— —u—s—e—r— —i—n—v—o—k—e—s— —'—c—o—n—t—e—n—t— —c—r—e—a—t—o—r—'—,— —a—s—k—s— —t—o— —w—r—i—t—e— —a— —b—l—o—g— —p—o—s—t—,— —a—r—t—i—c—l—e—,— —g—u—i—d—e—,— —o—r— —b—r—a—n—d— —v—o—i—c—e— —a—n—a—l—y—s—i—s— —(—r—o—u—t—e—s— —t—o— —c—o—n—t—e—n—t—-—p—r—o—d—u—c—t—i—o—n—)—,— —o—r— —a—s—k—s— —t—o— —p—l—a—n— —c—o—n—t—e—n—t—,— —b—u—i—l—d— —a— —t—o—p—i—c— —c—l—u—s—t—e—r—,— —o—r— —c—r—e—a—t—e— —a— —c—o—n—t—e—n—t— —c—a—l—e—n—d—a—r— —(—r—o—u—t—e—s— —t—o— —c—o—n—t—e—n—t—-—s—t—r—a—t—e—g—y—)—.— —D—o—e—s— —n—o—t— —h—a—n—d—l—e— —r—e—q—u—e—s—t—s— —d—i—r—e—c—t—l—y— ——— —i—d—e—n—t—i—f—i—e—s— —u—s—e—r— —i—n—t—e—n—t— —a—n—d— —r—e—d—i—r—e—c—t—s— —t—o— —c—o—n—t—e—n—t—-—p—r—o—d—u—c—t—i—o—n— —f—o—r— —w—r—i—t—i—n—g—/—S—E—O—/—b—r—a—n—d—-—v—o—i—c—e— —t—a—s—k—s— —o—r— —c—o—n—t—e—n—t—-—s—t—r—a—t—e—g—y— —f—o—r— —p—l—a—n—n—i—n—g— —t—a—s—k—s.
license: MIT
metadata:
  version: 2.0.0
  author: Alireza Rezvani
  category: marketing
  updated: 2026-03-06
  status: deprecated
---

# Content Creator → Redirected

> **This skill has been split into two specialist skills.** Use the one that matches your intent:

| You want to... | Use this instead |
|----------------|-----------------|
| **Write** a blog post, article, or guide | [content-production](../content-production/) |
| **Plan** what content to create, topic clusters, calendar | [content-strategy](../content-strategy/) |
| **Analyze brand voice** | [content-production](../content-production/) (includes `brand_voice_analyzer.py`) |
| **Optimize SEO** for existing content | [content-production](../content-production/) (includes `seo_optimizer.py`) |
| **Create social media content** | [social-content](../social-content/) |

## Why the Change

The original `content-creator` tried to do everything: planning, writing, SEO, social, brand voice. That made it a jack of all trades. The specialist skills do each job better:

- **content-production** — Full pipeline: research → brief → draft → optimize → publish. Includes all Python tools from the original content-creator.
- **content-strategy** — Strategic planning: topic clusters, keyword research, content calendars, prioritization frameworks.

## Proactive Triggers

- **User asks "content creator"** → Route to content-production (most likely intent is writing).
- **User asks "content plan" or "what should I write"** → Route to content-strategy.

## Output Artifacts

| When you ask for... | Routed to... |
|---------------------|-------------|
| "Write a blog post" | content-production |
| "Content calendar" | content-strategy |
| "Brand voice analysis" | content-production (`brand_voice_analyzer.py`) |
| "SEO optimization" | content-production (`seo_optimizer.py`) |

## Communication

This is a redirect skill. Route the user to the correct specialist — don't attempt to handle the request here.

## Related Skills

- **content-production**: Full content execution pipeline (successor).
- **content-strategy**: Content planning and topic selection (successor).
- **content-humanizer**: Post-processing AI content to sound authentic.
- **marketing-context**: Foundation context that both successors read.
