# SVG Patterns

Common fragments you can copy-paste and manipulate.

### 1. Circular Sticker with Bleed Context

```svg
<svg xmlns="http://www.w3.org/2000/svg" width="50mm" height="50mm" viewBox="-3 -3 56 56">
  <!-- 3mm Bleed Area -->
  <circle cx="25" cy="25" r="28" fill="#F0F0F0" id="bg-bleed"/>
  <!-- Trim Line Indicator (remove before export) -->
  <circle cx="25" cy="25" r="25" fill="none" stroke="#FF0000" stroke-dasharray="2,2" stroke-width="0.5" id="guide-trim"/>
  <!-- Safe Zone -->
  <circle cx="25" cy="25" r="20" fill="none" stroke="#0000FF" stroke-dasharray="1,1" stroke-width="0.5" id="guide-safe"/>
</svg>
```

### 2. Multi-line Text (SVG doesn't wrap natively)

```svg
<text x="10" y="20" font-family="Helvetica" font-size="10" fill="#111" id="multi-line-block">
  <tspan x="10" dy="0">First line of text</tspan>
  <tspan x="10" dy="1.2em">Second line of text breaks manually</tspan>
  <tspan x="10" dy="1.2em">Third line follows the grid.</tspan>
</text>
```

### 3. Isometric / Dot Grid Pattern

```svg
<defs>
  <pattern id="dot-grid" x="0" y="0" width="5" height="5" patternUnits="userSpaceOnUse">
    <circle fill="#CCCCCC" cx="2.5" cy="2.5" r="0.5"></circle>
  </pattern>
</defs>
<rect x="-3" y="-3" width="106" height="106" fill="url(#dot-grid)" />
```
