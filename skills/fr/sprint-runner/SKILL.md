# Skill : Sprint Runner

Execution de sprints pour le Coordinateur. Ce skill permet de comprendre la structure roadmap et d'executer les sprints a la demande de l'utilisateur.

---

## Structure Roadmap

Quand un projet utilise le swarm orchestration, la roadmap suit cette structure :

```
roadmap/
├── README.md           # Suivi global des plans
├── SPRINTS.md          # Index des sprints (optionnel)
├── plans/              # Plans individuels
│   └── plan-XX-*.md
└── sprints/            # Details des sprints (optionnel)
    └── sprint-XX-*.md
```

---

## Commandes utilisateur

| Demande | Action |
|---------|--------|
| "Lance sprint N" | Workflow "Lance sprint" |
| "Fais plan N" | Lire `plans/plan-0N-*.md`, executer |
| "Statut sprint" | Lire `SPRINTS.md`, resumer |
| "Cree un sprint" | Workflow "Creation sprint" |
| "Plans du sprint N" | Lire sprint, lister les plans |
| "Prochaine etape" | Analyser avancement, proposer |

---

## Workflow "Lance sprint N"

1. **Lire le sprint**
   ```
   Lire sprints/sprint-0N-*.md
   Extraire la liste des plans references
   ```

2. **Demander a l'utilisateur**
   ```
   ask_user(
     title: "Sprint N - Selection des plans"
     question: "Quels plans veux-tu executer ?"
     options: [liste des plans du sprint]
   )
   ```

3. **Executer les plans selectionnes**
   - Suivre le workflow standard du Coordinateur
   - Invoquer Executeur pour chaque plan
   - Consolider les rapports

4. **Mettre a jour apres chaque merge**
   - Cocher le plan dans la checklist du sprint
   - Mettre a jour le statut dans README.md

5. **Verifier completion du sprint**
   - Si tous les plans sont termines → proposer passage au sprint suivant
   - Si sprint final termine → proposer nouveau cycle

---

## Workflow "Creation sprint"

Si l'utilisateur demande de creer un sprint :

```
ask_user(
  title: "Creation de sprint"
  question: "Veux-tu que j'invoque le Roadmapper pour creer ce sprint ?"
  options: ["Oui, invoquer Roadmapper", "Non, je le ferai moi-meme"]
)
```

Si oui :
1. Invoquer `/roadmap` avec le contexte de la demande
2. Le Roadmapper cree le fichier `sprints/sprint-XX-*.md`
3. Le Roadmapper met a jour `SPRINTS.md`

---

## Workflow "Statut sprint"

1. Lire `SPRINTS.md` pour la vue d'ensemble
2. Identifier le sprint actif (premier non termine)
3. Lire le fichier du sprint actif
4. Calculer la progression (X/Y plans termines)
5. Presenter un resume :

```
## Statut Sprint

**Sprint actif** : Sprint N - [Nom]
**Progression** : X/Y plans termines (Z%)

### Plans termines
- [x] Plan XX - [description]

### Plans restants
- [ ] Plan YY - [description]

### Prochaine action suggeree
[Plan suivant a executer]
```

---

## Apres execution

Apres chaque merge reussi :

1. **Cocher dans le sprint**
   - Ouvrir `sprints/sprint-XX-*.md`
   - Cocher `- [x] Plan YY` dans la checklist

2. **Mettre a jour README.md**
   - Changer le statut du plan : "En attente" → "Termine"
   - Ajouter la version si applicable

3. **Verifier le sprint**
   - Si tous les plans coches → sprint termine
   - Mettre a jour statut dans `SPRINTS.md`

4. **Proposer la suite**
   ```
   ask_user(
     title: "Sprint N termine"
     question: "Passer au Sprint N+1 ?"
     options: ["Oui", "Non, faire une pause"]
   )
   ```

---

## Gestion des erreurs

### Plan non trouve

```
Le plan XX n'existe pas dans plans/.
Verifier le numero ou creer le plan avec /roadmap.
```

### Sprint non trouve

```
Le sprint N n'existe pas dans sprints/.
Sprints disponibles : [liste]
```

### Sprint sans plans

```
Le sprint N ne contient aucun plan.
Ajouter des plans avec /roadmap.
```

---

## Bonnes pratiques

1. **Un sprint a la fois** : Terminer le sprint actuel avant de passer au suivant
2. **Plans dans l'ordre** : Respecter les priorites P0 > P1 > P2
3. **Validation apres chaque plan** : Ne pas enchainer sans validation utilisateur
4. **Mise a jour immediate** : Cocher les plans des qu'ils sont merges
5. **Communication claire** : Toujours informer l'utilisateur de l'etat du sprint
