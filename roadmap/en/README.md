# Open-Flow Roadmap

This folder contains implementation plans for the open-flow project.

## Methodology

- Each plan is an **immutable** `plan-XX-name.md` file
- Tracking is done only via this README
- Implementation is done by the Executor agent

## Task Tracking

| # | Task | Plan | Branch | Version | Status |
|---|------|------|--------|---------|--------|
| 1 | Native macOS notifications with PyObjC | [plan-01](./plan-01-notify-pyobjc.md) | `main` | v0.2.0 | Done |
| 2 | macOS notifications with native Go binary | [plan-02](./plan-02-notify-go.md) | - | - | Cancelled |
| 3 | MCP screenshot tool | [plan-03](./plan-03-mcp-screenshot.md) | `feature/mcp-screenshot` | - | Pending |
| 4 | Interactive notification actions | [plan-04](./plan-04-notify-actions.md) | `feature/notify-actions` | - | Pending |
| 5 | Repository internationalization | [plan-05](./plan-05-i18n.md) | `feature/i18n` | v0.3.0 | Done |
| 6 | OpenFlow Analytics | [plan-06](./plan-06-analytics.md) | `feature/analytics` | - | Pending |

## History

- **2025-12-29**: Created plan 06 - OpenFlow Analytics
- **2025-12-29**: Task 05 completed - Multilingual installation (fr/en)
- **2025-12-29**: Created plan 05 - Repository internationalization
- **2025-12-28**: Created plan 04 - Interactive notification actions
- **2025-12-28**: Created plan 03 - MCP screenshot tool
- **2025-12-28**: Plan 02 cancelled (requires bundle ID for custom icon)
- **2025-12-28**: MCP notify refactored → ask_user (user questions only)
- **2025-12-28**: Created plan 02 - macOS notifications with native Go (replaces PyObjC)
- **2025-12-28**: Created plan 01 - Native macOS notifications
