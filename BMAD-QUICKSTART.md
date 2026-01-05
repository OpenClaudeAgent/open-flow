# BMAD Quick Start Guide

Bienvenue dans **OpenFlow-BMAD** ! Ce guide vous aide à démarrer avec la méthodologie BMAD.

## Installation

```bash
# Clone le repo
git clone <your-repo-url> ~/Projects/open-flow
cd ~/Projects/open-flow

# Installe les agents BMAD, skills et MCP servers
./install.sh

# Ou en anglais
./install.sh install --lang=en
```

## Choisir Votre Workflow

### Option 1 : Nouveau Projet (Workflow Complet)

**Quand l'utiliser** : Nouveau produit, feature complexe, besoin de planification détaillée

**Workflow** :
1. **Analysis** (Optionnel) → `/analyst`
2. **Planning** → `/pm`
3. **Solutioning** → `/ux-designer` → `/architect` → `/pm`
4. **Implementation** → `/sm` → `/dev` → `/tea`

**Temps estimé** : 2-4h pour setup complet

### Option 2 : Quick Flow (Rapide)

**Quand l'utiliser** : Petite feature, prototype, bug fix complexe

**Workflow** :
1. **Tech Spec** → `/quick-flow` + skill `bmad-tech-spec`
2. **Implementation** → `/quick-flow` + skill `bmad-quick-dev`
3. **Review** → `/quick-flow` + skill `bmad-code-review`

**Temps estimé** : 30min - 1h

---

## Workflow Complet : Étape par Étape

### Phase 1 : Analysis (Optionnel)

**Agent** : `/analyst`

**Objectif** : Comprendre le problème, faire de la recherche

**Actions** :
```bash
# Brainstorming projet
/analyst
> Charge le skill `bmad-core-brainstorming`
> Réponds aux questions de découverte

# Research (optionnel)
/analyst  
> Charge le skill `bmad-research`
> Définis le scope de recherche

# Product Brief
/analyst
> Charge le skill `bmad-product-brief`
> Crée le brief produit
```

**Output** : `_bmad-output/analysis/product-brief.md`

---

### Phase 2 : Planning

**Agent** : `/pm`

**Objectif** : Créer le PRD via interviews utilisateurs

**Actions** :
```bash
/pm
> Charge le skill `bmad-prd`
> Réponds aux questions WHY
> Définis le problème et le scope MVP
```

**Principes clés** :
- Demande 'POURQUOI ?' sans relâche
- Le PRD émerge des interviews, pas de templates
- Ship le minimum qui valide l'hypothèse

**Output** : `_bmad-output/prd/prd.md`

---

### Phase 3 : Solutioning

#### Étape 3.1 : UX Design (Optionnel)

**Agent** : `/ux-designer`

```bash
/ux-designer
> Charge le skill `bmad-ux-design`
> Crée le UX Design à partir du PRD

# Wireframes (optionnel)
/ux-designer
> Charge le skill `bmad-wireframe`
```

**Output** : `_bmad-output/ux/ux-design.md`

#### Étape 3.2 : Architecture

**Agent** : `/architect`

```bash
/architect
> Charge le skill `bmad-architecture`
> Conçois l'architecture dirigée par les user journeys
```

**Principes clés** :
- User journeys drive decisions
- Boring technology for stability
- Simple solutions that scale

**Output** : `_bmad-output/architecture/architecture.md`

#### Étape 3.3 : Epics & User Stories

**Agent** : `/pm`

```bash
/pm
> Charge le skill `bmad-epics-stories`
> Crée les epics et user stories à partir du PRD et Architecture
```

**Output** : `_bmad-output/epics/epic-*.md`

---

### Phase 4 : Implementation

#### Étape 4.1 : Sprint Planning

**Agent** : `/sm`

```bash
/sm
> Charge le skill `bmad-sprint-planning`
> Génère le sprint-status.yaml à partir des epics
```

**Output** : `_bmad-output/sprint-status.yaml`

#### Étape 4.2 : Create Stories

**Agent** : `/sm`

```bash
/sm
> Charge le skill `bmad-create-story`
> Crée une story developer-ready avec tasks/subtasks
```

**Output** : `_bmad-output/stories/story-*.md`

#### Étape 4.3 : Implementation (TDD)

**Agent** : `/dev`

```bash
/dev
> Charge le story file
> Charge le skill `bmad-dev-story`
> Implémente en suivant red-green-refactor

# Code Review (nouveau contexte + LLM)
/dev
> Charge le skill `bmad-code-review`
```

**Principes clés** :
- Story file = source unique de vérité
- Red-green-refactor obligatoire
- Tous les tests passent à 100%

---

## Quick Flow : Étape par Étape

### Étape 1 : Tech Spec

**Agent** : `/quick-flow`

```bash
/quick-flow
> Charge le skill `bmad-tech-spec`
> Décris la feature
> Génère un tech spec avec implementation-ready stories
```

**Output** : `_bmad-output/quick-flow/tech-spec.md`

### Étape 2 : Quick Dev

**Agent** : `/quick-flow`

```bash
/quick-flow
> Charge le skill `bmad-quick-dev`
> Implémente end-to-end en suivant le tech spec
```

### Étape 3 : Code Review

**Agent** : `/quick-flow` (nouveau contexte)

```bash
/quick-flow
> Charge le skill `bmad-code-review`
> Review approfondie du code
```

---

## Vérifier Ton Statut

**À tout moment** :

```bash
/bmad-master
> Charge le skill `bmad-workflow-status`
> Identifie où tu en es dans le projet
> Obtiens les prochaines étapes
```

---

## MCP Servers Disponibles

Les MCP servers OpenFlow sont conservés :

- **notify** : `ask_user`, `notify_commit`, `notify_merge`, `notify_sync`
- **screenshot** : Capture d'écran native macOS
- **lsmcp** : LSP tools pour TypeScript/Python/C++
- **sequential-thinking** : Raisonnement structuré

---

## Fichier `project-context.md`

**Crucial** : Si `**/project-context.md` existe, TOUS les agents BMAD le traitent comme une bible.

Crée-le avec :
```bash
/tech-writer
> Charge le skill `bmad-document-project`
```

---

## Tips & Best Practices

### Démarrer un Nouveau Projet

1. `/analyst` → Product Brief
2. `/pm` → PRD
3. `/architect` → Architecture
4. `/sm` → Sprint Planning
5. `/dev` → Implementation

### Feature Rapide

1. `/quick-flow` → Tech Spec
2. `/quick-flow` → Quick Dev
3. `/quick-flow` → Code Review

### Projet Existant (Brownfield)

1. `/tech-writer` → Document Project (`bmad-document-project`)
2. Crée `project-context.md`
3. Suis le workflow normal

---

## Ressources

- **README.md** : Documentation complète OpenFlow-BMAD
- **agents/en/** : Tous les agents BMAD disponibles
- **skills/en/bmad-*** : Tous les skills/workflows BMAD
- **BMAD Original** : https://github.com/bmad-code-org/BMAD-METHOD

---

## Besoin d'Aide ?

```bash
/bmad-master
> "Je veux [faire X], quel agent et workflow utiliser ?"
```

BMad Master connaît tout l'écosystème et peut te guider ! 🧙
