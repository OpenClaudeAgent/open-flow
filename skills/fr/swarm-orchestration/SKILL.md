---
name: swarm-orchestration
description: Orchestration de swarms - Coordinateur gère N exécuteurs parallèles, consolide, merges
---

# Skill Swarm Orchestration

Comment un Coordinateur orchestre plusieurs Exécuteurs en parallèle et consolide leurs travaux.

---

## Arborescence

```
COORDINATEUR
├─ Lire roadmap → Analyser dépendances
├─ ask_user: Sélectionner plans
├─ Invoquer Exécuteurs (parallèle)
│
├─ EXÉCUTEUR-1 (Plan-XX)
│  ├─ Impl + Refactoring → Tester → Quality
│  └─ Rapport → Coordinator
│
├─ EXÉCUTEUR-2 (Plan-YY) [parallèle]
│  └─ Idem
│
└─ Consolidate + Review + Merge
```

---

## Workflow Coordinateur (7 phases)

| Phase | Action |
|-------|--------|
| 1 | Load skill → Create todos → Read roadmap |
| 2 | Identify pending plans → Analyze dependencies |
| 3 | ask_user: Select plans for execution |
| 4 | Invoke Executors in parallel |
| 5 | Wait for all reports → Collect |
| 6 | Consolidate all → ask_user: Review |
| 7 | Update plans/roadmap → Merge all → Sync |

---

## Report Format

**Tous les agents utilisent ce format** (utilise reporting-* skills) :

```
✅ Results / Résultats
⚠️ Problems / Problèmes
🔧 Actions Required / Actions Requises
📌 Important Notes / Notes Importantes
```

Exécuteur → Load `reporting-executor` skill  
Refactoring → Load `reporting-refactoring` skill  
Tester → Load `reporting-tester` skill  
Quality → Load `reporting-quality` skill  

---

## Propagation Notes Importantes

```
REFACTORING notes → EXECUTOR includes integrally
                 ↓
TESTER notes → EXECUTOR includes integrally
                 ↓
QUALITY notes → EXECUTOR includes integrally
                 ↓
EXECUTOR consolidated report → COORDINATOR
                 ↓
COORDINATOR → USER (all notes preserved)
```

**CRITIQUE** : Notes JAMAIS résumées, toujours intégrales.

---

## Plan Dependencies

Avant invocation d'un Exécuteur, vérifier :

```
Plan-XX pending
├─ Requires Plan-ZZ?
│  ├─ If Plan-ZZ = Done → OK
│  ├─ If Plan-ZZ = Pending → Suggest order
│  └─ Else → OK
```

---

## Deux Modes (Identiques)

**Mode SIMPLE (N=1)** : Un plan, un exécuteur  
**Mode SWARM (N>1)** : Plusieurs plans, exécuteurs parallèles

Même architecture, juste N=1 ou N>1.

---

## Feedback Loop & Escalation

```
Executor has question → Report in Important Notes
                    ↓
Coordinator sees it → ask_user with context
                    ↓
User validates approach → Executor continues
```

Tout en contexte conversation, pas de fichiers créés.

---

## Key Points

- **Executors orchestrate sub-agents**: REFACTORING → TESTER → QUALITY
- **Reports cascade up**: Each level consolidates from its children
- **Important Notes propagate integrally**: Never summarized
- **User Validation at Coordinator**: After implementation
- **No executor merges**: Coordinator handles all
- **Communication in context**: No files created

---

## Coordinator vs Executor

| Aspect | Coordinator | Executor |
|--------|---|---|
| Scope | Roadmap + N plans | 1 plan |
| Invokes | Executors | Refactoring, Tester, Quality |
| Skills | swarm-orchestration, agentic-flow | agentic-flow + context skills |
| Reports | Consolidates N reports | Consolidates 3 sub-agent reports |
| Merges | Manages all | None (Coordinator handles) |

---

## Synchronisation Worktrees

Après merges (par Coordinator) :

```bash
make sync-worktrees
```

Synchronise tous worktrees avec main. Si conflit : reporter utilisateur.
