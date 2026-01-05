---
name: bmad-tech-spec
description: BMAD Tech Spec - Create technical specification with implementation-ready stories for Quick Flow
---

# Skill BMAD - Tech Spec (Quick Flow)

Ce skill guide la création d'un Technical Specification pour Quick Flow - minimum ceremony, maximum efficiency.

## Objectif

Créer un tech spec lean avec stories implémentables pour petites features ou prototypes rapides.

## Principes Quick Flow

1. **Specs are for building, not bureaucracy**
2. **Code that ships > perfect code that doesn't**
3. **Planning and execution = same coin**
4. **Minimum viable spec** : Juste assez pour implémenter

## Workflow Tech Spec

### Phase 1 : Understand the Feature

**Pose des questions directes** :
- What problem does this solve?
- Who is the user?
- What's the happy path?
- What edge cases matter?

### Phase 2 : Technical Approach

**Définis** :
- Components impliqués
- Data flow
- API contracts (si applicable)
- Technology choices (stack existing ou simple)

### Phase 3 : Implementation Stories

**Crée 2-5 stories** avec tasks/subtasks :

**Template Story** :
```markdown
## Story [N]: [Title]

**Goal**: [What this story achieves]

### Tasks
- [ ] Task 1: [Specific action]
- [ ] Task 2: [Specific action]
- [ ] Task 3: [Specific action]

### Acceptance
- [x] Criteria 1
- [x] Criteria 2
```

### Phase 4 : Quick Validation

**Checklist rapide** :
- [ ] Feature clairement définie
- [ ] Stories sont actionnables
- [ ] Tech approach est simple
- [ ] Peut être implémenté en 1-4h

## Template Tech Spec (Quick Flow)

```markdown
# Tech Spec: [Feature Name]

## Problem
[1-2 sentences: what problem this solves]

## User Flow
1. User does [action]
2. System responds with [result]
3. User sees [outcome]

## Technical Approach

### Components
- **Frontend**: [Component names]
- **Backend**: [Endpoints/functions]
- **Database**: [Tables/collections]

### Data Flow
```
[Simple diagram ou bullets]
User Input → API → Service → DB → Response → UI
```

### API Contract (if applicable)
```
POST /api/feature
Request: { field1, field2 }
Response: { result }
```

## Implementation Stories

### Story 1: [Core Feature]
**Goal**: Implement the main happy path

**Tasks**:
- [ ] Create [component/endpoint]
- [ ] Add [validation/logic]
- [ ] Test happy path

**Acceptance**:
- [x] User can [do action]
- [x] System returns [expected result]

### Story 2: [Edge Cases]
**Goal**: Handle errors and edge cases

**Tasks**:
- [ ] Add error handling for [case]
- [ ] Validate [input]
- [ ] Test edge cases

**Acceptance**:
- [x] Graceful error messages
- [x] No crashes on invalid input

### Story 3: [Polish]
**Goal**: Make it production-ready

**Tasks**:
- [ ] Add loading states
- [ ] Improve UX feedback
- [ ] Write tests

**Acceptance**:
- [x] Tests pass
- [x] UX feels smooth

## Tech Stack
- [List technologies used - keep it simple]

## Estimated Effort
[1-4 hours]

## Notes
[Any quick notes, gotchas, or context]
```

## Example Complet

```markdown
# Tech Spec: Add Dark Mode Toggle

## Problem
Users want to switch between light and dark themes for better readability.

## User Flow
1. User clicks theme toggle button in header
2. App switches to dark/light theme
3. Preference is saved in localStorage

## Technical Approach

### Components
- **Frontend**: ThemeToggle button, ThemeProvider context
- **Backend**: None (client-side only)
- **Storage**: localStorage

### Data Flow
```
User clicks → Update Context → Apply CSS classes → Save to localStorage
                                ↓
                          Load from localStorage on mount
```

## Implementation Stories

### Story 1: Theme Toggle Component
**Goal**: Create working theme toggle

**Tasks**:
- [ ] Create ThemeToggle button component
- [ ] Create ThemeContext with light/dark state
- [ ] Apply CSS classes based on theme

**Acceptance**:
- [x] User can toggle between themes
- [x] UI updates immediately

### Story 2: Persist Theme
**Goal**: Remember user preference

**Tasks**:
- [ ] Save theme to localStorage on change
- [ ] Load theme from localStorage on mount
- [ ] Set default to light if no preference

**Acceptance**:
- [x] Theme persists across page reloads
- [x] Defaults to light for new users

### Story 3: Dark Mode Styles
**Goal**: Make dark mode look good

**Tasks**:
- [ ] Add dark mode CSS variables
- [ ] Update all components for dark mode
- [ ] Test contrast and readability

**Acceptance**:
- [x] All components look good in dark mode
- [x] Text is readable on dark background

## Tech Stack
- React Context API
- CSS custom properties (variables)
- localStorage

## Estimated Effort
2-3 hours

## Notes
- Use CSS variables for easy theme switching
- Consider system preference (prefers-color-scheme) in future
```

## Output

Génère le tech spec dans : `_bmad-output/quick-flow/tech-spec.md`

## Next Steps

Après Tech Spec :

1. **Quick Dev** → Utilise `/quick-flow` + skill `bmad-quick-dev`
2. **Code Review** → Utilise `/quick-flow` (nouveau contexte) + skill `bmad-code-review`
