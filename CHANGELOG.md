# Changelog

## 2.0.0 — 2026-11-08

The library is now a curated set for one solo operator. It is no longer a copy of every skill pack.

| Measure | Before | After |
|---|---|---|
| Skills in the masterskills plugin | 361 | 137 |
| masterskills always-on cost (`claude plugin details`) | ~40,359 tokens | ~14,122 tokens |
| Duplicate third-party plugins in `plugins.lock.json` | 8 (~15,867 tokens) | 0 |
| document-skills plugin | not installed | ~759 tokens |
| Total always-on cost from these sources | ~56,226 tokens | ~14,881 tokens |

Why: Claude Code puts the name and description of every skill into one listing. The listing budget is about 1% of the context window. When the listing is too large, Claude Code drops the descriptions of the skills that you use least. With 361 skills plus duplicate plugins, most skills arrived name-only, so Claude could not match them to a request.

The duplicate-plugin numbers come from the latest versions of those plugins, not the 2.9.0 versions that the lockfile recorded.

### Do this once on each machine

Use PowerShell (Windows) or Bash/Zsh (macOS, Linux). The commands are the same in each shell. Run one command at a time.

1. Remove the duplicate plugins. Each command prints `Successfully uninstalled plugin: <name> (scope: user)`. If a plugin is not installed on that machine, the command prints a line that starts `Failed to uninstall plugin`. That is safe to ignore.

```
claude plugin uninstall business-growth-skills@claude-code-skills
```

```
claude plugin uninstall business-operations-skills@claude-code-skills
```

```
claude plugin uninstall c-level-skills@claude-code-skills
```

```
claude plugin uninstall engineering-advanced-skills@claude-code-skills
```

```
claude plugin uninstall engineering-skills@claude-code-skills
```

```
claude plugin uninstall marketing-skills@claude-code-skills
```

```
claude plugin uninstall pm-skills@claude-code-skills
```

```
claude plugin uninstall agent-skills@addy-agent-skills
```

2. Remove the two marketplaces that have no plugins left. Each command prints `Successfully removed marketplace: <name>`.

```
claude plugin marketplace remove claude-code-skills
```

```
claude plugin marketplace remove addy-agent-skills
```

3. Add the Anthropic document skills. The first command prints a line that starts `Successfully added marketplace: anthropic-agent-skills`. The second prints `Successfully installed plugin: document-skills@anthropic-agent-skills (scope: user)`.

```
claude plugin marketplace add anthropics/skills
```

```
claude plugin install document-skills@anthropic-agent-skills
```

4. Get this release of masterskills. The first command prints `Successfully updated marketplace: masterskills`. The second command must end with a line that names version 2.0.0. The exact wording of that line was not checked against a GitHub-hosted marketplace.

```
claude plugin marketplace update masterskills
```

```
claude plugin update masterskills@masterskills
```

5. Start a new Claude Code session. Run `/doctor`. A warning that starts `Skill listing will be truncated` must not appear. If it appears, it names the skills that lost their descriptions.

### Added

| Skill | Source | Reason |
|---|---|---|
| `skill-creator` | anthropics/skills 2c5958e (Apache-2.0) | Official skill authoring with evals and description tuning. Replaces `write-a-skill`. |
| `mcp-builder` | anthropics/skills 2c5958e (Apache-2.0) | MCP server design guides and an evaluation harness for the client MCP server work. Retired model IDs replaced. |
| `find-skills` | vercel-labs/skills d3701c1 (MIT) | Most-installed skill on skills.sh. Finds a skill on demand, so the core library can stay small. Step 6 now requires `skill-security-auditor` and owner approval before an install. |
| `job-application` | New | The job search is the primary goal. Screens a posting against the owner's rules, then drafts truthful materials. Private facts go in `profile.md`, which `.gitignore` excludes. |
| `document-skills` plugin | anthropics/skills, in `plugins.lock.json` | Word, PDF, Excel, and PowerPoint output for resumes, letters, and client files. The license does not allow a copy in this repo, so it installs as a plugin. |

### Replaced and narrowed

| Change | Reason |
|---|---|
| `write-a-skill`, `sample-skill` → `skill-creator` | One authoring skill with evals. |
| `mcp-server-builder` narrowed to the OpenAPI case | `mcp-builder` owns general MCP design. The two descriptions no longer compete. |
| `research-router` → `deep-research`, `recency-pulse`, `company-dossier` | 4 of the 6 specialists that the router used are retired. |
| `/grilling` → `grill-me`; `/tdd` → superpowers `test-driven-development`; `playwright-pro` → `pw` | The old names pointed at skills that do not exist in this library. |

### Review-cluster decisions (from SIMILAR_SKILLS_REVIEW.md)

| Cluster | Kept | Retired |
|---|---|---|
| Decision post-mortem | none | `cs-decision-post-mortem`, `em-failure-postmortem` |
| Landing page generation | `landing-page-html` | `landing-page-generator` |
| Markdown → HTML document | `markdown-html-orchestrator` (router), `md-document`, `md-review`, `md-slides` | none |
| Plan stress-testing | `grill-me`, `grill-with-docs`, `idea-roast-panel`, `pre-mortem-challenge` | `em-assumption-stress-test`, `executive-mentor` |
| Research summarization | `deep-research` | `research-router`, `research-summarizer` |
| Design critique (UI) | `impeccable`, `improve-ui`, `ui-craft` | `minoan-design-critique`, `minoan-frontend-design`, `ui-craft-critique`, `ui-ux-designer`, `open-design-critique` |
| Design critique (taste) | `tastemaker` | `taste-design-critique`, `critique-composition`, `critique-visual-hierarchy`, `critique-vocabulary` |
| Code review | `code-review`, `adversarial-reviewer` | `pr-review-expert`, `named-persona-adversarial-review`, `karpathy-coder` |
| Hallucination guards | `zero-hallucination-coder` | `strict-api` |
| Internal comms | none | `internal-comms`, `team-communications`, `internal-narrative`, `change-management` |
| Social media | `social-content`, `linkedin-post-writer` | `social-media-manager`, `social-media-analyzer`, `x-twitter-growth` |
| Competitive analysis | `competitive-teardown` | `competitive-intel`, `competitor-alternatives`, `marketing-strategy-pmm` |
| Experiment / A/B | `statistical-analyst`, `senior-data-scientist` | `ab-test-setup`, `experiment-designer` |
| Prompt management | `senior-prompt-engineer` | `prompt-engineer-toolkit`, `prompt-governance` |
| Skill authoring | `skill-creator`, `skill-tester`, `skill-security-auditor`, `writing-for-agents` | `write-a-skill`, `sample-skill` |
| Incident handling | none | `incident-commander`, `incident-response` |
| Security assessment | `security-pen-testing`, `ai-security`, `security-guidance`, `skill-security-auditor` | `red-team`, `senior-secops`, `senior-security`, `cloud-security`, `threat-detection` |
| Database | `database-designer`, `sql-database-assistant` | none |
| Agent/workflow design | `agent-designer`, `workflow-builder`, `loop-library` | `agent-workflow-designer` |
| Codebase architecture | `codebase-design`, `improve-codebase-architecture`, `domain-modeling` | `senior-architect` |
| Browser automation / scraping | `browser-automation`, `universal-scraping-architect`, `notebooklm` | none |
| Human-sounding output | `content-humanizer` | `behuman`, `caveman` (the caveman plugin stays) |
| Memory / self-improvement | `self-improving-agent`, `memory-*` (3) | `skillopt-sleep` |
| Ops documentation | `knowledge-ops`, `process-mapper` | `runbook-generator`, `business-operations-skills` |
| Test generation | `pw`, `pw-generate-tests`, `pw-review-tests`, `pw-fix-flaky-tests`, `pw-init-project`, `api-test-suite-builder` | `tdd-guide`, `senior-qa`, `pw-coverage-gaps` |
| Dependency / release hygiene | `ship-gate`, `dependency-auditor` | `tech-debt-tracker` |
| Leadership coaching | none | `founder-coach`, `executive-mentor`, `ceo-advisor`, `chief-of-staff` |

### Rejected candidates

These were reviewed and not added. Do not research them again unless the reason changes.

| Candidate | Reason |
|---|---|
| `claude-api` (anthropics/skills) | Claude Code ships it as a bundled skill. A copy would compete with it. |
| `docx`, `pdf`, `pptx`, `xlsx` copies (anthropics/skills) | The license does not allow redistribution. Installed as the `document-skills` plugin instead. |
| `frontend-design` (anthropics/skills) | `impeccable` and `ui-craft` cover it. A third frontend-build skill would compete for the same requests. |
| `webapp-testing` (anthropics/skills) | `pw` covers Playwright testing. |
| `react-best-practices`, `web-design-guidelines` (vercel-labs/agent-skills) | `senior-frontend`, `a11y-audit`, and `impeccable` cover the work. |
| `agent-browser` (vercel-labs) | Needs its own CLI. Claude in Chrome covers browser control. |
| n8n-io/skills plugin, czlonkowski/n8n-skills plugin | Each plugin has a SessionStart hook that adds its whole router skill to every session in every project: 27.6 KB and 17.6 KB. Install the n8n-io plugin only in an n8n project folder (see README). |
| `job-description-analyzer`, `resume-tailor`, `cover-letter-generator`, `interview-prep-generator`, `career-changer-translator` (Paramchoudhary/ResumeSkills) | A safety review found no security problem, but the examples invent metrics and titles, and two skills have no truthfulness rule. In a trial on one posting, an agent without the skill met every success criterion. The agent with the skill added a match score, a salary check, and application tips, but no better verdict. `job-application` holds the owner's rules instead. |
| `tailored-resume-generator` (ComposioHQ) | Generic prompt text. Same result as the trial above. |
| `resume-tailoring` (varunr89) | 1,319-line SKILL.md plus a 1,381-line workflow. High load cost for a task that the trial showed the base model does well. |
| addyosmani/agent-skills plugin | 25 process skills that duplicate superpowers, which is the process framework that the shepherd plugin routes to. Both ship a `test-driven-development` skill. |

### Fixed alongside

- 26 SKILL.md frontmatter blocks had lines that started with an em dash. The descriptions started with the em dash. The `landing-page-html` metadata did not parse as a mapping.
- `vector-design` frontmatter did not parse as YAML.
- `llm-cost-optimizer` description had 1,212 characters. The Agent Skills limit is 1,024.
- `pw` claimed agents, MCP servers, and hooks that this library does not ship.
- Many skills pointed at `cs-*` agents and `/cs:*` commands from the upstream repo. This library does not ship them. The pointers now name real skills.
- `handoff/scripts/skill_recommender.py` recommended 9 skills that do not exist here.
- `mcp-builder/scripts/evaluation.py` defaulted to a retired model ID.

### Follow-ups

- Descriptions still average about 400 characters. A pass that front-loads the trigger words and cuts each description to about 250 characters can cut the always-on cost by about a third. Do it only with a trigger probe for each change.
- `plugins/masterskills/plugin.json` is a stale file from before the build script. Claude Code reads `.claude-plugin/plugin.json` only.
- `autoresearch-agent` and `docker-development` keep upstream install notes for other tools (`clawhub`, `scripts/convert.sh`). These files do not exist here.
- Provenance notes in some `references/` and `scripts/` files name upstream paths. They are attribution, not routing, so they stay.

### Retired

All retired skills are in `archive/retired_skills/`. To restore one, run this from the repo root, then rebuild the manifest (Bash/Zsh or PowerShell):

```
git mv archive/retired_skills/<name> plugins/masterskills/skills/<name>
python scripts/build_manifest.py
```

Replace `<name>` with the skill name from the tables below.

#### Medical-device QMS, clinical, grant, and patent research (18)

| Skill | Reason |
|---|---|
| `capa-officer` | Off-profile: medical-device QMS |
| `fda-consultant-specialist` | Off-profile: FDA medical-device submissions |
| `mdr-745-specialist` | Off-profile: EU medical-device regulation |
| `qms-audit-expert` | Off-profile: ISO 13485 audits |
| `quality-documentation-manager` | Off-profile: medical-device document control |
| `quality-manager-qms-iso13485` | Off-profile: ISO 13485 QMS |
| `ra-qm-skills` | Router for retired regulatory/QMS set |
| `regulatory-affairs-head` | Off-profile: MedTech regulatory affairs |
| `risk-management-specialist` | Off-profile: ISO 14971 medical-device risk |
| `information-security-manager-iso27001` | Off-profile: HealthTech/MedTech ISMS |
| `clinical-research` | Off-profile: clinical study design |
| `nih-grant-research` | Off-profile: NIH grants |
| `research-finance` | Off-profile: R&D program finance |
| `research-ops-skills` | Router for retired research-ops set |
| `litreview` | Off-profile: academic PubMed literature review |
| `syllabus-reading-list` | Off-profile: course syllabus reading lists |
| `patent-landscape` | Off-profile: patent prior art |
| `market-research` | Research-ops member; deep-research covers ad-hoc sizing |

#### Compliance frameworks (5)

| Skill | Reason |
|---|---|
| `gdpr-dsgvo-expert` | Off-profile: GDPR/German BDSG; US solo operator |
| `eu-ai-act-specialist` | Off-profile: EU AI Act compliance |
| `iso42001-specialist` | Off-profile: ISO 42001 audits |
| `compliance-os` | Off-profile: multi-framework compliance orchestration |
| `soc2-compliance` | Off-profile: SOC 2 audit prep |

#### C-suite advisors, board, and founder-mode commands (46)

| Skill | Reason |
|---|---|
| `c-level-agents` | Startup C-suite persona suite; solo operator |
| `agent-protocol` | C-suite inter-agent protocol |
| `context-engine` | C-suite company-context loader |
| `chief-of-staff` | C-suite router |
| `cs-cross-model-eval` | C-suite founder-mode command |
| `cs-decision-post-mortem` | C-suite founder-mode command |
| `cs-execution-plan` | C-suite founder-mode command |
| `cs-founder-router` | C-suite founder-mode command |
| `cs-freeze-decision` | C-suite founder-mode command |
| `cs-log-decision` | C-suite founder-mode command |
| `cs-office-hours` | C-suite founder-mode command |
| `cs-onboard-company-context` | C-suite founder-mode command |
| `cs-strategy-brief` | C-suite founder-mode command |
| `decision-logger` | C-suite board-decision memory |
| `board-deck-builder` | Board/investor decks; no board |
| `board-meeting` | Multi-agent board deliberation; no board |
| `board-prep` | Board meeting prep; no board |
| `ceo-advisor` | C-suite advisor persona |
| `cfo-advisor` | C-suite advisor persona (startup fundraising) |
| `cmo-advisor` | C-suite advisor persona |
| `coo-advisor` | C-suite advisor persona |
| `cpo-advisor` | C-suite advisor persona |
| `cro-advisor` | C-suite advisor persona |
| `cto-advisor` | C-suite advisor persona |
| `ciso-advisor` | C-suite advisor persona |
| `chro-advisor` | C-suite advisor persona |
| `chief-ai-officer-advisor` | C-suite advisor persona |
| `chief-customer-officer-advisor` | C-suite advisor persona |
| `chief-data-officer-advisor` | C-suite advisor persona |
| `general-counsel-advisor` | C-suite advisor persona; legal advice excluded from scope |
| `vpe-advisor` | C-suite advisor persona |
| `company-os` | Company operating-system framework; solo operator |
| `culture-architect` | Company culture design; solo operator |
| `org-health-diagnostic` | Org health check; solo operator |
| `strategic-alignment` | Strategy cascade to teams; solo operator |
| `internal-narrative` | Multi-audience company narrative; solo operator |
| `scenario-war-room` | C-suite cascading scenarios |
| `intl-expansion` | International expansion |
| `ma-playbook` | M&A |
| `founder-coach` | Startup founder coaching |
| `executive-mentor` | Superseded by pre-mortem-challenge and idea-roast-panel (review cluster) |
| `em-assumption-stress-test` | Superseded by pre-mortem-challenge (review cluster) |
| `em-failure-postmortem` | Duplicate of cs-decision-post-mortem (review cluster); both C-suite |
| `em-hard-call` | Executive-mentor command |
| `arquiteto-de-empresa` | Company-from-scratch OKF bundle (Portuguese source) |
| `andreessen` | Persona decision skill; idea-roast-panel covers pressure tests |

#### Enterprise sales, finance, and internal operations (26)

| Skill | Reason |
|---|---|
| `commercial-skills` | Router for retired commercial set |
| `commercial-policy` | Enterprise discount policy |
| `commercial-forecaster` | Enterprise bookings forecast |
| `deal-desk` | Enterprise deal desk |
| `channel-economics` | Partner-channel economics |
| `partnerships-architect` | Startup partner tiers |
| `revenue-operations` | SaaS RevOps |
| `sales-engineer` | Enterprise pre-sales |
| `rfp-responder` | RFP bids; contract-and-proposal-writer covers proposals |
| `business-growth-skills` | Router for retired growth set |
| `customer-success-manager` | SaaS customer health scoring |
| `finance-skills` | Router for retired finance set |
| `financial-analyst` | Corporate DCF/ratio analysis |
| `saas-metrics-coach` | SaaS metrics; not a SaaS business |
| `business-operations-skills` | Router for retired ops set |
| `capacity-planner` | Erlang-C staffing |
| `procurement-optimizer` | Enterprise SaaS spend audit |
| `vendor-management` | Enterprise vendor scorecards |
| `runbook-generator` | Service runbooks; knowledge-ops covers SOP authoring |
| `meeting-cost-and-agenda` | Team meeting economics; solo operator |
| `meeting-analyzer` | Team meeting coaching; solo operator |
| `internal-comms` | Internal comms (review cluster); solo operator |
| `team-communications` | Internal comms (review cluster); solo operator |
| `change-management` | Org change rollout; solo operator |
| `interview-system-designer` | Hiring-side interview loops; job search is candidate-side |
| `tc-tracker` | Change records between sessions; handoff covers |

#### Atlassian, Scrum, and product-team tooling (21)

| Skill | Reason |
|---|---|
| `pm-skills` | Router for retired Atlassian/PM set |
| `jira-expert` | Not in stack (monday.com, Todoist) |
| `confluence-expert` | Not in stack |
| `atlassian-admin` | Not in stack |
| `atlassian-templates` | Not in stack |
| `scrum-master` | Team scrum coaching; solo operator |
| `senior-pm` | Enterprise portfolio PM |
| `agile-product-owner` | Team backlog ownership; solo operator |
| `testrail` | Not in stack |
| `browserstack` | Not in stack |
| `product-skills` | Router for retired product set |
| `product-strategist` | Head-of-Product toolkit |
| `product-analytics` | SaaS product KPIs |
| `product-research` | User research ops |
| `product-discovery` | Product-team discovery sprints |
| `product-manager-toolkit` | PM toolkit; not a PM role |
| `ux-researcher-designer` | UX research team toolkit |
| `roadmap-communicator` | Team roadmap comms |
| `apple-hig-expert` | Apple platforms not in use (Android, Quest) |
| `research-summarizer` | Unrouted summarizer (review cluster); deep-research and research-router cover |
| `code-to-prd` | Codebase-to-PRD; codebase-onboarding covers docs |

#### SaaS growth, paid ads, and prompt registries (29)

| Skill | Reason |
|---|---|
| `competitor-alternatives` | SaaS vs-pages |
| `programmatic-seo` | Pages at scale |
| `app-store-optimization` | No app in store; game paused |
| `paywall-upgrade-cro` | SaaS paywalls |
| `popup-cro` | Popups |
| `signup-flow-cro` | SaaS signup |
| `onboarding-cro` | SaaS activation |
| `churn-prevention` | SaaS cancel flows |
| `referral-program` | Referral/affiliate design |
| `paid-ads` | Ad campaign management excluded from services |
| `ad-creative` | Ad campaign management excluded from services |
| `marketing-demand-acquisition` | Demand-gen campaigns |
| `campaign-analytics` | Ad campaign attribution |
| `ab-test-setup` | Merged planner pair (review cluster); low traffic sites |
| `experiment-designer` | Merged planner pair (review cluster); statistical-analyst keeps analysis |
| `launch-strategy` | Product launches |
| `pricing-strategy` | SaaS tier pricing |
| `free-tool-strategy` | Engineering-as-marketing |
| `marketing-ideas` | SaaS growth ideas |
| `marketing-strategy-pmm` | Product marketing |
| `competitive-intel` | Ongoing competitor tracking for C-suite (review cluster); competitive-teardown kept |
| `marketing-psychology` | Copywriting covers |
| `x-twitter-growth` | Not an active channel; linkedin-post-writer kept |
| `social-media-analyzer` | Social analytics (review cluster) |
| `social-media-manager` | Social strategy (review cluster); social-content kept |
| `webinar-marketing` | Webinars |
| `email-template-builder` | React Email transactional systems |
| `prompt-engineer-toolkit` | Marketing prompt registry (review cluster) |
| `prompt-governance` | Production prompt registry (review cluster); senior-prompt-engineer kept |

#### Infrastructure, SRE, security-team, and duplicate engineering skills (69)

| Skill | Reason |
|---|---|
| `pr-review-expert` | Code-review cluster; code-review and adversarial-reviewer kept |
| `named-persona-adversarial-review` | Code-review cluster; adversarial-reviewer kept |
| `karpathy-coder` | Coding discipline duplicate of the shepherd plugin ladder |
| `minimalist-coder` | Efficiency ladder duplicate of the shepherd plugin ladder |
| `strict-api` | Subset of zero-hallucination-coder (review cluster) |
| `code-tour` | VS Code CodeTour files; codebase-onboarding kept |
| `tech-debt-tracker` | Release hygiene cluster; ship-gate and dependency-auditor kept |
| `focused-fix` | Debug cluster; diagnosing-bugs and superpowers systematic-debugging kept |
| `performance-profiler` | No profiling workload |
| `helm-chart-builder` | No Kubernetes |
| `kubernetes-operator` | No Kubernetes |
| `chaos-engineering` | No production fleet |
| `slo-architect` | No production fleet |
| `observability-designer` | No production fleet |
| `incident-commander` | SRE incident command; no production fleet |
| `migration-architect` | Zero-downtime migrations; no production fleet |
| `monorepo-navigator` | No monorepos |
| `azure-cloud-architect` | Cloud not in use; gcp-cloud-architect kept as the single cloud skill |
| `aws-solution-architect` | Cloud not in use; gcp-cloud-architect kept as the single cloud skill |
| `feature-flags-architect` | No flag platform |
| `terraform-patterns` | No IaC |
| `secrets-vault-manager` | HashiCorp Vault and cloud secret stores |
| `cloud-security` | Cloud posture; no cloud fleet |
| `senior-devops` | Overlaps ci-cd-pipeline-builder and docker-development |
| `red-team` | Offensive security engagements |
| `threat-detection` | Threat hunting |
| `incident-response` | Security incident response |
| `senior-secops` | SecOps program |
| `senior-security` | Router over retired security set |
| `senior-computer-vision` | No CV workload |
| `senior-data-engineer` | Spark/Airflow/Kafka scale |
| `senior-fullstack` | Overlaps senior-frontend and senior-backend |
| `senior-ml-engineer` | No MLOps workload |
| `senior-qa` | Test cluster; superpowers test-driven-development and pw-generate-tests kept |
| `tdd-guide` | Duplicate of superpowers test-driven-development |
| `senior-architect` | Codebase-architecture cluster; codebase-design kept |
| `saas-scaffolder` | SaaS boilerplate |
| `spec-to-repo` | Spec cluster; to-spec and superpowers writing-plans kept |
| `spec-driven-workflow` | Spec cluster; to-spec and superpowers writing-plans kept |
| `stripe-integration-expert` | No Stripe work |
| `snowflake-development` | Not in stack |
| `gemma-dev` | No Gemma work |
| `gemma-trainer` | No Gemma work |
| `git-worktree-manager` | Duplicate of superpowers using-git-worktrees |
| `agenthub` | Parallel competing agents; token cost on the 100 USD plan |
| `agenthub-board` | AgentHub command |
| `agenthub-eval` | AgentHub command |
| `agenthub-merge` | AgentHub command |
| `agenthub-run` | AgentHub command |
| `agenthub-status` | AgentHub command |
| `agent-workflow-designer` | Near-synonym of agent-designer (review cluster) |
| `agent-harness` | Overlaps fable-goal and loop-library |
| `agent-decision-receipts` | Signed action receipts; no need |
| `skillopt-sleep` | Competes with self-improving-agent (review cluster) |
| `llm-wiki` | Obsidian second brain; not in stack |
| `sample-skill` | Template, not a tool (review cluster) |
| `skill-readme-generate` | Bilingual Chinese README generator |
| `write-a-skill` | Replaced by skill-creator (Anthropic) |
| `collab-proof` | Session contribution analysis |
| `caveman` | Duplicate of the caveman plugin in plugins.lock.json |
| `behuman` | Changes reply style away from peer register; content-humanizer kept for drafts |
| `engineering-advanced-skills` | Index of mostly retired engineering skills |
| `pw-migrate-from-cypress-selenium` | No Cypress or Selenium suites |
| `pw-coverage-gaps` | Playwright sub-command; low use |
| `pw-test-report` | Playwright sub-command; low use |
| `scaffold-exercises` | Course-authoring tool (Matt Pocock courses) |
| `migrate-to-shoehorn` | TypeScript test library migration |
| `setup-ts-deep-modules` | TypeScript dependency-cruiser setup |
| `api-design-reviewer` | No REST API design work |

#### Design-critique and design-build duplicates (13)

| Skill | Reason |
|---|---|
| `throughline` | Figma review; Figma dropped |
| `minoan-design-critique` | Design-critique cluster; impeccable and improve-ui kept |
| `minoan-frontend-design` | Frontend-build cluster; impeccable and ui-craft kept |
| `open-design-critique` | Design-critique cluster |
| `ui-craft-critique` | Design-critique cluster |
| `ui-ux-designer` | Design-critique cluster |
| `taste-design-critique` | Taste cluster; tastemaker kept |
| `critique-composition` | Taste cluster; tastemaker kept |
| `critique-visual-hierarchy` | Taste cluster; tastemaker kept |
| `critique-vocabulary` | Taste cluster; team facilitation aid |
| `landing-page-generator` | Landing-page pair (review cluster); landing-page-html kept |
| `ui-design-system` | Token toolkit; design-system kept |
| `epic-design` | 2.5D scroll sites; landing-page-html covers site work |

#### Routers left without members (1)

| Skill | Reason |
|---|---|
| `research-router` | Router left with 2 of 6 specialists; deep-research, recency-pulse, and company-dossier route by description |
