---
name: bmad-checkpoints
description: Points de validation utilisateur (ask_user) aux moments critiques des workflows BMAD
---

# Skill BMAD - Checkpoints Validation

Ce skill definit QUAND utiliser `notify_ask_user` dans les workflows BMAD.

## Principe

Les checkpoints sont des **points de pause critiques** ou l'agent demande une decision/validation a l'utilisateur avant de continuer.

**Regle d'or** : Utilise `ask_user` uniquement aux moments ou une decision utilisateur est BLOQUANTE pour la suite.

## Checkpoints par Agent

### PM (Product Manager)

| Checkpoint | Trigger | Question | Options |
|------------|---------|----------|---------|
| **Validation scope MVP** | Fin PRD | "Scope MVP finalise. Valider avant architecture ?" | ["Valider", "Modifier scope"] |

### Architect

| Checkpoint | Trigger | Question | Options |
|------------|---------|----------|---------|
| **Choix stack/pattern** | Decision majeure | "Stack proposee: [X]. Pattern: [Y]. Valider ?" | ["Approuver", "Voir alternatives", "Modifier"] |

### Dev (Developer)

| Checkpoint | Trigger | Question | Options |
|------------|---------|----------|---------|
| **Tests echouent 3x** | Blocage | "Tests echouent apres 3 tentatives. Action ?" | ["Debug ensemble", "Voir logs", "Skip task"] |
| **Story complete** | Fin implementation | "Story X.Y terminee, tests OK. Creer PR ?" | ["Oui", "Encore du travail"] |

### SM (Scrum Master)

| Checkpoint | Trigger | Question | Options |
|------------|---------|----------|---------|
| **Sprint deraille** | Velocite < 50% | "Sprint en difficulte (X% velocite). Action ?" | ["Reduire scope", "Continuer", "Annuler sprint"] |

### TEA (Test Engineer)

| Checkpoint | Trigger | Question | Options |
|------------|---------|----------|---------|
| **Quality gates fail** | Blocage | "Quality gates echouent: [liste]. Action ?" | ["Corriger", "Forcer", "Voir details"] |

### Quick-Flow

| Checkpoint | Trigger | Question | Options |
|------------|---------|----------|---------|
| **Tech spec valide** | Avant implementation | "Tech spec pret. Valider avant dev ?" | ["Valider", "Modifier"] |

## Format ask_user

```
notify_ask_user(
  title: "[Emoji] Checkpoint: [Action]",
  question: "[Question claire]",
  options: ["Option 1", "Option 2", ...],
  urgency: "normal" | "high",  # high = blocage
  agent: "[Nom agent]",
  task: "[Task en cours]",
  branch: "[Branch]"
)
```

## Regles

### UTILISER ask_user pour :
- Blocages (tests fail 3x, quality gates, build fail)
- Decisions majeures avec alternatives
- Validations fin de phase critique

### NE PAS utiliser ask_user pour :
- Informer de progression (utilise todos)
- Confirmer actions triviales
- Questions multiples (1 question a la fois)

## Exemple

```
Story 1.2 - Task 3: Tests echouent

Tentative 1: FAIL
Tentative 2: FAIL  
Tentative 3: FAIL

--> CHECKPOINT DECLENCHE

notify_ask_user(
  title: "Tests Echouent",
  question: "Tests echouent apres 3 tentatives sur Task 3",
  options: ["Debug ensemble", "Voir logs", "Skip task"],
  urgency: "high",
  agent: "Dev",
  task: "Story 1.2 - Task 3",
  branch: "feature/story-1.2"
)

[ATTENTE REPONSE]
```
