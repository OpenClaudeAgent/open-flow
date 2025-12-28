---
name: agentic-flow
description: Workflow agentique - Cycle de vie feature, isolation worktrees, collaboration inter-agents
---

# Skill Agentic Flow

Ce skill decrit le workflow de developpement assiste par agents specialises, leurs responsabilites et leurs interactions.

---

## Vue d'ensemble

Cinq agents specialises, chacun dans son worktree isole :

```
                        UTILISATEUR
                             |
     +----------+-----+------+------+-----+----------+
     |          |           |             |          |
     v          v           v             v          v
  Roadmap   Executeur    Quality      Tester    Refactoring
  (Plan)    (Implem)     (Strat)      (Tests)   (Testab.)
     |          |           |             |          |
     v          v           v             v          v
  roadmap/    src/      quality/      tests/      src/
```

---

## Responsabilites

| Agent | Role | Produit | Scope |
|-------|------|---------|-------|
| **Roadmap** | Planification | Plans fonctionnels | `roadmap/` |
| **Executeur** | Implementation | Code source | `src/` |
| **Quality** | Strategie QA | Plans de test manuels | `quality/` |
| **Tester** | Tests auto | Tests unitaires/E2E | `tests/` |
| **Refactoring** | Testabilite | Code refactorise | `src/` |

---

## Cycle de vie d'une feature

```
1. IDEATION        → Utilisateur exprime le besoin
       ↓
2. PLANIFICATION   → Roadmap cree le plan (comportements, criteres)
       ↓
3. IMPLEMENTATION  → Executeur code selon le plan
       ↓
4. VALIDATION      → Utilisateur teste avec checklist
       ↓
5. MERGE           → Utilisateur merge sur main + tag
       ↓
6. QUALITE         → Quality (manuel) + Tester (auto) en parallele
       ↓
7. RELEASE         → Utilisateur publie
```

---

## Principes fondamentaux

### Isolation des agents

Chaque agent opere dans son propre worktree Git :

| Worktree | Branche | Agent |
|----------|---------|-------|
| `worktrees/feature/` | `worktree/feature` | Executeur |
| `worktrees/roadmap/` | `worktree/roadmap` | Roadmap |
| `worktrees/quality/` | `worktree/quality` | Quality |
| `worktrees/test/` | `worktree/test` | Tester |
| `worktrees/refactoring/` | `worktree/refactoring` | Refactoring |

**Avantages** :
- Pas de conflits entre agents
- Tracabilite par branche
- `main` sous controle utilisateur

### Communication inter-agents

Les agents ne communiquent **jamais directement**. Tout passe par :
1. **Artefacts** : Documents dans les dossiers dedies
2. **Utilisateur** : Orchestre et valide les transitions

**Exceptions** :
- Tandem Tester-Refactoring (avec validation utilisateur)
- Executeur → Tester → Quality (chaine de validation tests)

### Regles globales

| Regle | Description |
|-------|-------------|
| Dates systeme | Toujours `date +%Y-%m-%d` |
| Worktrees | Chaque agent dans son worktree |
| Validation | Aucun merge sans approbation explicite |
| Isolation | Ne pas modifier hors de son scope |

---

## Workflows specifiques

### Executeur : Cycle de validation

```
Selection → Preparation → Implementation → Tests? → Validation → Finalisation
                                             ↓
                                   Si echec: Tester → Quality
```

1. **Selection** : Prochaine tache selon priorites
2. **Preparation** : Sync main, branche feature
3. **Implementation** : Code dans `src/`
4. **Tests** : Si echec, invoquer Tester puis Quality
5. **Validation** : Checklist + scenarios avec utilisateur (voir detail ci-dessous)
6. **Finalisation** : Commit, proposition merge

#### Detail : Phase Validation

L'executeur doit generer une **checklist de validation avec scenarios concrets** :

1. **Lancer l'application** (`make run &` en arriere-plan)
2. **Generer des scenarios de test** bases sur le plan :
   - Scenario principal (happy path)
   - Scenarios secondaires
   - Cas limites (edge cases)
3. **Chaque scenario inclut** :
   - Actions concretes (clics, saisies, navigations)
   - Resultat attendu visible
4. **Notifier l'utilisateur** via MCP `ask_user`
5. **Iterer** jusqu'a validation complete

### Tandem Tester-Refactoring

```
Tester identifie code non testable
       ↓
Demande autorisation utilisateur
       ↓
Refactoring cree commit dans worktree/refactoring
       ↓
Tester cherry-pick ou applique patch
       ↓
Tester ecrit les tests
```

**Regles** :
- Validation utilisateur avant chaque invocation
- Pas de merge direct sur main
- Communication par commits (cherry-pick ou patches)

### Quality : Consolidation

```
Phase 1: Consolidation          Phase 2: Impacts
         ↓                              ↓
Extraire checklists plans      Identifier composants partages
         ↓                              ↓
Verifier obsolescence          Matrice d'impact
         ↓                              ↓
Liste consolidee               Checks de regression
```

---

## Matrice des interactions

| Source → Dest | Action |
|---------------|--------|
| Utilisateur → Roadmap | Idees, besoins |
| Roadmap → `roadmap/` | Plans, specs |
| Executeur ← `roadmap/` | Lit plans |
| Executeur → `src/` | Implementation |
| Quality ← `roadmap/` | Lit pour analyse |
| Quality → `quality/` | Plans de test |
| Tester ← `src/` | Lit code source |
| Tester → `tests/` | Tests automatises |
| Tester → Refactoring | Demande testabilite |
| Refactoring → `src/` | Code refactorise |

---

## Synchronisation worktrees

Apres merge sur main :

```bash
make sync-worktrees
```

- Synchronise tous les worktrees avec main
- Si conflit : reporter a l'utilisateur sans resoudre

---

## Avantages

| Aspect | Benefice |
|--------|----------|
| Parallelisation | Agents travaillent simultanement |
| Tracabilite | Contributions isolees et identifiables |
| Reversibilite | Retour arriere facile |
| Controle | Validation explicite a chaque etape |
| Transparence | Role clair de chaque agent |
