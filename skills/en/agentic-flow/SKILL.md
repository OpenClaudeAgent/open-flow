---
name: agentic-flow
description: Agentic workflow - Feature lifecycle, worktree isolation, inter-agent collaboration
---

# Agentic Flow Skill

This skill describes the development workflow assisted by specialized agents.

---

## Feature Lifecycle

```
┌─────────────────────────────────────────────────────────────────┐
│                        FEATURE LIFECYCLE                         │
└─────────────────────────────────────────────────────────────────┘

  1. IDEATION
     │
     │  User expresses the need
     │
     ▼
  2. PLANNING ────────────────────────► ROADMAP
     │                                   │
     │                                   ├── Output: roadmap/plan-XX.md
     │                                   │
     ▼◄──────────────────────────────────┘
  3. IMPLEMENTATION ──────────────────► EXECUTOR
     │                                   │
     │                                   ├── Skills: ui-design-principles, qml, qt-cpp
     │                                   ├── Output: src/
     │                                   │
     ▼◄──────────────────────────────────┘
  4. USER VALIDATION ─────────────────► EXECUTOR
     │                                   │
     │                                   ├── Launch app (make run &)
     │                                   ├── Generate test scenarios
     │                                   ├── 🔔 MCP ask_user "Validation required"
     │                                   ├── Iterate if problem
     │                                   │
     ▼◄──────────────────────────────────┘
   5. TESTS ──────────────────────────► TESTER (invoked by Executor)
      │                                   │
      │                                   ├── Skill: functional-testing
      │                                   ├── If not testable → REFACTORING
      │                                   │                        └── Skill: testability-patterns
      │                                   ├── Output: tests/
      │                                   ├── Run entire suite (make test)
      │                                   │
      ▼◄──────────────────────────────────┘
  6. QUALITY ─────────────────────────► QUALITY (invoked by Executor)
     │                                   │
     │                                   ├── Skills: code-review
     │                                   ├── Code review (src/) + Tests review (tests/)
     │                                   ├── Output: quality/validation-XX.md
     │                                   │
     ▼◄──────────────────────────────────┘
  7. MERGE ───────────────────────────► EXECUTOR
     │                                   │
     │                                   ├── 🔔 MCP ask_user "Should I merge?"
     │                                   ├── Skill: git-conventions
     │                                   ├── Commit + Version Tag
     │                                   │
     ▼◄──────────────────────────────────┘
  8. RELEASE
     │
     └── User publishes
```

---

## Agents and responsibilities

| Agent | Role | Scope | Skills |
|-------|------|-------|--------|
| **Roadmap** | Planning | `roadmap/` | - |
| **Executor** | Implementation | `src/` | ui-design-principles, qml, qt-cpp, git-conventions |
| **Tester** | Auto tests | `tests/` | functional-testing |
| **Quality** | QA + Code Review | `quality/` | code-review |
| **Refactoring** | Testability | `src/` | testability-patterns |

---

## MCP Notification Points

| Step | Agent | Title | Question |
|------|-------|-------|----------|
| Validation | Executor | "Validation required" | "Test the scenarios" |
| Merge | Executor | "Feature ready" | "Should I merge to main?" |
| Testability | Tester | "Authorization required" | "Invoke Refactoring?" |
| Manual tests | Quality | "Manual tests ready" | "Shall we begin?" |

---

## Skills by phase

### Phase 3: Implementation (Executor)

| Condition | Skill to load |
|-----------|---------------|
| `.qml` files | `qml` |
| UI components | `ui-design-principles` |
| Qt `.cpp/.h` files | `qt-cpp` |

### Phase 4: Tests (Tester)

| Condition | Skill to load |
|-----------|---------------|
| Always | `functional-testing` |
| Non-testable code | → Invoke Refactoring with `testability-patterns` |

### Phase 5: Quality

| Condition | Skill to load |
|-----------|---------------|
| Always | `code-review` |

### Phase 7: Merge (Executor)

| Condition | Skill to load |
|-----------|---------------|
| Commit/Tag | `git-conventions` |

---

## Agent Isolation (Worktrees)

Each agent operates in its own Git worktree:

| Worktree | Branch | Agent |
|----------|--------|-------|
| `worktrees/feature/[name]` | `feature/[name]` | Executor (created per feature) |
| `worktrees/roadmap/` | `worktree/roadmap` | Roadmap |
| `worktrees/quality/` | `worktree/quality` | Quality |
| `worktrees/test/` | `worktree/test` | Tester |
| `worktrees/refactoring/` | `worktree/refactoring` | Refactoring |

**Executor**: Creates a dedicated worktree for each feature:
```bash
git worktree add worktrees/feature/[name] -b feature/[name]
```

**Benefits**:
- No conflicts between agents
- Branch traceability
- Multiple features in parallel
- `main` under user control

---

## Global rules

| Rule | Description |
|------|-------------|
| System dates | Always `date +%Y-%m-%d` |
| Worktrees | Each agent in its worktree |
| Validation | No merge without explicit approval |
| Isolation | Don't modify outside your scope |
| MCP | Use `ask_user` according to agent instructions |

---

## Worktree synchronization

After merge to main:

```bash
make sync-worktrees
```

- Synchronizes all worktrees with main
- If conflict: report to user without resolving

---

## Specific workflows

### Tester-Refactoring Tandem

```
Tester identifies non-testable code
       ↓
🔔 ask_user "Authorization required"
       ↓
Refactoring (skill: testability-patterns)
       ↓
Tester writes the tests
```

### Quality: Double review

```
Executor invokes Quality
       ↓
Quality loads skill: code-review
       ↓
Phase 1: Code review (src/)
       ↓
Phase 2: Tests review (tests/)
       ↓
Consolidated report → Executor
```
