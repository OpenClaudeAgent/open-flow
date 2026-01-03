# Skill : Session Snapshot

Sauvegarde et rechargement de l'etat d'une session pour le debugging complexe.

---

## Concept

Avant une phase de debugging potentiellement longue, sauvegarder l'etat complet de la session :
- Etat des todos
- Plans en cours
- Rapports consolides
- Branches creees
- Problemes identifies
- **Todo complet de debugging** (nouveau)

Permet de reprendre la session plus tard sans perdre le contexte, meme apres plusieurs sessions de debugging.

---

## Workflow des Todos

### 1. Todo Complet (dans le snapshot)

Quand on cree un snapshot, generer un **todo complet contextuel** :

```
## Todos de Debugging

- [ ] Analyser le probleme : [description]
- [ ] Identifier la cause dans [fichiers]
- [ ] Appliquer la correction
- [ ] Reinvoquer Executeur si necessaire
- [ ] Retester le comportement
- [ ] Valider avec l'utilisateur
- [ ] ★ Recharger la session pour continuer (snapshot-XXX.md) ★
```

Le dernier item est **toujours** "Recharger la session" - c'est le point de reprise.

### 2. Todo Intermediaire (pendant debugging)

Quand on passe en debugging, creer un **todo leger** qui reference le snapshot :

```
- [ ] Debug en cours → voir .session/snapshot-XXX.md pour contexte complet
- [ ] [Item specifique au probleme actuel]
- [ ] [Item specifique 2]
```

Ce todo est leger et focuse sur l'action immediate.

### 3. Reprise (rechargement)

Quand on recharge une session :
1. Lire le snapshot
2. Extraire la section "Todos de Debugging"
3. Recreer les todos avec les statuts sauvegardes
4. Reprendre le workflow

---

## Structure

```
.session/
└── snapshot-YYYY-MM-DD-contexte.md
```

---

## Declenchement

Le Coordinateur **propose** avant la Phase 6 (Validation Interactive) :

```
ask_user(
  title: "Session Snapshot"
  question: "Veux-tu sauvegarder un snapshot de la session avant le debugging ?"
  options: ["Oui, creer snapshot", "Non, continuer"]
)
```

C'est toujours l'utilisateur qui decide. Le Coordinateur ne cree jamais de snapshot automatiquement.

---

## Creation d'un snapshot

### Workflow

1. Creer le dossier `.session/` si necessaire
2. Generer le nom : `snapshot-[YYYY-MM-DD]-[contexte].md`
3. **Analyser le contexte pour generer le Todo de Debugging**
4. Remplir le template avec l'etat actuel + todos de debugging
5. **Creer le Todo Intermediaire** (pendant le debugging)
6. Informer l'utilisateur : "Snapshot cree : [chemin]"

### Contenu a sauvegarder

| Element | Description |
|---------|-------------|
| Contexte | Plans en cours, phase actuelle, objectif |
| Todos Originaux | Copie complete de l'etat des todos actuels |
| **Todos de Debugging** | Todo complet genere pour le debugging (nouveau) |
| Branches | Liste des branches avec leur statut |
| Rapports | Rapports consolides des executeurs |
| Problemes | Liste des problemes identifies |
| Prochaines actions | Ce qui reste a faire |

### Generation du Todo de Debugging

Analyser le contexte (problemes detectes, rapports) pour generer un todo adapte :

```
Exemple pour un bug UI :
- [ ] Analyser le bug : bouton non cliquable dans SettingsPage
- [ ] Identifier le composant QML concerne
- [ ] Verifier les signaux/slots
- [ ] Appliquer la correction
- [ ] Tester manuellement
- [ ] Reinvoquer Tester pour tests automatises
- [ ] ★ Recharger session pour continuer ★
```

Le todo est **contextuel** - adapte au probleme specifique.

---

## Template Snapshot

```markdown
# Session Snapshot

**Date** : [YYYY-MM-DD HH:MM]
**Contexte** : [Description courte]
**Fichier** : .session/snapshot-[YYYY-MM-DD]-[contexte].md

---

## Etat General

- **Plans en cours** : [liste]
- **Phase actuelle** : [N] - [Nom]
- **Objectif** : [description]

---

## Todos Originaux

[Copie des todos au moment du snapshot]
- [x] Todo 1 (completed)
- [ ] Todo 2 (in_progress)
- [ ] Todo 3 (pending)

---

## Todos de Debugging

[Todo complet genere pour le debugging - A RECREER lors du rechargement]

| ID | Tache | Statut | Priorite |
|----|-------|--------|----------|
| D1 | Analyser le probleme : [description] | pending | high |
| D2 | Identifier la cause dans [fichiers] | pending | high |
| D3 | Appliquer la correction | pending | high |
| D4 | Reinvoquer Executeur si necessaire | pending | medium |
| D5 | Retester le comportement | pending | high |
| D6 | Valider avec l'utilisateur | pending | high |
| D7 | ★ Recharger session pour continuer ★ | pending | low |

**Note** : D7 est le point de reprise si la session est interrompue.
```

---

## Branches

| Branche | Plan | Statut | Notes |
|---------|------|--------|-------|
| `feature/xxx` | Plan XX | En cours | [notes] |
| `feature/yyy` | Plan YY | Pret merge | [notes] |

---

## Rapports Consolides

### Plan XX - [Nom]

[Rapport complet de l'executeur]

#### Problemes detectes
- [x] Probleme 1 (resolu)
- [ ] Probleme 2 (en cours)

### Plan YY - [Nom]

[Rapport complet de l'executeur]

---

## Problemes Identifies

| # | Probleme | Severite | Statut | Notes |
|---|----------|----------|--------|-------|
| 1 | [description] | Haute | En cours | [notes] |
| 2 | [description] | Moyenne | A faire | [notes] |

---

## Prochaines Actions

1. [ ] [Action 1]
2. [ ] [Action 2]
3. [ ] [Action 3]

---

## Notes de Debug

[Section a remplir pendant le debugging]

### Session 1 - [Date]
- [Notes]

### Session 2 - [Date]
- [Notes]

---

## Reprise

Pour reprendre cette session :
1. Lire ce fichier
2. Recreer les todos
3. Reprendre le contexte
4. Continuer la Phase 6
```

---

## Rechargement

Quand l'utilisateur demande de recharger une session :

### Workflow

1. Lister les snapshots dans `.session/`
2. Si plusieurs, demander lequel charger
3. Lire le fichier snapshot
4. **Extraire la section "Todos de Debugging"**
5. **Recreer les todos avec TodoWrite** (utiliser les statuts sauvegardes)
6. Presenter le contexte a l'utilisateur
7. Reprendre la Phase 6

### Recreation des Todos

Lors du rechargement, recreer les todos depuis la table "Todos de Debugging" :

```python
# Exemple de recreation
todos = [
    {"id": "D1", "content": "Analyser le probleme : [description]", "status": "completed", "priority": "high"},
    {"id": "D2", "content": "Identifier la cause dans [fichiers]", "status": "in_progress", "priority": "high"},
    {"id": "D3", "content": "Appliquer la correction", "status": "pending", "priority": "high"},
    # ... etc
]
TodoWrite(todos)
```

### Commandes utilisateur

| Demande | Action |
|---------|--------|
| "recharge la session" | Lister snapshots, charger le plus recent, recreer todos |
| "charge le snapshot X" | Charger un snapshot specifique, recreer todos |
| "liste les sessions" | Afficher les snapshots disponibles |

---

## Rappel au demarrage

Si `.session/` contient des snapshots :

```
Note: Des snapshots de session existent dans .session/
- snapshot-2025-01-03-plan-15.md (il y a 2h)
- snapshot-2025-01-02-plan-12.md (hier)

Utilise "recharge la session" pour reprendre.
```

---

## Finalisation

Quand le debugging est termine et la session complete :

1. L'utilisateur peut supprimer le snapshot manuellement
2. Ou le garder comme historique
3. Le Coordinateur ne supprime jamais les snapshots automatiquement

---

## Bonnes pratiques

1. **Un snapshot par phase de debugging** : Ne pas accumuler trop de snapshots
2. **Contexte clair** : Utiliser un nom descriptif (ex: `snapshot-2025-01-03-cache-invalidation.md`)
3. **Notes de debug** : Remplir la section pendant le debugging
4. **Nettoyer** : Supprimer les vieux snapshots quand ils ne sont plus utiles
