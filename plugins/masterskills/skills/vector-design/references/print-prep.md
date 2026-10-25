# Print Preparation Checklist

## Bleed

- The standard is **3mm** on all sides. (Or 5mm depending on the printer).
- If the final artboard is 100x100mm, the viewBox MUST support bleed: `-3 -3 106 106`. Fill backgrounds from x=-3, y=-3 spanning width 106 and height 106.

## Safe Zone

- Keep important text and logos **5mm inside** the trim edge.
- In a 100x100mm trim canvas, vital content stays between coordinates (5,5) and (95,95).

## Resolution & Physical Size

- `1 unit = 1mm` in this harness coordinate system.
- Sticker rounds: radii 50mm, 75mm, 100mm.
- Business card: 85×55mm (plus 3mm bleed = 91x61).
- Resolution defaults to 150dpi for `preview.png`, but prints at 300dpi.

## File Handoff

- Embed fonts.
- Bleeds must be covered by shapes.
- Check crop mark export via scripts.
