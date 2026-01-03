# Skill : Sprint Planning

Planification strategique par cycles et phases pour organiser les plans de la roadmap.

---

## Structure de fichiers (obligatoire)

```
roadmap/
├── README.md           # Suivi global (toujours present)
├── SPRINTS.md          # Index des sprints
├── plans/              # Dossier des plans (obligatoire)
│   └── plan-XX-*.md
└── sprints/            # Dossier des sprints
    └── sprint-XX-*.md
```

### Initialisation de la structure

Si la structure n'existe pas :

1. Creer `roadmap/plans/`
2. Creer `roadmap/sprints/`
3. Creer `roadmap/SPRINTS.md` avec template

### Migration (si plans a la racine)

Si des plans existent a la racine de `roadmap/` :

1. Creer `roadmap/plans/`
2. Deplacer tous les `plan-*.md` vers `plans/`
3. Mettre a jour les liens dans `README.md` : `./plan-XX.md` → `./plans/plan-XX.md`

---

## Template sprint individuel

Chaque fichier `sprints/sprint-XX-*.md` :

```markdown
# Sprint XX - [Nom]

**Objectif** : [Description]

---

## Plans

| Plan | Description | Test E2E | Statut |
|------|-------------|----------|--------|
| **XX** | [desc] | [test associe] | 🔴 |

---

## Checklist

- [ ] Plan XX - [description courte]
- [ ] Plan YY - [description courte]
```

---

## Cycles disponibles

### Cycle A : Qualite-First (defaut)

| Phase | Focus | Objectif |
|-------|-------|----------|
| 1 | Bugfixes + E2E | Corriger bugs, ajouter assertions E2E |
| 2 | Renforcement E2E | Filet de securite avant refactoring |
| 3 | Refactoring | Ameliorer qualite du code |
| 4 | Features | Nouvelles fonctionnalites |

**Usage** : Projet avec dette technique, phase de stabilisation

**Philosophie** : Les tests E2E servent de filet de securite pour le refactoring. Chaque bugfix est une opportunite d'ameliorer la couverture E2E.

### Cycle B : Feature-First

| Phase | Focus | Objectif |
|-------|-------|----------|
| 1 | Features quick wins | Valeur immediate, effort faible |
| 2 | Features complexes | Fonctionnalites majeures |
| 3 | E2E + Bugfixes | Stabilisation post-features |
| 4 | Refactoring | Nettoyage dette accumulee |

**Usage** : MVP, besoin de livrer rapidement de la valeur

### Cycle C : Maintenance

| Phase | Focus | Objectif |
|-------|-------|----------|
| 1 | Bugfixes critiques | Corrections urgentes |
| 2 | Couverture E2E | Tests de non-regression |
| 3 | Documentation | Mise a jour docs |
| 4 | Refactoring mineur | Quick wins qualite |

**Usage** : Projet mature, maintenance continue

---

## Assignation automatique

### Phase (selon type de plan)

| Mots-cles detectes | Type | Phase Cycle A | Phase Cycle B |
|--------------------|------|---------------|---------------|
| fix, bug, hotfix, crash, regression | Bugfix | 1 | 3 |
| test, e2e, assertion, coverage | E2E | 2 | 3 |
| refactor, cleanup, debt, quality | Refactoring | 3 | 4 |
| feature, add, new, enhance, implement | Feature | 4 | 1 ou 2 |
| doc, readme, documentation | Documentation | 4 | 4 |

### Priorite (selon criticite)

| Mots-cles detectes | Priorite | Description |
|--------------------|----------|-------------|
| crash, critical, blocker, security, data loss, urgent | **P0** | Bloquant, a traiter immediatement |
| bug, broken, regression, visible, user-facing | **P1** | Important, UX degradee |
| minor, polish, cleanup, nice-to-have, enhancement | **P2** | Souhaitable, non urgent |

**Si ambiguite** : Utiliser `ask_user` pour confirmer phase et/ou priorite.

---

## Workflow

### 1. Initialisation

Quand l'utilisateur demande d'initialiser le sprint planning :

```
ask_user(
  title: "Sprint Planning - Choix du cycle"
  question: "Quel cycle strategique utiliser ?"
  options: [
    "A: Qualite-First (Bug->E2E->Refacto->Features)",
    "B: Feature-First (Features->E2E->Refacto)",
    "C: Maintenance (Bugfix->E2E->Doc->Refacto)"
  ]
)
```

Puis creer `SPRINTS.md` avec le template approprie.

### 2. Assignation d'un nouveau plan

Quand tu crees un plan :

1. **Detecter le type** via mots-cles dans titre/contexte
2. **Determiner la priorite** via criticite
3. **Assigner a la phase** selon le cycle actif
4. **Ajouter dans SPRINTS.md** a la bonne phase
5. **Informer l'utilisateur** : "Plan XX assigne a Phase N (P1)"

### 3. Gestion des urgences

Si un plan urgent arrive hors-phase actuelle :

```
ask_user(
  title: "Plan urgent detecte"
  question: "Le plan [XX] est de type [bugfix] mais nous sommes en Phase [3-Refactoring]. Que faire ?"
  options: [
    "Integrer maintenant (interrompre phase)",
    "Reporter a la prochaine Phase 1",
    "Creer un hotfix hors-cycle"
  ]
)
```

### 4. Transition de phase

Quand tous les plans d'une phase sont termines :

1. Mettre a jour statut phase → "Termine"
2. Proposer passage a phase suivante
3. Si Phase 4 terminee → proposer nouveau cycle

### 5. Statut sprint

Quand l'utilisateur demande le statut :

- Afficher phase actuelle
- Lister plans en cours / termines / a faire
- Calculer progression (X/Y plans termines)
- Suggerer prochaines actions

---

## Template SPRINTS.md

```markdown
# [Projet] - Sprint Planning

## Configuration

- **Cycle actif** : [A/B/C] - [Nom du cycle]
- **Phase actuelle** : [N]
- **Date debut cycle** : [YYYY-MM-DD]

---

## Vue d'ensemble

| Phase | Focus | Plans | Statut |
|-------|-------|-------|--------|
| 1 | [Focus Phase 1] | [liens] | [emoji] |
| 2 | [Focus Phase 2] | [liens] | [emoji] |
| 3 | [Focus Phase 3] | [liens] | [emoji] |
| 4 | [Focus Phase 4] | [liens] | [emoji] |

Statuts : En cours | A faire | Termine

---

## Phase 1 : [Nom]

**Objectif** : [Description]

### Plans

| Priorite | Plan | Description | Statut |
|----------|------|-------------|--------|
| P0 | [lien] | [desc] | [emoji] |
| P1 | [lien] | [desc] | [emoji] |

### Checklist
- [ ] Plan XX
- [ ] Plan YY

---

## Phase 2 : [Nom]
[Meme structure]

---

## Phase 3 : [Nom]
[Meme structure]

---

## Phase 4 : [Nom]
[Meme structure]

---

## Plans non assignes

| Plan | Description | Type suggere | Phase suggere | Priorite |
|------|-------------|--------------|---------------|----------|
| [lien] | [desc] | [type] | [N] | [P?] |

---

## Historique des cycles

| Cycle | Dates | Phases completees | Plans | Notes |
|-------|-------|-------------------|-------|-------|
| 1 | [debut-fin] | 4/4 | [N] plans | [notes] |
```

---

## Commandes typiques

| Demande utilisateur | Action |
|---------------------|--------|
| "Initialiser sprint planning" | Creer SPRINTS.md avec cycle choisi |
| "Assigner plan XX" | Detecter type/priorite, ajouter a phase |
| "Statut sprint" | Resume phase actuelle + progression |
| "Prochaine phase" | Transition vers phase suivante |
| "Nouveau cycle" | Archiver cycle actuel, recommencer |

---

## Bonnes pratiques

1. **Un plan = une phase** : Eviter les plans qui chevauchent plusieurs phases
2. **Bugfix + E2E** : Chaque bugfix devrait inclure une assertion E2E
3. **P0 d'abord** : Dans une phase, traiter les P0 avant P1/P2
4. **Revue de phase** : Avant transition, valider avec utilisateur
5. **Flexibilite** : Le cycle est un guide, pas une contrainte rigide
