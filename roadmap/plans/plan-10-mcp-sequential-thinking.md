# Plan 10 - Integration du serveur MCP Sequential Thinking

## Contexte

Les agents Claude dans OpenCode abordent parfois des taches complexes de maniere trop lineaire, sans prendre le temps de decomposer le probleme, generer des hypotheses alternatives, ou reviser leur approche en cours de route.

Le projet officiel **Sequential Thinking** de ModelContextProtocol (MIT License) fournit un outil MCP qui facilite une pensee structuree et reflexive :
- Decomposition en etapes numerotees
- Revision et raffinement dynamique des pensees
- Ramification vers des chemins de pensee alternatifs
- Ajustement du nombre d'etapes selon la complexite
- Generation et verification d'hypotheses

Repository : https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking

## Objectif

Integrer le serveur MCP Sequential Thinking dans OpenFlow pour permettre aux agents Claude d'adopter une approche de reflexion structuree sur les taches complexes, ameliorant ainsi la qualite des decisions et la decomposition des problemes.

## Comportement attendu

### Installation

L'utilisateur execute `./install.sh` (ou `./install.sh mcp`) :
1. Le script verifie que Node.js >= 18 est installe
2. Si Node.js n'est pas disponible ou version insuffisante, un warning est affiche et sequential-thinking est ignore
3. Si Node.js est OK, le script configure sequential-thinking dans `opencode.json`
4. L'utilisateur voit "Configured MCP: sequential-thinking" dans le resume d'installation

### Configuration MCP

Le serveur est configure via npx (pas d'installation locale requise) :

```json
{
  "mcpServers": {
    "sequential-thinking": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-sequential-thinking"]
    }
  }
}
```

### Outil fourni

| Outil | Description |
|-------|-------------|
| `sequential_thinking` | Facilite un processus de pensee structure, etape par etape, avec revision dynamique |

### Parametres de l'outil

L'outil `sequential_thinking` accepte :
- `thought` : La pensee ou etape de raisonnement actuelle
- `nextThoughtNeeded` : Booleen indiquant si d'autres etapes sont necessaires
- `thoughtNumber` : Numero de l'etape actuelle
- `totalThoughts` : Nombre total d'etapes estimees (ajustable)
- `isRevision` : Indique si cette pensee revise une precedente
- `revisesThought` : Numero de la pensee revisee (si applicable)
- `branchFromThought` : Numero de la pensee d'ou part une branche alternative
- `branchId` : Identifiant de la branche de pensee

### Utilisation par les agents

Les agents Coordinateur et Executeur utiliseront cet outil en debut de tache complexe pour :
1. Decomposer le probleme en etapes logiques
2. Identifier les risques et alternatives
3. Valider leur approche avant de commencer l'implementation

### Modification des agents

#### coordinateur.md / coordinator.md
Ajouter une section recommandant l'utilisation de `sequential_thinking` pour :
- L'analyse initiale d'une demande utilisateur complexe
- La planification de taches multi-etapes
- L'evaluation des risques et alternatives

#### executeur.md / executor.md
Ajouter une section recommandant l'utilisation de `sequential_thinking` pour :
- La comprehension d'une tache complexe avant implementation
- La decomposition technique d'une feature
- L'analyse d'un bug difficile a reproduire

### Prerequis utilisateur

- Node.js >= 18 installe sur la machine

---

## Workflow Branche RC (Release Candidate)

En plus de l'integration Sequential Thinking, ajouter le workflow RC pour la validation multi-features.

### Contexte

Quand N plans s'executent en parallele sur N worktrees, la validation interactive devient complexe. Solution : branche RC temporaire.

### Workflow

```
feature/plan-A ──┐
feature/plan-B ──┼──► rc/test-YYYY-MM-DD ──► Tests integres
feature/plan-C ──┘         │
                           │ Si bug dans plan-B
                           ▼
                    Corriger sur feature/plan-B
                           │
                           ▼
                    Re-merger dans RC
                           │
                           ▼
                    Re-tester
                           │
                           ▼ Validation OK
                    Supprimer RC
                           │
                           ▼
                    Merger features → main
```

### Regles

1. **Creer RC** : `git checkout -b rc/test-$(date +%Y%m%d)` depuis main
2. **Merger features** : `git merge feature/plan-X` pour chaque feature
3. **Tester** : Redemarrer app, etablir plan de test complet
4. **Corriger** : Toujours sur branche originale, jamais sur RC
5. **Re-merger** : Apres correction, re-merger dans RC
6. **Finaliser** : Supprimer RC, merger features individuellement sur main

### Modifications agents/skills

#### coordinateur.md / coordinator.md
- Ajouter Phase 6.5 : "Branche RC" entre collecte rapports et validation
- Documenter commandes git pour RC

#### swarm-orchestration/SKILL.md
- Ajouter section "Validation Multi-Features avec RC"

#### interactive-validation/SKILL.md
- Ajouter section "Mode Multi-Features"

## Checklist de validation

### MCP Sequential Thinking
- [ ] Dossier `servers/sequential-thinking/` cree avec README.md et configure.py
- [ ] `install.sh` modifie pour gerer sequential-thinking (verification Node.js, appel configure.py)
- [ ] Configuration ajoutee correctement dans `opencode.json` apres installation
- [ ] Warning clair si Node.js < 18 ou absent
- [ ] Claude peut utiliser `sequential_thinking` pour decomposer un probleme

### Agents - Sequential Thinking
- [ ] Agent coordinateur.md (fr) : recommandation `sequential_thinking` en debut de tache
- [ ] Agent coordinator.md (en) : recommandation `sequential_thinking` en debut de tache
- [ ] Agent executeur.md (fr) : recommandation `sequential_thinking` en debut de tache
- [ ] Agent executor.md (en) : recommandation `sequential_thinking` en debut de tache

### Agents - Workflow RC
- [ ] Agent coordinateur.md (fr) : workflow RC pour validation multi-features
- [ ] Agent coordinator.md (en) : workflow RC pour validation multi-features

### Skills
- [ ] swarm-orchestration/SKILL.md (fr) : section RC
- [ ] swarm-orchestration/SKILL.md (en) : section RC
- [ ] interactive-validation/SKILL.md (fr) : mode multi-features
- [ ] interactive-validation/SKILL.md (en) : mode multi-features

### Documentation
- [ ] Documentation dans `servers/sequential-thinking/README.md` complete
