---
name: git-conventions
description: Conventions Git - Commits conventionnels, branching, semantic versioning, tags
---

# Skill Git Conventions

Ce skill contient les conventions Git pour un workflow propre et tracable.

---

## Commits conventionnels

### Format

```
<type>(<scope>): <description>

[body]

[footer]
```

### Types

| Type | Usage |
|------|-------|
| `feat` | Nouvelle fonctionnalite |
| `fix` | Correction de bug |
| `refactor` | Refactoring sans changement fonctionnel |
| `test` | Ajout ou modification de tests |
| `docs` | Documentation |
| `style` | Formatage, pas de changement de code |
| `chore` | Maintenance, config, deps |
| `perf` | Amelioration de performance |

### Scope

Le scope indique la zone affectee : `feat(auth)`, `fix(api)`, `refactor(core)`.

### Regles

- Description en minuscules, sans point final
- Imperatif present : "add" pas "added" ou "adds"
- Max 72 caracteres pour la premiere ligne
- Body optionnel pour les details

### Exemples

```
feat(player): add playback speed control
fix(auth): handle expired token refresh
refactor(api): extract http client interface
test(player): add unit tests for volume control
docs: update installation guide
```

---

## Branching Strategy

### Branches principales

| Branche | Role |
|---------|------|
| `main` | Production, toujours stable |
| `develop` | Integration (optionnel) |

### Branches de travail

| Pattern | Usage |
|---------|-------|
| `feature/<name>` | Nouvelle fonctionnalite |
| `fix/<name>` | Correction de bug |
| `refactor/<name>` | Refactoring |
| `hotfix/<name>` | Correction urgente prod |

### Regles

- Branches courtes (max quelques jours)
- Une branche = une fonctionnalite/fix
- Merge via PR/MR avec review
- Supprimer apres merge

---

## Semantic Versioning

### Format

```
MAJOR.MINOR.PATCH
```

### Incrementation

| Change | Increment | Exemple |
|--------|-----------|---------|
| Breaking change | MAJOR | 1.0.0 → 2.0.0 |
| Nouvelle feature | MINOR | 1.0.0 → 1.1.0 |
| Bug fix | PATCH | 1.0.0 → 1.0.1 |

### Pre-release

```
1.0.0-alpha.1
1.0.0-beta.2
1.0.0-rc.1
```

### Regles

- Commencer a `0.1.0` (developpement initial)
- `1.0.0` = premiere release stable
- Ne jamais modifier une version publiee

---

## Tags

### Format

```
v<MAJOR>.<MINOR>.<PATCH>
```

### Creation

```bash
# Tag annote (recommande)
git tag -a v1.2.0 -m "feat(player): add speed control"

# Pousser le tag
git push origin v1.2.0

# Pousser tous les tags
git push --tags
```

### Regles

- Toujours prefixer par `v`
- Tag annote avec message descriptif
- Tagger sur main apres merge

---

## Workflow type

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

- [ ] Commit message suit le format conventionnel
- [ ] Type correct (feat/fix/refactor/test/docs)
- [ ] Scope pertinent
- [ ] Description claire et concise
- [ ] Branche nommee correctement
- [ ] Tag avec version semantique
