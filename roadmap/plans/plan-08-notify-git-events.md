# Plan 08 - Notifications Git Events

**Date** : 2025-12-30  
**Branche** : `feature/notify-git-events`

## Contexte

Actuellement, le serveur MCP Notify expose un seul outil `ask_user` qui permet de poser des questions a l'utilisateur. Cependant, les agents effectuent des operations Git importantes (commits, merges, synchronisation worktrees) sans en informer l'utilisateur de maniere proactive.

L'utilisateur peut etre deconnecte ou travailler sur autre chose pendant que les agents travaillent. Il est utile d'etre notifie des evenements Git significatifs pour :
- Suivre la progression du travail des agents
- Etre informe des merges sur main (changements importants)
- Savoir quand les worktrees sont synchronises

## Objectif

Ajouter 3 nouveaux outils au serveur MCP Notify pour informer l'utilisateur des evenements Git :
1. **`notify_commit`** : Notifie quand un agent fait un commit
2. **`notify_merge`** : Notifie quand une branche est mergee sur main
3. **`notify_sync`** : Notifie quand les worktrees sont synchronises

Ces outils sont **informatifs** (pas de question), contrairement a `ask_user` qui est **interactif**.

## Comportement attendu

### 1. Outil `notify_commit`

Notifie l'utilisateur qu'un commit a ete effectue.

**Notification affichee :**
```
+-----------------------------------------------+
| [Icone OpenFlow]                              |
| feature/notify-actions              subtitle  |
| Commit effectue                        title  |
| fix(notify): add action button support        |
|                                               |
| Fichiers: server.py, notifier.py       body   |
+-----------------------------------------------+
```

**Parametres :**
| Parametre | Type | Requis | Description |
|-----------|------|--------|-------------|
| `branch` | string | Oui | Branche du commit |
| `message` | string | Oui | Message du commit (1ere ligne) |
| `files` | array | Non | Liste des fichiers modifies |
| `hash` | string | Non | Hash court du commit (7 chars) |
| `agent` | string | Non | Nom de l'agent qui commit |

**Retour :** `"Commit notified: <hash> on <branch>"`

### 2. Outil `notify_merge`

Notifie l'utilisateur qu'une branche a ete mergee sur main.

**Notification affichee :**
```
+-----------------------------------------------+
| [Icone OpenFlow]                              |
| open-flow                             subtitle |
| Merge sur main                          title |
| feature/notify-actions → main                 |
|                                               |
| 3 commits, 5 fichiers modifies          body  |
+-----------------------------------------------+
```

**Parametres :**
| Parametre | Type | Requis | Description |
|-----------|------|--------|-------------|
| `source_branch` | string | Oui | Branche source mergee |
| `commits_count` | integer | Non | Nombre de commits merges |
| `files_count` | integer | Non | Nombre de fichiers modifies |
| `version` | string | Non | Tag de version (ex: v0.5.0) |
| `repo` | string | Non | Nom du repository |
| `agent` | string | Non | Nom de l'agent qui merge |

**Retour :** `"Merge notified: <source_branch> → main"`

### 3. Outil `notify_sync`

Notifie l'utilisateur que les worktrees ont ete synchronises.

**Notification affichee :**
```
+-----------------------------------------------+
| [Icone OpenFlow]                              |
| open-flow                             subtitle |
| Worktrees synchronises                  title |
| 3 worktrees mis a jour avec main              |
|                                               |
| roadmap, executor, quality              body  |
+-----------------------------------------------+
```

**Parametres :**
| Parametre | Type | Requis | Description |
|-----------|------|--------|-------------|
| `worktrees` | array | Oui | Liste des worktrees synchronises |
| `source` | string | Non | Branche source (default: main) |
| `repo` | string | Non | Nom du repository |
| `conflicts` | array | Non | Liste des conflits detectes |

**Retour :** `"Sync notified: <count> worktrees updated"`

### 4. Niveau d'urgence par defaut

| Outil | Urgence | Son | Justification |
|-------|---------|-----|---------------|
| `notify_commit` | `low` | Ping discret | Evenement frequent, informatif |
| `notify_merge` | `normal` | Funk | Evenement important |
| `notify_sync` | `low` | Ping discret | Operation technique |

### 5. Integration dans le workflow agent

**Phase d'integration (apres implementation) :**

| Agent | Outil | Quand |
|-------|-------|-------|
| Executeur | `notify_commit` | Apres chaque commit |
| Coordinateur | `notify_merge` | Apres merge sur main |
| Coordinateur | `notify_sync` | Apres `make sync-worktrees` |
| Refactoring | `notify_commit` | Apres commits incrementaux |
| Tester | `notify_commit` | Apres ajout de tests |

**Fichiers a modifier pour integration :**
- `agents/fr/executeur.md` et `agents/en/executor.md`
- `agents/fr/coordinateur.md` et `agents/en/coordinator.md`
- `agents/fr/refactoring.md` et `agents/en/refactoring.md`
- `agents/fr/tester.md` et `agents/en/tester.md`
- `skills/fr/agentic-flow/SKILL.md` et `skills/en/agentic-flow/SKILL.md`
- `skills/fr/swarm-orchestration/SKILL.md` et `skills/en/swarm-orchestration/SKILL.md`

## Sous-taches

- **8.1** - Implementer `notify_commit` dans server.py
- **8.2** - Implementer `notify_merge` dans server.py
- **8.3** - Implementer `notify_sync` dans server.py
- **8.4** - Mettre a jour le schema MCP (3 nouveaux outils)
- **8.5** - Tester les 3 outils manuellement
- **8.6** - Mettre a jour servers/notify/README.md
- **8.7** - Integrer dans agents Executeur et Coordinateur
- **8.8** - Integrer dans skills agentic-flow et swarm-orchestration
- **8.9** - Tester l'integration complete (workflow reel)

## Priorite des sous-taches

| Priorite | Sous-tache | Dependances |
|----------|------------|-------------|
| 1 | 8.1 - notify_commit | Aucune |
| 2 | 8.2 - notify_merge | Aucune |
| 3 | 8.3 - notify_sync | Aucune |
| 4 | 8.4 - Schema MCP | 8.1, 8.2, 8.3 |
| 5 | 8.5 - Tests manuels | 8.4 |
| 6 | 8.6 - Documentation | 8.5 |
| 7 | 8.7 - Integration agents | 8.5 |
| 8 | 8.8 - Integration skills | 8.7 |
| 9 | 8.9 - Test integration | 8.8 |

## Checklist de validation

### Implementation MCP
- [ ] `notify_commit` envoie une notification avec branch + message + fichiers
- [ ] `notify_merge` envoie une notification avec source_branch + stats
- [ ] `notify_sync` envoie une notification avec liste worktrees
- [ ] Chaque outil retourne un message de confirmation
- [ ] Les urgences par defaut sont respectees (low/normal/low)

### Documentation
- [ ] README.md du serveur notify mis a jour avec les 3 outils
- [ ] Exemples d'utilisation documentes

### Integration agents
- [ ] Executeur utilise `notify_commit` apres ses commits
- [ ] Coordinateur utilise `notify_merge` apres merge sur main
- [ ] Coordinateur utilise `notify_sync` apres synchronisation
- [ ] Permissions MCP mises a jour si necessaire

### Integration skills
- [ ] `agentic-flow` documente quand utiliser `notify_commit`
- [ ] `swarm-orchestration` documente quand utiliser `notify_merge` et `notify_sync`

### Test integration
- [ ] Workflow complet teste : commit → merge → sync avec notifications
- [ ] Notifications recues correctement sur macOS
