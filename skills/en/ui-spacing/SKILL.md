---
name: ui-spacing
description: UI Spacing - 8px system, Gestalt, whitespace, layout, z-index
---

# UI Spacing

## Whitespace Principles

Whitespace is an **active element**, not passive. It plays a fundamental role in design.

### Whitespace Functions

| Function | Description |
|----------|-------------|
| **Comprehension** | Facilitates reading and visual parsing |
| **Relationships** | Creates logical element groupings |
| **Attention** | Guides the eye to important elements |
| **Aesthetics** | Brings elegance and breathing room |

### Micro vs Macro Whitespace

- **Micro whitespace**: Spacing between close elements (letters, lines, icon and text)
- **Macro whitespace**: Spacing between sections, page margins, major areas

---

## 8px System

Consistent base for all spacing:

```
space-1:  4px   (half-step, special cases)
space-2:  8px   (standard minimum)
space-3:  12px
space-4:  16px  (base, default spacing)
space-6:  24px
space-8:  32px
space-12: 48px
space-16: 64px
```

### Why 8px?

- Divisible by 2 and 4 (flexibility)
- Aligns with standard grids
- Works well on all screens (pixel density)
- Easy mental math

---

## Spacing Concepts (EightShapes)

### Inset (Internal Padding)

Spacing inside a container:

```
┌─────────────────┐
│     INSET       │
│  ┌───────────┐  │
│  │  Content  │  │
│  └───────────┘  │
│                 │
└─────────────────┘
```

| Type | Description | Example |
|------|-------------|---------|
| **Square** | Same value everywhere | `padding: 16px` |
| **Squish** | Vertical < Horizontal | `padding: 8px 16px` (buttons) |
| **Stretch** | Vertical > Horizontal | `padding: 16px 8px` (lists) |

### Stack (Vertical)

Vertical spacing between stacked elements:

```
┌─────────────┐
│  Element 1  │
└─────────────┘
      ↕ stack
┌─────────────┐
│  Element 2  │
└─────────────┘
      ↕ stack
┌─────────────┐
│  Element 3  │
└─────────────┘
```

Usage: `gap: var(--stack-elements)` or `margin-bottom`

### Inline (Horizontal)

Horizontal spacing between adjacent elements:

```
┌───────┐     ┌───────┐     ┌───────┐
│ Item  │←───→│ Item  │←───→│ Item  │
└───────┘inline└───────┘inline└───────┘
```

Usage: `gap: var(--inline-elements)` or `margin-right`

### Grid

Spacing in a 2D grid:

```
┌─────┐  ┌─────┐  ┌─────┐
│     │  │     │  │     │
└─────┘  └─────┘  └─────┘
   ↕ row-gap
┌─────┐  ┌─────┐  ┌─────┐
│     │  │     │  │     │
└─────┘  └─────┘  └─────┘
   ←column-gap→
```

---

## Gestalt Principles

### Proximity

> Elements close together are perceived as belonging to the same group.

```
✅ Good                   ❌ Bad
┌─────────────┐          ┌─────────────┐
│ Label       │          │ Label       │
│ Input ────  │          │             │
│             │          │             │
│ Label       │          │ Input ────  │
│ Input ────  │          │ Label       │
└─────────────┘          │ Input ────  │
                         └─────────────┘
```

### Common Region

> Elements within a delimited area are perceived as a group.

```css
/* Card as common region */
.card {
  padding: var(--inset-card);
  border: 1px solid var(--border);
  border-radius: var(--radius);
}
```

### Uniform Connectivity

> Visually connected elements are perceived as related.

- Connection lines
- Shared background
- Common borders

---

## Layout Patterns

### 12-Column Grid

```css
.grid {
  display: grid;
  grid-template-columns: repeat(12, 1fr);
  gap: var(--space-4);
}

/* Responsive columns */
.col-6 { grid-column: span 6; }  /* 50% */
.col-4 { grid-column: span 4; }  /* 33% */
.col-3 { grid-column: span 3; }  /* 25% */
```

### Flexbox vs Grid

| Flexbox | Grid |
|---------|------|
| 1D layout (row OR column) | 2D layout (rows AND columns) |
| Content defines size | Container defines size |
| Navigation, toolbars | Page layouts, grids |

```css
/* Flexbox: simple alignment */
.toolbar {
  display: flex;
  gap: var(--inline-elements);
  align-items: center;
}

/* Grid: complex layout */
.page {
  display: grid;
  grid-template-areas:
    "header header"
    "sidebar main"
    "footer footer";
  gap: var(--space-6);
}
```

### Responsive Strategies

```css
/* Mobile-first breakpoints */
--breakpoint-sm: 640px;
--breakpoint-md: 768px;
--breakpoint-lg: 1024px;
--breakpoint-xl: 1280px;

/* Responsive spacing */
.section {
  padding: var(--space-4);
}

@media (min-width: 768px) {
  .section {
    padding: var(--space-8);
  }
}
```

---

## Z-Index Management

### Standard Scale

```css
:root {
  --z-base: 0;
  --z-dropdown: 100;
  --z-sticky: 200;
  --z-fixed: 300;
  --z-modal-backdrop: 400;
  --z-modal: 500;
  --z-popover: 600;
  --z-tooltip: 700;
}
```

### Stacking Contexts

A new stacking context is created by:
- `position: fixed/sticky`
- `opacity < 1`
- `transform`, `filter`, `perspective`
- `isolation: isolate`

### Isolation Pattern

```css
/* Create an isolated context */
.component {
  isolation: isolate;
}

/* Internal z-index doesn't affect outside */
.component .internal {
  position: relative;
  z-index: 10; /* Only relative to .component */
}
```

---

## Density Modes

Adapt the interface based on usage context:

| Mode | Multiplier | Usage |
|------|------------|-------|
| **Compact** | 0.75x | Dense data, desktop power users |
| **Comfortable** | 1x | Standard usage, default |
| **Spacious** | 1.5x | Mobile, accessibility, reading |

```css
:root {
  --density: 1;
}

.compact { --density: 0.75; }
.spacious { --density: 1.5; }

.element {
  padding: calc(var(--space-4) * var(--density));
  gap: calc(var(--space-2) * var(--density));
}
```

---

## CSS Tokens

### Token Definition

```css
:root {
  /* Base spacing */
  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-6: 24px;
  --space-8: 32px;
  --space-12: 48px;
  --space-16: 64px;

  /* Inset patterns */
  --inset-button: 8px 16px;       /* squish */
  --inset-card: 16px;             /* square */
  --inset-input: 12px 16px;       /* squish */
  --inset-list-item: 12px 8px;    /* stretch */

  /* Stack spacing */
  --stack-xs: 4px;
  --stack-sm: 8px;
  --stack-md: 16px;
  --stack-lg: 24px;
  --stack-xl: 32px;
  --stack-elements: 16px;
  --stack-sections: 48px;

  /* Inline spacing */
  --inline-xs: 4px;
  --inline-sm: 8px;
  --inline-md: 16px;
  --inline-elements: 8px;
  --inline-actions: 12px;

  /* Grid */
  --grid-gap: 16px;
  --grid-columns: 12;
}
```

### Usage

```css
.button {
  padding: var(--inset-button);
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: var(--stack-sm);
}

.card {
  padding: var(--inset-card);
}

.card-content > * + * {
  margin-top: var(--stack-elements);
}

.button-group {
  display: flex;
  gap: var(--inline-actions);
}
```

---

## Spacing Checklist

- [ ] Use 8px system (avoid arbitrary values)
- [ ] Apply Gestalt proximity (related elements = close)
- [ ] Differentiate micro/macro whitespace
- [ ] Tokens for all spacing values
- [ ] Z-index within defined scale
- [ ] Test all 3 density modes
- [ ] Responsive layout with standard breakpoints
