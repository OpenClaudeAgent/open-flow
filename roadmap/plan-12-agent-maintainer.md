# Plan 12 - Agent Maintainer (surveillance et sante du projet)

## Contexte

A mesure qu'un projet grandit avec l'ajout de nouvelles fonctionnalites, il devient difficile de maintenir une vision globale de la codebase. Les problemes typiques sont :
- Fichiers qui deviennent trop grands (> 300-500 lignes)
- Code duplique entre plusieurs fichiers
- Architecture qui se degrade (dossiers mal organises)
- Perte de controle sur l'evolution du projet
- Accumulation de dette technique non detectee

Actuellement, les agents Executeur, Refactoring, Tester et Quality travaillent sur des taches specifiques sans avoir de vision d'ensemble sur la sante globale du projet.

## Objectif

Creer un nouvel agent **Maintainer** dont le role est de surveiller la sante globale du projet, generer des rapports de metriques, et recommander des actions de maintenance (refactoring, reorganisation, nettoyage).

## Comportement attendu

### Role du Maintainer

Le Maintainer est un agent de **surveillance et analyse**. Il ne modifie pas le code, il observe et rapporte.

Ses responsabilites :
1. Analyser la structure globale du projet
2. Detecter les problemes potentiels
3. Calculer des metriques d'evolution
4. Generer des rapports detailles
5. Recommander des actions de maintenance

### Quand invoquer le Maintainer

| Moment | Invoque par | Obligatoire |
|--------|-------------|-------------|
| A la creation d'un tag | Coordinateur | Oui |
| Fin de tache majeure | Executeur | Recommande |
| Sur demande utilisateur | N'importe qui | Manuel |

### Structure du dossier maintenance

```
maintenance/
  reports/
    report-YYYY-MM-DD-HHmmss.md    # Rapport horodate
    report-v0.7.0.md               # Rapport par tag
  templates/
    report-template.md             # Template de rapport
  metrics/
    metrics-history.json           # Historique des metriques
```

### Metriques calculees

#### Metriques globales
| Metrique | Description |
|----------|-------------|
| `total_lines` | Nombre total de lignes de code |
| `total_files` | Nombre total de fichiers |
| `lines_added` | Lignes ajoutees depuis dernier tag |
| `lines_removed` | Lignes supprimees depuis dernier tag |
| `net_change` | Variation nette (added - removed) |
| `churn_rate` | Taux de modification (added + removed) / total |

#### Metriques par fichier
| Metrique | Description | Seuil d'alerte |
|----------|-------------|----------------|
| `file_lines` | Lignes par fichier | > 400 |
| `file_functions` | Fonctions par fichier | > 20 |
| `function_lines` | Lignes par fonction | > 50 |
| `cyclomatic_complexity` | Complexite cyclomatique | > 10 |

#### Metriques de qualite
| Metrique | Description |
|----------|-------------|
| `duplicate_blocks` | Blocs de code dupliques detectes |
| `test_coverage` | Couverture de tests (si disponible) |
| `todo_count` | Nombre de TODO/FIXME dans le code |
| `deep_nesting` | Fichiers avec imbrication > 4 niveaux |

### Analyse structurelle

Le Maintainer analyse :

1. **Taille des fichiers**
   - Liste des fichiers > 300 lignes (warning)
   - Liste des fichiers > 500 lignes (critical)
   - Recommandation de split si necessaire

2. **Duplication de code**
   - Detection de blocs similaires (> 10 lignes)
   - Suggestion d'extraction en fonction/module commun

3. **Architecture des dossiers**
   - Dossiers avec trop de fichiers (> 15)
   - Dossiers trop profonds (> 4 niveaux)
   - Suggestion de reorganisation

4. **Coherence des responsabilites**
   - Fichiers qui font "trop de choses"
   - Imports circulaires potentiels
   - Couplage excessif entre modules

### Format du rapport

```markdown
# Rapport Maintainer - [DATE ou TAG]

## Resume executif
- Sante globale : [Bon / Attention / Critique]
- Actions recommandees : X
- Fichiers a surveiller : Y

## Metriques d'evolution
| Metrique | Valeur | Variation | Tendance |
|----------|--------|-----------|----------|
| Total lignes | 5420 | +320 | ↗️ |
| Total fichiers | 45 | +3 | → |
| ...

## Alertes

### Fichiers trop grands
- `src/executor.ts` : 523 lignes (CRITICAL)
- `src/utils/helpers.ts` : 380 lignes (WARNING)

### Code duplique detecte
- Bloc similaire dans `fileA.ts:45-60` et `fileB.ts:120-135`
  Suggestion : Extraire en fonction commune

### Architecture
- Dossier `src/utils/` contient 18 fichiers → envisager sous-dossiers

## Recommandations

### Priorite haute
1. [ ] Splitter `executor.ts` en modules (orchestration, execution, reporting)
2. [ ] Extraire fonction commune pour [description]

### Priorite moyenne
3. [ ] Reorganiser `src/utils/` en sous-categories
4. [ ] Ajouter tests pour [module]

### Priorite basse
5. [ ] Nettoyer les TODO obsoletes

## Historique des metriques
[Graphique ou tableau d'evolution sur les 5 derniers tags]
```

### Workflow d'invocation

```
Coordinateur (creation tag) / Executeur (fin de tache)
    |
    ├─ Invoque Maintainer avec contexte :
    │   - Tag actuel (ou commit pour Executeur)
    │   - Tag precedent (pour comparaison)
    │   - Scope (global ou dossier specifique)
    │
    ├─ Maintainer analyse et genere rapport
    │   └─ Ecrit dans maintenance/reports/report-vX.Y.Z.md
    │
    ├─ Agent invoquant lit le rapport
    │
    └─ Decisions possibles :
        - Creer le tag (sante OK)
        - Reporter le tag et invoquer Refactoring (problemes detectes)
        - Alerter utilisateur via MCP ask_user (etat critique)
          → Notification macOS avec options : "Forcer le tag" / "Annuler"
```

### Notification utilisateur (etat critique)

Quand le Maintainer detecte un etat critique, l'agent invoquant utilise le MCP `ask_user` :

```
ask_user(
    title: "Maintainer: Etat critique detecte"
    question: "Le rapport indique X fichiers > 500 lignes, Y blocs dupliques. Voulez-vous continuer ?"
    options: ["Forcer le tag", "Annuler et corriger"]
    urgency: "high"
)
```

Cela envoie une notification macOS native avec son pour attirer l'attention de l'utilisateur.

### Integration avec les autres agents

| Agent | Interaction avec Maintainer |
|-------|----------------------------|
| Coordinateur | Invoque a la creation d'un tag, lit rapport, decide |
| Executeur | Peut invoquer en fin de tache |
| Refactoring | Recoit recommandations du Maintainer |
| Quality | Complementaire (Quality = code, Maintainer = structure) |

### Fichier agent Maintainer

Creer `agents/fr/maintainer.md` et `agents/en/maintainer.md` avec :
- Instructions de l'agent
- Acces aux outils d'analyse (grep, wc, cloc si disponible)
- Template de rapport
- Seuils d'alerte configurables
- Workflow de generation de rapport

## Checklist de validation

- [ ] Dossier `maintenance/` cree avec structure (reports/, templates/, metrics/)
- [ ] Template de rapport cree dans `maintenance/templates/report-template.md`
- [ ] Agent `agents/fr/maintainer.md` cree avec instructions completes
- [ ] Agent `agents/en/maintainer.md` cree (version anglaise)
- [ ] Skill `skills/fr/maintenance-report/SKILL.md` cree
- [ ] Skill `skills/en/maintenance-report/SKILL.md` cree
- [ ] Coordinateur mis a jour pour invoquer Maintainer a la creation d'un tag
- [ ] Executeur mis a jour pour invoquer Maintainer (optionnel)
- [ ] Test : Maintainer genere un rapport sur open-flow
- [ ] Test : Rapport contient metriques correctes
- [ ] Test : Alertes detectees sur fichiers > seuil
- [ ] Test : MCP ask_user declenche en cas d'etat critique
- [ ] Documentation globale mise a jour (AGENTS.md)
