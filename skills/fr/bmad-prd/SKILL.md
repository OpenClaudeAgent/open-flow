---
name: bmad-prd
description: Création PRD BMAD - Créer un Document d'Exigences Produit via interviews utilisateurs et découverte des besoins
---

# Skill BMAD - PRD Creation

Ce skill guide la création d'un Product Requirements Document (PRD) selon la méthodologie BMAD.

## Objectif

Créer un PRD qui émerge des interviews utilisateurs, pas du remplissage de templates. Découvre ce dont les utilisateurs ont vraiment besoin.

## Principes BMAD pour le PRD

1. **WHY before WHAT** : Demande 'POURQUOI ?' sans relâche
2. **User interviews first** : Parle avec de vrais utilisateurs
3. **Ship minimum** : La plus petite chose qui valide l'hypothèse
4. **Technical feasibility = constraint** : Valeur utilisateur d'abord
5. **Jobs-to-be-Done** : Quel job l'utilisateur essaie-t-il d'accomplir ?

## Workflow PRD BMAD

### Phase 1 : User Interview & Discovery

**Questions à poser** :
- Quel problème essaies-tu de résoudre ?
- Comment résous-tu ce problème aujourd'hui ?
- Qu'est-ce qui ne fonctionne pas avec la solution actuelle ?
- Dans un monde parfait, comment ça fonctionnerait ?
- Qu'est-ce qui t'empêche d'atteindre ton objectif ?

### Phase 2 : Problem Definition

**Définir** :
- Le problème principal (en 1-2 phrases)
- Les utilisateurs impactés
- Les contraintes (temps, budget, technique)
- Les critères de succès mesurables

### Phase 3 : Solution Scope (MVP)

**Déterminer** :
- Scope minimum qui valide l'hypothèse
- Ce qui est IN scope vs OUT scope
- Critères d'acceptation principaux
- Métriques de succès

### Phase 4 : Requirements

**Documenter** :
- User stories principales
- Exigences fonctionnelles
- Exigences non-fonctionnelles
- Contraintes techniques

### Phase 5 : Validation

**Vérifier** :
- Le PRD répond au "WHY?"
- Les utilisateurs valident le scope
- Les critères de succès sont mesurables
- L'équipe peut estimer l'effort

## Template PRD BMAD

```markdown
# Product Requirements Document

## Problem Statement
[Le problème en 1-2 phrases claires]

## Users & Jobs-to-be-Done
- **User Persona 1** : [Job to be done]
- **User Persona 2** : [Job to be done]

## Success Criteria
1. [Métrique mesurable 1]
2. [Métrique mesurable 2]
3. [Métrique mesurable 3]

## MVP Scope

### IN Scope
- [Feature 1]
- [Feature 2]
- [Feature 3]

### OUT Scope (Future)
- [Feature postponée 1]
- [Feature postponée 2]

## User Stories
1. As a [user], I want to [action] so that [benefit]
2. As a [user], I want to [action] so that [benefit]
3. ...

## Functional Requirements
- [Requirement 1]
- [Requirement 2]
- ...

## Non-Functional Requirements
- Performance : [critères]
- Security : [critères]
- Accessibility : [critères]

## Technical Constraints
- [Contrainte 1]
- [Contrainte 2]
- ...

## Open Questions
- [Question 1]
- [Question 2]
- ...
```

## Output

Génère le PRD dans : `_bmad-output/prd/prd.md`

## Next Steps

Après le PRD :

1. **UX Design** (optionnel) → Utilise `/ux-designer` + skill `bmad-ux-design`
2. **Architecture** → Utilise `/architect` + skill `bmad-architecture`
3. **Epics & Stories** → Utilise `/pm` + skill `bmad-epics-stories`
