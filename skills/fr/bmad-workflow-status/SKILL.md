---
name: bmad-workflow-status
description: Statut Workflow BMAD - Suivre la progression du projet à travers les phases de la méthodologie BMAD
---

# Skill BMAD - Workflow Status

Ce skill permet de suivre la progression d'un projet à travers les phases de la méthodologie BMAD.

## Méthodologie BMAD (4 Phases)

La méthodologie BMAD (Build More, Architect Dreams) suit 4 phases principales :

### 1. Analysis (Optionnelle)
- **Agent** : Analyst (`/analyst`)
- **Outputs** : Product Brief, Research, Documentation projet existant
- **Workflows** : Brainstorming, Research, Product Brief

### 2. Planning
- **Agent** : PM (`/pm`)
- **Outputs** : PRD (Product Requirements Document)
- **Workflow** : Create PRD via interviews utilisateurs

### 3. Solutioning
- **Agents** : UX Designer (`/ux-designer`), Architect (`/architect`), PM (`/pm`)
- **Outputs** : UX Design, Architecture Document, Epics & User Stories
- **Workflows** :
  1. UX Design (optionnel)
  2. Architecture Document
  3. Epics & User Stories

### 4. Implementation
- **Agents** : SM (`/sm`), Dev (`/dev`), TEA (`/tea`)
- **Outputs** : Stories, Code, Tests
- **Workflows** :
  1. Sprint Planning
  2. Create Story
  3. Dev Story (implementation)
  4. Code Review

## Quick Flow (Alternative rapide)

Pour les petites features, utilise **Quick Flow** :

**Agent** : `/quick-flow`

**Workflow simplifié** :
1. Tech Spec
2. Quick Dev (implementation)
3. Code Review

## Vérifier le Statut

Pour savoir où tu en es dans ton projet :

1. **Nouveau projet** → Commence par Phase 1 (Analysis) ou Phase 2 (Planning)
2. **PRD existant** → Phase 3 (Solutioning)
3. **Architecture existante** → Phase 4 (Implementation)
4. **Petite feature** → Quick Flow

## Outputs Standards BMAD

Les outputs BMAD sont stockés dans `_bmad-output/` :

```
_bmad-output/
├── prd/                    # Phase 2 - Planning
│   └── prd.md
├── architecture/           # Phase 3 - Solutioning
│   └── architecture.md
├── ux/                     # Phase 3 - Solutioning
│   └── ux-design.md
├── epics/                  # Phase 3 - Solutioning
│   ├── epic-1.md
│   └── epic-2.md
└── stories/                # Phase 4 - Implementation
    ├── story-1.md
    └── story-2.md
```

## Utilisation

1. Identifie où tu en es dans le projet
2. Choisis le bon agent pour la phase actuelle
3. Suis les workflows dans l'ordre
4. Génère les outputs attendus

## Next Steps

Selon ta phase :

- **Phase 1** → Utilise `/analyst` puis skill `bmad-product-brief`
- **Phase 2** → Utilise `/pm` puis skill `bmad-prd`
- **Phase 3** → Utilise `/architect` puis skill `bmad-architecture`
- **Phase 4** → Utilise `/sm` puis skill `bmad-sprint-planning`
- **Quick Flow** → Utilise `/quick-flow` puis skill `bmad-tech-spec`
