---
name: ui-a11y
description: UI Accessibility - WCAG 2.1, ARIA, contrast, keyboard navigation, screen readers
---

# UI Accessibility (a11y)

## Reference Standards

| Standard | Description | Scope |
|----------|-------------|-------|
| **WCAG 2.1/2.2** | Web Content Accessibility Guidelines | Worldwide reference |
| **Section 508** | US Federal accessibility | USA |
| **EN 301 549** | European accessibility standard | Europe |

### WCAG Conformance Levels

- **Level A**: Absolute minimum (critical blockers)
- **Level AA**: Recommended standard (target for most projects)
- **Level AAA**: Excellence (not always achievable for all content)

---

## POUR Principles (WCAG)

### 1. Perceivable
Information must be presentable in ways all users can perceive.

- Text alternatives for non-text content
- Captions and alternatives for time-based media
- Adaptable content (different presentations)
- Distinguishable content (foreground/background separation)

### 2. Operable
UI components and navigation must be operable.

- Keyboard accessible
- Enough time to read/interact
- No content causing seizures (flash)
- Navigable

### 3. Understandable
Information and UI operation must be understandable.

- Readable and understandable text
- Predictable behavior
- Input assistance (errors)

### 4. Robust
Content must be interpretable by a variety of user agents.

- Compatible with assistive technologies
- Correct markup parsing

---

## WCAG Contrast

| Content Type | Level AA | Level AAA |
|--------------|----------|-----------|
| **Normal text** (<18pt) | 4.5:1 | 7:1 |
| **Large text** (>=18pt or 14pt bold) | 3:1 | 4.5:1 |
| **UI Components / Graphics** | 3:1 | 3:1 |

### Contrast Verification

```css
/* Good contrast examples */
.good-contrast {
  color: #1a1a1a;           /* Dark text */
  background: #ffffff;       /* Light background */
  /* Ratio: 16.1:1 - AAA */
}

.minimum-aa {
  color: #767676;           /* Gray */
  background: #ffffff;
  /* Ratio: 4.54:1 - AA for normal text */
}
```

---

## Keyboard Navigation

### Fundamental Rules

1. **Logical tab order**: Focus order follows visual/logical order
2. **Visible focus required**: Focus indicator always visible
3. **Skip links**: Links to skip to main content
4. **No keyboard trap**: User can always exit a component

### Standard Keys

| Key | Action |
|-----|--------|
| `Tab` | Next focusable element |
| `Shift+Tab` | Previous focusable element |
| `Enter` | Activate button/link |
| `Space` | Activate button, check checkbox |
| `Escape` | Close modal/menu |
| `Arrow keys` | Navigate within components (tabs, menus) |

### Visible Focus

```css
/* NEVER do this */
*:focus { outline: none; }

/* Always provide a focus style */
:focus-visible {
  outline: 2px solid #005fcc;
  outline-offset: 2px;
}

/* Custom focus acceptable */
button:focus-visible {
  box-shadow: 0 0 0 3px rgba(0, 95, 204, 0.5);
}
```

### Skip Link

```html
<body>
  <a href="#main-content" class="skip-link">
    Skip to main content
  </a>
  <header>...</header>
  <main id="main-content" tabindex="-1">
    <!-- Main content -->
  </main>
</body>
```

```css
.skip-link {
  position: absolute;
  left: -9999px;
}
.skip-link:focus {
  left: 10px;
  top: 10px;
  z-index: 9999;
}
```

---

## ARIA (Accessible Rich Internet Applications)

### Golden Rule

> **"No ARIA is better than bad ARIA"**
> 
> Use native HTML elements first. ARIA as last resort.

### Landmarks (Regions)

```html
<header role="banner">...</header>
<nav role="navigation">...</nav>
<main role="main">...</main>
<aside role="complementary">...</aside>
<footer role="contentinfo">...</footer>
```

**Note**: HTML5 elements have implicit roles. Explicit `role` useful for legacy support.

### Labels and Descriptions

```html
<!-- aria-label: invisible label -->
<button aria-label="Close modal">
  <svg>...</svg>
</button>

<!-- aria-labelledby: references an element -->
<dialog aria-labelledby="dialog-title">
  <h2 id="dialog-title">Confirmation</h2>
</dialog>

<!-- aria-describedby: additional description -->
<input 
  type="password" 
  aria-describedby="password-help"
>
<p id="password-help">
  Minimum 8 characters, 1 uppercase, 1 number
</p>
```

### Live Regions

To announce dynamic changes to screen readers.

```html
<!-- Polite announcements (waits for end of speech) -->
<div aria-live="polite" aria-atomic="true">
  3 results found
</div>

<!-- Urgent announcements (interrupts) -->
<div role="alert" aria-live="assertive">
  Error: Session expired
</div>

<!-- Status (polite by default) -->
<div role="status">
  Loading...
</div>
```

### Common ARIA Patterns

#### Dialog (Modal)

```html
<div 
  role="dialog" 
  aria-modal="true"
  aria-labelledby="modal-title"
>
  <h2 id="modal-title">Title</h2>
  <p>Content...</p>
  <button>Close</button>
</div>
```

#### Tabs

```html
<div role="tablist" aria-label="Options">
  <button role="tab" aria-selected="true" aria-controls="panel1">
    Tab 1
  </button>
  <button role="tab" aria-selected="false" aria-controls="panel2">
    Tab 2
  </button>
</div>
<div role="tabpanel" id="panel1" aria-labelledby="tab1">
  Panel 1 content
</div>
<div role="tabpanel" id="panel2" aria-labelledby="tab2" hidden>
  Panel 2 content
</div>
```

#### Menu

```html
<button aria-haspopup="true" aria-expanded="false">
  Menu
</button>
<ul role="menu">
  <li role="menuitem">Option 1</li>
  <li role="menuitem">Option 2</li>
</ul>
```

---

## Accessible Forms

### Associated Labels

```html
<!-- Method 1: for/id (recommended) -->
<label for="email">Email</label>
<input type="email" id="email" name="email">

<!-- Method 2: wrapping -->
<label>
  Email
  <input type="email" name="email">
</label>

<!-- Method 3: aria-labelledby -->
<span id="email-label">Email</span>
<input type="email" aria-labelledby="email-label">
```

### Accessible Errors

```html
<label for="email">Email</label>
<input 
  type="email" 
  id="email"
  aria-invalid="true"
  aria-describedby="email-error"
>
<p id="email-error" role="alert">
  Invalid email format
</p>
```

### Autocomplete

```html
<input 
  type="text" 
  name="name"
  autocomplete="name"
>
<input 
  type="email" 
  autocomplete="email"
>
<input 
  type="tel" 
  autocomplete="tel"
>
```

### Grouping with Fieldset

```html
<fieldset>
  <legend>Shipping Address</legend>
  <label for="street">Street</label>
  <input type="text" id="street">
  <!-- ... -->
</fieldset>
```

---

## Images and Media

### Contextual Alt Text

```html
<!-- Informative image -->
<img src="chart.png" alt="Q3 2024 Sales: 45% increase vs Q2">

<!-- Decorative image -->
<img src="decoration.png" alt="" role="presentation">

<!-- Complex image -->
<figure>
  <img src="infographic.png" alt="Process infographic" aria-describedby="desc">
  <figcaption id="desc">
    Detailed description of the infographic...
  </figcaption>
</figure>

<!-- Image-link -->
<a href="/home">
  <img src="logo.png" alt="Home - Company Name">
</a>
```

### Accessible Videos

```html
<video controls>
  <source src="video.mp4" type="video/mp4">
  <track kind="captions" src="captions-en.vtt" srclang="en" label="English">
  <track kind="descriptions" src="descriptions.vtt" srclang="en">
</video>

<!-- Or link to transcript -->
<p><a href="transcript.html">Read transcript</a></p>
```

---

## Motion and Animations

### Respecting User Preferences

```css
/* Reduce animations if requested */
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

### Animation Rules

| Rule | Description |
|------|-------------|
| **Pause required** | Animations >5s must be pausable |
| **No flash** | Maximum 3 flashes per second |
| **Auto-play** | Avoid or allow to stop |

```html
<!-- Pause button for animation -->
<button aria-pressed="false" onclick="toggleAnimation()">
  Pause animation
</button>
```

---

## Level AA Checklist

### Content

- [ ] Alt text for all informative images
- [ ] `alt=""` for decorative images
- [ ] Captions for videos
- [ ] Transcripts available

### Structure

- [ ] Logical heading hierarchy (h1 → h2 → h3)
- [ ] ARIA or HTML5 landmarks
- [ ] Page language declared (`<html lang="en">`)
- [ ] Language changes marked (`<span lang="fr">`)

### Navigation

- [ ] Complete keyboard navigation
- [ ] Visible focus on all elements
- [ ] Logical tab order
- [ ] Skip link to main content
- [ ] No keyboard trap

### Forms

- [ ] Labels associated with all fields
- [ ] Accessible error messages
- [ ] Clear instructions
- [ ] Appropriate autocomplete

### Visual

- [ ] Text contrast 4.5:1 minimum
- [ ] UI contrast 3:1 minimum
- [ ] 200% zoom without content loss
- [ ] No information by color alone

### Interactive

- [ ] Distinct focus/hover/active states
- [ ] Touch targets minimum 44x44px
- [ ] Feedback on actions (loading, success, error)

---

## Testing Tools

### Automated

| Tool | Type | Usage |
|------|------|-------|
| **axe DevTools** | Extension | Detailed audit, CI integration |
| **Lighthouse** | Chrome | Quick audit, score |
| **WAVE** | Extension | Visual problem display |
| **Pa11y** | CLI | CI/CD integration |

### Manual

| Test | How |
|------|-----|
| **Keyboard only** | Unplug mouse, navigate with Tab |
| **Screen reader** | VoiceOver (Mac), NVDA (Windows), TalkBack (Android) |
| **200% zoom** | Ctrl/Cmd + until 200% |
| **High contrast mode** | System settings |

### Screen Reader Commands

#### VoiceOver (Mac)

- `Cmd + F5`: Enable/disable
- `Ctrl + Option + arrows`: Navigate
- `Ctrl + Option + Space`: Activate

#### NVDA (Windows)

- `Insert + Space`: Forms mode
- `H`: Next heading
- `Tab`: Next focusable element

---

## Anti-Patterns

| Anti-Pattern | Problem | Solution |
|--------------|---------|----------|
| `outline: none` without alternative | Invisible focus | `:focus-visible` style |
| Clickable `div` without role | Not keyboard accessible | `<button>` or `role="button"` + tabindex |
| Placeholder as label | Disappears on focus | Visible label + placeholder |
| `aria-hidden="true"` on focusable content | Screen reader confusion | Remove from tab order too |
| Auto-play video with sound | Disruptive | Muted by default or no auto-play |
