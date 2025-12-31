# MCP Sequential Thinking

Server MCP pour la reflexion structuree et dynamique.

## Description

Utilise le package officiel `@modelcontextprotocol/server-sequential-thinking` (MIT License) pour faciliter une pensee en etapes :
- Decomposition en etapes numerotees
- Revision et raffinement dynamique
- Ramification vers des chemins alternatifs
- Ajustement du nombre d'etapes
- Generation et verification d'hypotheses

## Prerequis

- Node.js >= 18

## Installation

```bash
./install.sh mcp
```

Le script verifie Node.js et configure automatiquement via `npx`.

## Configuration

Ajoutee automatiquement dans `~/.config/opencode/opencode.json` :

```json
{
  "mcp": {
    "sequential-thinking": {
      "type": "local",
      "command": ["npx", "-y", "@modelcontextprotocol/server-sequential-thinking"],
      "enabled": true
    }
  }
}
```

## Outil fourni

| Outil | Description |
|-------|-------------|
| `sequential_thinking` | Pensee structuree etape par etape avec revision dynamique |

## Parametres

| Parametre | Type | Description |
|-----------|------|-------------|
| `thought` | string | Pensee ou etape actuelle |
| `nextThoughtNeeded` | boolean | D'autres etapes necessaires ? |
| `thoughtNumber` | number | Numero de l'etape actuelle |
| `totalThoughts` | number | Nombre total estime (ajustable) |
| `isRevision` | boolean | Revise une pensee precedente ? |
| `revisesThought` | number | Numero de la pensee revisee |
| `branchFromThought` | number | Point de branchement alternatif |
| `branchId` | string | Identifiant de la branche |

## Utilisation recommandee

**Coordinateur** : Analyse initiale de demandes complexes, planification multi-etapes, evaluation des risques.

**Executeur** : Comprehension de taches complexes, decomposition technique, analyse de bugs difficiles.

## Source

https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking
