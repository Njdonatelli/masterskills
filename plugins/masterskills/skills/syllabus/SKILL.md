---
name: syllabus
description: >-
  G—e—n—e—r—a—t—e—s— —a— —c—u—r—a—t—e—d— —s—u—p—p—l—e—m—e—n—t—a—r—y— —r—e—a—d—i—n—g— —l—i—s—t— —f—r—o—m— —a—n—y— —c—o—u—r—s—e— —s—y—l—l—a—b—u—s— —u—s—i—n—g— —C—o—n—s—e—n—s—u—s— —a—c—a—d—e—m—i—c— —s—e—a—r—c—h—.— —G—r—i—l—l—-—m—e— —i—n—t—a—k—e— —(—s—y—l—l—a—b—u—s— —i—n—p—u—t— —f—o—r—m—a—t— —+— —c—o—u—r—s—e— —a—u—d—i—e—n—c—e— —+— —y—e—a—r— —r—a—n—g—e—)— —p—l—u—s— —a— —g—r—o—u—p—i—n—g— —f—o—r—c—i—n—g—-—o—p—t—i—o—n—s— —c—h—e—c—k—p—o—i—n—t— —b—e—f—o—r—e— —a—n—y— —s—e—a—r—c—h— —r—u—n—s— ——— —s—o— —t—h—e— —r—e—a—d—i—n—g— —l—i—s—t— —m—a—t—c—h—e—s— —t—h—e— —c—o—u—r—s—e—'—s— —l—e—v—e—l— —a—n—d— —r—e—c—e—n—c—y— —n—e—e—d—.— —P—a—r—s—e—s— —t—h—e— —s—y—l—l—a—b—u—s— —t—o— —e—x—t—r—a—c—t— —t—o—p—i—c—s— —a—n—d— —l—e—a—r—n—i—n—g— —o—u—t—c—o—m—e—s—,— —s—e—a—r—c—h—e—s— —C—o—n—s—e—n—s—u—s— —f—o—r— —r—e—c—e—n—t— —p—e—e—r—-—r—e—v—i—e—w—e—d— —p—a—p—e—r—s— —p—e—r— —t—o—p—i—c—,— —a—n—d— —p—r—o—d—u—c—e—s— —a— —p—r—o—f—e—s—s—i—o—n—a—l—l—y— —f—o—r—m—a—t—t—e—d— —.—d—o—c—x— —w—i—t—h— —c—l—i—c—k—a—b—l—e— —C—o—n—s—e—n—s—u—s— —l—i—n—k—s—,— —p—l—a—i—n—-—l—a—n—g—u—a—g—e— —s—u—m—m—a—r—i—e—s— —c—a—l—i—b—r—a—t—e—d— —t—o— —a—u—d—i—e—n—c—e— —l—e—v—e—l—,— —a—n—d— —B—l—o—o—m—-—h—i—g—h—e—r—-—o—r—d—e—r— —d—i—s—c—u—s—s—i—o—n— —q—u—e—s—t—i—o—n—s— —t—i—e—d— —t—o— —c—o—u—r—s—e— —l—e—a—r—n—i—n—g— —g—o—a—l—s—.— —U—s—e— —w—h—e—n— —t—h—e— —u—s—e—r— —u—p—l—o—a—d—s— —a— —s—y—l—l—a—b—u—s—,— —c—o—u—r—s—e— —o—u—t—l—i—n—e—,— —o—r— —c—u—r—r—i—c—u—l—u—m— —d—o—c—u—m—e—n—t— —a—n—d— —w—a—n—t—s— —s—u—p—p—l—e—m—e—n—t—a—r—y— —r—e—a—d—i—n—g—s— —(—e—.—g—.—,— —'—c—r—e—a—t—e— —a— —r—e—a—d—i—n—g— —l—i—s—t— —f—r—o—m— —t—h—i—s— —s—y—l—l—a—b—u—s—'—,— —'—f—i—n—d— —r—e—c—e—n—t— —p—a—p—e—r—s— —f—o—r— —m—y— —c—o—u—r—s—e—'—)— ——— —e—v—e—n— —c—a—s—u—a—l— —m—e—n—t—i—o—n—s— —w—i—t—h— —a— —s—y—l—l—a—b—u—s— —a—t—t—a—c—h—e—d— —s—h—o—u—l—d— —t—r—i—g—g—e—r— —t—h—i—s— —s—k—i—l—l.
license: MIT
metadata:
  source_spec: "megaprompts/10-syllabus-megaprompt.md"
  build_pattern: "Path B (direct conversion)"
  research_pack_convention: "Agent Integrity Rules verbatim per PR #657 audit; bundled-JS-DOCX-generator variant"
  version: 1.0.0
---

# Syllabus — Course Supplementary Reading List

> **Portability:** Requires a Consensus MCP connection, Node.js with `docx` package, and file reading capability for the syllabus. Works in Claude Code CLI natively. In Claude.ai with Consensus MCP + Code Execution + file upload, the workflow is supported.

For an instructor or student with a course syllabus, produce a professional supplementary reading list as `.docx` containing recent peer-reviewed papers per course section.

## Architectural Pattern: Bundled Script

This skill uses a **bundled JavaScript helper script** for DOCX generation rather than inlining the 300+ lines of layout code:

- DOCX generation logic is reusable + complex
- Better separation of concerns: skill = orchestration + intelligence; script = mechanical document assembly
- Token-efficient: skill doesn't re-derive layout each run
- Easier to maintain and version

The bundled script is at `scripts/generate_reading_list.js`. The skill orchestrates the pipeline + invokes the script with JSON input.

## Agent Integrity Rules (Research-Pack Convention)

Locked verbatim per PR #657 audit.

- **Only use what Consensus returns.** Every paper title, author, journal, year, URL must come from this session's tool calls. Training-knowledge papers labeled `[Not from Consensus — model knowledge]` and excluded.
- **Confirm before moving on.** A search isn't complete until response received and inspected.
- **Track three counts.** Queries sent / papers received / papers cited. Surface in audit summary.
- **Surface gaps, don't fill them.** Section with one paper + note about limited results > section padded with fabrications.

## Phase 0: Grill-Me Intake (3 forcing questions)

### Q1 (root) — Syllabus input

> **Provide the syllabus — pick one:**
>
> 1. File path (PDF, DOCX, text) — I'll read it
> 2. Pasted content — paste below
> 3. Image of a printed syllabus — attach the image
>
> *Why I'm asking:* Each format needs a different reader (PDF / DOCX parser / vision). Picking upfront prevents wasted attempts.

Forcing choice. Refuse to start without a syllabus.

### Q2 (depends on Q1) — Course audience

> **Course audience — pick one:**
>
> 1. Undergraduate (intro level)
> 2. Undergraduate (advanced / upper division)
> 3. Graduate (Masters / early PhD)
> 4. Graduate (doctoral / advanced)
> 5. Professional / continuing education
> 6. Mixed
>
> *Why I'm asking:* Audience dictates summary jargon level and discussion-question complexity. Undergrad summaries define every term; grad summaries assume technical fluency. Discussion questions for undergrads test analysis; for grads test critique and extension.

See [`references/audience_calibration.md`](references/audience_calibration.md) for the canon.

### Q3 (depends on Q1) — Year range

> **Year range for papers — pick one:**
>
> 1. Last 1 year (most recent only)
> 2. Last 2 years (default — recent + a year of context)
> 3. Last 5 years (broader, includes foundational recent work)
>
> *Why I'm asking:* Reading lists go stale fast. 1-year filters keep things fresh; 5-year filters surface foundational recent work that's already standard. Drives the year_min parameter on every Consensus search.

Forcing choice with default (last 2 years).

**Stop condition:** 3 questions max before Phase 1. The post-Phase-2 group-and-confirm checkpoint is its own grill-me moment.

## Phase 1: Parse the Syllabus

Per Q1 input format:

- **PDF**: use PDF reader; extract text
- **DOCX**: use pandoc or DOCX parser; extract text
- **Text/pasted**: read directly
- **Image**: use vision; extract text

From extracted text:
1. Course title + instructor + term
2. Topic list (lecture titles, week-by-week breakdown, etc.)
3. Learning outcomes (if explicit; if missing, infer 3-5 from description)

Mark inferred learning outcomes as `[inferred]` in the DOCX.

## Phase 2: Group Topics + Confirm with User

### Group via topic_grouper.py

Use `scripts/topic_grouper.py` to cluster related topics into 6-12 sections. Heuristic: closely-related topics merge; cross-cutting topics get their own section.

### Group-and-Confirm Checkpoint (Forcing Options)

After grouping, present:

> **Proposed sections: [list with item counts]. Pick one:**
>
> 1. "Looks good — proceed with these sections"
> 2. "Merge sections [X] and [Y]"
> 3. "Split section [X] into two"
> 4. "Add a section for [topic]"
> 5. "Remove section [X]"
>
> *Why I'm asking:* Grouping drives search allocation. Wrong grouping wastes the search budget on bad clusters. This is the **last cheap moment** to correct course before searches consume Consensus calls.

**Refuse to start Phase 3 without explicit user choice.**

## Phase 3: Search Consensus per Section

Sequential, 1 q/sec. 1-2 queries per section.

### Applied-Domain Weaving (Critical)

Don't just search the topic — **search the topic + applied domain**:

| ❌ Generic | ✅ Applied-domain |
|---|---|
| "enzyme kinetics" | "enzyme kinetics food processing applications" |
| "machine learning" | "machine learning clinical decision support" |
| "thermodynamics" | "thermodynamics renewable energy systems" |
| "social network analysis" | "social network analysis public health interventions" |

Boosts paper relevance dramatically. See [`references/applied_domain_weaving.md`](references/applied_domain_weaving.md) for the canon.

### Per-Section Pattern

```
For each section:
  1. Construct query: "{topic-keywords} {applied-domain-angle}" + year_min from Q3
  2. Submit to Consensus (sequential, 1 q/sec gap enforced by citation_tracker)
  3. Receive results
  4. (If thin) submit one fallback query without applied-domain angle
  5. Select 1-3 papers per section (15-25 total across all sections)
```

### Selection Priorities

1. **Relevance** — paper directly addresses the section topic
2. **Reviews / meta-analyses** — synthesize the field
3. **Citation count** — established work
4. **Applied-domain connection** — tied to the course's domain (e.g., engineering vs theory)

## Phase 4: Write Summaries + Discussion Questions

### Summary writing

Per paper:
- Plain language (calibrated to audience from Q2)
- 2-3 sentences
- Define jargon if undergraduate audience; assume fluency if graduate

### Quality bars

| ✅ Good summary | ❌ Bad summary |
|---|---|
| "This review maps how different diets — Mediterranean, Nordic, vegetarian — reshape the types of fat molecules circulating in your blood, with implications for heart disease risk." | "This paper reviews lipidomic profiles across dietary interventions and their cardiometabolic implications." |

### Discussion question writing

Per paper:
- Bloom **higher-order** (apply / analyze / evaluate)
- Tied to a specific course learning outcome
- Promotes discussion, not just recall

| ✅ Good question | ❌ Bad question |
|---|---|
| "If dietary fat quality can reshape your lipoprotein lipidome, what does this suggest about the biochemical basis for dietary guidelines recommending unsaturated over saturated fats?" | "What did the authors find?" (Just recall) |

Use `scripts/discussion_question_validator.py` to flag recall-only questions.

## Phase 5: Generate .docx via Bundled Script

```bash
node scripts/generate_reading_list.js \
  --input /tmp/syllabus_data.json \
  --output /path/to/reading_list_<course>_<date>.docx
```

The script accepts JSON with this schema:

```json
{
  "courseTitle": "string",
  "courseSubtitle": "string",
  "generatedDate": "string",
  "yearRange": "string",
  "introText": "string",
  "learningOutcomes": ["string", ...],
  "sections": [
    {
      "heading": "string",
      "papers": [
        {
          "title": "string",
          "authors": "string",
          "journal": "string",
          "year": number,
          "url": "string",
          "summary": "string",
          "question": "string"
        }
      ]
    }
  ],
  "auditLog": {
    "totalQueriesSent": number,
    "totalPapersReceived": number,
    "totalPapersCited": number,
    "toolConstraints": "string",
    "searchDetails": [
      {
        "section": "string",
        "query": "string",
        "papersReturned": number,
        "papersSelected": number,
        "status": "string"
      }
    ],
    "failures": []
  }
}
```

The script handles:
- `docx` package require with multi-location fallback
- Title page, intro with Consensus link, learning outcomes box, numbered papers per section
- `ExternalHyperlink` with full Consensus URLs (never truncated)
- `LevelFormat.BULLET` for lists (not unicode bullets)
- Footer with generation metadata
- Input validation (missing fields → graceful error)

See [`references/bundled_script_pattern.md`](references/bundled_script_pattern.md) for why bundled vs inline.

## Phase 6: Deliver

- File path
- Audit summary in chat: "Saved {file}. {N} sections × {M} papers / {K} cited. Plan tier: {tier}."
- Validate: check zip integrity with `python3 -c "import zipfile,sys; zipfile.ZipFile(sys.argv[1]).testzip()" <docx>` (no output = intact), then confirm the required sections are present

## Tooling

| Script | Role |
|---|---|
| `scripts/citation_tracker.py` | Consensus three-count audit + 1s sequential discipline at `~/.syllabus_sessions/<session>.json` |
| `scripts/topic_grouper.py` | Heuristic 6-12 section grouping from extracted topics |
| `scripts/discussion_question_validator.py` | Bloom higher-order quality check; flags recall-only questions |
| `scripts/generate_reading_list.js` | **Bundled Node.js DOCX generator** — JSON input → .docx output |

## References

- [`references/applied_domain_weaving.md`](references/applied_domain_weaving.md) — search-quality canon (7+ sources)
- [`references/audience_calibration.md`](references/audience_calibration.md) — undergrad vs grad summary jargon (7+ sources)
- [`references/bundled_script_pattern.md`](references/bundled_script_pattern.md) — why bundle vs inline (7+ sources)

## Error Handling

| Failure | Behavior |
|---|---|
| Consensus rate-limit hit | Wait 3s, retry once, log |
| Search returns 0 for a section | Note section as "limited results — consider manual supplementation" |
| 3 consecutive failures | Stop, alert user, share collected so far |
| `docx` package not installed | Script attempts `npm install`; if still failing, fail with clear message |
| DOCX validation fails | Unpack XML, log issue, ask user to retry |
| Syllabus format unsupported | List supported formats, ask user to convert |
| Learning outcomes can't be extracted | Infer 3-5 from course description; mark as inferred in document |

## Anti-Patterns To Reject

- Parallelizing Consensus calls (rate limit)
- Searching topics without applied-domain angle (poor relevance)
- Padding sections with fabricated entries when Consensus returns thin
- Generic discussion questions ("What did the authors find?")
- Jargon-heavy summaries unsuitable for the course's audience level
- Skipping the group-and-confirm step (wastes searches)
- Truncating Consensus URLs in hyperlinks
- Inlining 300 lines of docx-generation JavaScript in the skill body (use bundled script)

---

**Version:** 1.0.0
**Source spec:** [`megaprompts/10-syllabus-megaprompt.md`](../../../../megaprompts/10-syllabus-megaprompt.md)
**Build pattern:** Path B (direct conversion). Bundled-JS-DOCX-generator variant.
