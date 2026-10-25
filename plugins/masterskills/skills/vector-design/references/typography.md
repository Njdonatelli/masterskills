# Typography Rules & Fundamentals

## Font Stacks for Print

- Avoid relying on Google Fonts referencing via `<style>@import...` for print. They will fail in Inkscape CLI unless locally installed.
- Ensure typefaces are embedded as Base64 data URIs or use widely supported system fonts: `Helvetica`, `Arial`, `Times`, `Courier`, `Georgia`.

## Modular Scale Ratios

- Use explicit scale ratios: 1.25 (Minor Third), 1.414 (Augmented Fourth), 1.618 (Golden Ratio).
- Don't guess text sizing—stick to the scale.

## Minimum Sizes

- At 300dpi outputs, the absolute minimum size for body print is **6pt**, and caption is **8pt**.

## Structural Rules

- **SVG text does not wrap:** You must manually break lines. Measure your character counts, calculate line breaks, and generate `<tspan x="..." dy="1.2em">` sequences.
- Use explicit display vs text faces.

## Typographic Crimes (AVOID)

1. Using Inter or DM Sans as a display/headline face.
2. All-caps with default tracking. (Always add tracking/letter-spacing to caps).
3. Mixing more than two type families.
4. Text centered on a dark background without appropriate high-contrast weight.
5. Decorative fonts used for body copy.
