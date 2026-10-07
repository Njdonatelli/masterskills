---
name: "interview-system-designer"
description: >-
  T—h—i—s— —s—k—i—l—l— —s—h—o—u—l—d— —b—e— —u—s—e—d— —w—h—e—n— —t—h—e— —u—s—e—r— —a—s—k—s— —t—o— —"—d—e—s—i—g—n— —i—n—t—e—r—v—i—e—w— —p—r—o—c—e—s—s—e—s—"—,— —"—c—r—e—a—t—e— —h—i—r—i—n—g— —p—i—p—e—l—i—n—e—s—"—,— —"—c—a—l—i—b—r—a—t—e— —i—n—t—e—r—v—i—e—w— —l—o—o—p—s—"—,— —"—g—e—n—e—r—a—t—e— —i—n—t—e—r—v—i—e—w— —q—u—e—s—t—i—o—n—s—"—,— —"—d—e—s—i—g—n— —c—o—m—p—e—t—e—n—c—y— —m—a—t—r—i—c—e—s—"—,— —"—a—n—a—l—y—z—e— —i—n—t—e—r—v—i—e—w—e—r— —b—i—a—s—"—,— —"—c—r—e—a—t—e— —s—c—o—r—i—n—g— —r—u—b—r—i—c—s—"—,— —"—b—u—i—l—d— —q—u—e—s—t—i—o—n— —b—a—n—k—s—"—,— —o—r— —"—o—p—t—i—m—i—z—e— —h—i—r—i—n—g— —s—y—s—t—e—m—s—"—.— —U—s—e— —f—o—r— —d—e—s—i—g—n—i—n—g— —r—o—l—e—-—s—p—e—c—i—f—i—c— —i—n—t—e—r—v—i—e—w— —l—o—o—p—s—,— —c—o—m—p—e—t—e—n—c—y— —a—s—s—e—s—s—m—e—n—t—s—,— —a—n—d— —h—i—r—i—n—g— —c—a—l—i—b—r—a—t—i—o—n— —s—y—s—t—e—m—s.
---

# Interview System Designer

Comprehensive interview loop planning and calibration support for role-based hiring systems.

## Overview

Use this skill to create structured interview loops, standardize question quality, and keep hiring signal consistent across interviewers.

## Core Capabilities

- Interview loop planning by role and level
- Round-by-round focus and timing recommendations
- Suggested question sets by round type
- Framework support for scoring and calibration
- Bias-reduction and process consistency guidance

## Quick Start

```bash
# Generate a loop plan for a role and level
python3 scripts/interview_planner.py --role "Senior Software Engineer" --level senior

# JSON output for integration with internal tooling
python3 scripts/interview_planner.py --role "Product Manager" --level mid --json
```

## Recommended Workflow

1. Run `scripts/interview_planner.py` to generate a baseline loop.
2. Align rounds to role-specific competencies.
3. Validate scoring rubric consistency with interview panel leads.
4. Review for bias controls before rollout.
5. Recalibrate quarterly using hiring outcome data.

## References

- `references/interview-frameworks.md`
- `references/bias_mitigation_checklist.md`
- `references/competency_matrix_templates.md`
- `references/debrief_facilitation_guide.md`

## Common Pitfalls

- Overweighting one round while ignoring other competency signals
- Using unstructured interviews without standardized scoring
- Skipping calibration sessions for interviewers
- Changing hiring bar without documenting rationale

## Best Practices

1. Keep round objectives explicit and non-overlapping.
2. Require evidence for each score recommendation.
3. Use the same baseline rubric across comparable roles.
4. Revisit loop design based on quality-of-hire outcomes.
