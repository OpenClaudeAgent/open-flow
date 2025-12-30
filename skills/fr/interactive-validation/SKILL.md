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

### Étape 1 : Préparer pour Validation Utilisateur
- Lister fichiers modifiés + features ajoutées
- Fournir instructions de test claires
- **Ask User** : "Voici ce qui a été implémenté. Prêt à tester ?"

### Étape 2 : UTILISATEUR Teste (pas l'agent)
- **L'UTILISATEUR teste lui-même** (pas l'agent)
- Agent attend le feedback utilisateur
- **Ask User** : "Quels comportements fonctionnent ? Lesquels échouent ?"

> ⚠️ **IMPORTANT** : L'agent ne peut PAS valider à la place de l'utilisateur.
> Les tests manuels sont effectués par l'UTILISATEUR, pas simulés par l'agent.

### Étape 3 : Itération si Problèmes
- Utilisateur rapporte les problèmes
- Demander corrections aux Executeurs
- Executeurs corrigent + réinvoquent sous-agents
- Recevoir rapport révisé
- **Ask User** : "Corrections appliquées. Peux-tu re-tester ?"
- Retour à Étape 2

### Étape 4 : Validation Finale par Utilisateur
- **Ask User** : "Tout fonctionne ? Validation finale confirmée ?"
- Attendre confirmation explicite de l'utilisateur
- Procéder Phase 7 (Merges) uniquement après confirmation

---

## Étapes de Validation

- **Étape 1** : Ask User - "App prête, quels fichiers tester ?"
- **Étape 2** : Ask User - "Quels comportements échouent ?"
- **Étape 3** : Ask User - "Corrections reçues, re-test ?"
- **Étape 4** : Ask User - "Validation finale confirmée ?"

---

## Principes

- ✅ **UTILISATEUR valide** - L'agent ne peut PAS valider à sa place
- ✅ Ask User interrompt l'utilisateur (peut être déconnecté)
- ✅ Attendre feedback explicite avant de continuer
- ✅ Itérer jusqu'à validation OK de l'utilisateur
- ✅ Todos tracking progression en temps réel
- ✅ Executor corrige, Coordinateur orchestre
- ✅ Ne jamais marquer "tests manuels" comme terminés sans feedback utilisateur

## Anti-patterns à éviter

- ❌ Marquer les tests comme "passés" sans feedback utilisateur
- ❌ Simuler des tests manuels automatiquement
- ❌ Passer à l'étape suivante sans confirmation explicite
- ❌ Assumer que l'implémentation fonctionne sans validation  
