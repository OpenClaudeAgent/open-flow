---
name: git-conventions
description: Git conventions - Conventional commits, branching, semantic versioning, tags
---

# Git Conventions Skill

This skill contains Git conventions for a clean and traceable workflow.

---

## Conventional Commits

### Format

```
<type>(<scope>): <description>

[body]

[footer]
```

### Types

| Type | Usage |
|------|-------|
| `feat` | New feature |
| `fix` | Bug fix |
| `refactor` | Refactoring without functional change |
| `test` | Adding or modifying tests |
| `docs` | Documentation |
| `style` | Formatting, no code change |
| `chore` | Maintenance, config, deps |
| `perf` | Performance improvement |

### Scope

The scope indicates the affected area: `feat(auth)`, `fix(api)`, `refactor(core)`.

### Rules

- Description in lowercase, no final period
- Imperative present: "add" not "added" or "adds"
- Max 72 characters for first line
- Optional body for details

### Examples

```
feat(player): add playback speed control
fix(auth): handle expired token refresh
refactor(api): extract http client interface
test(player): add unit tests for volume control
docs: update installation guide
```

---

## Branching Strategy

### Main branches

| Branch | Role |
|--------|------|
| `main` | Production, always stable |
| `develop` | Integration (optional) |

### Working branches

| Pattern | Usage |
|---------|-------|
| `feature/<name>` | New feature |
| `fix/<name>` | Bug fix |
| `refactor/<name>` | Refactoring |
| `hotfix/<name>` | Urgent production fix |

### Rules

- Short-lived branches (max a few days)
- One branch = one feature/fix
- Merge via PR/MR with review
- Delete after merge

---

## Semantic Versioning

### Format

```
MAJOR.MINOR.PATCH
```

### Incrementing

| Change | Increment | Example |
|--------|-----------|---------|
| Breaking change | MAJOR | 1.0.0 → 2.0.0 |
| New feature | MINOR | 1.0.0 → 1.1.0 |
| Bug fix | PATCH | 1.0.0 → 1.0.1 |

### Pre-release

```
1.0.0-alpha.1
1.0.0-beta.2
1.0.0-rc.1
```

### Rules

- Start at `0.1.0` (initial development)
- `1.0.0` = first stable release
- Never modify a published version

---

## Tags

### Format

```
v<MAJOR>.<MINOR>.<PATCH>
```

### Creation

```bash
# Annotated tag (recommended)
git tag -a v1.2.0 -m "feat(player): add speed control"

# Push the tag
git push origin v1.2.0

# Push all tags
git push --tags
```

### Rules

- Always prefix with `v`
- Annotated tag with descriptive message
- Tag on main after merge

---

## Typical Workflow

```
1. git checkout -b feature/my-feature
2. # ... commits ...
3. git push -u origin feature/my-feature
4. # ... PR/MR + review ...
5. git checkout main && git pull
6. git merge feature/my-feature
7. git tag -a v1.2.0 -m "feat: my feature"
8. git push && git push --tags
9. git branch -d feature/my-feature
```

---

## Checklist

- [ ] Commit message follows conventional format
- [ ] Correct type (feat/fix/refactor/test/docs)
- [ ] Relevant scope
- [ ] Clear and concise description
- [ ] Branch named correctly
- [ ] Tag with semantic version
