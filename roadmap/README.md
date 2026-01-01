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
| 3 | Outil MCP screenshot | [plan-03](./plan-03-mcp-screenshot.md) | `feature/mcp-screenshot` | v0.4.0 | Termine |
| 4 | Actions interactives dans les notifications | [plan-04](./plan-04-notify-actions.md) | `feature/notify-actions` | - | En attente |
| 5 | Internationalisation du repo | [plan-05](./plan-05-i18n.md) | `feature/i18n` | v0.3.0 | Termine |
| 6 | Analytics OpenFlow | [plan-06](./plan-06-analytics.md) | - | - | Abandonne |
| 7 | Serveur MCP OpenCode Session History | [plan-07](./plan-07-mcp-session-history.md) | `feature/opencode-session-history` | - | En attente |
| 8 | Notifications Git Events | [plan-08](./plan-08-notify-git-events.md) | `feature/notify-git-events` | v0.5.0 | Termine |
| 9 | Integration MCP lsmcp (outils LSP) | [plan-09](./plan-09-mcp-lsmcp.md) | `feature/mcp-lsmcp` | v0.6.0 | Termine |
| 10 | MCP Sequential Thinking + Workflow RC | [plan-10](./plan-10-mcp-sequential-thinking.md) | `main` | v0.6.0 | Termine |
| 11 | Support C/C++ dans lsmcp | [plan-11](./plan-11-lsmcp-cpp.md) | `feature/lsmcp-cpp` | v0.7.0 | Termine |
| 12 | Agent Maintainer (surveillance projet) | [plan-12](./plan-12-agent-maintainer.md) | `feature/agent-maintainer` | v0.8.0 | Termine |

## Historique

- **2025-12-31** : Tache 12 terminee - Agent Maintainer (surveillance et sante du projet) v0.8.0
- **2025-12-31** : Creation du plan 12 - Agent Maintainer (surveillance et sante du projet)
- **2025-12-31** : Tache 11 terminee - Support C/C++ dans lsmcp (clangd via --bin) v0.7.0
- **2025-12-31** : Creation du plan 11 - Support C/C++ dans lsmcp (preset clangd)
- **2025-12-31** : Tache 09 terminee - Integration MCP lsmcp (outils LSP) v0.6.0
- **2025-12-31** : Tache 10 terminee - MCP Sequential Thinking + Workflow RC v0.6.0
- **2025-12-31** : Creation du plan 10 - MCP Sequential Thinking (pensee structuree pour taches complexes)
- **2025-12-31** : Creation du plan 09 - Integration MCP lsmcp (outils LSP via serveur MIT existant)
- **2025-12-30** : Tache 08 terminee - Notifications Git Events (notify_commit, notify_merge, notify_sync) v0.5.0
- **2025-12-30** : Creation du plan 08 - Notifications Git Events (notify_commit, notify_merge, notify_sync)
- **2025-12-30** : Creation du plan 07 - Serveur MCP OpenCode Session History (recherche historique persistent)
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
