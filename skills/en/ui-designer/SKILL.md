---
name: ui-designer
description: Main UI skill - Orchestrates design system, colors, typography, spacing, responsive, a11y, components
---

# UI Designer Skill (Orchestrator)

This skill is the main entry point for all UI design work. It orchestrates specialized skills and provides common fundamental principles.

> "Good design is invisible. The user doesn't notice the interface, they simply accomplish their goals with pleasure."

---

## UI Skills Architecture

```
ui-designer (this skill)
├── ui-colors      → Palettes, contrast, dark mode, semantics
├── ui-typography  → Scales, hierarchy, responsive, readability
├── ui-spacing     → 8px grid, Gestalt, layout, breathing room
├── ui-responsive  → Mobile-first, breakpoints, adaptability
├── ui-a11y        → WCAG 2.1, ARIA, universal accessibility
└── ui-components  → Atomic Design, patterns, states, composition
```

### When to Load Which Skill

| Task | Skill to Load |
|------|---------------|
| Create/revise a color palette | `ui-colors` |
| Define typographic system | `ui-typography` |
| Work on layout/spacing | `ui-spacing` |
| Adapt for mobile/desktop | `ui-responsive` |
| Accessibility audit or improvement | `ui-a11y` |
| Create/standardize components | `ui-components` |
| New complete project | Load all skills |
| Global design review | This skill + checklist |

---

## Fundamental Principles

### Good Design Philosophy

Prioritize:
- **Elegance** over complexity
- **Space** over clutter
- **Subtlety** over exuberance
- **Consistency** over variety
- **Clarity** over decoration

### 60-30-10 Rule

Harmonious color distribution:
- **60%**: Dominant color (backgrounds, main surfaces)
- **30%**: Secondary color (components, cards, sections)
- **10%**: Accent color (buttons, links, focus, CTAs)

### Visual Hierarchy

The eye should immediately know where to look.

**Techniques:**
- **Size**: Important elements are larger
- **Weight**: Important text is bolder
- **Color**: Accents attract attention
- **Position**: Key content is placed at top/center
- **Space**: Isolation creates importance

### Single Focal Point

**Rule:** One focal point per screen/section. If everything is important, nothing is.

---

## Design Tokens - Standard Format

### DTCG Format (W3C Design Tokens)

```json
{
  "$schema": "https://design-tokens.github.io/community-group/format/",
  "colors": {
    "primary": {
      "$value": "#3B82F6",
      "$type": "color",
      "$description": "Primary color for main actions"
    },
    "neutral": {
      "50": { "$value": "#F8FAFC", "$type": "color" },
      "100": { "$value": "#F1F5F9", "$type": "color" },
      "200": { "$value": "#E2E8F0", "$type": "color" },
      "300": { "$value": "#CBD5E1", "$type": "color" },
      "400": { "$value": "#94A3B8", "$type": "color" },
      "500": { "$value": "#64748B", "$type": "color" },
      "600": { "$value": "#475569", "$type": "color" },
      "700": { "$value": "#334155", "$type": "color" },
      "800": { "$value": "#1E293B", "$type": "color" },
      "900": { "$value": "#0F172A", "$type": "color" }
    },
    "semantic": {
      "success": { "$value": "#22C55E", "$type": "color" },
      "warning": { "$value": "#F59E0B", "$type": "color" },
      "error": { "$value": "#EF4444", "$type": "color" },
      "info": { "$value": "#3B82F6", "$type": "color" }
    }
  },
  "typography": {
    "fontFamily": {
      "sans": { "$value": "Inter, system-ui, sans-serif", "$type": "fontFamily" },
      "mono": { "$value": "JetBrains Mono, monospace", "$type": "fontFamily" }
    },
    "fontSize": {
      "xs": { "$value": "0.75rem", "$type": "dimension" },
      "sm": { "$value": "0.875rem", "$type": "dimension" },
      "base": { "$value": "1rem", "$type": "dimension" },
      "lg": { "$value": "1.125rem", "$type": "dimension" },
      "xl": { "$value": "1.25rem", "$type": "dimension" },
      "2xl": { "$value": "1.5rem", "$type": "dimension" },
      "3xl": { "$value": "1.875rem", "$type": "dimension" },
      "4xl": { "$value": "2.25rem", "$type": "dimension" }
    },
    "lineHeight": {
      "tight": { "$value": "1.25", "$type": "number" },
      "normal": { "$value": "1.5", "$type": "number" },
      "relaxed": { "$value": "1.75", "$type": "number" }
    }
  },
  "spacing": {
    "0": { "$value": "0", "$type": "dimension" },
    "1": { "$value": "0.25rem", "$type": "dimension" },
    "2": { "$value": "0.5rem", "$type": "dimension" },
    "3": { "$value": "0.75rem", "$type": "dimension" },
    "4": { "$value": "1rem", "$type": "dimension" },
    "6": { "$value": "1.5rem", "$type": "dimension" },
    "8": { "$value": "2rem", "$type": "dimension" },
    "12": { "$value": "3rem", "$type": "dimension" },
    "16": { "$value": "4rem", "$type": "dimension" }
  },
  "borderRadius": {
    "none": { "$value": "0", "$type": "dimension" },
    "sm": { "$value": "0.25rem", "$type": "dimension" },
    "md": { "$value": "0.5rem", "$type": "dimension" },
    "lg": { "$value": "0.75rem", "$type": "dimension" },
    "xl": { "$value": "1rem", "$type": "dimension" },
    "full": { "$value": "9999px", "$type": "dimension" }
  },
  "shadow": {
    "sm": { 
      "$value": "0 1px 2px 0 rgb(0 0 0 / 0.05)", 
      "$type": "shadow" 
    },
    "md": { 
      "$value": "0 4px 6px -1px rgb(0 0 0 / 0.1), 0 2px 4px -2px rgb(0 0 0 / 0.1)", 
      "$type": "shadow" 
    },
    "lg": { 
      "$value": "0 10px 15px -3px rgb(0 0 0 / 0.1), 0 4px 6px -4px rgb(0 0 0 / 0.1)", 
      "$type": "shadow" 
    }
  }
}
```

### Equivalent CSS Variables

```css
:root {
  /* Colors */
  --color-primary: #3B82F6;
  --color-neutral-50: #F8FAFC;
  --color-neutral-100: #F1F5F9;
  --color-neutral-500: #64748B;
  --color-neutral-900: #0F172A;
  --color-success: #22C55E;
  --color-warning: #F59E0B;
  --color-error: #EF4444;
  
  /* Typography */
  --font-sans: Inter, system-ui, sans-serif;
  --font-mono: JetBrains Mono, monospace;
  --text-xs: 0.75rem;
  --text-sm: 0.875rem;
  --text-base: 1rem;
  --text-lg: 1.125rem;
  --text-xl: 1.25rem;
  --leading-tight: 1.25;
  --leading-normal: 1.5;
  
  /* Spacing (base 4px) */
  --space-1: 0.25rem;  /* 4px */
  --space-2: 0.5rem;   /* 8px */
  --space-3: 0.75rem;  /* 12px */
  --space-4: 1rem;     /* 16px */
  --space-6: 1.5rem;   /* 24px */
  --space-8: 2rem;     /* 32px */
  
  /* Border Radius */
  --radius-sm: 0.25rem;
  --radius-md: 0.5rem;
  --radius-lg: 0.75rem;
  --radius-full: 9999px;
  
  /* Shadows */
  --shadow-sm: 0 1px 2px 0 rgb(0 0 0 / 0.05);
  --shadow-md: 0 4px 6px -1px rgb(0 0 0 / 0.1);
  --shadow-lg: 0 10px 15px -3px rgb(0 0 0 / 0.1);
}
```

---

## Design Process

### 1. Structure First
- Define information hierarchy
- Place main elements
- Establish grid/layout
- **Skill:** `ui-spacing`

### 2. Spacing Next
- Apply spacing system
- Create visual groups (Gestalt)
- Ensure breathing room
- **Skill:** `ui-spacing`

### 3. Typography
- Establish typographic scale
- Define text hierarchy
- Verify readability
- **Skill:** `ui-typography`

### 4. Colors and Style
- Apply palette
- Add shadows/elevation
- Define visual states
- **Skill:** `ui-colors`

### 5. Components
- Standardize patterns
- Define all states
- Ensure consistency
- **Skill:** `ui-components`

### 6. Responsive
- Adapt for all screens
- Test breakpoints
- Optimize for mobile
- **Skill:** `ui-responsive`

### 7. Accessibility
- Check contrasts
- Add ARIA attributes
- Test keyboard navigation
- **Skill:** `ui-a11y`

### 8. Polish
- Check alignments
- Harmonize details
- Test interactive states

---

## Global Quality Checklist

### Colors
- [ ] Limited and consistent palette (5-7 colors max)
- [ ] Sufficient contrast (WCAG AA minimum)
- [ ] No garish or over-saturated colors
- [ ] Grays have a subtle tint (never pure)
- [ ] 60-30-10 rule respected
- [ ] Consistent dark mode (if applicable)

### Spacing
- [ ] Consistent spacing system (base 4px or 8px)
- [ ] Enough white space (breathing room)
- [ ] Generous padding in components
- [ ] Clear visual groups (Gestalt)
- [ ] No arbitrary values

### Typography
- [ ] Clear hierarchy (sizes, weights)
- [ ] Maximum 2 fonts
- [ ] Readable text (14px min, contrast, line-height 1.4-1.6)
- [ ] Optimal line width (60-80 characters)
- [ ] Consistent typographic scale

### Components
- [ ] Consistent border radius
- [ ] Subtle and appropriate shadows
- [ ] Interactive states defined (hover, focus, active, disabled)
- [ ] Subtle borders (1px max, muted color)
- [ ] Reusable patterns

### Accessibility
- [ ] WCAG AA contrast ratio (4.5:1 text, 3:1 UI)
- [ ] Visible focus on all interactive elements
- [ ] Functional keyboard navigation
- [ ] Appropriate ARIA attributes
- [ ] Alt text for images

### Responsive
- [ ] Mobile-first approach
- [ ] Consistent breakpoints
- [ ] Sufficient touch targets (44x44px min)
- [ ] No horizontal scroll
- [ ] Prioritized content on mobile

### Global Harmony
- [ ] Single focal point per view
- [ ] Alignments respected
- [ ] Consistency throughout design
- [ ] Design tokens used everywhere

---

## Anti-Patterns to Avoid

### Visuals
- **Too many colors**: Stick to your palette
- **Hard shadows**: Always diffuse and subtle
- **Thick borders**: 1px max, muted color
- **Inconsistent border radius**: Same radius for similar elements
- **Pure grays** (#808080, #cccccc): Always tint subtly
- **Text on image without overlay**: Always ensure readability

### Spacing
- **Elements stuck to edges**: Always add padding
- **Inconsistent spacing**: Use your system
- **Lack of breathing room**: When in doubt, add more space
- **Arbitrary values**: No "13px" or "27px"
- **Unclear visual groups**: Clear Gestalt principles

### Typography
- **Too many fonts**: 2 maximum
- **Too many sizes**: Use a defined scale
- **Text too small**: 14px minimum for body
- **Lines too long**: 80 characters max
- **Tight line-height**: 1.4 minimum for body

### Interactions
- **Invisible hover**: Must be perceptible
- **Invisible focus**: Critical for accessibility
- **Missing states**: Every interactive element has all states
- **Abrupt transitions**: 150-300ms ease

---

## Designer Mantras

- "When in doubt, remove rather than add"
- "White space is your friend"
- "Consistency beats originality"
- "Simple is not boring, simple is elegant"
- "Every pixel must have a reason to exist"
- "Design for the worst case, delight in the best"
- "Accessible design is good design"

---

## Resources

### Contrast Tools
- WebAIM Contrast Checker
- Coolors Contrast Checker
- Stark (Figma plugin)

### Reference Design Systems
- Tailwind CSS (tokens and utilities)
- Radix UI (accessible components)
- Shadcn/ui (modern patterns)
- Material Design 3 (guidelines)
- Apple Human Interface Guidelines

### Validation
- axe DevTools (accessibility)
- Lighthouse (performance + a11y)
- WAVE (Web Accessibility Evaluation)
