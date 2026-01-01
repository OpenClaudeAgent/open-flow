---
name: reporting-maintainer
description: Template rapport pour Maintainer - metriques, alertes, recommandations
---

# Reporting Template - Maintainer

Utilise ce template pour generer ton rapport de sante du projet.

## Rapport Maintainer - [TAG ou DATE]

### Resume Executif

| Indicateur | Valeur |
|------------|--------|
| Sante globale | [Bon / Attention / Critique] |
| Actions recommandees | [nombre] |
| Fichiers a surveiller | [nombre] |
| Alertes critiques | [nombre] |

### Metriques d'evolution

| Metrique | Actuel | Precedent | Variation |
|----------|--------|-----------|-----------|
| Total lignes | X | Y | +/-Z |
| Total fichiers | X | Y | +/-Z |
| Lignes ajoutees | X | - | - |
| Lignes supprimees | X | - | - |

### Alertes

#### Fichiers trop grands
| Fichier | Lignes | Severite |
|---------|--------|----------|
| `path/to/file.py` | 523 | CRITICAL |
| `path/to/other.ts` | 380 | WARNING |

#### TODO/FIXME
- TODO: [nombre] dans [X] fichiers
- FIXME: [nombre] dans [X] fichiers

### Recommandations

#### Priorite haute
1. [ ] [Action urgente]

#### Priorite moyenne
2. [ ] [Action recommandee]

#### Priorite basse
3. [ ] [Action optionnelle]

---

## Commandes utiles

```bash
# Compter lignes par extension
find . -name "*.py" -not -path "./node_modules/*" | xargs wc -l | tail -1

# Fichiers > 300 lignes
find . -name "*.py" -exec wc -l {} \; | awk '$1 > 300'

# TODO count
grep -rn "TODO" --include="*.py" | wc -l

# Git stats depuis tag
git diff --shortstat v0.7.0..HEAD
```

## Seuils de reference

| Metrique | OK | Warning | Critical |
|----------|----|---------|----------|
| Lignes/fichier | < 300 | 300-500 | > 500 |
| Fichiers/dossier | < 10 | 10-15 | > 15 |
| TODO total | < 10 | 10-20 | > 20 |
