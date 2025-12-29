---
name: ui-design-principles
description: UI design principles - Visual hierarchy, spacing, colors, typography, components
---

# UI Design Principles Skill

This skill contains fundamental principles of user interface design to create elegant and modern UIs.

---

## Philosophy

> "Good design is invisible. The user doesn't notice the interface, they simply accomplish their goals with pleasure."

Prioritize:
- **Elegance** over complexity
- **Space** over clutter
- **Subtlety** over exuberance
- **Consistency** over variety
- **Clarity** over decoration

---

## Fundamental Visual Principles

### 1. Visual Hierarchy

The eye should immediately know where to look.

**Techniques:**
- Size: Important elements are larger
- Weight: Important text is bolder
- Color: Accents attract attention
- Position: Key content placed at top/center
- Space: Isolation creates importance

**Rule:** One focal point per screen/section. If everything is important, nothing is.

---

### 2. White Space (Negative Space)

Empty space is not waste, it's design.

**Principles:**
- Generous padding inside components
- Comfortable margins between elements
- Groups are separated by more space than their internal elements
- Content breathes, never stuck to edges

**Golden rule:** When in doubt, add more space. An airy UI always looks more professional than a dense one.

---

### 3. Spacing System

Use a consistent system based on a multiplier.

**Recommended scale (base 4px or 8px):**
```
xs:  4px   - Minimal spacing, fine details
sm:  8px   - Between related elements
md:  16px  - Standard component padding
lg:  24px  - Between related sections
xl:  32px  - Between distinct sections
2xl: 48px  - Major separations
3xl: 64px  - Page margins, large spaces
```

**Rule:** Never use arbitrary values. All spacing must be a multiple of the system.

---

### 4. Colors

#### Modern Palette

**Structure of a good palette:**
- 1 primary color (main action, accent)
- 1-2 neutral colors (text, backgrounds, borders)
- 1 success color (green)
- 1 error color (red)
- 1 warning color (orange/yellow)

**Sophisticated neutrals:**
Never use pure gray (#808080). Add a subtle tint:
- Warm gray: beige/brown tint
- Cool gray: blue tint
- Colored gray: tint of your primary color

**Recommended ratios:**
- 60%: Dominant color (background, surfaces)
- 30%: Secondary color (components, cards)
- 10%: Accent color (buttons, links, focus)

**Contrast:**
- Main text: minimum ratio 7:1
- Secondary text: minimum ratio 4.5:1
- Interactive elements: clearly distinguishable

---

### 5. Typography

#### Hierarchy

```
Display/Hero:   32-48px  - Page titles, hero sections
Heading 1:      24-32px  - Section titles
Heading 2:      20-24px  - Subsections
Heading 3:      16-18px  - Component titles
Body:           14-16px  - Main text
Caption:        12-14px  - Secondary text, labels
Small:          10-12px  - Legal mentions, timestamps
```

#### Rules

- **2 fonts maximum**: One for titles, one for body (or one for everything)
- **Comfortable line-height**: 1.4-1.6 for body text
- **Line width**: 60-80 characters max for readability
- **Weight**: Use variations (300, 400, 500, 600, 700) for hierarchy

---

### 6. Shadows and Elevation

Shadows create depth and hierarchy.

**Principles:**
- Soft and diffuse shadows, never hard
- Higher element = wider and softer shadow
- Shadow color: black with low opacity (5-15%), or tinted

**Elevation scale:**
```
Level 0 (flat):     No shadow - elements at surface level
Level 1 (raised):   Subtle shadow - cards, resting buttons
Level 2 (floating): Medium shadow - dropdowns, popovers
Level 3 (overlay):  Pronounced shadow - modals, dialogs
```

---

### 7. Rounded Corners

Rounded corners soften the interface and make it more welcoming.

**Scale:**
```
none:   0px     - Elements that should blend (full-width)
sm:     4px     - Small elements (badges, chips)
md:     8px     - Standard elements (buttons, inputs)
lg:     12-16px - Cards, containers
xl:     24px    - Large cards, modals
full:   9999px  - Pills, circular avatars
```

**Consistency rule:** Child elements have equal or smaller corners than their parents.

---

### 8. Borders

Borders define and separate.

**Principles:**
- Thickness: 1px is almost always enough
- Color: Subtle, never pure black (use light gray or muted color)
- Usage: To delimit, not to decorate

**Alternatives to borders:**
- Background color difference
- White space
- Subtle shadow

---

## Component Patterns

### Buttons

**Hierarchy:**
1. **Primary**: Main action, solid color, strong contrast
2. **Secondary**: Secondary actions, outline or neutral background
3. **Ghost/Text**: Tertiary actions, transparent background

**States:**
- Default: Base state
- Hover: Slight modification (darken/lighten 10%)
- Pressed: More pronounced than hover
- Focused: Visible ring/outline for accessibility
- Disabled: Reduced opacity (50-60%), forbidden cursor

---

### Cards

**Anatomy:**
- Background distinct from surface (lighter or darker)
- Generous internal padding (16-24px)
- Consistent rounded corners (8-16px)
- Optional shadow for elevation

---

### Inputs and Forms

**Principles:**
- Labels always visible (no placeholder-only)
- Clear states: default, focus, error, disabled
- Error messages below field, in red
- Generous vertical spacing between fields (16-24px)

**Focus state:**
- Colored ring/outline (primary color)
- Never just a subtle border change

---

## "Beautiful UI" Checklist

Before finalizing, verify:

### Colors
- [ ] Limited and consistent palette
- [ ] Sufficient contrast for readability
- [ ] No garish or overly saturated colors
- [ ] Grays have a subtle tint

### Spacing
- [ ] Consistent spacing system
- [ ] Enough white space
- [ ] Generous padding in components
- [ ] Clear visual groups

### Typography
- [ ] Clear hierarchy (sizes, weights)
- [ ] Maximum 2 fonts
- [ ] Readable text (size, contrast, line-height)

### Components
- [ ] Consistent rounded corners
- [ ] Subtle and appropriate shadows
- [ ] Interactive states defined (hover, focus, active)
- [ ] Subtle or absent borders

### Harmony
- [ ] Single focal point per view
- [ ] Alignments respected
- [ ] Consistency throughout the design

---

## Mantras

- "When in doubt, remove rather than add"
- "White space is your friend"
- "Consistency beats originality"
- "Simple is not boring, simple is elegant"
- "Every pixel must have a reason to exist"
