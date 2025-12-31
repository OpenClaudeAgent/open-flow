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

### Step 1: Prepare for User Validation
- List modified files + added features
- Provide clear testing instructions
- **Ask User**: "Here's what was implemented. Ready to test?"

### Step 2: USER Tests (not the agent)
- **The USER tests themselves** (not the agent)
- Agent waits for user feedback
- **Ask User**: "What behaviors work? Which ones fail?"

> ⚠️ **IMPORTANT**: The agent CANNOT validate on behalf of the user.
> Manual tests are performed by the USER, not simulated by the agent.

### Step 3: Iteration if Problems
- User reports problems
- Request corrections from Executors
- Executors fix + re-invoke sub-agents
- Receive revised report
- **Ask User**: "Corrections applied. Can you re-test?"
- Back to Step 2

### Step 4: Final Validation by User
- **Ask User**: "Everything works? Final validation confirmed?"
- Wait for explicit user confirmation
- Proceed Phase 7 (Merges) only after confirmation

---

## Validation Steps

- **Step 1**: Ask User - "App ready, which files to test?"
- **Step 2**: Ask User - "What behaviors fail?"
- **Step 3**: Ask User - "Corrections received, re-test?"
- **Step 4**: Ask User - "Final validation confirmed?"

---

## Principles

- ✅ **USER validates** - Agent CANNOT validate on their behalf
- ✅ Ask User interrupts user (may be disconnected)
- ✅ Wait for explicit feedback before continuing
- ✅ Iterate until user validation OK
- ✅ Todos track progress in real-time
- ✅ Executor fixes, Coordinator orchestrates
- ✅ Never mark "manual tests" as complete without user feedback

## Anti-patterns to avoid

- ❌ Marking tests as "passed" without user feedback
- ❌ Simulating manual tests automatically
- ❌ Moving to next step without explicit confirmation
- ❌ Assuming implementation works without validation  

---

## Multi-Features Mode (RC)

When multiple features need to be validated together:

1. **Create RC branch**: `git checkout -b rc/test-$(date +%Y%m%d) main`
2. **Merge all features** into RC
3. **USER tests** the integrated whole
4. **If bug**: Fix on original branch → Re-merge into RC → Re-test
5. **Validation OK**: Delete RC → Merge features individually

> ⚠️ NEVER fix directly on the RC branch.
> Fixes are made on the original feature branches.
