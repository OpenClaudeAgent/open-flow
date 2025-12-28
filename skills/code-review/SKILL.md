---
name: code-review
description: Principes de revue de code - Checklist, feedback constructif, bonnes pratiques
---

# Skill Code Review

Ce skill contient les principes pour des revues de code efficaces et constructives.

---

## Objectifs d'une revue

| Objectif | Description |
|----------|-------------|
| Qualite | Detecter bugs, edge cases, erreurs |
| Coherence | Maintenir les standards du projet |
| Partage | Diffuser la connaissance dans l'equipe |
| Apprentissage | Apprendre des autres approches |

---

## Checklist du reviewer

### Fonctionnel

- [ ] Le code fait ce qu'il est cense faire
- [ ] Les edge cases sont geres
- [ ] Les erreurs sont gerees correctement
- [ ] Pas de regression sur l'existant

### Qualite

- [ ] Code lisible et comprehensible
- [ ] Nommage clair et coherent
- [ ] Pas de duplication
- [ ] Complexite raisonnable
- [ ] Fonctions courtes et focalisees

### Architecture

- [ ] Respect des patterns du projet
- [ ] Separation des responsabilites
- [ ] Pas de couplage excessif
- [ ] Abstraction au bon niveau

### Securite

- [ ] Pas de donnees sensibles exposees
- [ ] Inputs valides et sanitizes
- [ ] Pas de vulnerabilites connues
- [ ] Authentification/autorisation correctes

### Performance

- [ ] Pas de requetes N+1
- [ ] Pas de boucles inutiles
- [ ] Ressources liberees correctement
- [ ] Cache utilise si pertinent

### Tests

- [ ] Tests presents et pertinents
- [ ] Cas nominaux et edge cases couverts
- [ ] Tests lisibles et maintenables
- [ ] Pas de tests flaky

---

## Feedback constructif

### Ton

| Eviter | Preferer |
|--------|----------|
| "C'est faux" | "Je pense que X serait mieux parce que Y" |
| "Pourquoi tu as fait ca?" | "Peux-tu m'expliquer le choix de X?" |
| "Toujours faire X" | "Dans ce cas, X pourrait aider parce que Y" |
| Imperatifs | Questions et suggestions |

### Structure d'un commentaire

```
[Observation] + [Raison] + [Suggestion]

"Cette fonction fait 50 lignes (observation).
Ca la rend difficile a tester (raison).
On pourrait extraire la validation en methode separee (suggestion)."
```

### Types de commentaires

| Prefixe | Signification |
|---------|---------------|
| `nit:` | Nitpick, detail mineur, non bloquant |
| `suggestion:` | Idee d'amelioration, non bloquant |
| `question:` | Demande de clarification |
| `issue:` | Probleme a corriger avant merge |
| `praise:` | Compliment, bonne pratique |

### Exemples

```
nit: On pourrait utiliser `const` ici au lieu de `let`.

suggestion: Cette logique pourrait etre extraite en fonction
utilitaire pour reutilisation.

question: Je ne comprends pas pourquoi on catch l'erreur ici
sans la propager. C'est voulu?

issue: Cette requete SQL est vulnerable aux injections.
Utiliser des prepared statements.

praise: Bonne utilisation du pattern Strategy ici,
ca rend le code tres extensible.
```

---

## Bonnes pratiques

### Pour le reviewer

1. **Comprendre le contexte** : Lire la description, le ticket associe
2. **Vue d'ensemble d'abord** : Parcourir tous les fichiers avant de commenter
3. **Limiter le scope** : Max 400 lignes par review, sinon demander un split
4. **Etre reactif** : Repondre dans les 24h
5. **Approuver explicitement** : Dire quand c'est bon

### Pour l'auteur

1. **PR atomiques** : Une fonctionnalite = une PR
2. **Description claire** : Contexte, approche, points d'attention
3. **Self-review** : Relire avant de demander une review
4. **Repondre a tout** : Meme pour dire "fait" ou expliquer pourquoi non
5. **Ne pas prendre perso** : Les commentaires portent sur le code

---

## Decisions de revue

| Decision | Quand |
|----------|-------|
| **Approve** | Code pret a merger |
| **Approve with comments** | Mineurs, auteur peut merger apres |
| **Request changes** | Bloquant, doit etre corrige |
| **Comment** | Questions ou observations, pas de decision |

---

## Anti-patterns

### Reviewer

- Commentaires vagues ("c'est pas bien")
- Imposer son style personnel
- Bloquer pour des nitpicks
- Review apres plusieurs jours
- Rewrite complet en commentaire

### Auteur

- PR de 2000+ lignes
- Pas de description
- Ignorer les commentaires
- Argumenter chaque suggestion
- Forcer le merge

---

## Metriques

| Metrique | Cible |
|----------|-------|
| Temps de premiere reponse | < 24h |
| Duree moyenne d'une review | < 48h |
| Taille des PRs | < 400 lignes |
| Commentaires par review | 3-10 (ni trop, ni trop peu) |
