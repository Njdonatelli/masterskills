---
name: "competitive-teardown"
description: >-
  A—n—a—l—y—z—e—s— —c—o—m—p—e—t—i—t—o—r— —p—r—o—d—u—c—t—s— —a—n—d— —c—o—m—p—a—n—i—e—s— —b—y— —s—y—n—t—h—e—s—i—z—i—n—g— —d—a—t—a— —f—r—o—m— —p—r—i—c—i—n—g— —p—a—g—e—s—,— —a—p—p— —s—t—o—r—e— —r—e—v—i—e—w—s—,— —j—o—b— —p—o—s—t—i—n—g—s—,— —S—E—O— —s—i—g—n—a—l—s—,— —a—n—d— —s—o—c—i—a—l— —m—e—d—i—a— —i—n—t—o— —s—t—r—u—c—t—u—r—e—d— —c—o—m—p—e—t—i—t—i—v—e— —i—n—t—e—l—l—i—g—e—n—c—e—.— —P—r—o—d—u—c—e—s— —f—e—a—t—u—r—e— —c—o—m—p—a—r—i—s—o—n— —m—a—t—r—i—c—e—s— —s—c—o—r—e—d— —a—c—r—o—s—s— —1—2— —d—i—m—e—n—s—i—o—n—s—,— —S—W—O—T— —a—n—a—l—y—s—e—s—,— —p—o—s—i—t—i—o—n—i—n—g— —m—a—p—s—,— —U—X— —a—u—d—i—t—s—,— —p—r—i—c—i—n—g— —m—o—d—e—l— —b—r—e—a—k—d—o—w—n—s—,— —a—c—t—i—o—n— —i—t—e—m— —r—o—a—d—m—a—p—s—,— —a—n—d— —s—t—a—k—e—h—o—l—d—e—r— —p—r—e—s—e—n—t—a—t—i—o—n— —t—e—m—p—l—a—t—e—s—.— —U—s—e— —w—h—e—n— —c—o—n—d—u—c—t—i—n—g— —c—o—m—p—e—t—i—t—o—r— —a—n—a—l—y—s—i—s—,— —c—o—m—p—a—r—i—n—g— —p—r—o—d—u—c—t—s— —a—g—a—i—n—s—t— —c—o—m—p—e—t—i—t—o—r—s—,— —r—e—s—e—a—r—c—h—i—n—g— —t—h—e— —c—o—m—p—e—t—i—t—i—v—e— —l—a—n—d—s—c—a—p—e—,— —b—u—i—l—d—i—n—g— —b—a—t—t—l—e— —c—a—r—d—s— —f—o—r— —s—a—l—e—s—,— —p—r—e—p—a—r—i—n—g— —f—o—r— —a— —p—r—o—d—u—c—t— —s—t—r—a—t—e—g—y— —o—r— —r—o—a—d—m—a—p— —s—e—s—s—i—o—n—,— —r—e—s—p—o—n—d—i—n—g— —t—o— —a— —c—o—m—p—e—t—i—t—o—r—'—s— —n—e—w— —f—e—a—t—u—r—e— —o—r— —p—r—i—c—i—n—g— —c—h—a—n—g—e—,— —o—r— —p—e—r—f—o—r—m—i—n—g— —a— —q—u—a—r—t—e—r—l—y— —c—o—m—p—e—t—i—t—i—v—e— —r—e—v—i—e—w.
---

# Competitive Teardown

**Tier:** POWERFUL  
**Category:** Product Team  
**Domain:** Competitive Intelligence, Product Strategy, Market Analysis

---

## When to Use

- Before a product strategy or roadmap session
- When a competitor launches a major feature or pricing change
- Quarterly competitive review
- Before a sales pitch where you need battle card data
- When entering a new market segment

---

## Teardown Workflow

Follow these steps in sequence to produce a complete teardown:

1. **Define competitors** — List 2–4 competitors to analyze. Confirm which is the primary focus.
2. **Collect data** — Use `references/data-collection-guide.md` to gather raw signals from at least 3 sources per competitor (website, reviews, job postings, SEO, social).  
   _Validation checkpoint: Before proceeding, confirm you have pricing data, at least 20 reviews, and job posting counts for each competitor._
3. **Score using rubric** — Apply the 12-dimension rubric below to produce a numeric scorecard for each competitor and your own product.  
   _Validation checkpoint: Every dimension should have a score and at least one supporting evidence note._
4. **Generate outputs** — Populate the templates in `references/analysis-templates.md` (Feature Matrix, Pricing Analysis, SWOT, Positioning Map, UX Audit).
5. **Build action plan** — Translate findings into the Action Items template (quick wins / medium-term / strategic).
6. **Package for stakeholders** — Assemble the Stakeholder Presentation using outputs from steps 3–5.

---

## Data Collection Guide

> Full executable scripts for each source are in `references/data-collection-guide.md`. Summaries of what to capture are below.

### 1. Website Analysis

Key things to capture:
- Pricing tiers and price points
- Feature lists per tier
- Primary CTA and messaging
- Case studies / customer logos (signals ICP)
- Integration logos
- Trust signals (certifications, compliance badges)

### 2. App Store Reviews

Review sentiment categories:
- **Praise** → what users love (defend / strengthen these)
- **Feature requests** → unmet needs (opportunity gaps)
- **Bugs** → quality signals
- **UX complaints** → friction points you can beat them on

**Sample App Store query (iTunes Search API):**
```
GET https://itunes.apple.com/search?term=<competitor_name>&entity=software&limit=1
# Extract trackId, then:
GET https://itunes.apple.com/rss/customerreviews/id=<trackId>/sortBy=mostRecent/json?l=en&limit=50
```
Parse `entry[].content.label` for review text and `entry[].im:rating.label` for star rating.

### 3. Job Postings (Team Size & Tech Stack Signals)

Signals from job postings:
- **Engineering volume** → scaling vs. consolidating
- **Specific tech mentions** → stack (React/Vue, Postgres/Mongo, AWS/GCP)
- **Sales/CS ratio** → product-led vs. sales-led motion
- **Data/ML roles** → upcoming AI features
- **Compliance roles** → regulatory expansion

### 4. SEO Analysis

SEO signals to capture:
- Top 20 organic keywords (intent: informational / navigational / commercial)
- Domain Authority / backlink count
- Blog publishing cadence and topics
- Which pages rank (product pages vs. blog vs. docs)

### 5. Social Media Sentiment

Capture recent mentions via Twitter/X API v2, Reddit, or LinkedIn. Look for recurring praise, complaints, and feature requests. See `references/data-collection-guide.md` for API query examples.

---

## Scoring Rubric (12 Dimensions, 1-5)

| # | Dimension | 1 (Weak) | 3 (Average) | 5 (Best-in-class) |
|---|-----------|----------|-------------|-------------------|
| 1 | **Features** | Core only, many gaps | Solid coverage | Comprehensive + unique |
| 2 | **Pricing** | Confusing / overpriced | Market-rate, clear | Transparent, flexible, fair |
| 3 | **UX** | Confusing, high friction | Functional | Delightful, minimal friction |
| 4 | **Performance** | Slow, unreliable | Acceptable | Fast, high uptime |
| 5 | **Docs** | Sparse, outdated | Decent coverage | Comprehensive, searchable |
| 6 | **Support** | Email only, slow | Chat + email | 24/7, great response |
| 7 | **Integrations** | 0-5 integrations | 6-25 | 26+ or deep ecosystem |
| 8 | **Security** | No mentions | SOC2 claimed | SOC2 Type II, ISO 27001 |
| 9 | **Scalability** | No enterprise tier | Mid-market ready | Enterprise-grade |
| 10 | **Brand** | Generic, unmemorable | Decent positioning | Strong, differentiated |
| 11 | **Community** | None | Forum / Slack | Active, vibrant community |
| 12 | **Innovation** | No recent releases | Quarterly | Frequent, meaningful |

**Example completed row** (Competitor: Acme Corp, Dimension 3 – UX):

| Dimension | Acme Corp Score | Evidence |
|-----------|----------------|---------|
| UX | 2 | App Store reviews cite "confusing navigation" (38 mentions); onboarding requires 7 steps before TTFV; no onboarding wizard; CC required at signup. |

Apply this pattern to all 12 dimensions for each competitor.

---

## Templates

> Full template markdown is in `references/analysis-templates.md`. Abbreviated reference below.

### Feature Comparison Matrix

Rows: core features, pricing tiers, platform capabilities (web, iOS, Android, API).  
Columns: your product + up to 3 competitors.  
Score each cell 1–5. Sum to get total out of 60.  
**Score legend:** 5=Best-in-class, 4=Strong, 3=Average, 2=Below average, 1=Weak/Missing

### Pricing Analysis

Capture per competitor: model type (per-seat / usage-based / flat rate / freemium), entry/mid/enterprise price points, free trial length.  
Summarize: price leader, value leader, premium positioning, your position, and 2–3 pricing opportunity bullets.

### SWOT Analysis

For each competitor: 3–5 bullets per quadrant (Strengths, Weaknesses, Opportunities for us, Threats to us). Anchor every bullet to a data signal (review quote, job posting count, pricing page, etc.).

### Positioning Map

2x2 axes (e.g., Simple ↔ Complex / Low Value ↔ High Value). Place each competitor and your product. Bubble size = market share or funding. See `references/analysis-templates.md` for ASCII and editable versions.

### UX Audit Checklist

Onboarding: TTFV (minutes), steps to activation, CC-required, onboarding wizard quality.  
Key workflows: steps, friction points, comparative score (yours vs. theirs).  
Mobile: iOS/Android ratings, feature parity, top complaint and praise.  
Navigation: global search, keyboard shortcuts, in-app help.

### Action Items

| Horizon | Effort | Examples |
|---------|--------|---------|
| Quick wins (0–4 wks) | Low | Add review badges, publish comparison landing page |
| Medium-term (1–3 mo) | Moderate | Launch free tier, improve onboarding TTFV, add top-requested integration |
| Strategic (3–12 mo) | High | Enter new market, build API v2, achieve SOC2 Type II |

### Stakeholder Presentation (7 slides)

1. **Executive Summary** — Threat level (LOW/MEDIUM/HIGH/CRITICAL), top strength, top opportunity, recommended action
2. **Market Position** — 2x2 positioning map
3. **Feature Scorecard** — 12-dimension radar or table, total scores
4. **Pricing Analysis** — Comparison table + key insight
5. **UX Highlights** — What they do better (3 bullets) vs. where we win (3 bullets)
6. **Voice of Customer** — Top 3 review complaints (quoted or paraphrased)
7. **Our Action Plan** — Quick wins, medium-term, strategic priorities; Appendix with raw data

## Related Skills

- **Product Strategist** (`product-team/product-strategist/`) — Competitive insights feed OKR and strategy planning
- **Landing Page Generator** (`product-team/landing-page-generator/`) — Competitive positioning informs landing page messaging
