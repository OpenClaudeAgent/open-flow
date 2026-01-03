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

Allows resuming the session later without losing context, even after multiple debugging sessions.

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
3. Fill template with current state
4. Inform user: "Snapshot created: [path]"

### Content to save

| Element | Description |
|---------|-------------|
| Context | Plans in progress, current phase, objective |
| Todos | Complete copy of todos state |
| Branches | List of branches with their status |
| Reports | Consolidated executor reports |
| Problems | List of identified problems |
| Next actions | What remains to be done |

---

## Snapshot Template

```markdown
# Session Snapshot

**Date**: [YYYY-MM-DD HH:MM]
**Context**: [Short description]

---

## General State

- **Plans in progress**: [list]
- **Current phase**: [N] - [Name]
- **Objective**: [description]

---

## Todos

```
[Complete copy of current todos with statuses]
- [x] Todo 1 (completed)
- [ ] Todo 2 (in_progress)
- [ ] Todo 3 (pending)
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
4. Recreate todos according to saved state
5. Present context to user
6. Resume Phase 6

### User commands

| Request | Action |
|---------|--------|
| "reload the session" | List snapshots, load most recent |
| "load snapshot X" | Load a specific snapshot |
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
