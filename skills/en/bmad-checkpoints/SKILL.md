---
name: bmad-checkpoints
description: User validation points (ask_user) at critical moments in BMAD workflows
---

# Skill BMAD - Validation Checkpoints

This skill defines WHEN to use `notify_ask_user` in BMAD workflows.

## Principle

Checkpoints are **critical pause points** where the agent requests a decision/validation from the user before continuing.

**Golden rule**: Use `ask_user` only at moments where a user decision is BLOCKING for the next step.

## Checkpoints by Agent

### PM (Product Manager)

| Checkpoint | Trigger | Question | Options |
|------------|---------|----------|---------|
| **MVP scope validation** | End of PRD | "MVP scope finalized. Validate before architecture?" | ["Validate", "Modify scope"] |

### Architect

| Checkpoint | Trigger | Question | Options |
|------------|---------|----------|---------|
| **Stack/pattern choice** | Major decision | "Proposed stack: [X]. Pattern: [Y]. Validate?" | ["Approve", "See alternatives", "Modify"] |

### Dev (Developer)

| Checkpoint | Trigger | Question | Options |
|------------|---------|----------|---------|
| **Tests fail 3x** | Blocker | "Tests failing after 3 attempts. Action?" | ["Debug together", "View logs", "Skip task"] |
| **Story complete** | End of implementation | "Story X.Y done, tests OK. Create PR?" | ["Yes", "More work needed"] |

### SM (Scrum Master)

| Checkpoint | Trigger | Question | Options |
|------------|---------|----------|---------|
| **Sprint derails** | Velocity < 50% | "Sprint struggling (X% velocity). Action?" | ["Reduce scope", "Continue", "Cancel sprint"] |

### TEA (Test Engineer)

| Checkpoint | Trigger | Question | Options |
|------------|---------|----------|---------|
| **Quality gates fail** | Blocker | "Quality gates failing: [list]. Action?" | ["Fix", "Force", "View details"] |

### Quick-Flow

| Checkpoint | Trigger | Question | Options |
|------------|---------|----------|---------|
| **Tech spec validated** | Before implementation | "Tech spec ready. Validate before dev?" | ["Validate", "Modify"] |

## ask_user Format

```
notify_ask_user(
  title: "[Emoji] Checkpoint: [Action]",
  question: "[Clear question]",
  options: ["Option 1", "Option 2", ...],
  urgency: "normal" | "high",  # high = blocker
  agent: "[Agent name]",
  task: "[Current task]",
  branch: "[Branch]"
)
```

## Rules

### USE ask_user for:
- Blockers (tests fail 3x, quality gates, build fail)
- Major decisions with alternatives
- Critical phase-end validations

### DO NOT use ask_user for:
- Progress updates (use todos)
- Trivial action confirmations
- Multiple questions (1 question at a time)

## Example

```
Story 1.2 - Task 3: Tests failing

Attempt 1: FAIL
Attempt 2: FAIL  
Attempt 3: FAIL

--> CHECKPOINT TRIGGERED

notify_ask_user(
  title: "Tests Failing",
  question: "Tests failing after 3 attempts on Task 3",
  options: ["Debug together", "View logs", "Skip task"],
  urgency: "high",
  agent: "Dev",
  task: "Story 1.2 - Task 3",
  branch: "feature/story-1.2"
)

[WAITING FOR RESPONSE]
```
