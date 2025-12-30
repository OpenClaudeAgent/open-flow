---
name: ui-components
description: UI Components - Atomic Design, interaction patterns, states, design systems
---

# UI Components Skill

This skill contains principles for designing UI components, from Atomic Design to advanced interaction patterns.

---

## Atomic Design (Brad Frost)

Atomic Design is a methodology for creating modular and consistent design systems.

```
Atoms → Molecules → Organisms → Templates → Pages
```

### Levels

| Level | Definition | Examples |
|-------|-----------|----------|
| **Atoms** | Basic, indivisible UI elements | Button, Icon, Label, Input, Badge |
| **Molecules** | Groups of atoms working together | Search bar (input + button), Form field (label + input + error) |
| **Organisms** | Groups of molecules forming a section | Header, Card, Form, Navigation |
| **Templates** | Page structures without real content | Layout with placeholders, page grid |
| **Pages** | Templates with real content | Homepage, Dashboard |

### Key Principles

- **Bottom-up**: Build small elements before large ones
- **Reusability**: Each level can be reused everywhere
- **Consistency**: Modifying an atom impacts the whole system
- **Documentation**: Each component is documented in isolation

---

## Essential Components by Category

### General

| Component | Usage | Variants |
|-----------|-------|----------|
| **Button** | Primary and secondary actions | Primary, Secondary, Ghost, Link, Icon |
| **Icon** | Visual representation of action/concept | Sizes (sm, md, lg), Filled, Outlined |
| **Typography** | Structured text | Heading 1-6, Body, Caption, Label |

### Layout

| Component | Usage | Key Properties |
|-----------|-------|----------------|
| **Grid** | Column-based layout | columns, gap, responsive breakpoints |
| **Flex** | Flexible layout | direction, justify, align, wrap |
| **Divider** | Visual separation | orientation (horizontal/vertical), variant |
| **Space** | Spacing between elements | size (xs, sm, md, lg, xl) |
| **Container** | Centered container with max-width | size, padding |

### Navigation

| Component | Usage | Considerations |
|-----------|-------|----------------|
| **Tabs** | Switch between views | Active state, disabled, icons |
| **Breadcrumb** | Show navigation hierarchy | Separator, collapsible |
| **Menu** | List of actions/links | Nested, icons, keyboard nav |
| **Pagination** | Navigate between data pages | Simple/complex, page size |
| **Sidebar** | Lateral navigation | Collapsible, nested items |

### Data Entry

| Component | Usage | States |
|-----------|-------|--------|
| **Input** | Text input | Text, Password, Number, Search |
| **Select** | Selection from a list | Single, Multiple, Searchable |
| **Checkbox** | Multiple selection | Checked, Indeterminate, Group |
| **Radio** | Single selection | Group, Horizontal/Vertical |
| **Switch** | Toggle on/off | With label, Sizes |
| **DatePicker** | Date selection | Range, Time, Presets |
| **Slider** | Value selection on a range | Range, Steps, Marks |
| **TextArea** | Multiline input | Auto-resize, Max length |

### Data Display

| Component | Usage | Variants |
|-----------|-------|----------|
| **Card** | Information container | Clickable, Hoverable, Bordered |
| **Table** | Tabular data | Sortable, Selectable, Expandable |
| **List** | List of elements | Simple, With actions, Virtualized |
| **Avatar** | User representation | Image, Initials, Icon, Group |
| **Badge** | Numeric/status indicator | Dot, Count, Colors |
| **Tag** | Categorization/labels | Closable, With icon, Colors |
| **Tooltip** | Contextual info on hover | Positions, Arrow |

### Feedback

| Component | Usage | Variants |
|-----------|-------|----------|
| **Alert** | Important inline message | Info, Success, Warning, Error |
| **Modal** | Blocking dialog | Sizes, Closable, Centered |
| **Toast** | Temporary notification | Positions, Auto-dismiss, Actions |
| **Progress** | Progress indication | Bar, Circle, Steps |
| **Skeleton** | Loading placeholder | Text, Avatar, Card, Custom |
| **Spinner** | Loading in progress | Sizes, Colors, Overlay |

---

## Component States

Every interactive component must define all its visual states.

### Standard States

| State | Description | Visual Treatment |
|-------|-------------|------------------|
| **Default** | Base state at rest | Standard style |
| **Hover** | Cursor above | Slight modification (brightness, shadow) |
| **Active/Pressed** | Being clicked | Depression effect (scale, reduced shadow) |
| **Focus** | Selected by keyboard | Visible ring/outline (accessibility) |
| **Disabled** | Non-interactive | Reduced opacity (50-60%), cursor: not-allowed |
| **Loading** | Action in progress | Spinner, "Loading..." text, disabled |
| **Error** | Validation error | Red border, error message |
| **Success** | Successful action | Green border, visual feedback |

### Example: Button States

```
Default   → Background: primary, cursor: pointer
Hover     → Background: primary-dark (+10% darker)
Active    → Background: primary-darker, transform: scale(0.98)
Focus     → Box-shadow: 0 0 0 3px primary-alpha
Disabled  → Opacity: 0.5, cursor: not-allowed
Loading   → Spinner + text, pointer-events: none
```

### Transitions

- **Duration**: 150-200ms for micro-interactions
- **Easing**: ease-out for entries, ease-in for exits
- **Properties**: background-color, border-color, box-shadow, transform

---

## Interaction Patterns

### Forms

| Pattern | Description | Implementation |
|---------|-------------|----------------|
| **Inline Validation** | Real-time validation | onBlur or onChange with debounce |
| **Multi-step Form** | Form in steps | Progress indicator, validation per step |
| **Autosave** | Automatic saving | Debounce, status indicator |
| **Field Dependencies** | Conditional fields | Show/hide based on values |
| **Smart Defaults** | Intelligent pre-filling | History, geolocation, preferences |

### Navigation

| Pattern | Description | When to Use |
|---------|-------------|-------------|
| **Tabs** | Mutually exclusive content | 2-7 items, related content |
| **Accordion** | Expandable content | FAQ, optional details |
| **Dropdown Menu** | Hidden actions/options | Secondary actions |
| **Command Palette** | Action search | Power users, shortcuts |
| **Breadcrumb** | Navigation path | Deep hierarchies |

### Data Patterns

| Pattern | Description | UX |
|---------|-------------|-----|
| **Filter** | Reduce results | Visible filters or in panel |
| **Sort** | Reorder results | Direction indicator |
| **Search** | Text search | Autocomplete, highlights |
| **Pagination** | Navigation by pages | Or infinite scroll |
| **Bulk Actions** | Actions on multiple selection | Checkbox + action bar |

### Feedback Patterns

| Pattern | Description | Duration |
|---------|-------------|----------|
| **Toast** | Non-blocking notification | 3-5 seconds |
| **Inline Message** | Contextual feedback | Until resolution |
| **Modal Confirmation** | Destructive action | Requires explicit action |
| **Progress Indicator** | Long operation | Until completion |
| **Optimistic Update** | UI updated before server | Rollback on error |

### Onboarding Patterns

| Pattern | Description | Usage |
|---------|-------------|-------|
| **Coachmarks** | Highlight points on UI | Key features, 3-5 max |
| **Walkthrough** | Step-by-step guided tour | First use |
| **Empty State CTA** | Guide in empty states | First action |
| **Contextual Tooltips** | Help on hover | Complex features |
| **Checklist** | Onboarding progress | Multi-step setup |

---

## Empty States

Empty states are opportunities to guide the user.

### Empty State Anatomy

```
+----------------------------------+
|                                  |
|       [Illustration/Icon]        |
|                                  |
|         Explanatory Title        |
|    Optional secondary message    |
|                                  |
|      [ Call-to-Action ]          |
|                                  |
|       Help link (optional)       |
+----------------------------------+
```

### Types of Empty States

| Type | Message | CTA |
|------|---------|-----|
| **First use** | "Welcome! Create your first project" | "Create a project" |
| **No results** | "No results for 'xyz'" | "Modify filters" |
| **Cleared** | "All items are processed" | "View history" |
| **Error** | "Unable to load data" | "Retry" |
| **No permission** | "You don't have access to this section" | "Request access" |

### Best Practices

- **Illustration**: Light, consistent with brand
- **Tone**: Friendly, not guilt-inducing
- **Clear action**: Single main CTA
- **Help**: Link to documentation if relevant

---

## Loading States

Clearly communicate that something is happening.

### When to Use What

| Pattern | Unknown Duration | Known Duration | Predictable Structure |
|---------|-----------------|----------------|----------------------|
| **Spinner** | Yes | - | - |
| **Progress Bar** | - | Yes | - |
| **Skeleton** | - | - | Yes |

### Spinner

```
Usage: Loading of unknown duration
Placement: Center of concerned container
Size: Proportional to the area
Accompaniment: Optional text ("Loading...")
```

### Progress Bar

```
Usage: Upload, download, step-by-step processing
Information: Percentage, remaining time (if calculable)
Types: Determinate (known %), Indeterminate (unknown %)
```

### Skeleton

```
Usage: Content with predictable structure
Advantage: Reduces Cumulative Layout Shift (CLS)
Implementation: Animated gray shapes mimicking content
Animation: Pulse or shimmer (left to right)
```

### Best Practices

- **Instant (< 100ms)**: No indicator
- **Short (100ms - 1s)**: Subtle indicator (opacity change)
- **Medium (1s - 10s)**: Spinner or skeleton
- **Long (> 10s)**: Progress bar with estimation

---

## Design Tokens for Components

Tokens standardize component properties.

### Spacing Tokens

```css
/* Component spacing */
--button-padding-x: var(--space-4);      /* 16px */
--button-padding-y: var(--space-2);      /* 8px */
--card-padding: var(--space-4);          /* 16px */
--input-padding-x: var(--space-3);       /* 12px */
--input-padding-y: var(--space-2);       /* 8px */
--modal-padding: var(--space-6);         /* 24px */
```

### Size Tokens

```css
/* Component heights */
--input-height-sm: 32px;
--input-height-md: 40px;
--input-height-lg: 48px;
--button-height-sm: 32px;
--button-height-md: 40px;
--button-height-lg: 48px;

/* Touch targets (minimum 44px for mobile) */
--touch-target-min: 44px;
```

### Border Radius Tokens

```css
--button-radius: var(--radius-md);       /* 8px */
--card-radius: var(--radius-lg);         /* 12px */
--input-radius: var(--radius-md);        /* 8px */
--badge-radius: var(--radius-full);      /* 9999px */
--modal-radius: var(--radius-xl);        /* 16px */
```

### Shadow Tokens

```css
--card-shadow: var(--shadow-sm);
--dropdown-shadow: var(--shadow-md);
--modal-shadow: var(--shadow-lg);
--button-shadow: none;
--button-shadow-hover: var(--shadow-sm);
```

---

## Best Practices

### Composition over Inheritance

```
Good:  <Card><CardHeader/><CardBody/><CardFooter/></Card>
Bad:   <Card header="..." body="..." footer="..." />
```

- Composed components rather than monolithic
- Slots/children for content
- Props for configuration

### Single Responsibility

Each component does ONE thing well:
- `Button`: Triggers an action
- `Input`: Text input
- `Card`: Visual container

No "god" components that do everything.

### Props Consistency

Use the same prop names everywhere:

| Prop | Usage | Values |
|------|-------|--------|
| `size` | Component size | 'sm', 'md', 'lg' |
| `variant` | Visual style | 'primary', 'secondary', 'ghost' |
| `disabled` | Disabled state | boolean |
| `loading` | Loading state | boolean |
| `fullWidth` | Takes full width | boolean |

### Theming via Tokens

```
Good:  background: var(--color-primary);
Bad:   background: #3B82F6;
```

- All values via tokens
- Enables theming (dark mode, white label)
- Facilitates global modifications

### Accessibility

Every interactive component must:
- Have a visible focus state
- Be keyboard navigable
- Have appropriate ARIA attributes
- Respect color contrasts

---

## Component Checklist

Before finalizing a component:

### Structure
- [ ] Clear single responsibility
- [ ] Props consistent with system
- [ ] Composition prioritized

### States
- [ ] All visual states defined
- [ ] Smooth transitions (150-200ms)
- [ ] Loading state if relevant

### Accessibility
- [ ] Visible focus state
- [ ] Keyboard navigation
- [ ] ARIA attributes
- [ ] Sufficient contrast

### Tokens
- [ ] Spacing via tokens
- [ ] Colors via tokens
- [ ] No hardcoded values

### Documentation
- [ ] Props documented
- [ ] Variants illustrated
- [ ] Usage examples
