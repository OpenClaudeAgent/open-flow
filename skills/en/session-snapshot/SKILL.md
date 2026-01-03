# Skill: Session Snapshot

Save and reload session state for complex debugging.

---

## Concept

Before a potentially long debugging phase, save the complete session state:
- Todos state
- Plans in progress
- Consolidated reports
- Created branches
- Identified problems
- **Complete debugging todo** (new)

Allows resuming the session later without losing context, even after multiple debugging sessions.

---

## Todo Workflow

### 1. Complete Todo (in the snapshot)

When creating a snapshot, generate a **contextual complete todo**:

```
## Debugging Todos

- [ ] Analyze the problem: [description]
- [ ] Identify cause in [files]
- [ ] Apply the fix
- [ ] Re-invoke Executor if needed
- [ ] Retest the behavior
- [ ] Validate with user
- [ ] ★ Reload session to continue (snapshot-XXX.md) ★
```

The last item is **always** "Reload session" - it's the resume point.

### 2. Intermediate Todo (during debugging)

When entering debugging, create a **lightweight todo** that references the snapshot:

```
- [ ] Debug in progress → see .session/snapshot-XXX.md for full context
- [ ] [Specific action for current problem]
- [ ] [Specific action 2]
```

This todo is lightweight and focused on immediate action.

### 3. Resume (reload)

When reloading a session:
1. Read the snapshot
2. Extract the "Debugging Todos" section
3. Recreate todos with saved statuses
4. Resume the workflow

---

## Structure

```
.session/
└── snapshot-YYYY-MM-DD-context.md
```

---

## Triggering

The Coordinator **proposes** before Phase 6 (Interactive Validation):

```
ask_user(
  title: "Session Snapshot"
  question: "Do you want to save a session snapshot before debugging?"
  options: ["Yes, create snapshot", "No, continue"]
)
```

It's always the user who decides. The Coordinator never creates snapshots automatically.

---

## Creating a Snapshot

### Workflow

1. Create `.session/` folder if needed
2. Generate name: `snapshot-[YYYY-MM-DD]-[context].md`
3. **Analyze context to generate Debugging Todo**
4. Fill template with current state + debugging todos
5. **Create Intermediate Todo** (during debugging)
6. Inform user: "Snapshot created: [path]"

### Content to save

| Element | Description |
|---------|-------------|
| Context | Plans in progress, current phase, objective |
| Original Todos | Complete copy of current todos state |
| **Debugging Todos** | Complete todo generated for debugging (new) |
| Branches | List of branches with their status |
| Reports | Consolidated executor reports |
| Problems | List of identified problems |
| Next actions | What remains to be done |

### Debugging Todo Generation

Analyze context (detected problems, reports) to generate an adapted todo:

```
Example for a UI bug:
- [ ] Analyze bug: button not clickable in SettingsPage
- [ ] Identify the QML component
- [ ] Check signals/slots
- [ ] Apply the fix
- [ ] Test manually
- [ ] Re-invoke Tester for automated tests
- [ ] ★ Reload session to continue ★
```

The todo is **contextual** - adapted to the specific problem.

---

## Snapshot Template

```markdown
# Session Snapshot

**Date**: [YYYY-MM-DD HH:MM]
**Context**: [Short description]
**File**: .session/snapshot-[YYYY-MM-DD]-[context].md

---

## General State

- **Plans in progress**: [list]
- **Current phase**: [N] - [Name]
- **Objective**: [description]

---

## Original Todos

[Copy of todos at snapshot time]
- [x] Todo 1 (completed)
- [ ] Todo 2 (in_progress)
- [ ] Todo 3 (pending)

---

## Debugging Todos

[Complete todo generated for debugging - TO RECREATE on reload]

| ID | Task | Status | Priority |
|----|------|--------|----------|
| D1 | Analyze the problem: [description] | pending | high |
| D2 | Identify cause in [files] | pending | high |
| D3 | Apply the fix | pending | high |
| D4 | Re-invoke Executor if needed | pending | medium |
| D5 | Retest the behavior | pending | high |
| D6 | Validate with user | pending | high |
| D7 | ★ Reload session to continue ★ | pending | low |

**Note**: D7 is the resume point if session is interrupted.
```

---

## Branches

| Branch | Plan | Status | Notes |
|--------|------|--------|-------|
| `feature/xxx` | Plan XX | In progress | [notes] |
| `feature/yyy` | Plan YY | Ready to merge | [notes] |

---

## Consolidated Reports

### Plan XX - [Name]

[Complete executor report]

#### Detected problems
- [x] Problem 1 (resolved)
- [ ] Problem 2 (in progress)

### Plan YY - [Name]

[Complete executor report]

---

## Identified Problems

| # | Problem | Severity | Status | Notes |
|---|---------|----------|--------|-------|
| 1 | [description] | High | In progress | [notes] |
| 2 | [description] | Medium | To do | [notes] |

---

## Next Actions

1. [ ] [Action 1]
2. [ ] [Action 2]
3. [ ] [Action 3]

---

## Debug Notes

[Section to fill during debugging]

### Session 1 - [Date]
- [Notes]

### Session 2 - [Date]
- [Notes]

---

## Resume

To resume this session:
1. Read this file
2. Recreate todos
3. Resume context
4. Continue Phase 6
```

---

## Reloading

When user asks to reload a session:

### Workflow

1. List snapshots in `.session/`
2. If multiple, ask which one to load
3. Read snapshot file
4. **Extract the "Debugging Todos" section**
5. **Recreate todos with TodoWrite** (use saved statuses)
6. Present context to user
7. Resume Phase 6

### Todo Recreation

On reload, recreate todos from the "Debugging Todos" table:

```python
# Example recreation
todos = [
    {"id": "D1", "content": "Analyze the problem: [description]", "status": "completed", "priority": "high"},
    {"id": "D2", "content": "Identify cause in [files]", "status": "in_progress", "priority": "high"},
    {"id": "D3", "content": "Apply the fix", "status": "pending", "priority": "high"},
    # ... etc
]
TodoWrite(todos)
```

### User commands

| Request | Action |
|---------|--------|
| "reload the session" | List snapshots, load most recent, recreate todos |
| "load snapshot X" | Load a specific snapshot, recreate todos |
| "list sessions" | Show available snapshots |

---

## Startup Reminder

If `.session/` contains snapshots:

```
Note: Session snapshots exist in .session/
- snapshot-2025-01-03-plan-15.md (2h ago)
- snapshot-2025-01-02-plan-12.md (yesterday)

Use "reload the session" to resume.
```

---

## Finalization

When debugging is complete and session is done:

1. User can delete snapshot manually
2. Or keep it as history
3. Coordinator never deletes snapshots automatically

---

## Best Practices

1. **One snapshot per debugging phase**: Don't accumulate too many snapshots
2. **Clear context**: Use a descriptive name (e.g., `snapshot-2025-01-03-cache-invalidation.md`)
3. **Debug notes**: Fill the section during debugging
4. **Cleanup**: Delete old snapshots when no longer useful
