---
name: interactive-validation
description: Interactive validation with manual testing and user feedbacks
---

# Interactive Validation - Skill

Functional validation process with user: manual tests, feedbacks, iteration.

## When to use Ask User

Use Ask User (MCP Notify) to interrupt user:
1. **Phase 5 (Coordinator)**: Reports received with problems/questions
2. **Phase 6 (Coordinator)**: Validation (app ready? feedbacks? final approval?)
3. **Phase 1 (Executor)**: If ambiguity on plan (optional)

---

## Workflow (4 steps)

### Step 1: Prepare App
- List modified files + added features
- Ask: "Ready to test?"

### Step 2: Manual Tests
- User tests app
- Reports problems, validations, feedbacks

### Step 3: Iteration if Problems
- Request corrections from Executors
- Executors re-invoke sub-agents
- Receive revised report
- Back to Step 2 (re-test)

### Step 4: Final Validation
- Request final confirmation
- Proceed Phase 7 (Merges)

---

## Validation Steps

- **Step 1**: Ask User - "App ready, which files to test?"
- **Step 2**: Ask User - "What behaviors fail?"
- **Step 3**: Ask User - "Corrections received, re-test?"
- **Step 4**: Ask User - "Final validation confirmed?"

---

## Principles

- ✅ Ask User interrupts user (may be disconnected)
- ✅ Iterate until validation OK
- ✅ Todos track progress in real-time
- ✅ Executor fixes, Coordinator orchestrates
- ✅ Include important comments integrally  
