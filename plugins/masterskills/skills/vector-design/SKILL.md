---
name: vector-design
description: Vector graphics design tool - create SVG logos, mascots, icons with render-critique-export loop. Write SVG directly, render previews, get automated critique, export to print-ready PDF. Trigger: /vector [command] or describe any vector graphics task (logo, mascot, icon, poster, etc.)
---

# vector-design

Write SVG directly, render previews, get automated critique, export to print-ready PDF. No libraries, no API — just raw SVG and a render loop.

## What This Does

- **Create SVG designs** directly — logos, mascots, icons, posters, brand assets
- **Render previews** — see what your SVG looks like as PNG
- **Automated critique** — lint checks for common SVG problems
- **Export to PDF** — print-ready output via Inkscape

## Quick Start

```bash
# Create a new design
python render.py --create my-logo

# Edit the SVG
# Open vector-designs/my-logo/canvas.svg and write your SVG

# Preview
python render.py --design my-logo

# Get critique
python critique.py --design my-logo

# Export to PDF
python export.py --output my-logo.pdf --design my-logo
```

## Commands

| Command | Purpose |
|---------|--------|
| `python render.py --create name --brief` | Create + gather brief interactively |
| `python render.py --design name` | Render SVG → PNG |
| `python render.py --list` | List all designs |
| `python critique.py --design name` | Critique design |
| `python export.py --output file.pdf --design name` | Export to PDF |

## Design Organization

Designs live in `vector-designs/[brand]/[variation]/`:

```
vector-designs/
├── client-logo/
│   ├── logo-main/
│   ├── logo-inverted/
│   └── icon/
├── client-poster/
│   ├── poster-sale/
│   └── poster-event/
```

Nested folders work: `python render.py --create client-logo/icon`

## SVG Conventions

- **Units**: `viewBox="0 0 80 80"` = 80mm at 1 unit = 1mm
- **Pixel size**: Use 800×800 for preview (1mm = 10px at 150dpi render)
- **IDs**: Always label elements with `id="element-name"`
- **Text**: Use `<tspan>` for line breaks (SVG doesn't wrap)

```svg
<svg width="800" height="800" viewBox="0 0 80 80" xmlns="http://www.w3.org/2000/svg">
  <rect id="background" width="80" height="80" fill="#1A365D"/>
  <text id="logo-text" x="40" y="45" text-anchor="middle">MY BRAND</text>
</svg>
```

## Design Loop (Mandatory)

1. **BRIEF**: Gather requirements — inspiration, colors, mood
2. **CREATE**: `python render.py --create brand/variation`
3. **DRAFT**: Write SVG to `vector-designs/[name]/canvas.svg`
4. **RENDER**: `python render.py --design [name]`
5. **INSPECT**: Open preview.png, check visually
6. **CRITIQUE**: `python critique.py --design [name]`
7. **FIX**: Address all FAIL/WARN items
8. **REPEAT** until score ≥ 80
9. **EXPORT**: `python export.py --output [name].pdf --design [name]`

---

## Brief Gathering (Required BEFORE Creating)

**Never start designing without understanding:**

### Step 1: Collect Inspiration

Ask the user for:
1. **References** — Any logos/brands they like? (URLs or names)
2. **What to avoid** — Any styles they hate?
3. **Colors** — Any brand colors to use? Or preferences?
4. **Mood** — 3 keywords describing desired feel

### Step 2: Document the Brief

Before creating, write to `vector-designs/[name]/BRIEF.md`:

```markdown
# Brief: [Brand Name]

## inspiration
- Likes: [reference 1], [reference 2]
- Avoid: [styles to skip]

## colors
- Primary: [hex or name]
- Accent: [hex or name]
- Avoid: [colors to avoid]

## mood
- Keywords: [keyword 1], [keyword 2], [keyword 3]

## notes
[Any specific requirements]
```

### Step 3: Show Direction Swatches

Before full design:
- Create 3 small SVG swatches (50x50mm) in the canvas
- One swatch per direction that matches the brief
- Get user to pick ONE direction
- THEN execute full design

## When the Brief is Vague

**DO NOT start designing until you understand the brand.**

### Step 1: Ask These 3 Questions

1. **Industry/Type**: What does this brand do? (fashion, tech, food, lifestyle, etc.)
2. **Audience**: Who is the target? (young professionals, families, luxury buyers, etc.)
3. **Mood**: What's the vibe?

   - Bold/Agressive — sporty, energy drinks, fitness
   - Luxurious — premium brands, jewelry, high-end services
   - Playful — kids, toys, casual food/餐饮
   - Trustworthy — finance, legal, medical
   - Minimal — tech SaaS, modern startups

### Step 2: Propose 3 Brand-Specific Directions

Match the mood to design philosophy:

| Mood | Direction 1 | Direction 2 | Direction 3 |
|------|-------------|-------------|-------------|
| Bold | Constructivist (red/black/diagonals) | Bauhaus (geometric/shapes) | Kinetic (motion/speed) |
| Luxurious | Art Deco (gold/ornament) | Swiss (minimal/premium) | Contemporary (editorial) |
| Playful | Organic (rounded/earthy) | Retro Letterpress (texture) | Maximalist (colorful) |
| Trustworthy | Corporate Modernism | Swiss (clean grid) | Japanese Minimal |
| Minimal | Japanese Minimal | Swiss | Corporate Modernism |

### Step 3: Visual Examples

Before drafting, create 3 small SVG swatches (one per direction) in the canvas to show the user. Ask them to pick ONE before proceeding to full design.

**Never create full designs from multiple directions simultaneously** — waste of effort. Get alignment first.

### Example Interaction

```
You: For this fashion brand targeting young professionals, I recommend:
1. Constructivist — bold diagonals, high energy
2. Art Deco — gold accents, premium feel  
3. Minimal Swiss — clean, modern

Which direction feels right for the brand?
User: I like the first one
You: Great, I'll develop the constructivist direction...
```

## Brand Asset Protocol

When working with a specific brand:
1. Gather: Get all logos, colors, fonts from brief
2. Extract: Read exact color values from provided SVGs
3. Verify: Confirm values against brand guidelines
4. Document: Write to DESIGN_LOG.md in the design folder
5. Use: Only use extracted brand values

## Enhanced Critique (Anti-Slop)

The critique.py now catches AI/generic patterns:

**FAILS (score -20 each)**:
- Purple-to-blue gradients (AI generic signature)
- Over-complex shapes (10+ shapes, not scalable)

**WARNINGS (score -5 to -15)**:
- Too many colors (>5, not restrained)
- Excessive centered text (>3, generic layout)
- All rounded rectangles (AI modern look)
- Missing element IDs

**PASS indicators**:
- Good typography hierarchy (size contrast)
- Color economy (≤5 colors)
- Balanced composition

**Score thresholds**:
- 90+: [EXCELLENT] — premium, unique
- 75-89: [GOOD] — usable, minor fixes
- 60-74: [NEEDS WORK] — should revise
- <60: [REVISIONS NEEDED] — major problems

Run critique before every export. Minimum score: 80

## Requirements

- `resvg-py` — for rendering (runs via `uv run --with resvg-py`)
- `inkscape` — optional, for PDF export

```bash
uv run --with resvg-py render.py --check
```

## Notes for Agents

- Always label elements with meaningful IDs — critique checks for this
- Never regenerate entire SVG for small fixes — edit by ID
- Render → inspect → critique → fix is mandatory before declaring done
- Use `references/directions.md` when style is unclear
- When brief is vague: ASK 3 QUESTIONS first (industry, audience, mood)
- Show direction swatches, get user pick BEFORE full design