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

Permet de reprendre la session plus tard sans perdre le contexte, meme apres plusieurs sessions de debugging.

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
3. Remplir le template avec l'etat actuel
4. Informer l'utilisateur : "Snapshot cree : [chemin]"

### Contenu a sauvegarder

| Element | Description |
|---------|-------------|
| Contexte | Plans en cours, phase actuelle, objectif |
| Todos | Copie complete de l'etat des todos |
| Branches | Liste des branches avec leur statut |
| Rapports | Rapports consolides des executeurs |
| Problemes | Liste des problemes identifies |
| Prochaines actions | Ce qui reste a faire |

---

## Template Snapshot

```markdown
# Session Snapshot

**Date** : [YYYY-MM-DD HH:MM]
**Contexte** : [Description courte]

---

## Etat General

- **Plans en cours** : [liste]
- **Phase actuelle** : [N] - [Nom]
- **Objectif** : [description]

---

## Todos

```
[Copie complete des todos actuels avec statuts]
- [x] Todo 1 (completed)
- [ ] Todo 2 (in_progress)
- [ ] Todo 3 (pending)
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
4. Recreer les todos selon l'etat sauvegarde
5. Presenter le contexte a l'utilisateur
6. Reprendre la Phase 6

### Commandes utilisateur

| Demande | Action |
|---------|--------|
| "recharge la session" | Lister snapshots, charger le plus recent |
| "charge le snapshot X" | Charger un snapshot specifique |
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
