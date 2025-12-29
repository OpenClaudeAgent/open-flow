---
name: clean-code
description: Clean code principles - Naming, functions, DRY, KISS, YAGNI
---

# Clean Code Skill

This skill contains fundamental principles for writing clean, readable, and maintainable code.

---

## Fundamental principles

### DRY - Don't Repeat Yourself

Every piece of knowledge must have a single, unambiguous representation.

**Violation symptoms**:
- Copy-paste code
- Logic duplicated in multiple places
- Repeated constants

**Solutions**:
- Extract into function/method
- Create abstractions
- Centralize constants

### KISS - Keep It Simple, Stupid

Simplicity is the ultimate sophistication.

**Violation symptoms**:
- Over-engineering
- Premature abstractions
- Complex solutions for simple problems

**Solutions**:
- Start simple, add complexity if needed
- Prefer readability over cleverness
- Solve the current problem, not hypothetical future ones

### YAGNI - You Ain't Gonna Need It

Don't implement something until it's necessary.

**Violation symptoms**:
- "Just in case" features
- Abstractions for non-existent use cases
- Configuration for unlikely scenarios

**Solutions**:
- Implement the minimum required
- Add when need is real
- Refactor rather than predict

---

## Naming

### Variables

| Type | Convention | Example |
|------|------------|---------|
| Boolean | is/has/can/should prefix | `isVisible`, `hasError`, `canEdit` |
| Collection | Plural | `users`, `items`, `errors` |
| Counter | count/num suffix | `userCount`, `numItems` |

### Functions

| Type | Convention | Example |
|------|------------|---------|
| Action | Verb + noun | `getUser`, `saveDocument`, `validateInput` |
| Boolean | is/has/can prefix | `isValid`, `hasPermission` |
| Transformation | to + type | `toString`, `toJson` |
| Event handler | on + event | `onClick`, `onSubmit` |

### Classes

| Type | Convention | Example |
|------|------------|---------|
| Entity | Singular noun | `User`, `Document` |
| Service | Name + Service | `AuthService`, `PaymentService` |
| Repository | Name + Repository | `UserRepository` |
| Factory | Name + Factory | `ConnectionFactory` |

### General rules

- Descriptive and pronounceable names
- Avoid obscure abbreviations
- Length proportional to scope
- Consistency throughout project

---

## Functions

### Size

- **Ideally**: 5-15 lines
- **Maximum**: 20-30 lines
- If longer: extract sub-functions

### Parameters

| Number | Verdict |
|--------|---------|
| 0 | Ideal |
| 1-2 | Good |
| 3 | Acceptable |
| 4+ | Refactor (parameter object) |

### Single Responsibility

One function = one thing.

```
// BAD
function processUser(user) {
    validate(user);
    save(user);
    sendEmail(user);
    log(user);
}

// GOOD
function processUser(user) {
    validateUser(user);
    saveUser(user);
    notifyUser(user);
}
```

### Abstraction level

A function should stay at a single abstraction level.

```
// BAD - Mixes high and low level
function renderPage() {
    const html = "<html>";
    loadData();
    processTemplates();
    return html + "</html>";
}

// GOOD - Single level
function renderPage() {
    const data = loadData();
    const content = processTemplates(data);
    return wrapInHtml(content);
}
```

---

## Comments

### Good comments

- **Intent**: Why, not how
- **Clarification**: Complex regex, algorithms
- **Warning**: Consequences, pitfalls
- **TODO**: Temporary, with ticket

### Bad comments

- Code paraphrase
- Commented code
- Modification logs
- Noise ("default constructor")

### Golden rule

If you need a comment, first ask if the code can be clearer.

---

## Structure

### Early return

```
// BAD
function process(data) {
    if (data) {
        if (data.valid) {
            // ... 50 lines
        }
    }
}

// GOOD
function process(data) {
    if (!data) return;
    if (!data.valid) return;
    // ... 50 lines
}
```

### Avoid nesting

Maximum 2-3 indentation levels.

### Positive conditions

```
// BAD
if (!isNotValid)

// GOOD
if (isValid)
```

---

## Code smells

| Smell | Description | Solution |
|-------|-------------|----------|
| Long method | Function too long | Extract |
| Large class | Class too big | Separate responsibilities |
| Long parameter list | Too many params | Parameter object |
| Duplicate code | Copy-paste | Extract function/class |
| Dead code | Unused code | Delete |
| Magic numbers | Hardcoded values | Named constants |
| Feature envy | Method uses another class too much | Move |
| Data clumps | Repeated data groups | Create object |

---

## Checklist

- [ ] Descriptive and consistent names
- [ ] Short functions (< 20 lines)
- [ ] Functions with few parameters (< 4)
- [ ] Single abstraction level per function
- [ ] No duplication
- [ ] No magic numbers
- [ ] No commented code
- [ ] Early returns used
- [ ] Maximum 2-3 indentation levels
