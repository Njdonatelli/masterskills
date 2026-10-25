# Anti-Slop (How to NOT Look Like AI)

These patterns make designs immediately recognizable as AI-generated. Avoid at all costs.

---

## Color Anti-Patterns

### #1 Purple-to-Blue Gradient
**AI Signature**: Most recognizable AI pattern
```svg
<!-- ❌ NEVER -->
<linearGradient id="ai" x1="0%" y1="0%" x2="100%" y2="100%">
  <stop offset="0%" stop-color="#6366f1"/>
  <stop offset="100%" stop-color="#8b5cf6"/>
</linearGradient>
```

**Always use instead**: Solid colors or brand-specific palette

### #2 Cyan Accent on Dark Navy
```svg
<!-- ❌ AI generic -->
<rect fill="#1e293b"/>
<text fill="#06b6d4">TEXT</text>
```

### #3 Pure White Text on Saturated Background
Readable but generic. Add subtle darkening or use off-white.

---

## Font Anti-Patterns

### #1 Inter (ANY USE)
Inter is the most used AI font. It screams "I was generated."
```svg
<!-- ❌ NEVER -->
<text font-family="Inter">TEXT</text>
```

**Use instead**: 
- Helvetica (classic)
- Arial Black (bold statements)
- Georgia (editorial)
- System fonts only when needed

### #2 "WELCOME TO" Pattern
```svg
<!-- ❌ Template -->
<text font-size="8">WELCOME TO</text>
<text font-size="28">MY BRAND</text>
```

### #3 All Caps With Default Tracking
```svg
<!-- ❌ AI default -->
<TEXT TEXT-ANCHOR="MIDDLE"/>
```
Add proper tracking: `letter-spacing="0.1em"` for caps

---

## Layout Anti-Patterns

### #1 Perfect Center Alignment
```svg
<!-- ❌ Lazy centering -->
<text text-anchor="middle" x="40">CENTERED</text>
```

**Premium uses asymmetry**: Shift 5-10%, use grid alignment instead

### #2 Three Equal Columns
```svg
<!-- ❌ Template layout -->
<g id="col1"/><g id="col2"/><g id="col3"/>
```

### #3 Hero + Overlay + CTA
```svg
<!-- ❌ Web landing page -->
<image/> <text/> <rect fill="#button"/>
```

---

## Shape Anti-Patterns

### #1 All Rounded Rectangles
```svg
<!-- ❌ Modern AI generic -->
<rect rx="8" ry="8"/>
```

**Premium option**: Mix sharp + rounded, or fully sharp for bold

### #2 Floating Card Effect
```svg
<!-- ❌ Common AI -->
<rect fill="#1e293b"/> <!-- dark bg -->
<rect fill="#ffffff" filter="url(#shadow)"/> <!-- floating card -->
```

### #3 Glowing Orb / Bokeh
```svg
<!-- ❌ AI decoration -->
<circle filter="url(#glow)"/>
```

---

## Content Anti-Patterns

### #1 "Get Started" / "Learn More"
```svg
<!-- ❌ Template button text -->
<text>GET STARTED</text>
```

### #2 Decorative Star/Shine Shapes
```svg
<!-- ❌ Generic AI decoration -->
<polygon points="star shape"/>
```

### #3 Placeholder QR Code
Real QR codes work. Decorative ones look fake.

---

## SVG Anti-Patterns

### #1 Over-Complex Paths
```svg
<!-- ❌ Too many points -->
<path d="M0,0 L1,1 L2,2 L3,3..."/>
```
Keep paths simple. 10 points max per element.

### #2 Unused Definitions
```svg
<!-- ❌ bloat -->
<defs> <gradient id="unused"/> </defs>
```

### #3 Excessive Transforms
Multiple transforms = hard to edit and print.

---

## Premium Principles

Instead of anti-patterns, follow these:

| Anti-Pattern | Premium Instead |
|-------------|----------------|
| Purple gradient | Solid brand color |
| Inter font | Helvetica/Arial |
| Centered | Grid-aligned / asymmetric |
| Rounded all | Sharp + occasional round |
| "Get Started" | Brand-specific CTA |
| 3 columns | 2 columns or single focal |
| Gradient background | Solid color or texture |
| Generic icon | Custom geometry |

---

## Quick Checklist

Before export, search for:
- [ ] `#6366f1` or `#8b5cf6` (purple)
- [ ] `font-family="Inter"` 
- [ ] `text-anchor="middle"` > 3 uses
- [ ] `rx="` or `ry="` on all rects
- [ ] "WELCOME" or "GET STARTED"
- [ ] `linearGradient` with purple/blue

If found → **REVISE** before export.

---

## The Real Rule

**Design looks premium when it has a point of view.**

AI generates average. You choose intentionally.
- Intentional alignment
- Intentional color (restrained)
- Intentional typography
- Intentional shapes

Average = generic. Intentional = premium.