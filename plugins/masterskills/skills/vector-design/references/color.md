# Color Systems

## Using OKLCH

- oklch is preferred over hex codes during design. It's perceptual, maintains consistent lightness across hues, and prevents muddy muddy gradients.
- For print PDFs, explicitly pair the CMYK equivalent in a code comment.
  `<!-- Brand Orange: oklch(65% 0.2 40) | CMYK 0/55/85/0 | RGB #E8753A -->`

## Print Limitations

- CMYK model limits vividness. Out-of-gamut reds, bright oranges, and neon greens often look dull.
- Total Ink Limit should not exceed 300% in deep blacks (e.g. use C:60 M:40 Y:40 K:100 vs C:100 M:100 Y:100 K:100).
- When a client demands a specific brand, utilize Pantone or Spot layers in comments.

## Avoiding AI Slop Color Usage

- **DO NOT** use purple-to-blue diagonal gradients.
- **DO NOT** use cyan accents on dark navy.
- **DO NOT** throw pure white text on saturated bright backgrounds without checking WCAG contrast.
- Prefer grounded, restricted palettes.
