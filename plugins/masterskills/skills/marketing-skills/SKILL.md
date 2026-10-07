---
name: "marketing-skills"
description: >-
  D—i—r—e—c—t—o—r—y— —a—n—d— —r—o—u—t—e—r— —f—o—r— —t—h—e— —m—a—r—k—e—t—i—n—g— —s—k—i—l—l—s— —l—i—b—r—a—r—y—.— —U—s—e— —w—h—e—n— —y—o—u— —n—e—e—d— —t—o— —f—i—n—d— —t—h—e— —r—i—g—h—t— —m—a—r—k—e—t—i—n—g— —s—k—i—l—l— —f—o—r— —a— —t—a—s—k—,— —s—e—e— —w—h—a—t— —m—a—r—k—e—t—i—n—g— —c—a—p—a—b—i—l—i—t—i—e—s— —e—x—i—s—t—,— —o—r— —g—e—t— —o—r—i—e—n—t—e—d— —i—n— —t—h—i—s— —p—l—u—g—i—n—.— —4—4— —s—p—e—c—i—a—l—i—s—t— —s—k—i—l—l—s— —a—c—r—o—s—s— —8— —p—o—d—s— —(—c—o—n—t—e—n—t—,— —S—E—O— —+— —A—E—O—,— —C—R—O—,— —c—h—a—n—n—e—l—s—,— —g—r—o—w—t—h—,— —i—n—t—e—l—l—i—g—e—n—c—e—,— —s—a—l—e—s— —e—n—a—b—l—e—m—e—n—t—,— —o—p—s—)—,— —5—9— —s—t—d—l—i—b— —P—y—t—h—o—n— —t—o—o—l—s—.— —R—o—u—t—e—s— —t—o— —o—n—e— —s—k—i—l—l— ——— —i—t— —d—o—e—s— —n—o—t— —e—x—e—c—u—t—e— —m—a—r—k—e—t—i—n—g— —w—o—r—k— —i—t—s—e—l—f.
version: 2.10.3
author: Alireza Rezvani
license: MIT
tags:
  - marketing
  - router
  - index
agents:
  - claude-code
  - codex-cli
  - openclaw
---

# Marketing Skills — Directory + Router

This is the index skill for the marketing plugin. It does one job: route you to the right specialist skill, then get out of the way. For request-by-request routing logic, [../marketing-ops/SKILL.md](../marketing-ops/SKILL.md) is the canonical router — this file is the map.

**Counts (kept honest):** 44 specialist skills in `skills/` (plus this index and the deprecated `content-creator` redirect), 1 video skill in `video-content-strategist/`, 59 stdlib-only Python tools. No pip installs needed.

## Start Here

1. **First run ever?** Use `skills/marketing-context/` to create `.claude/product-marketing-context.md`. Every other skill reads it for brand voice, personas, and competitive landscape.
2. **Know your task?** Find it in the route table below and load only that skill's `SKILL.md`.
3. **Ambiguous request?** Load `skills/marketing-ops/` — its routing matrix maps phrasings to skills.

## Route Table

All paths are relative to `marketing-skill/`.

### Foundation + Ops
| Task | Skill |
|---|---|
| Capture brand/product context (run first) | `skills/marketing-context/` |
| Route a request, plan campaigns, pick channels | `skills/marketing-ops/` |
| Demand gen programs, funnel + CRM ops | `skills/marketing-demand-acquisition/` |
| Positioning, ICP, product marketing strategy | `skills/marketing-strategy-pmm/` |
| Brand voice/visual consistency audits | `skills/brand-guidelines/` |

### Content
| Task | Skill |
|---|---|
| Write blog posts, articles, guides | `skills/content-production/` |
| Plan what content to create | `skills/content-strategy/` |
| Edit copy (Seven Sweeps) | `skills/copy-editing/` |
| Fix AI-sounding content | `skills/content-humanizer/` |
| Landing/sales page copy | `skills/copywriting/` |
| Headlines, hooks, idea generation | `skills/marketing-ideas/` |
| Persuasion frameworks, mental models | `skills/marketing-psychology/` |

### SEO + AEO
| Task | Skill |
|---|---|
| Traditional SEO audit | `skills/seo-audit/` |
| AI search citations (ChatGPT, Perplexity, AI Overviews) | `skills/aeo/` |
| Programmatic SEO at scale | `skills/programmatic-seo/` |
| Structured data / schema.org | `skills/schema-markup/` |
| Site structure, internal linking | `skills/site-architecture/` |

### CRO (conversion)
| Task | Skill |
|---|---|
| Landing/marketing page conversion | `skills/page-cro/` |
| Forms | `skills/form-cro/` |
| Signup flow | `skills/signup-flow-cro/` |
| Onboarding/activation | `skills/onboarding-cro/` |
| Popups/modals | `skills/popup-cro/` |
| Paywall/upgrade screens | `skills/paywall-upgrade-cro/` |
| A/B test design + sample size | `skills/ab-test-setup/` |

### Channels
| Task | Skill |
|---|---|
| Email sequences/drips | `skills/email-sequence/` |
| Cold outbound email | `skills/cold-email/` |
| Paid ads (Google/Meta/LinkedIn) | `skills/paid-ads/` |
| Ad creative + copy | `skills/ad-creative/` |
| Social calendar + management | `skills/social-media-manager/` |
| Platform-native social posts | `skills/social-content/` |
| X/Twitter growth | `skills/x-twitter-growth/` |
| YouTube (data + strategy) | `skills/youtube-full/` |
| Video content strategy | `video-content-strategist/` (sibling folder, own plugin) |
| Webinars (funnel math) | `skills/webinar-marketing/` |
| App Store / Play Store (ASO) | `skills/app-store-optimization/` |

### Growth
| Task | Skill |
|---|---|
| Launches (PH, HN, etc.) | `skills/launch-strategy/` |
| Pricing + packaging | `skills/pricing-strategy/` |
| Referral programs | `skills/referral-program/` |
| Free tools as acquisition | `skills/free-tool-strategy/` |
| Churn prevention | `skills/churn-prevention/` |

### Intelligence + Sales Enablement
| Task | Skill |
|---|---|
| Campaign performance, attribution | `skills/campaign-analytics/` |
| Tracking plans, UTM, GA4 key events | `skills/analytics-tracking/` |
| Social account analysis | `skills/social-media-analyzer/` |
| Competitor/alternatives pages | `skills/competitor-alternatives/` |
| LLM prompt templates + governance for marketing teams | `skills/prompt-engineer-toolkit/` |

## Python Tools

Each skill documents its own tools in its SKILL.md (a "Tools" or workflow section with exact CLI lines). Invoke from the skill's folder:

```bash
python3 skills/<skill>/scripts/<tool>.py --help
```

All 59 scripts are stdlib-only; most run a demo with no args.

## Rules

- Load ONE specialist skill per task — never bulk-load.
- If `.claude/product-marketing-context.md` exists, read it before any marketing task.
- `content-creator` is deprecated — use `skills/content-production/`.
- Don't pip-install anything for these tools.
