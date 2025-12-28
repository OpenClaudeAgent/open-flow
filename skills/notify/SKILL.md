# Skill: Notifications Utilisateur

Ce skill decrit quand et comment utiliser le serveur MCP `notify` pour communiquer avec l'utilisateur.

## Principe

L'utilisateur n'est pas toujours devant son ecran. Quand tu as besoin de son attention, **envoie une notification systeme** via MCP `notify`.

## Quand notifier

### Toujours notifier

| Situation | Type | Titre | Message |
|-----------|------|-------|---------|
| Tache terminee | `success` | Tache terminee | [Nom] - Pret pour review |
| Validation requise | `info` | Validation requise | [Contexte] - Action attendue |
| Decision necessaire | `warning` | Decision requise | [Question courte] |
| Erreur bloquante | `error` | Erreur | [Description courte] |
| Attente utilisateur | `info` | En attente | [Ce qui est attendu] |

### Ne pas notifier

- Progression intermediaire (utilise les todos)
- Messages informatifs non-bloquants
- Confirmations de commandes simples

## Comment notifier

```
Utilise l'outil MCP "notify" avec :
- title: Titre court (max 50 caracteres)
- message: Description claire de l'action attendue
- type: info | success | warning | error
- sound: true (par defaut)
```

## Types de notification

| Type | Usage | Exemple |
|------|-------|---------|
| `info` | Information, action requise | Tests prets, validation UI |
| `success` | Tache completee avec succes | Feature mergee, plan cree |
| `warning` | Attention requise, decision | Autorisation, conflit detecte |
| `error` | Probleme bloquant | Build echoue, erreur critique |

## Bonnes pratiques

1. **Sois concis** : L'utilisateur lit sur une petite notification
2. **Sois actionnable** : Dis ce qui est attendu
3. **Choisis le bon type** : Ca determine l'urgence percue
4. **Une notification par evenement** : Pas de spam

## Exemples

### Validation utilisateur requise
```
Type: info
Titre: "Validation requise"
Message: "Feature X - Application lancee, merci de tester"
```

### Tache terminee
```
Type: success
Titre: "Feature prete"
Message: "Login OAuth - Pret pour merge sur main"
```

### Autorisation necessaire
```
Type: warning
Titre: "Autorisation requise"
Message: "Code non testable - Refactoring necessaire ?"
```

### Erreur bloquante
```
Type: error
Titre: "Build echoue"
Message: "3 erreurs de compilation - Intervention requise"
```
