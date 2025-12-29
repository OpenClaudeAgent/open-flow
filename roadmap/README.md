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
| 3 | Outil MCP screenshot | [plan-03](./plan-03-mcp-screenshot.md) | `main` | v0.4.0 | Termine |
| 4 | Actions interactives dans les notifications | [plan-04](./plan-04-notify-actions.md) | `feature/notify-actions` | - | En attente |
| 5 | Internationalisation du repo | [plan-05](./plan-05-i18n.md) | `feature/i18n` | v0.3.0 | Termine |
| 6 | Analytics OpenFlow | [plan-06](./plan-06-analytics.md) | - | - | Abandonne |

## Historique

- **2025-12-29** : Tache 03 terminee - MCP screenshot (capture ecran/fenetre macOS) v0.4.0
- **2025-12-29** : Plan 06 abandonne - Hors scope, deplace vers [opencode-monitor](https://github.com/OpenClaudeAgent/opencode-monitor)
- **2025-12-29** : Creation du plan 06 - Analytics OpenFlow
- **2025-12-29** : Tache 05 terminee - Installation multilingue (fr/en)
- **2025-12-29** : Creation du plan 05 - Internationalisation du repo
- **2025-12-28** : Creation du plan 04 - Actions interactives dans les notifications
- **2025-12-28** : Creation du plan 03 - Outil MCP screenshot
- **2025-12-28** : Plan 02 annule (necessite bundle ID pour icone custom)
- **2025-12-28** : Refonte MCP notify → ask_user (questions utilisateur uniquement)
- **2025-12-28** : Creation du plan 02 - Notifications macOS avec Go natif (remplace PyObjC)
- **2025-12-28** : Creation du plan 01 - Notifications macOS natives
