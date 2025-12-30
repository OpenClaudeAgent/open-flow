# Plan 07 - Serveur MCP OpenCode Session History

## Contexte

Lors des sessions OpenCode longues, l'agent accumule du contexte dans l'historique des messages. Cependant, lors de compactions de session (context window limitations), ce contexte peut être perdu. 

OpenCode stocke **persistemment** tout l'historique dans `~/.local/share/opencode/storage/` avec une structure hiérarchique :

```
session/          → Métadonnées des sessions (projectID, title, parentID, timestamps)
message/          → Métadonnées des messages (role, agent, tokens, parentID)
part/             → Contenu fragmenté (text, reasoning, step-start/finish)
session_diff/     → Diffs entre sessions
session_share/    → Partage de sessions
todo/             → Todos
```

**Problème** : Les agents n'ont actuellement pas accès à cet historique persistant. Créer un serveur MCP qui expose cet historique permettrait :
- De retrouver du contexte perdu lors de compactions
- De rechercher dans l'historique des sessions
- De partager des sessions entre agents
- D'analyser l'historique complet d'un projet

## Objectif

Créer un **serveur MCP (Model Context Protocol)** qui expose une API de recherche et de lecture de l'historique persistant des sessions OpenCode, permettant aux agents de :
1. Récupérer l'historique complet d'une session
2. Rechercher des sessions par titre, timestamp, agent, contenu
3. Naviguer le graphe de filiation (parent-child relationships)
4. Accéder au contenu complet des messages et parts
5. Analyser les statistiques des sessions (tokens, additions/deletions, durée)

## Comportement attendu

**En tant qu'agent** (ex: roadmap, executor, quality), je peux :

1. **Lister les sessions d'un projet**
   - Je fournis un `sessionName` ou `projectID`
   - Je reçois la liste des sessions avec titre, timestamps, agents impliqués
   - Exemple: "Affiche-moi toutes les sessions du projet opencode-monitor"

2. **Récupérer l'historique complet d'une session**
   - Je fournis un `sessionID`
   - Je reçois la conversation complète (messages + parts) dans l'ordre chronologique
   - Les références parent-child sont incluses pour tracer les relations
   - Exemple: "Donne-moi tout l'historique de la session Quality review Plan 15"

3. **Rechercher dans les sessions**
   - Je fournis des critères : titre, timestamps, agent, contenu (regex)
   - Je reçois les sessions correspondantes avec extraits pertinents
   - Exemple: "Cherche toutes les sessions de testing du 28 décembre"
   - Exemple: "Cherche les sessions contenant 'ask_user'"

4. **Naviguer le graphe de filiation**
   - Je demande l'arborescence d'une session (parents et enfants)
   - Je reçois le graphe complet avec les métadonnées
   - Exemple: "Montre-moi la chaîne complète depuis la planification jusqu'à la validation"

5. **Analyser les statistiques**
   - Pour une session, je reçois :
     - Durée (created → updated)
     - Agents impliqués
     - Tokens consommés (input, output, reasoning, cache)
     - Changements (additions/deletions/files)
     - Nombre de messages
   - Exemple: "Combien de tokens ont été utilisés dans cette session ?"

6. **Retrouver du contexte perdu**
   - En cas de compaction, je demande l'historique de la session actuelle
   - Le serveur me retourne le contexte complet depuis le début

## Spécifications

### Structure du Serveur MCP

**Langage** : Python (cohérent avec notify et screenshot servers)

**Localisation** : `servers/opencode-session-history/`

**Dépendances** :
- Protocol d'OpenCode (introspection du stockage)
- Regex pour recherche (re, rg)
- JSON parsing

### Ressources OpenCode à Accéder

| Resource | Chemin | Format | Clé | Contenu |
|----------|--------|--------|-----|---------|
| Sessions | `~/.local/share/opencode/storage/session/[projectID]/` | JSON | `sessionID` | Métadonnées: id, projectID, parentID, title, time, summary |
| Messages | `~/.local/share/opencode/storage/message/[sessionID]/` | JSON | `messageID` | Métadonnées: id, sessionID, role, agent, tokens, parentID |
| Parts | `~/.local/share/opencode/storage/part/[messageID]/` | JSON | `partID` | Contenu: id, sessionID, messageID, type, text/reasoning |

### Endpoints MCP (Outils à Exposer)

#### Tool 1: `list_sessions`
```
Paramètres:
  - sessionName (string): Nom/pattern d'une session (optionnel)
  - projectID (string): ID du projet (optionnel, inféré si sessionName fourni)
  - limit (int): Max résultats (default: 50)

Retour:
  - Array de sessions avec: id, title, created, updated, agent, parentID, summary
```

#### Tool 2: `get_session_history`
```
Paramètres:
  - sessionID (string): Session ID à récupérer

Retour:
  - Historique complet: messages + parts assemblés
  - Format: Conversation chronologique avec métadonnées
  - Relations parent-child incluses
```

#### Tool 3: `search_sessions`
```
Paramètres:
  - query (string): Recherche libre (titre, contenu, regex)
  - agent (string): Filter par agent (quality, tester, executor, etc.)
  - projectID (string): Filter par projet
  - startDate (timestamp): Filter par date min
  - endDate (timestamp): Filter par date max
  - limit (int): Max résultats (default: 20)

Retour:
  - Array de sessions matching + extraits pertinents
```

#### Tool 4: `get_session_lineage`
```
Paramètres:
  - sessionID (string): Session de référence

Retour:
  - Arborescence complète:
    - parentSessions: chaîne parentale jusqu'à la racine
    - childSessions: tous les descendants
    - siblings: sessions au même niveau
```

#### Tool 5: `get_session_stats`
```
Paramètres:
  - sessionID (string): Session à analyser

Retour:
  - Statistiques:
    - duration (ms)
    - agents (array)
    - tokens { input, output, reasoning, cache_read, cache_write }
    - changes { additions, deletions, files }
    - messageCount
    - partCount
```

### Indexation & Performance

Pour sessions longues (16735+ parts), l'indexation sera :
1. **Lazy**: Fichiers lus à la demande
2. **Cached**: Résultats cachés en mémoire (LRU)
3. **Searchable**: Préparation pour full-text search (grep avec rg)

### Gestion de la Session ID Utilisateur

Chaque agent générera une UUID au démarrage (ou recevra via env var)
Le serveur utilisera cette ID pour lier les sessions actuelles à l'historique.

## Documentation

Ce serveur MCP est **additionnel** et n'impacte pas la doc globale du projet **actuellement**, mais pour la **cohérence future** :

**À documenter au niveau global** (après implémentation) :
1. **README.md du projet** : Mentionner le nouveau serveur `opencode-session-history` dans la liste des servers MCP disponibles
2. **Installation** : Instructions pour installer le serveur (dans `install.sh` si applicable)
3. **Usage guide** : Comment les agents/utilisateurs peuvent accéder à l'historique via ce serveur
4. **Architecture docs** : Expliquer comment les sessions OpenCode sont exposées via MCP

**Recommandation** : Ces updates devraient être faites après le merge du serveur (subtask 7.9 crée le README.md du serveur, puis le README.md du projet peut être updaté en post-merge).

## Sous-tâches

| Priorité | Subtask | Dépendances | Description |
|----------|---------|-------------|-------------|
| 1 | 7.1 - Parser OpenCode storage | None | Implémenter la lecture des fichiers session/message/part |
| 2 | 7.2 - Indexation & cache | 7.1 | Créer un index en mémoire avec LRU cache |
| 3 | 7.3 - Tool list_sessions | 7.2 | Exposer les sessions par project/name |
| 4 | 7.4 - Tool get_session_history | 7.1 | Assembler messages + parts en conversation |
| 5 | 7.5 - Tool search_sessions | 7.2 | Recherche par titre/agent/contenu (grep) |
| 6 | 7.6 - Tool get_session_lineage | 7.2 | Graphe parent-child |
| 7 | 7.7 - Tool get_session_stats | 7.2 | Agrégation de statistiques |
| 8 | 7.8 - Tests unitaires | 7.3-7.7 | Coverage des 5 tools |
| 9 | 7.9 - Documentation & examples | 7.8 | README avec exemples d'usage |

## Checklist de validation

- [ ] Parser OpenCode storage sans erreur
- [ ] Lister sessions avec pagination
- [ ] Récupérer l'historique complet d'une session
- [ ] Recherche par titre et contenu fonctionnelle
- [ ] Graphe de filiation correct (parentID links)
- [ ] Statistiques précises (tokens, durée, agents)
- [ ] Performance acceptable pour sessions longues (1000+ messages)
- [ ] Cache LRU fonctionne correctement
- [ ] Tests unitaires pour tous les outils
- [ ] Documentation avec exemples
- [ ] Gestion des erreurs robuste (fichiers manquants, JSON malformé)
- [ ] Global documentation evaluated

## Notes Additionnelles

### Cas d'usage prioritaires

1. **Retrouver du contexte** : Un agent peut demander l'historique au démarrage
2. **Analyser une feature** : Tracer toute une feature de la planification au test
3. **Déboguer** : Trouver quand/où une décision a été prise
4. **Partager** : Exporter une session complète pour collaboration

### Intégration Future

- Exporter sessions en Markdown/PDF
- Webhooks pour notifications
- Full-text search (Elasticsearch si sessions énormes)
- UI Web pour naviguer l'historique

### Fichiers Impactés

- Création: `servers/opencode-session-history/` (nouveau serveur MCP)
- Création: `servers/opencode-session-history/README.md` (documentation serveur)
- Modification: Aucune au code existant (additionnel)

---

**Créé le**: 2025-12-30  
**Scope**: Nouveau serveur MCP pour historique des sessions  
**Estimation**: ~3-4 jours (subtasks 7.1-7.9)
