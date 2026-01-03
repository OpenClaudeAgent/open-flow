# Plan 03 - Outil MCP screenshot

**Date** : 2025-12-28  
**Branche** : `feature/mcp-screenshot`

## Contexte

Lors du developpement d'interfaces utilisateur ou du debug de problemes visuels, il est souvent utile de capturer l'ecran pour :

1. **Documenter un bug visuel** : L'utilisateur decrit un probleme d'affichage, l'agent peut capturer ce qu'il voit
2. **Valider une implementation UI** : Comparer l'apparence reelle avec les maquettes
3. **Creer de la documentation** : Captures d'ecran pour les guides utilisateur
4. **Debug collaboratif** : Partager rapidement l'etat visuel avec l'utilisateur

Actuellement, l'utilisateur doit manuellement faire une capture d'ecran et la partager, ce qui interrompt le flux de travail.

## Objectif

Creer un nouvel outil MCP `screenshot` qui permet a un agent de capturer l'ecran (ou une fenetre specifique) et de retourner l'image pour analyse ou documentation.

## Comportement attendu

### 1. Modes de capture

L'outil propose plusieurs modes de capture :

| Mode | Description |
|------|-------------|
| `screen` | Capture l'ecran entier (ecran principal par defaut) |
| `window` | Capture une fenetre specifique par son titre |
| `region` | Capture une region definie par des coordonnees |
| `interactive` | Demande a l'utilisateur de selectionner une zone |

### 2. Parametres de l'outil

| Parametre | Type | Requis | Description |
|-----------|------|--------|-------------|
| `mode` | string | Non | Mode de capture : `screen`, `window`, `region`, `interactive`. Defaut: `screen` |
| `window_title` | string | Non | Titre (partiel) de la fenetre a capturer. Requis si mode=`window` |
| `region` | object | Non | Coordonnees `{x, y, width, height}`. Requis si mode=`region` |
| `screen_index` | number | Non | Index de l'ecran pour les configurations multi-moniteurs. Defaut: 0 |
| `format` | string | Non | Format de sortie : `png`, `jpg`. Defaut: `png` |
| `delay` | number | Non | Delai en secondes avant la capture. Defaut: 0 |

### 3. Retour de l'outil

L'outil retourne :
- Le chemin du fichier capture (stocke temporairement)
- Les metadonnees de l'image (dimensions, format)
- Optionnellement, l'image encodee en base64 pour les clients qui le supportent

### 4. Stockage des captures

- Les captures sont stockees dans un dossier temporaire dedie
- Nommage : `screenshot-YYYYMMDD-HHMMSS.png`
- Nettoyage automatique des captures de plus de 24h
- Option pour specifier un chemin de destination personnalise

### 5. Comportement par plateforme

#### macOS
- Utilise `screencapture` (outil natif) ou les APIs Cocoa via PyObjC
- Support du mode interactif natif (`screencapture -i`)
- Capture de fenetre par titre possible

#### Linux
- Utilise `gnome-screenshot`, `scrot`, ou `import` (ImageMagick)
- Fallback vers `xdotool` + `import` pour la capture de fenetre
- Mode interactif via `gnome-screenshot -a` ou `scrot -s`

#### Windows
- Utilise PowerShell avec les APIs .NET
- Capture de fenetre via titre avec `Get-Process`
- Mode interactif via `Snipping Tool` ou equivalent

### 6. Integration avec les agents

Les agents peuvent utiliser cet outil pour :
- Capturer l'etat actuel de l'application en cours de developpement
- Documenter les etapes de validation avec des captures
- Inclure des captures dans les rapports de bug

### 7. Gestion des erreurs

| Situation | Comportement |
|-----------|--------------|
| Fenetre non trouvee | Message d'erreur avec liste des fenetres disponibles |
| Outil de capture absent | Fallback vers une alternative ou message explicite |
| Region invalide | Message d'erreur avec les dimensions de l'ecran |
| Permission refusee | Instructions pour accorder les permissions (macOS) |

### 8. Permissions (macOS)

Sur macOS, la capture d'ecran necessite l'autorisation "Screen Recording" dans :
- Preferences Systeme > Securite et confidentialite > Confidentialite > Enregistrement de l'ecran

L'outil doit :
- Detecter si la permission est accordee
- Guider l'utilisateur pour l'activer si necessaire

## Sous-taches

- **3.1** - Creer la structure du module screenshot dans `servers/notify/`
- **3.2** - Implementer la capture d'ecran sur macOS
- **3.3** - Implementer la capture d'ecran sur Linux
- **3.4** - Implementer la capture d'ecran sur Windows
- **3.5** - Ajouter le support de la capture de fenetre par titre
- **3.6** - Ajouter le mode interactif (selection utilisateur)
- **3.7** - Implementer le stockage temporaire et nettoyage
- **3.8** - Enregistrer l'outil dans le serveur MCP
- **3.9** - Gerer les permissions macOS avec message explicite

## Priorite des sous-taches

| Priorite | Sous-tache | Dependances |
|----------|------------|-------------|
| 1 | 3.1 - Structure module | Aucune |
| 2 | 3.2 - macOS | 3.1 |
| 3 | 3.8 - Serveur MCP | 3.2 |
| 4 | 3.7 - Stockage temporaire | 3.2 |
| 5 | 3.5 - Capture fenetre | 3.2 |
| 6 | 3.6 - Mode interactif | 3.2 |
| 7 | 3.9 - Permissions macOS | 3.2 |
| 8 | 3.3 - Linux | 3.1 |
| 9 | 3.4 - Windows | 3.1 |

## Checklist de validation

### Capture basique
- [ ] Une capture d'ecran entier fonctionne sur macOS
- [ ] Le fichier est cree dans le dossier temporaire
- [ ] Les metadonnees (dimensions, format) sont retournees
- [ ] Le delai de capture fonctionne correctement

### Capture de fenetre
- [ ] La capture par titre de fenetre fonctionne
- [ ] Une recherche partielle du titre fonctionne (ex: "Terminal" trouve "Terminal - zsh")
- [ ] Un message clair est affiche si la fenetre n'est pas trouvee

### Mode interactif
- [ ] L'utilisateur peut selectionner une zone a capturer
- [ ] La selection peut etre annulee
- [ ] Le retour indique si l'utilisateur a annule

### Stockage
- [ ] Les fichiers sont nommes avec timestamp
- [ ] Les captures de plus de 24h sont supprimees automatiquement
- [ ] Un chemin personnalise peut etre specifie

### Multi-plateforme
- [ ] Linux : au moins un backend fonctionne (gnome-screenshot, scrot, ou import)
- [ ] Windows : la capture via PowerShell fonctionne
- [ ] Fallback gracieux si l'outil de capture n'est pas installe

### Permissions
- [ ] macOS : Detection de l'absence de permission
- [ ] macOS : Message clair pour guider l'utilisateur vers les preferences

### Integration MCP
- [ ] L'outil `screenshot` apparait dans la liste des outils
- [ ] Le schema des parametres est correctement documente
- [ ] Les erreurs sont retournees de maniere structuree
