# Similar skills — review queue

Generated 2026-10-25 from a full read of all 360 `SKILL.md` descriptions after the
description repair and generic-name renames. Nothing here has been merged or removed;
each cluster is a decision for the owner. "Overlap" is functional overlap as described,
not a measure of quality.

Suggested resolutions: **keep both** (distinct enough, tighten descriptions so routing
is unambiguous), **merge** (fold one into the other), **retire** (move to
`archive/retired_skills/`).

## High overlap — likely redundant

| Cluster | Skills | Overlap | Note |
|---|---|---|---|
| Decision post-mortem | `cs-decision-post-mortem`, `em-failure-postmortem` | Both run a blameless retrospective on a decision/launch that went wrong | Same job, two plugins. Pick one; the other's trigger phrases (`/cs:post-mortem`, `/em:postmortem`) can be folded in. |
| Landing page generation | `landing-page-html`, `landing-page-generator` | Both generate conversion landing pages | Differ only by output (single HTML + GSAP vs Next.js/Tailwind TSX). Merge into one with an output switch, or keep both and say so in both descriptions. |
| Markdown → HTML document | `md-document`, `markdown-html-orchestrator` | Both convert long-form markdown into a single-file interactive HTML | `markdown-html-orchestrator` is a router over `md-document` / `md-review` / `md-slides`. Keep, but the router description should say it routes. |
| Plan stress-testing | `pre-mortem-challenge`, `em-assumption-stress-test`, `executive-mentor`, `idea-roast-panel`, `grill-me` | All pressure-test a plan or idea before commitment | Five entry points for one activity. `grill-me` (interview) and `idea-roast-panel` (5-angle panel) have distinct formats; the other three are near-duplicates. |
| Research summarization | `research-router`, `deep-research`, `research-summarizer` | Multi-source research and synthesis | `research-router` already routes to `deep-research`; `research-summarizer` is a non-dev summarizer that the router does not know about. Add it to the router or retire it. |
| Design critique (UI) | `minoan-design-critique`, `ui-craft-critique`, `ui-ux-designer`, `open-design-critique`, `improve-ui`, `impeccable` (critique mode) | All review an existing UI and report problems | Six critique skills imported 2026-10-25 for comparison. Expect to keep 1–2 after trialing. `improve-ui` is the only one that writes implementation plans; `open-design-critique` is the only scored HTML report. |
| Design critique (taste/visual) | `tastemaker`, `taste-design-critique`, `critique-composition`, `critique-visual-hierarchy`, `critique-vocabulary` | Taste-level critique and critique language | Same import batch. `critique-composition` and `critique-visual-hierarchy` are narrow lenses; `tastemaker` is the full method; `taste-design-critique` + `critique-vocabulary` are facilitation aids. |
| Code review | `code-review`, `pr-review-expert`, `adversarial-reviewer`, `named-persona-adversarial-review`, `karpathy-coder` | Review a diff/PR for quality | `code-review` (standards + spec axes) and `pr-review-expert` (security/quality of diffs) overlap most. The adversarial pair are deliberately different stances. `karpathy-coder` is a coding discipline, not a reviewer — description says "reviewing" and should be narrowed. |
| Hallucination guards | `strict-api`, `zero-hallucination-coder` | Prevent invented APIs/imports | `zero-hallucination-coder` is a full workflow that includes what `strict-api` does. Retire `strict-api` or make it the lightweight trigger for the other. |
| Internal comms | `internal-comms`, `team-communications`, `internal-narrative`, `change-management` | Write internal announcements and updates | `internal-comms` (change announcements) vs `team-communications` (3P updates, newsletters) are the direct overlap. `internal-narrative` is cross-audience story consistency; `change-management` is the rollout framework. |
| Social media | `social-content`, `social-media-manager`, `social-media-analyzer`, `x-twitter-growth`, `linkedin-post-writer` | Social strategy/content/analysis | `social-content` (write posts) vs `social-media-manager` (strategy + calendar) blur. `x-twitter-growth` and `linkedin-post-writer` are platform-specific and `linkedin-post-writer` is personal to Nick — keep. |
| Competitive analysis | `competitive-intel`, `competitive-teardown`, `competitor-alternatives`, `marketing-strategy-pmm` | Competitor tracking and positioning | `competitive-intel` (ongoing tracking) and `competitive-teardown` (one-shot product teardown) overlap in output. `competitor-alternatives` is SEO "vs" pages — distinct. |
| Experiment / A/B | `ab-test-setup`, `experiment-designer`, `statistical-analyst`, `senior-data-scientist` | Design and analyze experiments | `ab-test-setup` and `experiment-designer` both plan tests; `statistical-analyst` analyzes results. Keep the analysis one; merge the two planners. |
| Prompt management | `prompt-engineer-toolkit`, `prompt-governance`, `senior-prompt-engineer` | Prompt versioning, eval, A/B | `prompt-engineer-toolkit` is marketing-prompt specific; the other two overlap on production prompt registries and evals. |
| Skill authoring | `write-a-skill`, `sample-skill`, `skill-tester`, `skill-security-auditor`, `writing-for-agents` | Create / validate skills | `sample-skill` is a template, not a tool — candidate for `archive/`. The rest are distinct stages (write / test / audit / style). |

## Medium overlap — distinct scope, ambiguous routing

| Cluster | Skills | Why it is ambiguous |
|---|---|---|
| Incident handling | `incident-commander`, `incident-response` | One is SRE (outages), one is security (breaches). Descriptions both say "incident response". Rename or qualify: `incident-commander-sre`, `security-incident-response`. |
| Security assessment | `security-pen-testing`, `red-team`, `senior-secops`, `senior-security`, `cloud-security`, `ai-security`, `threat-detection` | `senior-security` already routes to the others. Fine as a set, but `security-pen-testing` vs `red-team` (offensive, authorized) need a one-line "use X not Y" in each. |
| Database | `database-designer`, `sql-database-assistant` | Schema design vs query writing; both claim "optimize queries" and "migrations". |
| Agent/workflow design | `agent-designer`, `agent-workflow-designer`, `workflow-builder`, `loop-library` | First two are near-synonyms by name. `workflow-builder` is Claude Code Workflow `.js` files; `loop-library` is loop patterns. |
| Product leadership | `product-manager-toolkit`, `product-strategist`, `cpo-advisor`, `product-skills` (router), `agile-product-owner` | Layered PM / Head of Product / CPO. Keep, but descriptions should name the seniority tier they serve. |
| Revenue / finance advisors | `revenue-operations`, `commercial-forecaster`, `cro-advisor`; `financial-analyst`, `saas-metrics-coach`, `cfo-advisor`, `finance-skills` (router) | Analyst-tool vs advisor-persona pairs. Expected pattern across the C-suite set; just confirm the routers list every member. |
| Medical device QMS | `quality-manager-qms-iso13485`, `qms-audit-expert`, `quality-documentation-manager`, `capa-officer`, `ra-qm-skills` (router) | Role-split of one domain. OK if the router stays current. |
| FDA regulatory | `fda-consultant-specialist`, `regulatory-affairs-head` | Both prepare 510(k)/PMA/De Novo packages. |
| AI governance | `eu-ai-act-specialist`, `iso42001-specialist`, `chief-ai-officer-advisor`, `compliance-os` | Risk classification under EU AI Act appears in all three non-router skills. |
| Codebase architecture | `codebase-design`, `improve-codebase-architecture`, `domain-modeling`, `senior-architect` | `codebase-design` is the vocabulary; `improve-codebase-architecture` is the scan tool that uses it. Keep; the pair should cross-reference. |
| Browser automation / scraping | `browser-automation`, `universal-scraping-architect`, `notebooklm` | First two both do scraping and data extraction. |
| Human-sounding output | `behuman`, `content-humanizer`, `caveman` (inverse) | `behuman` changes Claude's response style; `content-humanizer` edits a draft. Both triggered by "sounds like AI". |
| Memory / self-improvement | `self-improving-agent`, `skillopt-sleep`, `memory-extract-skill`, `memory-promote-to-rules`, `memory-save-note` | `self-improving-agent` is the umbrella for the three `memory-*` commands; `skillopt-sleep` is a competing nightly consolidation design. |
| Ops documentation | `knowledge-ops`, `runbook-generator`, `business-operations-skills`, `process-mapper` | SOP/runbook authoring appears in three descriptions. |
| Paid advertising | `paid-ads`, `ad-creative`, `marketing-demand-acquisition`, `campaign-analytics` | Campaign setup vs creative vs demand-gen strategy vs analysis. Routable, but `marketing-ops` (router) should enumerate them. |
| Test generation | `tdd-guide`, `senior-qa`, `pw-generate-tests`, `api-test-suite-builder`, `pw-coverage-gaps` | `senior-qa` and `tdd-guide` both generate unit tests and analyze coverage. |
| Dependency / release hygiene | `dependency-auditor`, `ship-gate`, `tech-debt-tracker` | `ship-gate` includes dependency and code-quality checks the other two do in depth. |
| Leadership coaching | `founder-coach`, `executive-mentor`, `ceo-advisor`, `chief-of-staff` | Personal development vs adversarial partner vs strategy advisor vs router. |

## Broken or stale cross-references found during the pass

- `a11y-audit`, `browser-automation`, `self-improving-agent`, `zero-hallucination-coder` refer to a skill named **`playwright-pro`**. No such skill exists here; the Playwright toolkit is `pw` (plus the `pw-*` sub-commands). Update the four references or add a `playwright-pro` alias line to `pw`.
- `minoan-design-critique` recommends `/design-audit` and `/design-polish`; `minoan-frontend-design` references a `rocaille-shader` skill. None are in the repo.
- `ask-matt` and the `*-skills` routers (`business-growth-skills`, `finance-skills`, `pm-skills`, `product-skills`, `ra-qm-skills`, `research-ops-skills`, `commercial-skills`, `engineering-advanced-skills`) list member skills by name. They were not updated for today's renames (none of the renamed skills appear in them on a grep, but confirm after the next build).

## Renames applied 2026-10-25

Generic names that collided in meaning were renamed to function. Slash-trigger phrases
(`/pw:fix`, `/hub:run`, `/cs:brief`, …) are unchanged inside each description, so
invocation by trigger still works; invocation by old directory name does not.

| Old | New |
|---|---|
| fix / generate / init / report / review / migrate / coverage | pw-fix-flaky-tests / pw-generate-tests / pw-init-project / pw-test-report / pw-review-tests / pw-migrate-from-cypress-selenium / pw-coverage-gaps |
| setup / loop / resume | autoresearch-setup / autoresearch-loop / autoresearch-resume |
| board / eval / merge / run / status | agenthub-board / agenthub-eval / agenthub-merge / agenthub-run / agenthub-status |
| brief / decide / execute / freeze / office-hours / onboard / post-mortem / cross-eval / founder-mode | cs-strategy-brief / cs-log-decision / cs-execution-plan / cs-freeze-decision / cs-office-hours / cs-onboard-company-context / cs-decision-post-mortem / cs-cross-model-eval / cs-founder-router |
| hard-call / postmortem / stress-test | em-hard-call / em-failure-postmortem / em-assumption-stress-test |
| extract / promote / remember | memory-extract-skill / memory-promote-to-rules / memory-save-note |
| capture / teach / implement / triage / prototype / research / reflect / roast | brain-dump-capture / teach-concept / implement-from-spec / issue-triage / throwaway-prototype / research-router / step-back-reflect / idea-roast-panel |
| landing / wizard / dossier / pulse / grants / syllabus / patent / meetings | landing-page-html / bash-setup-wizard / company-dossier / recency-pulse / nih-grant-research / syllabus-reading-list / patent-landscape / meeting-cost-and-agenda |
| challenge / loop-me / minimalist / deep-work / wait-what | pre-mortem-challenge / workflow-spec-grill / minimalist-coder / deep-work-planner / wait-what-repitch |
