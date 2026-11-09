# Motion: checked numbers

Motion is an open axis like any other. First decide whether the thing should move at all: it earns motion when the movement shows state, cause or spatial relationship. Then use the numbers below.

A governing design system's motion tokens win over this table. These numbers fill what the system leaves open. For easing curves, springs, choreography and performance, `ui-craft/references/motion.md` is the full reference; this file holds only the values checked for this skill and how far to trust each.

Confidence: **A** stated in a primary source. **B** consistent with primary sources or published design systems. **C** from a single short video, unconfirmed; tune by eye.

| Rule | Value | Conf. | Source |
| --- | --- | --- | --- |
| Entrances and exits | `ease-out`, ideally a custom curve | A | Kowalski |
| Elements already on screen that move | `ease-in-out` | A | Kowalski |
| Dropdowns, tooltips, popovers | 150-250 ms; everyday UI stays under 300 ms | B | Kowalski skills |
| Press feedback | `scale(0.97)` on `:active`, about 100-160 ms | A | Kowalski |
| Enter scale | from `scale(0.95)` with `opacity: 0`; never from `scale(0)` | A | Kowalski skills |
| Popover origin | `transform-origin` at the trigger, on enter and exit. Modals stay centred | A | Kowalski |
| Exit vs enter | exit 20-35% shorter (250 in / 200 out) | A | Material 3, Atlassian |
| Everyday UI springs | no overshoot; bounce only after a gesture that carried momentum | B | Apple, via Kowalski |
| Dragging | track the pointer 1:1; no easing while held | B | Apple, via Kowalski |
| Past a drag limit | diminishing resistance, then return | B | Apple, via Kowalski |
| List stagger | 30-80 ms between siblings; start at 30 | B | ui-craft |
| Shared element | one element morphs (`layoutId`, View Transitions, FLIP) | B | ui-craft |
| State swap | old and new overlap; no blank frame between | B | ui-craft |
| Icon swap | scale, opacity and a few px of blur together | B | ui-craft |
| Reveals and colour inversion | `clip-path` mask in place of a crossfade | B | Kowalski skills |
| Secondary detail settles after its parent | about 50 ms later | C | video |
| Moving toggle knob | stretches about 12% mid-travel | C | video |
| Object crossing the canvas | curved path, about 32 px of arc | C | video |
| Success | one pulse, once | C | video |

Always ship `prefers-reduced-motion` with the animation: the user still arrives at the right end state.

## Sources

- Emil Kowalski, "7 practical animation tips": https://emilkowal.ski/ui/7-practical-animation-tips
- Emil Kowalski, skills repository (emil-design-eng, apple-design): https://github.com/emilkowalski/skills
- Material Design, "Duration & easing" (objects leaving the screen take shorter durations): https://m1.material.io/motion/duration-easing.html
- Material Components motion duration tokens (200 ms and 250 ms slots): https://github.com/material-components/material-components-android/blob/master/docs/theming/Motion.md
- Atlassian Design, "Applying motion" (exits 50-100 ms shorter than entrances): https://atlassian.design/foundations/motion/applying-motion
- Apple, "Designing Fluid Interfaces", WWDC 2018 (read here through Kowalski's apple-design summary, not directly)
