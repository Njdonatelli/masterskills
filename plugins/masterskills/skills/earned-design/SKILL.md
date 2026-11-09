---
name: earned-design
description: Decision protocol for any visual output (page, dashboard, deck, doc, chart). Derives each open choice from subject, audience and intent so it stops reading as AI-made. Yields to design systems.
---

# Earned design

Output reads as AI-made when its choices are **defaults**: the nearest option for the category, taken with no reason from this subject. A tell (the purple gradient, the cream page with one italic word, four equal cards) is the fossil of a default. Removing a tell without making the decision behind it installs the neighbouring default, and that one becomes next year's tell. So this protocol produces decisions. The tells are a diagnostic you run on the render afterwards.

A choice is **earned** when you can finish "because this subject / this audience / this intent ..." with a clause that would be false for a different brief.

Applies to anything a person will look at: page, app screen, dashboard, deck, document, chart, diagram, image. For a full UI build, load `ui-craft` (new) or `impeccable` (existing) after step 2 and hand them the read as their brief. For a critique of finished work, use `tastemaker`.

## 1. Sort fixed from open

List what is already decided: a governing design system, a brand, a pinned reference, an aesthetic the user stated, the host's template. Fixed things win in full. Applying them is following the brief, and they are never defaults, whatever a tells list says about them.

Everything else is open. Under a design system the open set is still most of the work: what leads, what is cut, structure, density, how numbers are shown, the copy, which single element gets the accent, what moves.

Done when you can name both lists.

## 2. Write the read

Three lines, before any layout:

- **Subject**: the one fact that makes this thing itself and not its category.
- **Scene**: who looks at it, where, in what state, how often.
- **Intent**: the one thing they do or know when they leave.

Take them from the material you were given. Done when each line would be wrong for a neighbouring brief.

## 3. Rank

Order the content by what the scene needs first. One thing leads at a visibly different scale, the rest step down, and whatever serves no line of the read is cut. Equal weight means the ranking was skipped: four same-size cards, six same-length bullets, three matching columns.

The lead is usually the thing that needs action (the exception, the change, the deadline), which is often not the biggest number.

The intent line gets a place on the first screen: the action, and how to take it, in plain words.

Done when you can point to where the eye lands first and give the reason from the read.

## 4. Decide each open axis

The axes: ground and colour, type, structure, imagery, copy voice, motion. For each one that is open:

1. Name the **default**: what this category always gets.
2. Name the **escape**: what you get by merely avoiding the default. It is the next default, already spent.
3. Name your **reflex**: the first face, ground and accent that came to mind. You reach for the same ones on every brief, so they are defaults whatever reason you can attach. Set them aside.
4. Choose from the matching part of the subject's own world: colour from its materials and places, lettering from its signage and print, structure from how its audience already reads this kind of information, imagery from its real objects.
5. Run the **swap test**: put a different organisation's name on it. A choice that survives the swap unchanged is still a default. Redo it.

Take qualities from that world, not replicas of its objects. A page dressed as a form, a ticket, a label or a terminal is a **costume**, and a costume is the same move on every brief. A replica earns a place only as one element, where the object is something the reader will actually handle.

Convention can be earned. An operator who opens a screen every morning wants a quiet, familiar table, and choosing that for that reason passes.

Spend on **one move**: a single idea that carries the subject, executed completely. Write three candidates before choosing. The first is usually the brief's own metaphor (a tool library becomes a library card); everyone reaches it, so it stays only if it beats the other two.

The move carries the content and never costs it: every fact stays as easy to find and read as it would be in plain type, the output is no longer than its content needs, and no copy explains the design. Keep every other axis quiet. Quiet still means finished spacing, alignment and scale. Where there is nothing to say, leave space.

Done when each open axis has a one-clause "because" that fails the swap.

## 5. Make the content true and specific

- Numbers have shape: unit, period, comparison, source. "9 late, up from 4 last week" carries more than "+125%".
- Each line of copy says something only this subject can say. A line that fits a competitor is rewritten or cut. Say each thing once.
- Proof is real or absent. Reviews, logos, customer counts, quotes and performance claims come from the material, never from you. Label sample data as sample.
- Call things what the audience calls them.
- A fact the material lacks (how to sign up, where to send an approval) stays a marked gap and goes in your report to the user. A plausible guess is never printed as fact.

## 6. Render, look, diagnose

Render the output and look at the image: first screen, full length, narrow width; every slide of a deck; page one of a document.

1. Squint. The eye lands where step 3 said it would.
2. Repeat the swap test on the render.
3. Read [references/tells.md](references/tells.md) and check each row. For every hit that is neither fixed by the system nor earned, find the decision it stands in for and make that decision. Restyling the symptom installs the escape.
4. Set check, when you have made more than one output: put them side by side. Two unrelated briefs that share ground, type voice and structure, or the same kind of move, were given a style, not a decision. Rerun step 4 on the later one.
5. If anything moves, apply [references/motion.md](references/motion.md).

Done when the squint and the swap pass on the render and every remaining tell has its "because".

## Medium notes

- **Deck**: one claim per slide, written as the slide title. Rank across the whole deck, not only within a slide. The intent line is the last slide.
- **Document**: the finding and the ask come first. Structure carries it: a tight table before a card grid, a number before an adjective.
- **Chart**: the title states the finding. One series carries the accent. Label directly.
- **Dashboard**: the lead is what changed or needs action today. Stable totals are secondary.

## Reporting

Give the user the read and the one move in two lines. The work shows the rest.
