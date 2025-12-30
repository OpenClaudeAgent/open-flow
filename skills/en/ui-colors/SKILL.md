---
name: ui-colors
description: UI Color Theory - Palettes, harmonies, WCAG contrast, dark mode
---

# Skill UI Colors

This skill contains color theory applied to user interface design: palette creation, harmonies, accessibility, and dark mode adaptation.

---

## Fundamentals

### Color Wheel

The color wheel is the fundamental tool for understanding color relationships.

**Primary Colors:**
- Red, Yellow, Blue
- Cannot be created by mixing

**Secondary Colors:**
- Orange (red + yellow)
- Green (yellow + blue)
- Purple (blue + red)

**Tertiary Colors:**
- Mix of a primary and an adjacent secondary
- Ex: Red-orange, Blue-green, Yellow-green

---

### HSL Model (Hue, Saturation, Lightness)

The HSL model is more intuitive than RGB for creating coherent palettes.

**Hue: 0-360°**
```
0°/360° : Red
60°     : Yellow
120°    : Green
180°    : Cyan
240°    : Blue
300°    : Magenta
```

**Saturation: 0-100%**
- 0%: Gray (no color)
- 50%: Desaturated/soft color
- 100%: Pure vivid color

**Lightness: 0-100%**
- 0%: Black
- 50%: Pure color
- 100%: White

**Practical rule:**
- For variations of the same color, keep Hue fixed
- Adjust Saturation and Lightness to create your shades

---

## Color Harmonies

### 1. Monochromatic

A single hue with saturation and lightness variations.

**Advantages:**
- Always harmonious
- Elegant and sophisticated
- Easy to implement

**UI Usage:**
- Minimalist interfaces
- Data-focused dashboards
- Professional applications

---

### 2. Analogous

2-3 adjacent colors on the wheel (30° apart).

**Examples:**
- Blue → Blue-green → Green
- Orange → Red-orange → Red

**Advantages:**
- Naturally harmonious
- Smooth transitions
- Comfortable for the eye

**UI Usage:**
- Creative applications
- Lifestyle/wellness sites
- Soft and welcoming interfaces

---

### 3. Complementary

Opposite colors on the wheel (180°).

**Examples:**
- Blue ↔ Orange
- Red ↔ Green
- Purple ↔ Yellow

**Advantages:**
- Strong contrast
- Dynamic and energetic
- Attention-grabbing

**UI Usage:**
- Call-to-action
- Elements to highlight
- Caution: use sparingly

---

### 4. Split-Complementary

One color + the two adjacent to its complement.

**Example:**
- Blue + Yellow-orange + Red-orange

**Advantages:**
- Strong contrast but less tense
- More flexibility than pure complementary

---

### 5. Triadic

Three equidistant colors (120°).

**Examples:**
- Red, Yellow, Blue (primaries)
- Orange, Green, Purple (secondaries)

**Advantages:**
- Visual balance
- Rich but harmonious palette

**UI Usage:**
- Playful applications
- Children's interfaces
- Expressive brands

---

### 60-30-10 Rule

Ideal color distribution in an interface:

```
60%: Dominant color (background, surfaces)
     → Neutral or very light color

30%: Secondary color (components, cards)
     → Variations of dominant or soft secondary

10%: Accent color (CTA, links, focus)
     → Vivid primary color
```

**Concrete example:**
- 60%: White/light gray background
- 30%: White cards, dark gray text
- 10%: Blue buttons, links, active icons

---

## Color Psychology

### Blue
- **Associations:** Trust, stability, professionalism, calm
- **Usage:** Finance, tech, social networks, healthcare
- **Examples:** Facebook, LinkedIn, PayPal, IBM

### Red
- **Associations:** Urgency, energy, passion, danger, excitement
- **Usage:** Alerts, promotions, food, entertainment
- **Examples:** YouTube, Netflix, Coca-Cola

### Green
- **Associations:** Success, nature, growth, health, money
- **Usage:** Validation, eco-friendly, finance, health
- **Examples:** Spotify, WhatsApp, Starbucks

### Orange
- **Associations:** Energy, creativity, accessibility, warmth
- **Usage:** CTA, soft warnings, young brands
- **Examples:** Firefox, SoundCloud, Amazon (buttons)

### Yellow
- **Associations:** Optimism, attention, warning
- **Usage:** Highlights, warnings, joyful brands
- **Caution:** Hard to read on light backgrounds

### Purple
- **Associations:** Luxury, creativity, mystery, wisdom
- **Usage:** Premium brands, creative tech
- **Examples:** Twitch, Cadbury

### Black
- **Associations:** Elegance, luxury, sophistication, power
- **Usage:** Fashion, luxury, premium tech
- **Examples:** Apple, Chanel, Nike

### White
- **Associations:** Purity, simplicity, minimalism, space
- **Usage:** Default background, clean interfaces

---

## UI Palette Structure

```
Complete UI Palette
├── Primary (1-2 accent colors)
│   └── primary-50 → primary-900 (10 shades)
│
├── Secondary (optional)
│   └── secondary-50 → secondary-900
│
├── Accent (1 color)
│   └── For specific highlights
│
├── Neutrals (grays)
│   ├── neutral-50   (almost white)
│   ├── neutral-100
│   ├── neutral-200
│   ├── neutral-300
│   ├── neutral-400
│   ├── neutral-500  (medium gray)
│   ├── neutral-600
│   ├── neutral-700
│   ├── neutral-800
│   └── neutral-900  (almost black)
│
└── Semantic (functional colors)
    ├── Success (green)
    │   └── success-light, success, success-dark
    ├── Warning (orange/yellow)
    │   └── warning-light, warning, warning-dark
    ├── Error (red)
    │   └── error-light, error, error-dark
    └── Info (blue)
        └── info-light, info, info-dark
```

### Generating a Color Scale

To create a scale from 50 to 900 from a base color:

```
50   : Lightness 97%  (very light background)
100  : Lightness 94%
200  : Lightness 86%
300  : Lightness 74%
400  : Lightness 62%
500  : Lightness 50%  (base color)
600  : Lightness 40%
700  : Lightness 32%
800  : Lightness 24%
900  : Lightness 16%  (text on light background)
```

---

## Contrast and Accessibility (WCAG)

### Minimum Contrast Ratios

**Level AA (recommended minimum):**
- Normal text: 4.5:1
- Large text (18px+ or 14px+ bold): 3:1
- UI components and graphics: 3:1

**Level AAA (optimal):**
- Normal text: 7:1
- Large text: 4.5:1

### Ratio Calculation

```
Ratio = (L1 + 0.05) / (L2 + 0.05)

Where L1 = luminance of the lighter color
      L2 = luminance of the darker color
```

### Usage by Ratio

| Ratio | Recommended Usage |
|-------|-------------------|
| 21:1  | Maximum (black on white) |
| 7:1+  | Main text (AAA) |
| 4.5:1 | Main text (AA), large text (AAA) |
| 3:1   | Large text (AA), icons, borders |
| < 3:1 | Decorative only |

### Color Accessibility Checklist

- [ ] Main text on background: ratio ≥ 4.5:1
- [ ] Secondary text on background: ratio ≥ 4.5:1
- [ ] Links distinguishable (not only by color)
- [ ] Focus states visible: ratio ≥ 3:1
- [ ] Input borders: ratio ≥ 3:1
- [ ] Functional icons: ratio ≥ 3:1
- [ ] Don't convey info by color alone
- [ ] Test with color blindness simulator

### Types of Color Blindness

**Protanopia/Deuteranopia (red-green):**
- ~8% of men affected
- Red and green are confused
- Solution: Don't oppose red/green alone

**Tritanopia (blue-yellow):**
- More rare
- Blue and yellow are confused

**Achromatopsia:**
- Vision in grayscale
- Very rare

---

## Dark Mode

### Fundamental Principles

**Don't just invert colors!**

Dark mode is not `filter: invert(1)`. It requires specific thought.

### Surfaces and Elevation

In dark mode, elevated surfaces are LIGHTER (opposite of light mode).

```
Light Mode:           Dark Mode:
Higher surface ──┐    Higher surface ──┐
  (shadow)       │      (lighter)      │
Base surface ────┘    Base surface ────┘
```

**Dark elevation scale:**
```
dp0  : #121212 (base surface)
dp1  : #1e1e1e (cards)
dp2  : #232323 (navigation)
dp3  : #252525 (drawers)
dp4  : #272727 (app bars)
dp6  : #2c2c2c (menus)
dp8  : #2e2e2e (modals)
dp12 : #333333 (dialogs)
dp16 : #353535 (pickers)
dp24 : #383838 (max elevation)
```

### Colors in Dark Mode

**Saturation:**
- Reduce saturation of primary colors (70-80%)
- Overly vivid colors are harsh on dark backgrounds

**Semantic colors:**
- Success: Move from saturated green to desaturated green
- Error: Less vivid red, more salmon
- Warning: Less intense orange

**Text:**
- Primary text: #FFFFFF with 87% opacity
- Secondary text: #FFFFFF with 60% opacity
- Disabled text: #FFFFFF with 38% opacity

### Tokens for Dual Theme

```css
/* Light Mode */
:root {
  --color-surface: #ffffff;
  --color-surface-elevated: #f5f5f5;
  --color-text-primary: rgba(0, 0, 0, 0.87);
  --color-text-secondary: rgba(0, 0, 0, 0.60);
  --color-primary: hsl(220, 90%, 50%);
}

/* Dark Mode */
[data-theme="dark"] {
  --color-surface: #121212;
  --color-surface-elevated: #1e1e1e;
  --color-text-primary: rgba(255, 255, 255, 0.87);
  --color-text-secondary: rgba(255, 255, 255, 0.60);
  --color-primary: hsl(220, 70%, 60%); /* desaturated + lightened */
}
```

### Dark Mode Checklist

- [ ] Elevated surfaces are lighter (no black shadows)
- [ ] Desaturated primary colors
- [ ] Text contrast verified (≥ 4.5:1)
- [ ] No pure white (#fff) → use opacity
- [ ] No pure black (#000) as surface → #121212
- [ ] Semantic colors adjusted
- [ ] Icons and illustrations adapted
- [ ] Test in real conditions (OLED screen)

---

## Recommended CSS Design Tokens

### Complete Structure

```css
:root {
  /* === PRIMARY === */
  --color-primary-50: hsl(220, 90%, 97%);
  --color-primary-100: hsl(220, 90%, 94%);
  --color-primary-200: hsl(220, 90%, 86%);
  --color-primary-300: hsl(220, 90%, 74%);
  --color-primary-400: hsl(220, 90%, 62%);
  --color-primary-500: hsl(220, 90%, 50%);
  --color-primary-600: hsl(220, 90%, 40%);
  --color-primary-700: hsl(220, 90%, 32%);
  --color-primary-800: hsl(220, 90%, 24%);
  --color-primary-900: hsl(220, 90%, 16%);

  /* === NEUTRALS (blue-tinted) === */
  --color-neutral-50: hsl(220, 20%, 98%);
  --color-neutral-100: hsl(220, 15%, 95%);
  --color-neutral-200: hsl(220, 12%, 88%);
  --color-neutral-300: hsl(220, 10%, 75%);
  --color-neutral-400: hsl(220, 8%, 60%);
  --color-neutral-500: hsl(220, 6%, 45%);
  --color-neutral-600: hsl(220, 8%, 35%);
  --color-neutral-700: hsl(220, 10%, 25%);
  --color-neutral-800: hsl(220, 12%, 18%);
  --color-neutral-900: hsl(220, 15%, 10%);

  /* === SEMANTIC === */
  /* Success */
  --color-success-light: hsl(145, 65%, 92%);
  --color-success: hsl(145, 65%, 42%);
  --color-success-dark: hsl(145, 65%, 32%);

  /* Warning */
  --color-warning-light: hsl(38, 95%, 92%);
  --color-warning: hsl(38, 95%, 50%);
  --color-warning-dark: hsl(38, 95%, 38%);

  /* Error */
  --color-error-light: hsl(0, 85%, 95%);
  --color-error: hsl(0, 85%, 55%);
  --color-error-dark: hsl(0, 85%, 40%);

  /* Info */
  --color-info-light: hsl(205, 85%, 92%);
  --color-info: hsl(205, 85%, 50%);
  --color-info-dark: hsl(205, 85%, 38%);

  /* === SURFACES === */
  --color-background: var(--color-neutral-50);
  --color-surface: #ffffff;
  --color-surface-elevated: var(--color-neutral-100);

  /* === TEXT === */
  --color-text-primary: var(--color-neutral-900);
  --color-text-secondary: var(--color-neutral-600);
  --color-text-disabled: var(--color-neutral-400);
  --color-text-inverse: #ffffff;

  /* === BORDERS === */
  --color-border: var(--color-neutral-200);
  --color-border-strong: var(--color-neutral-300);
}
```

### Token Usage

```css
.button-primary {
  background-color: var(--color-primary-500);
  color: var(--color-text-inverse);
}

.button-primary:hover {
  background-color: var(--color-primary-600);
}

.card {
  background-color: var(--color-surface);
  border: 1px solid var(--color-border);
}

.alert-success {
  background-color: var(--color-success-light);
  color: var(--color-success-dark);
  border-left: 4px solid var(--color-success);
}
```

---

## Recommended Tools

### Palette Creation

- **Coolors** (coolors.co) - Quick generation
- **Adobe Color** (color.adobe.com) - Advanced harmonies
- **Huemint** (huemint.com) - AI for palettes
- **Realtime Colors** (realtimecolors.com) - Preview in context

### Contrast Verification

- **WebAIM Contrast Checker** (webaim.org/resources/contrastchecker)
- **Colour Contrast Analyser** (TPGi) - Desktop application
- **Stark** - Figma/Sketch plugin

### Color Blindness Testing

- **Sim Daltonism** (macOS) - Real-time simulation
- **Colorblindly** - Chrome extension
- **Coblis** (color-blindness.com/coblis-color-blindness-simulator)

### Dev Extensions

- **VisBug** - Visual inspection
- **CSS Overview** (Chrome DevTools) - Analysis of colors used
- **ColorZilla** - Advanced color picker

---

## Final Colors Checklist

### Palette
- [ ] Limited palette (1-2 primaries, 1 accent, neutrals, semantics)
- [ ] Complete shade scale (50-900)
- [ ] Tinted neutrals (no pure grays)
- [ ] Semantic colors defined

### Harmony
- [ ] Color scheme identified (mono, analogous, etc.)
- [ ] 60-30-10 rule followed
- [ ] Consistency throughout the application

### Accessibility
- [ ] Text contrast ≥ 4.5:1 (AA)
- [ ] UI element contrast ≥ 3:1
- [ ] Info not conveyed by color alone
- [ ] Color blindness testing done

### Dark Mode (if applicable)
- [ ] Elevated surfaces are lighter
- [ ] Desaturated colors
- [ ] Text with opacity (not pure white/black)
- [ ] CSS tokens for easy switching

---

## Anti-Patterns

- **Too many colors**: 3-4 colors max + neutrals
- **Pure gray**: Always tint subtly
- **Maximum saturation everywhere**: Tiring for the eye
- **Color = only differentiation**: Add shape/text/icon
- **Dark mode = inversion**: Requires specific design
- **Ignoring contrast**: Always check WCAG
- **Random colors**: Always start from a harmony

---

## Mantras

- "Fewer colors, more impact"
- "Contrast is not optional"
- "Neutrals do 90% of the work"
- "High saturation = use sparingly"
- "Dark mode is a design, not a filter"
