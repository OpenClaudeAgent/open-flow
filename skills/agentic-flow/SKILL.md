---
name: agentic-flow
description: Workflow agentique - Cycle de vie feature, isolation worktrees, collaboration inter-agents
---

# Skill Agentic Flow

Ce skill decrit le workflow de developpement assiste par agents specialises.

---

## Feature Lifecycle

```
┌─────────────────────────────────────────────────────────────────┐
│                        FEATURE LIFECYCLE                         │
└─────────────────────────────────────────────────────────────────┘

  1. IDEATION
     │
     │  Utilisateur exprime le besoin
     │
     ▼
  2. PLANIFICATION ─────────────────► ROADMAP
     │                                   │
     │                                   ├── Output: roadmap/plan-XX.md
     │                                   │
     ▼◄──────────────────────────────────┘
  3. IMPLEMENTATION ────────────────► EXECUTEUR
     │                                   │
     │                                   ├── Skills: ui-design-principles, qml, qt-cpp
     │                                   ├── Output: src/
     │                                   │
     ▼◄──────────────────────────────────┘
  4. VALIDATION UTILISATEUR ────────► EXECUTEUR
     │                                   │
     │                                   ├── Lance app (make run &)
     │                                   ├── Genere scenarios de test
     │                                   ├── 🔔 MCP ask_user "Validation requise"
     │                                   ├── Itere si probleme
     │                                   │
     ▼◄──────────────────────────────────┘
  5. TESTS ─────────────────────────► TESTER (invoque par Executeur)
     │                                   │
     │                                   ├── Skill: functional-testing
     │                                   ├── Si non testable → REFACTORING
     │                                   │                        └── Skill: testability-patterns
     │                                   ├── Output: tests/
     │                                   │
     ▼◄──────────────────────────────────┘
  6. QUALITY ───────────────────────► QUALITY (invoque par Executeur)
     │                                   │
     │                                   ├── Skills: code-review
     │                                   ├── Code review (src/) + Tests review (tests/)
     │                                   ├── Output: quality/validation-XX.md
     │                                   │
     ▼◄──────────────────────────────────┘
  7. MERGE ─────────────────────────► EXECUTEUR
     │                                   │
     │                                   ├── 🔔 MCP ask_user "Je merge ?"
     │                                   ├── Skill: git-conventions
     │                                   ├── Commit + Tag version
     │                                   │
     ▼◄──────────────────────────────────┘
  8. RELEASE
     │
     └── Utilisateur publie
```

---

## Agents et responsabilites

| Agent | Role | Scope | Skills |
|-------|------|-------|--------|
| **Roadmap** | Planification | `roadmap/` | - |
| **Executeur** | Implementation | `src/` | ui-design-principles, qml, qt-cpp, git-conventions |
| **Tester** | Tests auto | `tests/` | functional-testing |
| **Quality** | QA + Code Review | `quality/` | code-review |
| **Refactoring** | Testabilite | `src/` | testability-patterns |

---

## Points de notification MCP

| Etape | Agent | Titre | Question |
|-------|-------|-------|----------|
| Validation | Executeur | "Validation requise" | "Teste les scenarios" |
| Merge | Executeur | "Feature prete" | "Je merge sur main ?" |
| Testabilite | Tester | "Autorisation requise" | "Invoquer Refactoring ?" |
| Tests manuels | Quality | "Tests manuels prets" | "On commence ?" |

---

## Skills par phase

### Phase 3 : Implementation (Executeur)

| Condition | Skill a charger |
|-----------|-----------------|
| Fichiers `.qml` | `qml` |
| Composants UI | `ui-design-principles` |
| Fichiers `.cpp/.h` Qt | `qt-cpp` |

### Phase 4 : Tests (Tester)

| Condition | Skill a charger |
|-----------|-----------------|
| Toujours | `functional-testing` |
| Code non testable | → Invoquer Refactoring avec `testability-patterns` |

### Phase 5 : Quality

| Condition | Skill a charger |
|-----------|-----------------|
| Toujours | `code-review` |

### Phase 7 : Merge (Executeur)

| Condition | Skill a charger |
|-----------|-----------------|
| Commit/Tag | `git-conventions` |

---

## Isolation des agents (Worktrees)

Chaque agent opere dans son propre worktree Git :

| Worktree | Branche | Agent |
|----------|---------|-------|
| `worktrees/feature/[nom]` | `feature/[nom]` | Executeur (cree par feature) |
| `worktrees/roadmap/` | `worktree/roadmap` | Roadmap |
| `worktrees/quality/` | `worktree/quality` | Quality |
| `worktrees/test/` | `worktree/test` | Tester |
| `worktrees/refactoring/` | `worktree/refactoring` | Refactoring |

**Executeur** : Cree un worktree dedie pour chaque feature :
```bash
git worktree add worktrees/feature/[nom] -b feature/[nom]
```

**Avantages** :
- Pas de conflits entre agents
- Tracabilite par branche
- Plusieurs features en parallele
- `main` sous controle utilisateur

---

## Regles globales

| Regle | Description |
|-------|-------------|
| Dates systeme | Toujours `date +%Y-%m-%d` |
| Worktrees | Chaque agent dans son worktree |
| Validation | Aucun merge sans approbation explicite |
| Isolation | Ne pas modifier hors de son scope |
| MCP | Utiliser `ask_user` selon instructions agent |

---

## Synchronisation worktrees

Apres merge sur main :

```bash
make sync-worktrees
```

- Synchronise tous les worktrees avec main
- Si conflit : reporter a l'utilisateur sans resoudre

---

## Workflows specifiques

### Tandem Tester-Refactoring

```
Tester identifie code non testable
       ↓
🔔 ask_user "Autorisation requise"
       ↓
Refactoring (skill: testability-patterns)
       ↓
Tester ecrit les tests
```

### Quality : Double review

```
Executeur invoque Quality
       ↓
Quality charge skill: code-review
       ↓
Phase 1: Review code (src/)
       ↓
Phase 2: Review tests (tests/)
       ↓
Rapport consolide → Executeur
```
