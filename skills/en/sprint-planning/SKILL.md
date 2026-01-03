# Skill: Sprint Planning

Strategic planning by cycles and phases to organize roadmap plans.

## Available Cycles

### Cycle A: Quality-First (default)

| Phase | Focus | Objective |
|-------|-------|-----------|
| 1 | Bugfixes + E2E | Fix bugs, add E2E assertions |
| 2 | E2E Reinforcement | Safety net before refactoring |
| 3 | Refactoring | Improve code quality |
| 4 | Features | New functionalities |

**Usage**: Project with technical debt, stabilization phase

**Philosophy**: E2E tests serve as a safety net for refactoring. Each bugfix is an opportunity to improve E2E coverage.

### Cycle B: Feature-First

| Phase | Focus | Objective |
|-------|-------|-----------|
| 1 | Quick win features | Immediate value, low effort |
| 2 | Complex features | Major functionalities |
| 3 | E2E + Bugfixes | Post-feature stabilization |
| 4 | Refactoring | Clean accumulated debt |

**Usage**: MVP, need to deliver value quickly

### Cycle C: Maintenance

| Phase | Focus | Objective |
|-------|-------|-----------|
| 1 | Critical bugfixes | Urgent corrections |
| 2 | E2E Coverage | Non-regression tests |
| 3 | Documentation | Update docs |
| 4 | Minor refactoring | Quality quick wins |

**Usage**: Mature project, continuous maintenance

---

## Automatic Assignment

### Phase (by plan type)

| Detected keywords | Type | Phase Cycle A | Phase Cycle B |
|-------------------|------|---------------|---------------|
| fix, bug, hotfix, crash, regression | Bugfix | 1 | 3 |
| test, e2e, assertion, coverage | E2E | 2 | 3 |
| refactor, cleanup, debt, quality | Refactoring | 3 | 4 |
| feature, add, new, enhance, implement | Feature | 4 | 1 or 2 |
| doc, readme, documentation | Documentation | 4 | 4 |

### Priority (by criticality)

| Detected keywords | Priority | Description |
|-------------------|----------|-------------|
| crash, critical, blocker, security, data loss, urgent | **P0** | Blocking, handle immediately |
| bug, broken, regression, visible, user-facing | **P1** | Important, degraded UX |
| minor, polish, cleanup, nice-to-have, enhancement | **P2** | Desirable, not urgent |

**If ambiguous**: Use `ask_user` to confirm phase and/or priority.

---

## Workflow

### 1. Initialization

When user asks to initialize sprint planning:

```
ask_user(
  title: "Sprint Planning - Cycle Choice"
  question: "Which strategic cycle to use?"
  options: [
    "A: Quality-First (Bug->E2E->Refacto->Features)",
    "B: Feature-First (Features->E2E->Refacto)",
    "C: Maintenance (Bugfix->E2E->Doc->Refacto)"
  ]
)
```

Then create `SPRINTS.md` with the appropriate template.

### 2. Assigning a new plan

When creating a plan:

1. **Detect type** via keywords in title/context
2. **Determine priority** via criticality
3. **Assign to phase** based on active cycle
4. **Add to SPRINTS.md** in the right phase
5. **Inform user**: "Plan XX assigned to Phase N (P1)"

### 3. Handling urgencies

If an urgent plan arrives outside current phase:

```
ask_user(
  title: "Urgent plan detected"
  question: "Plan [XX] is type [bugfix] but we're in Phase [3-Refactoring]. What to do?"
  options: [
    "Integrate now (interrupt phase)",
    "Defer to next Phase 1",
    "Create hotfix outside cycle"
  ]
)
```

### 4. Phase transition

When all plans in a phase are complete:

1. Update phase status -> "Done"
2. Propose moving to next phase
3. If Phase 4 complete -> propose new cycle

### 5. Sprint status

When user asks for status:

- Show current phase
- List in-progress / done / pending plans
- Calculate progress (X/Y plans done)
- Suggest next actions

---

## SPRINTS.md Template

```markdown
# [Project] - Sprint Planning

## Configuration

- **Active cycle**: [A/B/C] - [Cycle name]
- **Current phase**: [N]
- **Cycle start date**: [YYYY-MM-DD]

---

## Overview

| Phase | Focus | Plans | Status |
|-------|-------|-------|--------|
| 1 | [Phase 1 Focus] | [links] | [emoji] |
| 2 | [Phase 2 Focus] | [links] | [emoji] |
| 3 | [Phase 3 Focus] | [links] | [emoji] |
| 4 | [Phase 4 Focus] | [links] | [emoji] |

Statuses: In progress | Pending | Done

---

## Phase 1: [Name]

**Objective**: [Description]

### Plans

| Priority | Plan | Description | Status |
|----------|------|-------------|--------|
| P0 | [link] | [desc] | [emoji] |
| P1 | [link] | [desc] | [emoji] |

### Checklist
- [ ] Plan XX
- [ ] Plan YY

---

## Phase 2: [Name]
[Same structure]

---

## Phase 3: [Name]
[Same structure]

---

## Phase 4: [Name]
[Same structure]

---

## Unassigned Plans

| Plan | Description | Suggested type | Suggested phase | Priority |
|------|-------------|----------------|-----------------|----------|
| [link] | [desc] | [type] | [N] | [P?] |

---

## Cycle History

| Cycle | Dates | Phases completed | Plans | Notes |
|-------|-------|------------------|-------|-------|
| 1 | [start-end] | 4/4 | [N] plans | [notes] |
```

---

## Typical Commands

| User request | Action |
|--------------|--------|
| "Initialize sprint planning" | Create SPRINTS.md with chosen cycle |
| "Assign plan XX" | Detect type/priority, add to phase |
| "Sprint status" | Current phase summary + progress |
| "Next phase" | Transition to next phase |
| "New cycle" | Archive current cycle, restart |

---

## Best Practices

1. **One plan = one phase**: Avoid plans spanning multiple phases
2. **Bugfix + E2E**: Each bugfix should include an E2E assertion
3. **P0 first**: Within a phase, handle P0 before P1/P2
4. **Phase review**: Before transition, validate with user
5. **Flexibility**: The cycle is a guide, not a rigid constraint
