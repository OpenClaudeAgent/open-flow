# Skill: User Questions (ask_user)

This skill describes when and how to use the MCP `notify` (tool `ask_user`) to ask questions to the user.

## Principle

The `ask_user` tool is for asking questions to the user when you need an answer to continue. It is NOT for informing or notifying - it's for ASKING.

## Usage Restriction

**You should only use this tool IF:**
1. The user explicitly asked you to notify them
2. Your agent instructions specify to use this tool

**You should NOT use this tool for:**
- Informing about task completion (use conversation)
- Progress updates (use todos)
- Confirming simple actions (use conversation)

## When to use ask_user

| Situation | Title | Question | Options |
|-----------|-------|----------|---------|
| Need validation | "Validation required" | "[Context] - Can you validate?" | ["Looks good", "Problem"] |
| Need decision | "Decision required" | "[Specific question]" | [possible choices] |
| Need authorization | "Authorization required" | "May I [action]?" | ["Yes", "No"] |

## Parameters

| Parameter | Required | Description |
|-----------|----------|-------------|
| `title` | Yes | Short title (max 50 characters) |
| `question` | Yes | The question to ask |
| `options` | No | List of possible answers |
| `urgency` | No | low / normal / high |
| `repo` | No | Repository name |
| `branch` | No | Current git branch |
| `agent` | No | Agent name |
| `task` | No | Current task |

## Examples

### User validation required
```
Title: "Validation required"
Question: "The application is ready. Can you test feature X?"
Options: ["Looks good", "There's a problem"]
```

### Decision required
```
Title: "Decision required"
Question: "Should I use approach A or B?"
Options: ["Approach A", "Approach B", "Other suggestion"]
```

### Authorization required
```
Title: "Authorization required"
Question: "Code is not testable - May I invoke the refactoring agent?"
Options: ["Yes", "No"]
```

## Best Practices

1. **Be concise**: Short and clear questions
2. **Provide options**: Make it easy for the user to respond
3. **One question at a time**: No multiple questions
4. **Minimal context**: repo + branch are usually enough
