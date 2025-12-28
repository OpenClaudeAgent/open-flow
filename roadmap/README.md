# Roadmap Open-Flow

Ce dossier contient les plans d'implementation pour le projet open-flow.

## Methodologie

- Chaque plan est un fichier `plan-XX-nom.md` **immutable**
- Le suivi se fait uniquement via ce README
- L'implementation est faite par l'agent Executeur

## Suivi des taches

| # | Tache | Plan | Branche | Version | Statut |
|---|-------|------|---------|---------|--------|
| 1 | Notifications macOS natives avec PyObjC | [plan-01](./plan-01-notify-pyobjc.md) | `main` | v0.2.0 | Termine |
| 2 | Notifications macOS avec binaire Go natif | [plan-02](./plan-02-notify-go.md) | - | - | Annule |

## Historique

- **2025-12-28** : Plan 02 annule (necessite bundle ID pour icone custom)
- **2025-12-28** : Refonte MCP notify → ask_user (questions utilisateur uniquement)
- **2025-12-28** : Creation du plan 02 - Notifications macOS avec Go natif (remplace PyObjC)
- **2025-12-28** : Creation du plan 01 - Notifications macOS natives
