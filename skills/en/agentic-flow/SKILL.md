---
name: agentic-flow
description: Executor's agentic workflow - Analysis, implementation, sequential sub-agents
---

# Skill Agentic Flow

Workflow of **Executor** invoked by Coordinator.

**For multi-plan orchestration**, see skill `swarm-orchestration`.

---

## Executor Workflow (5 phases)

| Phase | Action |
|-------|--------|
| 1 | Load skill → Create todos → Analyze plan |
| 2 | Load relevant skills → Implement → Build |
| 3 | Invoke REFACTORING → TESTER → QUALITY (sequential) |
| 4 | Consolidate all reports (see reporting-* skills) |
| 5 | User Validation at Coordinator → Final report |

---

## Dynamic Skills Analysis

Executor identifies and loads skills based on files:

| File | Skill |
|------|-------|
| `.qml` | `qml` |
| UI components | `ui-design-principles` |
| `.cpp` / `.h` Qt | `qt-cpp` |
| Non-testable code | Assign to REFACTORING |

---

## Sequential Sub-Agents

Executor invokes in this **MANDATORY** order:

**1. REFACTORING** (skill: testability-patterns)
   └─ Worktree: Shared | Report: reporting-refactoring

**2. TESTER** (skill: functional-testing)
   └─ Worktree: Shared | Report: reporting-tester

**3. QUALITY** (skill: code-review)
   └─ Worktree: Shared (read-only) | Report: reporting-quality

---

## Reporting Skills

Use specialized skills to structure reports:

```
Executor → Load reporting-executor skill
├─ Include FULL report from Refactoring
├─ Include FULL report from Tester
├─ Include FULL report from Quality
└─ Consolidate all Important Notes (integrally)
```

**CRITICAL**: Important Notes are NEVER summarized.

---

## Shared Worktree Model

All agents use the SAME worktree created by Executor:

```
worktrees/feature/[name]
├─ Executor: R/W src/
├─ Refactoring: R/W src/
├─ Tester: R/W tests/
└─ Quality: read-only src/ + tests/
```

**Benefits**: No conflicts, isolation by feature, centralized merge.

---

## User Iteration

If User Validation fails (at Coordinator):

Coordinator requests correction → Executor fixes → Re-invokes sub-agents if needed

**No complete re-implementation.**

---

## Global Rules

| Rule | Description |
|------|-------------|
| System dates | `date +%Y-%m-%d` |
| Worktree | Shared by all (Executor + sub-agents) |
| User Validation | At Coordinator after implementation |
| Merges | Coordinator handles |
| Important Notes | Propagated integrally |
| Communication | Conversation context only |

---

## Worktree Synchronization

After merge (by Coordinator):

```bash
make sync-worktrees
```

Synchronizes all worktrees with main. If conflict: report to user.
