---
name: code-review
description: Code review principles - Checklist, constructive feedback, best practices
---

# Code Review Skill

This skill contains principles for effective and constructive code reviews.

---

## Review objectives

| Objective | Description |
|-----------|-------------|
| Quality | Detect bugs, edge cases, errors |
| Consistency | Maintain project standards |
| Sharing | Spread knowledge in the team |
| Learning | Learn from other approaches |

---

## Reviewer checklist

### Functional

- [ ] Code does what it's supposed to do
- [ ] Edge cases are handled
- [ ] Errors are handled correctly
- [ ] No regression on existing functionality

### Quality

- [ ] Code is readable and understandable
- [ ] Naming is clear and consistent
- [ ] No duplication
- [ ] Reasonable complexity
- [ ] Short and focused functions

### Architecture

- [ ] Project patterns respected
- [ ] Separation of concerns
- [ ] No excessive coupling
- [ ] Abstraction at the right level

### Security

- [ ] No sensitive data exposed
- [ ] Inputs validated and sanitized
- [ ] No known vulnerabilities
- [ ] Authentication/authorization correct

### Performance

- [ ] No N+1 queries
- [ ] No unnecessary loops
- [ ] Resources properly released
- [ ] Cache used if relevant

### Tests

- [ ] Tests present and relevant
- [ ] Nominal and edge cases covered
- [ ] Tests readable and maintainable
- [ ] No flaky tests

---

## Constructive feedback

### Tone

| Avoid | Prefer |
|-------|--------|
| "That's wrong" | "I think X would be better because Y" |
| "Why did you do that?" | "Can you explain the choice of X?" |
| "Always do X" | "In this case, X could help because Y" |
| Imperatives | Questions and suggestions |

### Comment structure

```
[Observation] + [Reason] + [Suggestion]

"This function is 50 lines (observation).
That makes it hard to test (reason).
We could extract validation into a separate method (suggestion)."
```

### Comment types

| Prefix | Meaning |
|--------|---------|
| `nit:` | Nitpick, minor detail, non-blocking |
| `suggestion:` | Improvement idea, non-blocking |
| `question:` | Request for clarification |
| `issue:` | Problem to fix before merge |
| `praise:` | Compliment, good practice |

### Examples

```
nit: We could use `const` here instead of `let`.

suggestion: This logic could be extracted into a utility
function for reuse.

question: I don't understand why we catch the error here
without propagating it. Is that intentional?

issue: This SQL query is vulnerable to injections.
Use prepared statements.

praise: Good use of the Strategy pattern here,
makes the code very extensible.
```

---

## Best practices

### For the reviewer

1. **Understand context**: Read description, related ticket
2. **Overview first**: Go through all files before commenting
3. **Limit scope**: Max 400 lines per review, otherwise request split
4. **Be responsive**: Respond within 24h
5. **Approve explicitly**: Say when it's good

### For the author

1. **Atomic PRs**: One feature = one PR
2. **Clear description**: Context, approach, attention points
3. **Self-review**: Re-read before requesting review
4. **Respond to everything**: Even to say "done" or explain why not
5. **Don't take it personally**: Comments are about the code

---

## Review decisions

| Decision | When |
|----------|------|
| **Approve** | Code ready to merge |
| **Approve with comments** | Minor items, author can merge after |
| **Request changes** | Blocking, must be fixed |
| **Comment** | Questions or observations, no decision |

---

## Anti-patterns

### Reviewer

- Vague comments ("that's not good")
- Imposing personal style
- Blocking for nitpicks
- Review after several days
- Complete rewrite in comments

### Author

- 2000+ line PRs
- No description
- Ignoring comments
- Arguing every suggestion
- Force merging

---

## Metrics

| Metric | Target |
|--------|--------|
| Time to first response | < 24h |
| Average review duration | < 48h |
| PR size | < 400 lines |
| Comments per review | 3-10 (not too few, not too many) |
