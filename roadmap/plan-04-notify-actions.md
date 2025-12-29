# Plan 04 - Actions interactives dans les notifications

**Date** : 2025-12-28  
**Branche** : `feature/notify-actions`

## Contexte

Actuellement, l'outil `ask_user` envoie une notification qui affiche une question, mais :

1. **Pas de reponse directe** : L'utilisateur doit revenir dans le terminal pour repondre
2. **Friction dans le workflow** : Le changement de contexte interrompt la concentration
3. **Options non cliquables** : Les options sont affichees en texte mais pas interactives

L'objectif est de transformer les notifications en veritables dialogues interactifs ou l'utilisateur peut repondre directement depuis la notification.

## Objectif

Ameliorer l'outil `ask_user` pour permettre a l'utilisateur de repondre directement via des boutons dans la notification macOS, et recuperer cette reponse dans le flux MCP.

## Contraintes techniques

### Limitation macOS

Sur macOS, les notifications avec actions (boutons) ont des contraintes :

1. **`NSUserNotification` (deprecated)** : Supporte `actionButtonTitle` (un seul bouton) + bouton "Fermer"
2. **`UNUserNotificationCenter` (moderne)** : Supporte plusieurs actions, mais necessite un bundle .app avec permissions
3. **Delegate pattern** : Pour capturer le clic, il faut un delegate qui reste actif

### Approche recommandee

Utiliser `NSUserNotification` avec :
- Un bouton d'action principal (ex: "Oui" ou "Valider")
- Le bouton "Fermer" comme reponse negative implicite
- Un delegate pour capturer la reponse

Pour les questions avec plus de 2 options, fallback vers une approche alternative (voir ci-dessous).

## Comportement attendu

### 1. Notifications binaires (Oui/Non)

Pour les questions simples a deux choix :

```
+-----------------------------------------------+
| [Icone OpenFlow]                              |
| open-flow @ feature/x                subtitle |
| Decision requise                        title |
| Voulez-vous merger sur main ?         message |
|                                               |
|              [Fermer]  [Oui, merger]  buttons |
+-----------------------------------------------+
```

- **Bouton d'action** : Premiere option positive (ex: "Oui", "Valider", "Continuer")
- **Bouton Fermer** : Interprete comme reponse negative ou annulation

### 2. Capture de la reponse

Quand l'utilisateur clique :
- **Bouton d'action** : L'outil retourne `{"response": "accepted", "choice": "Oui, merger"}`
- **Bouton Fermer** : L'outil retourne `{"response": "dismissed", "choice": null}`
- **Notification expiree** : L'outil retourne `{"response": "timeout", "choice": null}`

### 3. Questions a choix multiples (3+ options)

Pour les questions avec plus de 2 options, deux approches possibles :

#### Option A : Notification + prompt terminal
La notification alerte l'utilisateur, qui repond ensuite dans le terminal.
- Simple a implementer
- Coherent avec le comportement actuel

#### Option B : Fenetre de dialogue native
Afficher une vraie boite de dialogue macOS avec tous les boutons.
- Meilleure UX
- Plus complexe (necessite PyObjC NSAlert)

**Recommandation** : Commencer par Option A, ajouter Option B plus tard si necessaire.

### 4. Timeout et comportement asynchrone

Le probleme principal : MCP est synchrone, mais attendre une reponse utilisateur peut prendre du temps.

Solutions possibles :

| Approche | Description | Avantage | Inconvenient |
|----------|-------------|----------|--------------|
| **Timeout court** | Attendre 30-60s max, puis timeout | Simple | Peut manquer la reponse |
| **Polling** | L'agent rappelle periodiquement pour verifier | Flexible | Complexe cote agent |
| **Webhook/callback** | Notification declenche un callback | Temps reel | Necessite serveur HTTP |

**Recommandation** : Timeout de 60 secondes avec message clair si expire.

### 5. Nouveau schema de l'outil

L'outil `ask_user` evolue avec :

| Parametre | Type | Description |
|-----------|------|-------------|
| `action_label` | string | Texte du bouton d'action (defaut: "OK") |
| `wait_for_response` | boolean | Attendre la reponse utilisateur (defaut: false) |
| `timeout` | number | Timeout en secondes si wait_for_response=true (defaut: 60) |

### 6. Comportement selon `wait_for_response`

#### `wait_for_response: false` (defaut, comportement actuel)
- Envoie la notification et retourne immediatement
- Retour : `{"sent": true, "message": "Question envoyee"}`

#### `wait_for_response: true`
- Envoie la notification et attend la reponse
- Bloque jusqu'au clic ou timeout
- Retour : `{"response": "accepted|dismissed|timeout", "choice": "..."}`

### 7. Implementation du delegate

Pour capturer les clics, il faut :

1. Creer une classe delegate `NSUserNotificationCenterDelegate`
2. Implementer `userNotificationCenter:didActivateNotification:`
3. Garder une reference au delegate pendant l'attente
4. Utiliser un mecanisme de synchronisation (Event, Queue) pour communiquer la reponse

### 8. Compatibilite multi-plateforme

| Plateforme | Comportement |
|------------|--------------|
| **macOS** | Boutons natifs via NSUserNotification |
| **Linux** | `notify-send` avec actions (si supporte par le DE) |
| **Windows** | Toast avec boutons via XML template |

Les actions sur Linux/Windows sont un "nice to have" - le fallback reste la notification simple.

## Sous-taches

- **4.1** - Implementer le delegate NSUserNotificationCenter pour capturer les clics
- **4.2** - Ajouter le parametre `action_label` pour personnaliser le bouton
- **4.3** - Ajouter le parametre `wait_for_response` avec mecanisme d'attente
- **4.4** - Implementer le timeout avec retour structure
- **4.5** - Mettre a jour le schema MCP avec les nouveaux parametres
- **4.6** - Gerer le cas des questions a 2 options (mapping sur action/fermer)
- **4.7** - Documenter le nouveau comportement dans le skill `notify`
- **4.8** - Tester la compatibilite avec le workflow existant (wait_for_response: false)

## Priorite des sous-taches

| Priorite | Sous-tache | Dependances |
|----------|------------|-------------|
| 1 | 4.1 - Delegate NSUserNotificationCenter | Aucune |
| 2 | 4.3 - wait_for_response + attente | 4.1 |
| 3 | 4.4 - Timeout | 4.3 |
| 4 | 4.2 - action_label | 4.1 |
| 5 | 4.6 - Questions 2 options | 4.2 |
| 6 | 4.5 - Schema MCP | 4.2, 4.3 |
| 7 | 4.8 - Tests compatibilite | 4.5 |
| 8 | 4.7 - Documentation skill | 4.5 |

## Risques et mitigation

| Risque | Impact | Mitigation |
|--------|--------|------------|
| Delegate non appele (app en background) | Reponse jamais recue | Timeout obligatoire |
| NSUserNotification deprecated | Futur macOS pourrait le supprimer | Prevoir migration vers UNUserNotificationCenter |
| Blocage MCP pendant l'attente | Agent bloque | Timeout raisonnable (60s) |
| Utilisateur absent | Timeout systematique | Message clair + option de re-notification |

## Checklist de validation

### Notification avec action
- [ ] Un bouton d'action apparait sur la notification macOS
- [ ] Le texte du bouton correspond a `action_label`
- [ ] Le bouton "Fermer" est present

### Capture de reponse
- [ ] Clic sur le bouton d'action retourne `response: accepted`
- [ ] Clic sur Fermer retourne `response: dismissed`
- [ ] Expiration du timeout retourne `response: timeout`

### Mode synchrone
- [ ] `wait_for_response: true` bloque jusqu'a la reponse
- [ ] Le timeout fonctionne correctement (60s par defaut)
- [ ] La reponse est correctement retournee au client MCP

### Compatibilite
- [ ] `wait_for_response: false` (defaut) fonctionne comme avant
- [ ] Les agents existants ne sont pas impactes
- [ ] Linux/Windows continuent de fonctionner (sans actions)

### Questions a 2 options
- [ ] `options: ["Oui", "Non"]` mappe correctement sur action/fermer
- [ ] Le bouton d'action affiche la premiere option
- [ ] Le retour inclut le choix textuel

### Edge cases
- [ ] Plusieurs notifications en attente sont gerees correctement
- [ ] Fermeture de la notification via swipe = dismissed
- [ ] Notification dans le centre de notifications (pas juste banner)
