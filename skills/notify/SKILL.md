# Skill: Questions Utilisateur (ask_user)

Ce skill decrit quand et comment utiliser le MCP `notify` (tool `ask_user`) pour poser des questions a l'utilisateur.

## Principe

Le tool `ask_user` sert a poser des questions a l'utilisateur quand tu as besoin d'une reponse pour continuer. Ce n'est PAS pour informer ou notifier - c'est pour DEMANDER.

## Restriction d'usage

**Tu ne dois utiliser ce tool QUE SI :**
1. L'utilisateur t'a explicitement demande de le notifier
2. Tes instructions d'agent specifient d'utiliser ce tool

**Tu ne dois PAS utiliser ce tool pour :**
- Informer de la completion d'une tache (utilise la conversation)
- Donner des mises a jour de progression (utilise les todos)
- Confirmer des actions simples (utilise la conversation)

## Quand utiliser ask_user

| Situation | Titre | Question | Options |
|-----------|-------|----------|---------|
| Besoin de validation | "Validation requise" | "[Contexte] - Peux-tu valider ?" | ["C'est bon", "Probleme"] |
| Besoin de decision | "Decision requise" | "[Question specifique]" | [choix possibles] |
| Besoin d'autorisation | "Autorisation requise" | "Puis-je [action] ?" | ["Oui", "Non"] |

## Parametres

| Parametre | Requis | Description |
|-----------|--------|-------------|
| `title` | Oui | Titre court (max 50 caracteres) |
| `question` | Oui | La question a poser |
| `options` | Non | Liste des reponses possibles |
| `urgency` | Non | low / normal / high |
| `repo` | Non | Nom du repository |
| `branch` | Non | Branche git actuelle |
| `agent` | Non | Nom de l'agent |
| `task` | Non | Tache en cours |

## Exemples

### Validation utilisateur requise
```
Titre: "Validation requise"
Question: "L'application est prete. Peux-tu tester la feature X ?"
Options: ["C'est bon", "Il y a un probleme"]
```

### Decision requise
```
Titre: "Decision requise"
Question: "Dois-je utiliser l'approche A ou B ?"
Options: ["Approche A", "Approche B", "Autre suggestion"]
```

### Autorisation requise
```
Titre: "Autorisation requise"
Question: "Code non testable - Puis-je invoquer l'agent refactoring ?"
Options: ["Oui", "Non"]
```

## Bonnes pratiques

1. **Sois concis** : Questions courtes et claires
2. **Propose des options** : Facilite la reponse de l'utilisateur
3. **Une question a la fois** : Pas de questions multiples
4. **Contexte minimal** : repo + branch suffisent generalement
