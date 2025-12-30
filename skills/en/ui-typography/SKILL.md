---
name: ui-typography
description: UI Typography - Scales, hierarchy, readability, responsive, accessibility
---

# UI Typography

## Font Classifications

### Serif
- Decorative strokes at letter extremities
- Classic, traditional, formal
- **Usage**: Long printed texts, editorial, luxury
- **Examples**: Georgia, Times New Roman, Merriweather

### Sans-serif
- No serifs, clean lines
- Modern, minimalist, screen-readable
- **Usage**: UI, web, mobile, digital body text
- **Examples**: Inter, Roboto, Open Sans, SF Pro

### Monospace
- Fixed width for each character
- Technical, code, data
- **Usage**: Code editors, terminals, data tables
- **Examples**: JetBrains Mono, Fira Code, SF Mono

### Display
- Decorative, expressive, visual impact
- **Usage**: Titles, logos, headlines (never body text)
- **Examples**: Playfair Display, Lobster, Impact

---

## Typographic Hierarchy

Scale based on 1.25 ratio (Major Third):

```
h1    → 2.441rem  (39px)  — Main title
h2    → 1.953rem  (31px)  — Major sections
h3    → 1.563rem  (25px)  — Subsections
h4    → 1.25rem   (20px)  — Subtitles
body  → 1rem      (16px)  — Body text
small → 0.8rem    (13px)  — Annotations, captions
```

### Hierarchy Rules
- **Maximum 3-4 levels** visible simultaneously
- **Sufficient contrast** between each level (min 1.25x)
- **Consistency**: same font for all headings

---

## Type Scale

### 1.25 Ratio (Major Third) — Recommended
```
base × 1.25^n

n=-1 → 0.8rem    (small)
n=0  → 1rem      (body)
n=1  → 1.25rem   (h4)
n=2  → 1.563rem  (h3)
n=3  → 1.953rem  (h2)
n=4  → 2.441rem  (h1)
```

### Other Common Ratios
| Ratio | Name | Usage |
|-------|------|-------|
| 1.125 | Major Second | Compact interfaces |
| 1.25  | Major Third | General UI (recommended) |
| 1.333 | Perfect Fourth | Editorial |
| 1.5   | Perfect Fifth | Impact titles |

### CSS Variables
```css
:root {
  --type-ratio: 1.25;
  --font-size-base: 1rem;
  --font-size-sm: calc(var(--font-size-base) / var(--type-ratio));
  --font-size-lg: calc(var(--font-size-base) * var(--type-ratio));
  --font-size-xl: calc(var(--font-size-lg) * var(--type-ratio));
  --font-size-2xl: calc(var(--font-size-xl) * var(--type-ratio));
  --font-size-3xl: calc(var(--font-size-2xl) * var(--type-ratio));
}
```

---

## Readability

### Line Height
```css
body     → line-height: 1.5;    /* Body text */
headings → line-height: 1.2;    /* Titles */
compact  → line-height: 1.3;    /* Dense UI */
```

### Letter Spacing
```css
body     → letter-spacing: 0;           /* Normal */
headings → letter-spacing: -0.02em;     /* Tighter headings */
uppercase → letter-spacing: 0.05em;     /* Spaced uppercase */
small    → letter-spacing: 0.01em;      /* Slightly spaced small text */
```

### Optimal Line Length
```css
.content {
  max-width: 65ch;  /* 45-75 characters recommended */
}
```

| Context | Width | Characters |
|---------|-------|------------|
| Optimal | 65ch | ~65 characters |
| Minimum | 45ch | ~45 characters |
| Maximum | 75ch | ~75 characters |

---

## Responsive Typography

### Fluid Typography with clamp()
```css
/* Responsive base */
html {
  font-size: clamp(1rem, 0.5vw + 0.875rem, 1.25rem);
}

/* Responsive title */
h1 {
  font-size: clamp(1.75rem, 4vw + 1rem, 3rem);
}

/* Generic formula */
font-size: clamp(min, preferred, max);
```

### Typographic Breakpoints
```css
:root {
  --font-size-base: 1rem;
}

@media (min-width: 768px) {
  :root {
    --font-size-base: 1.0625rem; /* 17px */
  }
}

@media (min-width: 1200px) {
  :root {
    --font-size-base: 1.125rem; /* 18px */
  }
}
```

---

## Font Pairing

### Fundamental Rules
1. **Contrast, not conflict** — Pair different but complementary fonts
2. **Maximum 2-3 families** — Beyond that, visual inconsistency
3. **Similar x-height** — Similar x-height for harmony

### Classic Combinations

| Headings | Body | Style |
|----------|------|-------|
| Playfair Display | Source Sans Pro | Elegant editorial |
| Montserrat | Open Sans | Modern professional |
| Roboto Slab | Roboto | Google Material |
| Lora | Lato | Warm accessible |
| Inter | Inter | Minimalist (single family) |

### Anti-patterns
- ❌ Two similar serifs
- ❌ Two sans-serifs too similar
- ❌ More than 3 families
- ❌ Display font as body text

---

## System Fonts vs Custom

### Recommended System Stack
```css
:root {
  --font-sans: system-ui, -apple-system, BlinkMacSystemFont, 
               'Segoe UI', Roboto, 'Helvetica Neue', Arial, sans-serif;
  
  --font-mono: ui-monospace, 'SF Mono', 'Cascadia Code', 
               'Source Code Pro', Menlo, Consolas, monospace;
}
```

### System Fonts Advantages
- ✅ Zero download, optimal performance
- ✅ Native familiarity for users
- ✅ OS-optimized rendering

### When to Use Custom Fonts
- Strong branding requiring unique identity
- Special characters (languages, icons)
- Specific typographic requirements

### Mandatory Fallbacks
```css
/* Always end with a generic family */
font-family: 'Custom Font', 'Fallback Font', sans-serif;
font-family: 'Code Font', 'Fallback Mono', monospace;
```

---

## Accessibility

### Minimum Size
```css
body {
  font-size: 1rem;      /* 16px absolute minimum */
  font-size: 1.125rem;  /* 18px recommended */
}

/* Never below 12px */
.small-text {
  font-size: max(0.75rem, 12px);
}
```

### Text/Background Contrast
| Level | Ratio | Usage |
|-------|-------|-------|
| AA | 4.5:1 | Normal text |
| AA Large | 3:1 | Text ≥18px or bold ≥14px |
| AAA | 7:1 | Enhanced accessibility |

### WCAG Text Spacing
Support user adjustments without content loss:
```css
/* UI must remain functional with: */
line-height: 1.5;           /* 1.5× font size */
letter-spacing: 0.12em;     /* 0.12× font size */
word-spacing: 0.16em;       /* 0.16× font size */
/* Paragraph spacing: 2× font size */
```

### Best Practices
- ✅ Never disable user zoom
- ✅ Use `rem`/`em` (not `px` for font-size)
- ✅ Test with 200% zoom
- ✅ Avoid justified text

---

## Complete CSS Tokens

```css
:root {
  /* Sizes */
  --font-size-xs: 0.75rem;    /* 12px */
  --font-size-sm: 0.875rem;   /* 14px */
  --font-size-base: 1rem;     /* 16px */
  --font-size-lg: 1.125rem;   /* 18px */
  --font-size-xl: 1.25rem;    /* 20px */
  --font-size-2xl: 1.5rem;    /* 24px */
  --font-size-3xl: 1.875rem;  /* 30px */
  --font-size-4xl: 2.25rem;   /* 36px */
  
  /* Line Heights */
  --line-height-tight: 1.2;
  --line-height-snug: 1.375;
  --line-height-normal: 1.5;
  --line-height-relaxed: 1.625;
  --line-height-loose: 2;
  
  /* Font Weights */
  --font-weight-light: 300;
  --font-weight-normal: 400;
  --font-weight-medium: 500;
  --font-weight-semibold: 600;
  --font-weight-bold: 700;
  
  /* Letter Spacing */
  --letter-spacing-tighter: -0.05em;
  --letter-spacing-tight: -0.025em;
  --letter-spacing-normal: 0;
  --letter-spacing-wide: 0.025em;
  --letter-spacing-wider: 0.05em;
  
  /* Font Families */
  --font-sans: system-ui, -apple-system, sans-serif;
  --font-serif: Georgia, Cambria, serif;
  --font-mono: ui-monospace, monospace;
}
```

---

## Typography Checklist

- [ ] Base font-size ≥ 16px
- [ ] Consistent scale (1.25 ratio)
- [ ] Line-height 1.5 for body text
- [ ] Max-width ~65ch for paragraphs
- [ ] Maximum 2-3 font families
- [ ] Generic fallbacks defined
- [ ] Contrast ≥ 4.5:1 (AA)
- [ ] Relative units (rem/em)
- [ ] 200% zoom test OK
- [ ] Responsive with clamp() or media queries
