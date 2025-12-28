# Plan 02 - Notifications macOS natives avec Go

**Date** : 2025-12-28  
**Branche** : `feature/notify-go`

## Contexte

Le plan 01 a implémenté les notifications via PyObjC, mais cette approche présente une limitation fondamentale :

1. **Identité "Python"** : Les notifications apparaissent sous "Python" dans les préférences système de macOS, car l'application émettrice est l'interpréteur Python lui-même
2. **Pas de bundle .app** : Sans application bundle, impossible d'avoir une icône propre dans le Dock/Centre de notifications
3. **NSUserNotification deprecated** : L'API utilisée est obsolète depuis macOS 10.14 (remplacée par UNUserNotificationCenter)

Une application Go compilée et packagée comme bundle .app résout ces problèmes en créant une véritable identité d'application.

## Objectif

Remplacer l'implémentation Python/PyObjC par un binaire Go natif qui :
- Envoie des notifications via les APIs Cocoa modernes (UNUserNotificationCenter)
- Est packagé comme bundle .app avec sa propre identité ("OpenFlow")
- Possède sa propre icône visible dans les notifications et préférences système
- Peut être appelé par le serveur MCP Python ou remplacer entièrement ce dernier

## Analyse des options

### Option A : Helper Go appelé par Python

Le serveur MCP reste en Python. Un binaire Go est appelé en subprocess pour envoyer les notifications.

**Avantages** :
- Migration incrémentale, moins de risques
- Le protocole MCP reste géré par le code Python existant
- Plus facile à maintenir si le serveur MCP évolue

**Inconvénients** :
- Overhead du subprocess à chaque notification
- Deux langages à maintenir
- Complexité de packaging (Python + binaire Go)

### Option B : Serveur MCP entièrement en Go

Le serveur MCP est réécrit en Go. Il gère le protocole MCP et envoie directement les notifications.

**Avantages** :
- Un seul langage, un seul binaire
- Performance optimale
- Distribution simplifiée (un seul exécutable)

**Inconvénients** :
- Réécriture complète du serveur
- Moins de flexibilité pour le scripting
- Courbe d'apprentissage si peu familier avec Go

### Recommandation

**Option A** est recommandée pour une première itération :
- Moins de risques
- Le binaire Go peut être développé et testé indépendamment
- Migration vers Option B possible ultérieurement si pertinent

## Comportement attendu

### 1. Binaire Go `openflow-notify`

Un exécutable Go qui accepte des paramètres en ligne de commande :

```
openflow-notify --title "Titre" --message "Message" [options]
```

Options supportées :
- `--title` : Titre de la notification (requis)
- `--message` : Corps du message (requis)
- `--type` : Type (info|success|warning|error), défaut: info
- `--sound` : Jouer un son (true|false), défaut: true
- `--agent` : Nom de l'agent, affiché en subtitle
- `--task` : Nom de la tâche, préfixé au message

Alternativement, les paramètres peuvent être passés en JSON via stdin pour éviter les problèmes d'échappement.

### 2. Bundle .app

Le binaire est intégré dans un bundle macOS :

```
OpenFlow.app/
  Contents/
    Info.plist          # Métadonnées de l'application
    MacOS/
      openflow-notify   # Binaire principal
    Resources/
      icon.icns         # Icône de l'application
```

Le `Info.plist` définit :
- `CFBundleIdentifier` : com.openflow.notify (ou équivalent)
- `CFBundleName` : OpenFlow
- Application en mode "agent" (pas de Dock icon au lancement)

### 3. Apparence de la notification

```
+---------------------------------------+
| [Icône OpenFlow]                      |
| Agent Executeur              subtitle |
| ✅ Validation requise          title  |
| Tache terminée avec succès   message  |
+---------------------------------------+
```

- L'icône OpenFlow est visible
- Dans Préférences Système > Notifications, l'app apparaît comme "OpenFlow"
- Le clic sur la notification ne lance rien

### 4. Intégration avec le serveur MCP Python

Le notifier Python détecte si le binaire Go est disponible :
- Si `openflow-notify` est trouvé dans le bundle .app, l'utiliser
- Sinon, fallback vers PyObjC ou osascript

### 5. Compatibilité multi-plateforme

- **macOS** : Utilise le binaire Go avec bundle .app
- **Linux** : Continue d'utiliser `notify-send` (Go peut être ajouté plus tard)
- **Windows** : Continue d'utiliser PowerShell toast (Go peut être ajouté plus tard)

### 6. Installation

Le bundle .app doit être installé dans un emplacement accessible :
- Option 1 : Dans le dossier du projet (`servers/notify/OpenFlow.app/`)
- Option 2 : Dans `/Applications/` ou `~/Applications/`
- Option 3 : Build à la volée via script d'installation

## Sous-tâches

- **2.1** - Créer le projet Go avec structure de base
- **2.2** - Implémenter l'envoi de notification via APIs Cocoa (macdriver ou CGo)
- **2.3** - Ajouter le support des paramètres CLI (title, message, type, sound, agent, task)
- **2.4** - Créer le bundle .app avec Info.plist et icône
- **2.5** - Désactiver le comportement au clic (notification passive)
- **2.6** - Modifier le notifier Python pour appeler le binaire Go si disponible
- **2.7** - Créer le script de build/installation
- **2.8** - Tester l'apparence dans Préférences Système > Notifications

## Priorité des sous-tâches

| Priorité | Sous-tâche | Dépendances |
|----------|------------|-------------|
| 1 | 2.1 - Projet Go de base | Aucune |
| 2 | 2.2 - APIs Cocoa | 2.1 |
| 3 | 2.3 - Paramètres CLI | 2.2 |
| 4 | 2.5 - Désactiver clic | 2.2 |
| 5 | 2.4 - Bundle .app | 2.3 |
| 6 | 2.8 - Test Préférences | 2.4 |
| 7 | 2.6 - Intégration Python | 2.4 |
| 8 | 2.7 - Script build | 2.4 |

## Ressources techniques

### Bibliothèques Go pour macOS

1. **progrium/macdriver** : Bindings Go pour APIs Apple, approche recommandée
2. **caseymrm/menuet** : Inclut support notifications, plus haut niveau
3. **CGo direct** : Plus de contrôle, mais plus complexe

### API moderne : UNUserNotificationCenter

L'API `UNUserNotificationCenter` (disponible depuis macOS 10.14) est préférable à `NSUserNotification` :
- API moderne et maintenue par Apple
- Meilleur contrôle sur le comportement au clic
- Support des actions et catégories

## Checklist de validation

### Binaire Go
- [ ] Le binaire `openflow-notify` se compile sans erreur
- [ ] Il accepte les paramètres `--title` et `--message`
- [ ] Il supporte les paramètres optionnels `--type`, `--sound`, `--agent`, `--task`
- [ ] Une notification s'affiche correctement sur macOS

### Bundle .app
- [ ] Le bundle est créé avec la bonne structure
- [ ] L'icône est visible dans la notification
- [ ] L'application apparaît comme "OpenFlow" dans Préférences Système > Notifications
- [ ] L'application ne montre pas d'icône dans le Dock au lancement

### Comportement
- [ ] Le clic sur la notification ne lance aucune application
- [ ] Le son est joué selon le paramètre
- [ ] Le subtitle affiche l'agent si fourni
- [ ] Le message inclut la tâche si fournie
- [ ] Les emojis s'affichent correctement selon le type

### Intégration
- [ ] Le notifier Python détecte et utilise le binaire Go
- [ ] Fallback vers PyObjC/osascript si binaire absent
- [ ] Linux continue de fonctionner avec notify-send
- [ ] Windows continue de fonctionner avec PowerShell

### Installation
- [ ] Le script de build génère le bundle .app
- [ ] Le script d'installation place le bundle au bon endroit
- [ ] Documentation d'installation mise à jour
