# Plan 01 - Notifications macOS natives avec PyObjC

**Date** : 2025-12-28  
**Branche** : `feature/notify-pyobjc`

## Contexte

Le serveur MCP Notify utilise actuellement `osascript` (AppleScript) pour envoyer des notifications sur macOS. Cette approche presente plusieurs problemes :

1. **Comportement au clic non desire** : Cliquer sur une notification ouvre AppleScript Editor
2. **Pas d'icone personnalisee** : Seuls des emojis dans le titre sont possibles
3. **Manque de contexte** : Impossible de savoir quel agent a envoie la notification
4. **Pas de subtitle** : AppleScript ne permet pas d'utiliser le champ subtitle natif de macOS

## Objectif

Remplacer l'implementation `osascript` par une implementation native utilisant PyObjC pour acceder directement aux APIs macOS de notification, tout en conservant la compatibilite avec Linux et Windows.

## Comportement attendu

### 1. Apparence de la notification

La notification macOS doit s'afficher avec la structure suivante :

```
+---------------------------------------+
| [Icone open-flow]                     |
| Agent Executeur              subtitle |
| Validation requise             title  |
| Tache terminee avec succes   message  |
+---------------------------------------+
```

- **Icone** : Une icone dediee open-flow (pas l'icone AppleScript)
- **Subtitle** : Affiche le nom de l'agent si fourni (ex: "Agent Executeur")
- **Title** : Le titre de la notification avec emoji selon le type
- **Message** : Le corps du message

### 2. Nouveaux parametres MCP

L'outil `notify` accepte deux nouveaux parametres optionnels :

| Parametre | Type | Description | Exemple |
|-----------|------|-------------|---------|
| `agent` | string | Nom de l'agent qui envoie la notification | "executeur", "tester", "quality" |
| `task` | string | Nom ou numero de la tache en cours | "Plan 03", "Tests unitaires" |

Quand `agent` est fourni, le subtitle affiche "Agent [Nom]" (avec majuscule).
Quand `task` est fourni, il est ajoute au message entre parentheses.

### 3. Comportement au clic

- Cliquer sur la notification ne doit **rien ouvrir**
- La notification se ferme simplement
- Aucune application ne doit etre lancee

### 4. Icone personnalisee

- Une icone dediee est utilisee pour identifier les notifications open-flow
- L'icone doit etre visible dans le centre de notifications
- Format PNG ou ICNS, taille recommandee 128x128 ou plus

### 5. Compatibilite multi-plateforme

- **macOS** : Utilise PyObjC avec les APIs natives
- **Linux** : Continue d'utiliser `notify-send` (comportement inchange)
- **Windows** : Continue d'utiliser PowerShell toast (comportement inchange)

Les nouveaux parametres (`agent`, `task`) sont ignores sur Linux/Windows si non supportes.

### 6. Gestion des erreurs

- Si PyObjC n'est pas installe, fallback vers `osascript`
- Si l'icone n'est pas trouvee, la notification s'affiche sans icone custom
- Les erreurs sont loguees mais n'empechent pas l'envoi de la notification

### 7. Dependances

- PyObjC doit etre ajoute comme dependance optionnelle pour macOS
- L'installation doit rester simple : `uv pip install -e .` ou equivalent

## Sous-taches

- **1.1** - Ajouter PyObjC aux dependances du projet
- **1.2** - Implementer l'envoi de notification via PyObjC
- **1.3** - Ajouter le support du subtitle (parametre `agent`)
- **1.4** - Ajouter le support du parametre `task`
- **1.5** - Integrer une icone personnalisee
- **1.6** - Desactiver le comportement au clic
- **1.7** - Mettre a jour le schema MCP avec les nouveaux parametres
- **1.8** - Ajouter le fallback vers osascript si PyObjC absent

## Priorite des sous-taches

| Priorite | Sous-tache | Dependances |
|----------|------------|-------------|
| 1 | 1.1 - Dependances PyObjC | Aucune |
| 2 | 1.2 - Implementation PyObjC | 1.1 |
| 3 | 1.6 - Desactiver clic | 1.2 |
| 4 | 1.3 - Support subtitle/agent | 1.2 |
| 5 | 1.7 - Schema MCP | 1.3, 1.4 |
| 5 | 1.4 - Support task | 1.2 |
| 6 | 1.5 - Icone personnalisee | 1.2 |
| 7 | 1.8 - Fallback osascript | 1.2 |

## Checklist de validation

### Fonctionnalites de base
- [ ] Une notification macOS s'affiche correctement avec PyObjC
- [ ] Le titre contient l'emoji selon le type (info, success, warning, error)
- [ ] Le message s'affiche dans le corps de la notification
- [ ] Le son est joue selon le parametre `sound`

### Nouveaux parametres
- [ ] Le parametre `agent` affiche "Agent [Nom]" dans le subtitle
- [ ] Le parametre `task` est ajoute au message
- [ ] Les parametres sont optionnels et la notification fonctionne sans eux

### Comportement au clic
- [ ] Cliquer sur la notification ne lance aucune application
- [ ] La notification se ferme proprement

### Icone
- [ ] L'icone open-flow s'affiche dans la notification
- [ ] L'icone est visible dans le centre de notifications macOS

### Compatibilite
- [ ] Linux : `notify-send` fonctionne toujours
- [ ] Windows : Toast PowerShell fonctionne toujours
- [ ] macOS sans PyObjC : Fallback vers osascript fonctionne

### Integration MCP
- [ ] Le schema MCP documente les nouveaux parametres `agent` et `task`
- [ ] L'outil repond correctement via le protocole MCP
