---
name: interactive-validation
description: Validation interactive avec tests manuels et feedbacks utilisateur
---

# Validation Interactive - Skill

Processus de validation fonctionnelle avec l'utilisateur : tests manuels, feedbacks, itération.

## Quand utiliser Ask User

Utiliser Ask User (MCP Notify) pour interrompre l'utilisateur :
1. **Phase 5 (Coordinateur)** : Rapports reçus avec problèmes/questions
2. **Phase 6 (Coordinateur)** : Validation (app prête ? feedbacks ? validation finale ?)
3. **Phase 1 (Executeur)** : Si ambiguïté sur le plan (optionnel)

---

## Workflow (4 étapes)

### Étape 1 : Préparer App
- Lister fichiers modifiés + features ajoutées
- Demander : "Prêt à tester ?"

### Étape 2 : Tests Manuels
- Utilisateur teste l'app
- Rapporte problèmes, validations, feedbacks

### Étape 3 : Itération si Problèmes
- Demander corrections aux Executeurs
- Executeurs réinvoquent sous-agents
- Recevoir rapport révisé
- Retour à Étape 2 (re-test)

### Étape 4 : Validation Finale
- Demander confirmation finale
- Procéder Phase 7 (Merges)

---

## Étapes de Validation

- **Étape 1** : Ask User - "App prête, quels fichiers tester ?"
- **Étape 2** : Ask User - "Quels comportements échouent ?"
- **Étape 3** : Ask User - "Corrections reçues, re-test ?"
- **Étape 4** : Ask User - "Validation finale confirmée ?"

---

## Principes

- ✅ Ask User interrompt l'utilisateur (peut être déconnecté)
- ✅ Itérer jusqu'à validation OK
- ✅ Todos tracking progression en temps réel
- ✅ Executor corrige, Coordinateur orchestre
- ✅ Inclure commentaires importants intégralement  
