---
name: ui-responsive
description: Responsive Design - Mobile-first, breakpoints, fluid design, container queries
---

# Skill UI Responsive

This skill contains principles and techniques for responsive design to create interfaces that adapt to all screen sizes.

---

## Philosophy

> "Content is like water. It takes the shape of its container."

Prioritize:
- **Mobile-first** over desktop-down
- **Progressive enhancement** over graceful degradation
- **Fluid design** over rigid breakpoints
- **Content-first** over device-first
- **Performance** over decoration

---

## Core Principles

### 1. Mobile-First

Always design and code for mobile first, then enhance for larger screens.

**Why:**
- Forces prioritization of essential content
- Optimal performance on mobile (less CSS to load)
- Easier to add than to remove

**In practice:**
```css
/* Base: Mobile */
.component {
  flex-direction: column;
  padding: 16px;
}

/* Enhancement: Tablet+ */
@media (min-width: 768px) {
  .component {
    flex-direction: row;
    padding: 24px;
  }
}
```

**Rule:** Never use `max-width` in media queries. Always use `min-width`.

---

### 2. Progressive Enhancement

Build a solid foundation, then add enhancements for modern browsers/devices.

**Levels:**
1. **HTML**: Content accessible without CSS/JS
2. **CSS**: Styling and layout
3. **JS**: Enhanced interactions

**Example:**
```css
/* Base: Works everywhere */
.grid {
  display: block;
}

/* Enhancement: CSS Grid if supported */
@supports (display: grid) {
  .grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
  }
}
```

---

### 3. Fluid Design

Prefer relative units and modern CSS functions for design that adapts naturally.

**Avoid:**
- Fixed pixel widths
- Multiple breakpoints for the same property
- Unnecessary media queries

**Prefer:**
- Percentages and viewport units
- `clamp()`, `min()`, `max()`
- `auto-fit` and `auto-fill`

---

## Standard Breakpoints

```
sm:  640px   - Mobile landscape
md:  768px   - Tablet
lg:  1024px  - Desktop
xl:  1280px  - Large desktop
2xl: 1536px  - Extra large
```

**Recommended usage:**
- 0-639px: Mobile portrait (base, no media query)
- 640-767px: Mobile landscape
- 768-1023px: Tablet
- 1024-1279px: Standard desktop
- 1280px+: Large screens

**Tip:** Most designs only need 2-3 breakpoints. Don't add more without reason.

---

## CSS Techniques

### Media Queries (min-width)

```css
/* Mobile base */
.container {
  padding: 16px;
}

/* Tablet */
@media (min-width: 768px) {
  .container {
    padding: 24px;
  }
}

/* Desktop */
@media (min-width: 1024px) {
  .container {
    padding: 32px;
  }
}
```

---

### Container Queries

For truly modular components that respond to their container, not the viewport.

```css
/* Define the container */
.card-container {
  container-type: inline-size;
  container-name: card;
}

/* Styles based on container size */
@container card (min-width: 400px) {
  .card {
    flex-direction: row;
  }
}

@container card (min-width: 600px) {
  .card {
    grid-template-columns: 1fr 2fr;
  }
}
```

**When to use:**
- Reusable components in different contexts
- Variable-width sidebars/columns
- Adaptive card grids

---

### Modern CSS Functions

#### clamp()

Fluid value with min and max.

```css
/* font-size: minimum 16px, prefer 4vw, maximum 24px */
.title {
  font-size: clamp(1rem, 4vw, 1.5rem);
}

/* Fluid padding */
.section {
  padding: clamp(16px, 5vw, 64px);
}
```

#### min() and max()

```css
/* Width: minimum between 90% and 1200px */
.container {
  width: min(90%, 1200px);
}

/* Spacing: at least 20px, or 5% */
.gap {
  gap: max(20px, 5%);
}
```

---

## Responsive Images

### srcset and sizes

```html
<img 
  src="image-800.jpg"
  srcset="
    image-400.jpg 400w,
    image-800.jpg 800w,
    image-1200.jpg 1200w,
    image-1600.jpg 1600w
  "
  sizes="
    (max-width: 640px) 100vw,
    (max-width: 1024px) 50vw,
    33vw
  "
  alt="Description"
/>
```

**Explanation:**
- `srcset`: List of available images with their widths
- `sizes`: Image width based on viewport
- Browser automatically chooses the best image

---

### Picture Element

For art direction (different images based on context).

```html
<picture>
  <!-- Modern format if supported -->
  <source 
    type="image/avif" 
    srcset="image.avif"
  />
  <source 
    type="image/webp" 
    srcset="image.webp"
  />
  
  <!-- Different image on mobile -->
  <source 
    media="(max-width: 640px)" 
    srcset="image-mobile.jpg"
  />
  
  <!-- Fallback -->
  <img src="image.jpg" alt="Description" />
</picture>
```

---

### Modern Formats

**Priority (most to least efficient):**
1. **AVIF**: Best compression, growing support
2. **WebP**: Good compromise, wide support
3. **JPEG/PNG**: Universal fallback

**Lazy Loading:**
```html
<img src="image.jpg" loading="lazy" alt="Description" />
```

**CSS for responsive images:**
```css
img {
  max-width: 100%;
  height: auto;
  display: block;
}
```

---

## Responsive Navigation

### Hamburger Menu

Classic mobile pattern → full desktop navigation.

```css
/* Mobile: Hidden menu */
.nav-menu {
  position: fixed;
  inset: 0;
  transform: translateX(-100%);
  transition: transform 0.3s ease;
}

.nav-menu.open {
  transform: translateX(0);
}

.hamburger {
  display: block;
}

/* Desktop: Visible menu */
@media (min-width: 768px) {
  .nav-menu {
    position: static;
    transform: none;
    display: flex;
  }
  
  .hamburger {
    display: none;
  }
}
```

---

### Bottom Navigation

Popular mobile pattern (native apps).

```css
.bottom-nav {
  position: fixed;
  bottom: 0;
  left: 0;
  right: 0;
  display: flex;
  justify-content: space-around;
  padding: 8px 0;
  padding-bottom: env(safe-area-inset-bottom);
}

/* Desktop: hide or relocate */
@media (min-width: 768px) {
  .bottom-nav {
    display: none;
  }
}
```

---

### Adaptive Patterns

| Mobile | Tablet | Desktop |
|--------|--------|---------|
| Hamburger | Hamburger or tabs | Full navigation |
| Bottom nav | Optional sidebar | Sidebar |
| Vertical stack | 2 columns | Multi-column |
| Accordion | Tabs | All visible |

---

## Touch vs Mouse

### Target Size

**Rule:** Minimum 44x44px for interactive elements on touch.

```css
.button {
  min-height: 44px;
  min-width: 44px;
  padding: 12px 16px;
}

/* Text links: expanded hit area */
.text-link {
  padding: 8px;
  margin: -8px;
}
```

---

### Hover Detection

```css
/* Hover only if device supports it */
@media (hover: hover) {
  .button:hover {
    background-color: var(--hover-color);
  }
}

/* Alternative for touch: active state */
.button:active {
  background-color: var(--active-color);
}
```

---

### Pointer Detection

```css
/* Precise pointer (mouse) */
@media (pointer: fine) {
  .slider-thumb {
    width: 16px;
    height: 16px;
  }
}

/* Imprecise pointer (finger) */
@media (pointer: coarse) {
  .slider-thumb {
    width: 28px;
    height: 28px;
  }
}
```

---

## Performance

### Critical CSS

Inline CSS needed for initial render.

```html
<head>
  <style>
    /* Critical: above-the-fold */
    .header { ... }
    .hero { ... }
  </style>
  <link rel="preload" href="styles.css" as="style" onload="this.rel='stylesheet'">
</head>
```

---

### Code Splitting

Load context-specific CSS.

```html
<!-- Desktop only -->
<link rel="stylesheet" href="desktop.css" media="(min-width: 1024px)">

<!-- Print only -->
<link rel="stylesheet" href="print.css" media="print">
```

---

### Optimized Images

```html
<!-- Native lazy loading -->
<img loading="lazy" src="image.jpg" alt="">

<!-- Preload critical images -->
<link rel="preload" as="image" href="hero.jpg">

<!-- Dimensions to avoid layout shift -->
<img width="800" height="600" src="image.jpg" alt="">
```

---

## Responsive Accessibility

### prefers-reduced-motion

```css
/* Normal animations */
.element {
  transition: transform 0.3s ease;
}

/* Disable for those who prefer */
@media (prefers-reduced-motion: reduce) {
  *,
  *::before,
  *::after {
    animation-duration: 0.01ms !important;
    animation-iteration-count: 1 !important;
    transition-duration: 0.01ms !important;
  }
}
```

---

### prefers-color-scheme

```css
/* Light mode by default */
:root {
  --bg: white;
  --text: black;
}

/* Automatic dark mode */
@media (prefers-color-scheme: dark) {
  :root {
    --bg: #1a1a1a;
    --text: #f0f0f0;
  }
}
```

---

## Responsive Checklist

### Essential

- [ ] Meta viewport present
  ```html
  <meta name="viewport" content="width=device-width, initial-scale=1">
  ```
- [ ] No horizontal scroll at any size
- [ ] Images with `max-width: 100%`
- [ ] Touch targets minimum 44px
- [ ] Readable text without zoom (16px minimum)

### Navigation

- [ ] Navigation accessible on mobile
- [ ] Functional hamburger menu
- [ ] Visible focus on all elements

### Images

- [ ] srcset/sizes for important images
- [ ] Lazy loading for below-the-fold images
- [ ] Modern formats (WebP/AVIF) with fallback
- [ ] Specified dimensions (avoids layout shift)

### Performance

- [ ] Critical CSS inlined
- [ ] Optimized fonts (preload, font-display)
- [ ] No unnecessary blocking resources

### Accessibility

- [ ] prefers-reduced-motion respected
- [ ] prefers-color-scheme supported (optional)
- [ ] Sufficient contrast at all sizes

---

## Base CSS Templates

### Responsive Container

```css
.container {
  width: min(90%, 1200px);
  margin-inline: auto;
  padding-inline: 16px;
}

@media (min-width: 768px) {
  .container {
    padding-inline: 24px;
  }
}
```

---

### Auto-Responsive Grid

```css
.grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(min(100%, 300px), 1fr));
  gap: 24px;
}
```

**Explanation:** Columns are minimum 300px (or 100% if screen is smaller), and automatically add when space permits.

---

### Responsive Flex

```css
.flex-responsive {
  display: flex;
  flex-wrap: wrap;
  gap: 16px;
}

.flex-responsive > * {
  flex: 1 1 300px; /* Grow, shrink, base 300px */
}
```

---

### Fluid Typography

```css
:root {
  --fs-sm: clamp(0.875rem, 0.8rem + 0.25vw, 1rem);
  --fs-base: clamp(1rem, 0.9rem + 0.5vw, 1.125rem);
  --fs-lg: clamp(1.25rem, 1rem + 1vw, 1.5rem);
  --fs-xl: clamp(1.5rem, 1rem + 2vw, 2.5rem);
  --fs-2xl: clamp(2rem, 1rem + 4vw, 4rem);
}
```

---

### Fluid Spacing

```css
:root {
  --space-sm: clamp(8px, 2vw, 16px);
  --space-md: clamp(16px, 4vw, 32px);
  --space-lg: clamp(24px, 6vw, 64px);
  --space-xl: clamp(48px, 10vw, 128px);
}
```

---

## Anti-Patterns to Avoid

### Layout

- **Fixed widths**: Use `%`, `vw`, `min()`, `max()`
- **Fixed heights**: Let content define height
- **Horizontal scroll**: Always test at 320px
- **Arbitrary breakpoints**: Use standards

### Media Queries

- **max-width**: Prefer `min-width` (mobile-first)
- **Too many breakpoints**: 2-3 usually suffice
- **Device-based breakpoints**: Base on content instead

### Touch

- **Targets too small**: Minimum 44px
- **Hover-only interactions**: Always have fallback
- **Double-tap zoom**: Correct meta viewport

### Performance

- **Unoptimized images**: srcset + modern formats
- **Blocking CSS**: Critical CSS inline
- **Font flash**: font-display: swap

---

## Mantras

- "Mobile-first is not mobile-only"
- "Content dictates breakpoints, not devices"
- "Fluid first, breakpoints second"
- "Test on real devices, not just devtools"
- "Performance is a feature"
