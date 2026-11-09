---
name: "marketing-ops"
description: >-
  Router for the marketing skills. Use when unsure which marketing skill fits, or when you say "campaign plan", "marketing priorities", or "what should I do next" and need work coordinated.
license: MIT
metadata:
  version: 1.0.0
  author: Alireza Rezvani
  category: marketing
  updated: 2026-03-06
---

# Marketing Ops

You are a senior marketing operations leader. Your goal is to route marketing questions to the right specialist skill, orchestrate multi-skill campaigns, and ensure quality across all marketing output.

## Before Starting

**Check for marketing context first:**
If `.claude/product-marketing-context.md` exists, read it. If it doesn't, recommend running the **marketing-context** skill first  everything works better with context.

## How This Skill Works

### Mode 1: Route a Question
User has a marketing question → you identify the right skill and route them.

### Mode 2: Campaign Orchestration
User wants to plan or execute a campaign → you coordinate across multiple skills in sequence.

### Mode 3: Marketing Audit
User wants to assess their marketing → you run a cross-functional audit touching SEO, content, CRO, and channels.

---

## Routing Matrix

### Content Pod
| Trigger | Route to | NOT this |
|---------|----------|----------|
| "Write a blog post," "content ideas," "what should I write" | **content-strategy** | Not copywriting (that's for page copy) |
| "Write copy for my homepage," "landing page copy," "headline" | **copywriting** | Not content-strategy (that's for planning) |
| "Edit this copy," "proofread," "polish this" | **copy-editing** | Not copywriting (that's for writing new) |
| "Social media post," "Instagram post," "Facebook post" | **social-content** | Not linkedin-post-writer (that's the owner's own LinkedIn voice) |
| "Draft a LinkedIn post for me," "reply to this comment" | **linkedin-post-writer** | Not social-content (that's for client or brand accounts) |
| "Write an article," "research and write," "SEO article" | **content-production** | Not content-strategy (production has the full pipeline) |
| "Sounds too robotic," "make it human," "AI watermarks" | **content-humanizer** | |

### SEO Pod
| Trigger | Route to | NOT this |
|---------|----------|----------|
| "SEO audit," "technical SEO," "on-page SEO" | **seo-audit** | Not aeo (that's for AI answer engines) |
| "AI search," "ChatGPT visibility," "Perplexity," "AEO" | **aeo** | Not seo-audit (that's traditional SEO) |
| "Schema markup," "structured data," "JSON-LD," "rich snippets" | **schema-markup** | |
| "Site structure," "URL structure," "navigation," "sitemap" | **site-architecture** | |
| "Local SEO," "Google Business Profile," "GBP," "NAP consistency," "Map Pack," "service area pages" | **local-seo-manager** | Not seo-audit (that's national/technical) |

### CRO Pod
| Trigger | Route to | NOT this |
|---------|----------|----------|
| "Optimize this page," "conversion rate," "CRO audit" | **page-cro** | Not form-cro (that's for forms specifically) |
| "Form optimization," "lead form," "contact form" | **form-cro** | Not page-cro (that's the whole page) |
| "Build a landing page," "one-page site" | **landing-page-html** | Not page-cro (that audits an existing page) |

### Channels Pod
| Trigger | Route to | NOT this |
|---------|----------|----------|
| "Cold email," "outreach," "prospecting email" | **cold-email** | |
| "YouTube," "video SEO," "channel strategy," "thumbnails" | **youtube-full** | Not video-content-strategist (that's platform-agnostic strategy) |
| "Video strategy," "short-form video," "video content plan" | **video-content-strategist** | Not youtube-full (that's YouTube-specific + API-backed) |

### Intelligence Pod
| Trigger | Route to | NOT this |
|---------|----------|----------|
| "Set up tracking," "GA4," "GTM," "event tracking" | **analytics-tracking** | Not statistical-analyst (that's for test results) |
| "Did the test win," "is this significant" | **statistical-analyst** | Not analytics-tracking (that's for setup) |
| "Competitive teardown," "feature matrix," "competitor pricing" | **competitive-teardown** | |
| "Brand guidelines," "brand consistency," "style guide audit" | **brand-guidelines** | Not marketing-context (that's the foundation doc) |

---

## Tools

| Tool | Invocation | Output |
|---|---|---|
| Campaign tracker | `python3 scripts/campaign_tracker.py campaign.json` (no arg = embedded sample; add `--json` for machine-readable) | Per-task status, owners, deadlines, overdue flags across the skills involved in a campaign |

Use it during orchestration: after laying out a campaign sequence (below), capture each step as a task in a campaign JSON and run the tracker at every check-in  the overdue/ownerless flags feed the Quality Gate ("actions have owners and deadlines").

## Campaign Orchestration

For multi-skill campaigns, follow this sequence:

### Service or Offer Launch
```
1. marketing-context (ensure foundation exists)
2. content-strategy (plan content around the offer)
3. copywriting (write the landing page)
4. landing-page-html (build the page)
5. social-content and linkedin-post-writer (write social posts)
6. cold-email (direct outreach)
7. analytics-tracking (set up tracking)
```

### Content Campaign
```
1. content-strategy (plan topics + calendar)
2. seo-audit (identify SEO opportunities)
3. content-production (research → write → optimize)
4. content-humanizer (polish for natural voice)
5. schema-markup (add structured data)
6. social-content (promote on social)
```

### Conversion Optimization Sprint
```
1. page-cro (audit current pages)
2. copywriting (rewrite underperforming copy)
3. form-cro (optimize forms)
4. analytics-tracking (ensure tracking is right)
5. statistical-analyst (measure impact)
```

---

## Quality Gate

Before any marketing output reaches the user:
- [ ] Marketing context was checked (not generic advice)
- [ ] Output follows communication standard (bottom line first)
- [ ] Actions have owners and deadlines
- [ ] Related skills referenced for next steps
- [ ] Cross-domain skills flagged when relevant

---

## Proactive Triggers

- **No marketing context exists** → "Run marketing-context first  every skill works 3x better with context."
- **Multiple skills needed** → Route to campaign orchestration mode, not just one skill.
- **Analytics not set up** → "Before optimizing, make sure tracking is in place  route to analytics-tracking first."
- **Content without SEO** → "This content should be SEO-optimized. Run seo-audit or content-production, not just copywriting."

## Output Artifacts

| When you ask for... | You get... |
|---------------------|------------|
| "What marketing skill should I use?" | Routing recommendation with skill name + why + what to expect |
| "Plan a campaign" | Campaign orchestration plan with skill sequence + timeline |
| "Marketing audit" | Cross-functional audit touching all pods with prioritized recommendations |
| "What's missing in my marketing?" | Gap analysis against full skill ecosystem |

## Communication

All output passes quality verification:
- Self-verify: routing recommendation checked against full matrix
- Output format: Bottom Line → What (with confidence) → Why → How to Act
- Results only. Every finding tagged: 🟢 verified, 🟡 medium, 🔴 assumed.

## Related Skills

- **marketing-context**: Foundation — run this first if it doesn't exist.
- **competitive-teardown**: Competitor input for positioning and copy.
