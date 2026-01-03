# Plan 06 - Analytics OpenFlow

> **STATUT : ABANDONNE**
> 
> Ce plan est hors scope pour open-flow qui se concentre sur la definition des agents et skills.
> 
> Cette fonctionnalite est implementee dans le projet **OpenCode Monitor** :
> - Repository : https://github.com/OpenClaudeAgent/opencode-monitor
> - Plan : `roadmap/plan-16-analytics.md`

## Contexte

OpenCode stocke des donnees riches sur chaque session dans `~/.local/share/opencode/storage/` :
- **Sessions** : Metadonnees (projet, titre, timestamps)
- **Messages** : Role, agent utilise, modele, tokens, cout
- **Parts** : Contenu des messages, appels d'outils (tools), resultats

Ces donnees permettent d'analyser l'utilisation des agents, skills et workflows definis dans ce repo (open-flow). Actuellement, il n'existe aucun moyen de visualiser ces metriques ou de detecter des patterns problematiques (boucles infinies d'agents, sur-utilisation de certains outils, etc.).

## Objectif

Creer un script CLI qui analyse les sessions OpenCode et genere un rapport statistique sur l'utilisation des composants OpenFlow (agents, skills, workflows).

## Comportement attendu

### Invocation

```bash
# Analyse complete
./scripts/openflow-analytics

# Analyse d'un projet specifique
./scripts/openflow-analytics --project open-flow

# Analyse des N derniers jours
./scripts/openflow-analytics --days 7

# Export JSON pour traitement externe
./scripts/openflow-analytics --format json > report.json
```

### Rapport genere

Le script affiche un rapport structure en plusieurs sections :

#### 1. Resume global
```
=== OpenFlow Analytics ===
Periode: 2025-12-22 -> 2025-12-29 (7 jours)
Sessions analysees: 42
Messages totaux: 1,234
Tokens consommes: 2.4M (input: 1.8M, output: 600K)
Cout estime: $45.23
```

#### 2. Utilisation des agents
```
=== Agents ===
Agent          | Sessions | Messages | Tokens   | Cout
---------------|----------|----------|----------|--------
executeur      | 15       | 234      | 890K     | $12.50
roadmap        | 8        | 89       | 120K     | $2.30
build (defaut) | 35       | 567      | 1.2M     | $25.00
explore        | 12       | 156      | 45K      | $1.20
tester         | 3        | 45       | 89K      | $3.10
quality        | 2        | 23       | 34K      | $1.13
```

#### 3. Utilisation des skills
```
=== Skills ===
Skill                | Invocations | Par agent
---------------------|-------------|------------------
agentic-flow         | 23          | executeur (20), build (3)
clean-code           | 5           | quality (5)
notify               | 12          | executeur (12)
(aucun skill charge) | 156         | -
```

#### 4. Utilisation des outils
```
=== Tools (top 10) ===
Tool      | Invocations | Succes | Echecs | Temps moyen
----------|-------------|--------|--------|------------
edit      | 456         | 450    | 6      | 0.2s
read      | 1,234       | 1,234  | 0      | 0.1s
bash      | 345         | 320    | 25     | 2.3s
task      | 89          | 85     | 4      | 45.2s
glob      | 234         | 234    | 0      | 0.3s
```

#### 5. Analyse des chaines d'agents (nested agents)
```
=== Chaines d'invocation ===
Profondeur max observee: 3

Patterns detectes:
- executeur -> tester (15 fois)
- executeur -> quality (8 fois)
- executeur -> refactoring -> tester (2 fois)

Sessions avec profondeur > 2:
- ses_abc123: executeur -> tester -> explore (3 niveaux)
- ses_def456: executeur -> refactoring -> tester (3 niveaux)
```

#### 6. Alertes et anomalies
```
=== Alertes ===
[WARN] Session ses_xyz789: 12 invocations de 'task' en cascade
[WARN] Agent 'explore' invoque 45 fois dans une seule session
[INFO] Skill 'qml' jamais utilise sur la periode
```

### Filtres disponibles

| Option | Description |
|--------|-------------|
| `--project <name>` | Filtre par nom de projet |
| `--days <n>` | Analyse des N derniers jours |
| `--agent <name>` | Focus sur un agent specifique |
| `--format <txt\|json>` | Format de sortie |
| `--verbose` | Details supplementaires |

### Detection des anomalies

Le script detecte automatiquement :
1. **Boucles d'agents** : Un agent qui s'invoque lui-meme (directement ou indirectement)
2. **Sur-utilisation** : Plus de 10 invocations de `task` dans une session
3. **Profondeur excessive** : Chaines d'agents > 3 niveaux
4. **Skills inutilises** : Skills definis mais jamais charges
5. **Echecs repetitifs** : Outils avec taux d'echec > 20%

## Specifications

*(Section reservee a l'Executeur pour les details techniques)*

### Structure des donnees OpenCode

```
~/.local/share/opencode/storage/
├── session/{project_hash}/{session_id}.json  # Metadonnees session
├── message/{session_id}/{message_id}.json    # Messages avec agent, tokens
├── part/{message_id}/{part_id}.json          # Contenu, tool calls
└── todo/                                      # Todos
```

### Champs cles

**Session** :
- `id`, `projectID`, `directory`, `title`
- `time.created`, `time.updated`

**Message** :
- `sessionID`, `role` (user/assistant)
- `agent` (executeur, roadmap, build, explore...)
- `modelID`, `providerID`
- `tokens` (input, output, cache.read, cache.write)
- `cost`

**Part (type: tool)** :
- `tool` (edit, read, bash, task, skill, glob...)
- `state.status` (completed, error...)
- `state.input`, `state.output`

## Checklist de validation

- [ ] Le script s'execute sans erreur avec `./scripts/openflow-analytics`
- [ ] Le resume global affiche les bonnes statistiques
- [ ] Les agents custom (executeur, roadmap, etc.) sont correctement identifies
- [ ] Les skills charges sont detectes via le tool "skill"
- [ ] Les chaines d'agents sont reconstruites via le tool "task"
- [ ] Les alertes de boucles/sur-utilisation s'affichent correctement
- [ ] Le filtre `--project` fonctionne
- [ ] Le filtre `--days` fonctionne
- [ ] L'export `--format json` produit du JSON valide
- [ ] Le script fonctionne meme avec 0 sessions (message informatif)
