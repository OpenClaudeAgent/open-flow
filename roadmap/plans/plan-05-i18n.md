# Plan 05 - Internationalisation du repo

## Contexte

Le repo contient des agents, skills et documentation en français. Pour permettre une adoption plus large, le système d'installation doit supporter plusieurs langues.

## Objectif

Permettre d'installer les fichiers (agents, skills, règles, roadmap) dans différentes langues via un paramètre de l'installeur.

## Comportement attendu

### Structure des fichiers

Les fichiers sont organisés par langue dans des sous-dossiers :

```
agents/
  fr/
    executeur.md
    ...
  en/
    executor.md
    ...
skills/
  fr/
    agentic-flow/SKILL.md
    ...
  en/
    agentic-flow/SKILL.md
    ...
roadmap/
  fr/
    README.md
    plan-01-notify-pyobjc.md
    ...
  en/
    README.md
    ...
AGENTS.fr.md
AGENTS.en.md
```

### Installation

L'utilisateur lance l'installation avec un paramètre de langue :

```bash
./install.sh install --lang=fr   # Installe en français
./install.sh install --lang=en   # Installe en anglais
./install.sh install             # Langue par défaut (français)
```

### Fallback

- Langue par défaut : **français**
- Si un fichier n'existe pas dans la langue demandée, l'installeur utilise la version **anglaise**
- L'installeur affiche un warning quand il utilise le fallback

### Affichage

L'installeur indique la langue utilisée dans le résumé d'installation :

```
Language: fr (default)
```

ou

```
Language: en
  - executor.md (fallback: fr)
```

## Checklist de validation

- [x] Structure dossiers par langue créée
- [x] Fichiers existants migrés vers `fr/`
- [x] Paramètre `--lang` ou `-l` fonctionnel
- [x] Fallback français opérationnel
- [x] Warning affiché lors du fallback
- [x] Résumé d'installation indique la langue
