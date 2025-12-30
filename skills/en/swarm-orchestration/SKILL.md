---
name: swarm-orchestration
description: Swarms orchestration - Coordinator manages N parallel executors, consolidates, merges
---

# Skill Swarm Orchestration

How a Coordinator orchestrates multiple Executors in parallel and consolidates their work.

---

## Architecture

```
COORDINATOR
├─ Read roadmap → Analyze dependencies
├─ ask_user: Select plans
├─ Invoke Executors (parallel)
│
├─ EXECUTOR-1 (Plan-XX)
│  ├─ Impl + Refactoring → Tester → Quality
│  └─ Report → Coordinator
│
├─ EXECUTOR-2 (Plan-YY) [parallel]
│  └─ Same
│
└─ Consolidate + Review + Merge
```

---

## Coordinator Workflow (7 phases)

| Phase | Action |
|-------|--------|
| 1 | Load skill → Create todos → Read roadmap |
| 2 | Identify pending plans → Analyze dependencies |
| 3 | ask_user: Select plans for execution |
| 4 | Invoke Executors in parallel |
| 5 | Wait for all reports → Collect |
| 6 | Consolidate all → ask_user: Review |
| 7 | Update plans/roadmap → Merge all → Sync |

---

## Report Format

**All agents use this format** (use reporting-* skills):

```
✅ Results
⚠️ Problems
🔧 Actions Required
📌 Important Notes
```

Executor → Load `reporting-executor` skill  
Refactoring → Load `reporting-refactoring` skill  
Tester → Load `reporting-tester` skill  
Quality → Load `reporting-quality` skill  

---

## Important Notes Propagation

```
REFACTORING notes → EXECUTOR includes integrally
                 ↓
TESTER notes → EXECUTOR includes integrally
                 ↓
QUALITY notes → EXECUTOR includes integrally
                 ↓
EXECUTOR consolidated report → COORDINATOR
                 ↓
COORDINATOR → USER (all notes preserved)
```

**CRITICAL**: Notes NEVER summarized, always integral.

---

## Plan Dependencies

Before invoking an Executor, verify:

```
Plan-XX pending
├─ Requires Plan-ZZ?
│  ├─ If Plan-ZZ = Done → OK
│  ├─ If Plan-ZZ = Pending → Suggest order
│  └─ Else → OK
```

---

## Two Modes (Identical)

**Simple Mode (N=1)**: One plan, one executor  
**Swarm Mode (N>1)**: Multiple plans, parallel executors

Same architecture, just N=1 or N>1.

---

## Feedback Loop & Escalation

```
Executor has question → Report in Important Notes
                    ↓
Coordinator sees it → ask_user with context
                    ↓
User validates approach → Executor continues
```

All in conversation context, no files created.

---

## Key Points

- **Executors orchestrate sub-agents**: REFACTORING → TESTER → QUALITY
- **Reports cascade up**: Each level consolidates from its children
- **Important Notes propagate integrally**: Never summarized
- **User Validation at Coordinator**: After implementation
- **No executor merges**: Coordinator handles all
- **Communication in context**: No files created

---

## Coordinator vs Executor

| Aspect | Coordinator | Executor |
|--------|---|---|
| Scope | Roadmap + N plans | 1 plan |
| Invokes | Executors | Refactoring, Tester, Quality |
| Skills | swarm-orchestration, agentic-flow | agentic-flow + context skills |
| Reports | Consolidates N reports | Consolidates 3 sub-agent reports |
| Merges | Manages all | None (Coordinator handles) |

---

## Worktree Synchronization

After merges (by Coordinator):

```bash
make sync-worktrees
```

Synchronizes all worktrees with main. If conflict: report to user.
