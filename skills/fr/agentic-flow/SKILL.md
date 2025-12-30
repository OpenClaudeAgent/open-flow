---
name: agentic-flow
description: Workflow agentique de l'Exécuteur - Analyse, implémentation, sous-agents séquentiels
---

# Skill Agentic Flow

Workflow de l'**Exécuteur** invoqué par Coordinateur.

**Pour multi-plans orchestrés**, voir skill `swarm-orchestration`.

---

## Workflow Exécuteur (5 phases)

| Phase | Action |
|-------|--------|
| 1 | Load skill → Create todos → Analyze plan |
| 2 | Load relevant skills → Implement → Build |
| 3 | Invoke REFACTORING → TESTER → QUALITY (sequential) |
| 4 | Consolidate all reports (see reporting-* skills) |
| 5 | User Validation at Coordinator → Final report |

---

## Analyse Dynamique Skills

L'Exécuteur identifie et charge les skills selon les fichiers :

| Fichier | Skill |
|---------|-------|
| `.qml` | `qml` |
| UI components | `ui-design-principles` |
| `.cpp` / `.h` Qt | `qt-cpp` |
| Code non testable | Assign to REFACTORING |

---

## Sous-Agents Séquentiels

Exécuteur invoque dans cet ordre **OBLIGATOIRE** :

**1. REFACTORING** (skill: testability-patterns)
   └─ Worktree: Partagé | Rapport: reporting-refactoring

**2. TESTER** (skill: functional-testing)
   └─ Worktree: Partagé | Rapport: reporting-tester

**3. QUALITY** (skill: code-review)
   └─ Worktree: Partagé (read-only) | Rapport: reporting-quality

---

## Reporting Skills

Utilise les skills spécialisés pour structurer rapports :

```
Exécuteur → Load reporting-executor skill
├─ Inclure rapport COMPLET Refactoring
├─ Inclure rapport COMPLET Tester
├─ Inclure rapport COMPLET Quality
└─ Consolidate all Important Notes (intégralement)
```

**CRITIQUE** : Notes Importantes ne sont JAMAIS résumées.

---

## Shared Worktree Model

Tous les agents utilisent le MÊME worktree créé par Exécuteur :

```
worktrees/feature/[nom]
├─ Executor: R/W src/
├─ Refactoring: R/W src/
├─ Tester: R/W tests/
└─ Quality: read-only src/ + tests/
```

**Avantages** : Pas de conflits, isolation par feature, merge centralisé.

---

## Itération Utilisateur

Si User Validation échoue (au Coordinateur) :

Coordinateur demande correction → Exécuteur corrige → Réinvoque sous-agents si nécessaire

**Pas de réimplémentation complète.**

---

## Règles Globales

| Règle | Description |
|-------|-------------|
| Dates système | `date +%Y-%m-%d` |
| Worktree | Partagé par tous (Executor + sous-agents) |
| User Validation | Au Coordinateur après implémentation |
| Merges | Coordinateur gère |
| Notes Importantes | Propagées intégralement |
| Communication | Contexte conversation uniquement |

---

## Synchronisation Worktrees

Après merge (par Coordinateur) :

```bash
make sync-worktrees
```

Synchronise tous worktrees avec main. Si conflit : reporter utilisateur.
