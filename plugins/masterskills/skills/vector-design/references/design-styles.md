# Design Philosophies — Complete Reference

Each philosophy is a complete design system. Choose ONE and execute fully. Do not mix.

---

## 1. Constructivist (推荐: Bold brands)

**Philosophy**: Design as propaganda. Bold, loud, unapologetic.

**Colors**: 
- Primary Red: #E63946
- Black: #0D0D0D  
- White: #F4F4F4

**Elements**:
- Diagonal lines at 45°
- Sharp angles (no curves)
- Asymmetric composition
- Type at slight angles (2-5°)
- Overlapping shapes
- High contrast

**Typography**:
- Condensed bold caps
- Helvetica Black, Arial Black
- Tight tracking (-0.02em)

**Don't use**: Rounded corners, gradients, centered text

**Example**: Energy drinks, sports brands, streetwear

```svg
<!-- Structure -->
<rect fill="#0D0D0D"/>
<polygon fill="#E63946" points="0,80 30,80 0,50"/>
<text font-weight="900" transform="rotate(-3)">BRAND</text>
```

---

## 2. Swiss International

**Philosophy**: Grid + hierarchy = trust. Clean, objective, timeless.

**Colors**:
- Black: #000000
- White: #FFFFFF
- One accent: #E63946 or #1A365D

**Elements**:
- Strict grid alignment
- Flush-left text
- Size = importance
- Generous negative space
- Horizontal rules/lines

**Typography**:
- Helvetica, Akzidenz-Grotesk, Arial
- Left aligned
- Clear size hierarchy (3 sizes max)

**Don't use**: Centered text, gradients, decorative elements

**Example**: Financial services, architecture, cultural institutions

```svg
<!-- Structure -->
<rect fill="#FFFFFF"/>
<line x1="10" y1="20" x2="10" y2="70" stroke="#000000" stroke-width="8"/>
<text x="20" font-size="24">HEADLINE</text>
<text x="20" font-size="12">Body text aligned left</text>
```

---

## 3. Bauhaus Geometric

**Philosophy**: Form follows function. Shapes speak.

**Colors** (Primary + Neutrals):
- Red: #E63946
- Blue: #1A365D
- Yellow: #D69E2E
- Black/White

**Elements**:
- Circle + square + triangle
- Type as architecture (integrated with shapes)
- No decoration
- Flat, bold shapes

**Typography**:
- Bold sans-serif
- Integrated with geometry

**Don't use**: Gradients, shadows, photos

**Example**: Design studios, furniture, art schools

---

## 4. Japanese Minimal

**Philosophy**: Absence is presence. Less, but better.

**Colors**:
- Off-white: #FAFAFA
- Charcoal: #333333
- One accent: #E63946 (sparingly)

**Elements**:
- 80%+ negative space
- Single focal element
- Thin lines
- Hidden depth (not obvious)
- Restrained

**Typography**:
- Clean sans-serif
- Lots of whitespace around text

**Don't use**: Many elements, bold colors, gradients

**Example**: Tech SaaS, wellness, Japanese restaurants

---

## 5. Art Deco

**Philosophy**: Luxury through geometry. Glamour + structure.

**Colors**:
- Gold: #D4AF37
- Black: #0D0D0D
- Cream: #F5F5DC

**Elements**:
- Symmetry (vertical axis)
- Geometric ornament (sunburst, fan patterns)
- Tall condensed caps
- Vertical lines
- Stepped borders

**Typography**:
- Condensed serif or slab
- Didot, Bodoni, or custom condensed

**Don't use**: Asymmetry, handwritten, casual

**Example**: Luxury hotels, jewelry, premium real estate

---

## 6. Contemporary Editorial

**Philosophy**: Magazine cover energy. Confident, current, bold.

**Colors**:
- Black, White
- One bold accent

**Elements**:
- Giant display number/letter
- Small precise body text
- 80% negative space
- Mixed font weights
- Generous margins

**Typography**:
- Large display + small body contrast
- Bold + light weights

**Don't use**: Even sizing, many colors

**Example**: Events, publications, cultural programs

---

## 7. Organic / Natural

**Philosophy**: Design as nature. Grounded, warm, approachable.

**Colors**:
- Earth: #8B7355, #556B2F
- Cream: #F5F5DC
- Terracotta: #C4A77D

**Elements**:
- Rounded forms (not circles)
- Botanical line work
- Hand-drawn feel
- Natural textures

**Typography**:
- Humanist sans or slab
- Warm, readable

**Don't use**: Perfect geometry, neon colors

**Example**: Restaurants, cafes, skincare, organic brands

---

## 8. Retro Letterpress

**Philosophy**: Craft authenticity. Vintage, tactile, real.

**Colors**:
- Kraft: #C4A77D
- Ink Black: #1A1A1A
- Cream: #F5F5DC

**Elements**:
- Subtle noise texture
- Ink-trap serifs (slight stroke variation)
- Offset printing (imperfect registration)
- Simple borders

**Typography**:
- Serif with character
- Caslon, Clarendon

**Don't use**: Perfect digital look, gradients

**Example**: Coffee roasters, artisan goods, heritage brands

---

## 9. Corporate Modernism

**Philosophy**: Professional, clean, modern. Trust + innovation.

**Colors**:
- Navy: #1A365D
- Slate: #4A5568
- White

**Elements**:
- Clean grid
- Subtle shadows
- Rounded corners
- Data-forward visuals

**Typography**:
- Modern sans-serif
- Inter, Roboto, SF Pro

**Don't use**: Too many colors, loud elements

**Example**: Tech startups, B2B services

---

## 10. Kinetic / Motion

**Philosophy**: Design that moves. Even when static.

**Colors**:
- High contrast
- Speed accent

**Elements**:
- Diagonal composition
- Motion lines
- Overlapping translucent shapes
- Text at angles

**Typography**:
- Italic emphasis
- Diagonal text

**Don't use**: Static centered layouts

**Example**: Delivery, sports, streaming

---

## 11. Brutalist Editorial

**Philosophy**: Raw function. Heavy, loud, honest.

**Colors**:
- Black, White
- Raw materials only

**Elements**:
- Heavy rules/lines
- Compressed type
- Asymmetric grids
- Raw negative space

**Typography**:
- Bold condensed
- Non-aligned elements

**Don't use**: Decorative elements

---

## 12. Psychedelic / Maximalist

**Philosophy**: Full expression. Abundance, confidence.

**Colors**:
- Full spectrum
- Saturated

**Elements**:
- Full bleed color
- Overlapping elements
- Pattern-heavy

**Don't use**: Minimal whitespace (by design)

---

## Choosing Your Direction

**Process**:
1. Ask: Industry? Audience? Mood?
2. Match to philosophy (see table in directions.md)
3. Show swatches
4. Get user pick
5. Execute FULLY — don't mix

**Premium rule**: One philosophy executed well > five mixed half-ways.

---

## Common Mistakes

- Using Inter font (generic)
- Purple-to-blue gradient (AI signature)
- Centered everything (lazy)
- Too many colors (no restraint)
- Rounded everything (modern generic)
- "Welcome" text (template)

See `anti-slop.md` for full anti-pattern list.