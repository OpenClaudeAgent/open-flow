# Plan 14 - Base Class pour serveurs MCP

**Statut** : En attente  
**Phase** : Maintenance  
**Priorité** : P2  
**Date** : 2026-01-03  
**Branche** : `feature/mcp-base-class`

## Contexte

Les serveurs MCP `notify` et `screenshot` partagent une structure quasi-identique :

| Élément | notify/server.py | screenshot/server.py |
|---------|------------------|---------------------|
| `server = Server("name")` | ✓ | ✓ |
| `@server.list_tools()` | ✓ | ✓ |
| `@server.call_tool()` | ✓ | ✓ |
| `async def main()` | ✓ | ✓ |
| `def run()` | ✓ | ✓ |

**Problèmes** :
- Code boilerplate répété
- Pas de pattern unifié
- Difficile d'ajouter des fonctionnalités transversales (logging, métriques)

## Objectif

Créer une classe de base `BaseMCPServer` qui encapsule le pattern commun, permettant aux serveurs de se concentrer sur leur logique métier.

## Comportement attendu

### 1. Classe de base

```python
# servers/common/base_server.py
from abc import ABC, abstractmethod
from typing import Any
import asyncio

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import TextContent, Tool

class BaseMCPServer(ABC):
    """Base class for MCP servers."""
    
    def __init__(self, name: str):
        self.name = name
        self.server = Server(name)
        self._register_handlers()
    
    def _register_handlers(self) -> None:
        """Register MCP handlers."""
        @self.server.list_tools()
        async def list_tools() -> list[Tool]:
            return self.get_tools()
        
        @self.server.call_tool()
        async def call_tool(name: str, arguments: dict) -> list[TextContent]:
            return await self.handle_tool(name, arguments)
    
    @abstractmethod
    def get_tools(self) -> list[Tool]:
        """Return list of available tools."""
        pass
    
    @abstractmethod
    async def handle_tool(self, name: str, arguments: dict) -> list[TextContent]:
        """Handle tool invocation."""
        pass
    
    async def _main(self) -> None:
        """Main async entry point."""
        async with stdio_server() as (read_stream, write_stream):
            await self.server.run(
                read_stream,
                write_stream,
                self.server.create_initialization_options(),
            )
    
    def run(self) -> None:
        """Run the server."""
        asyncio.run(self._main())
```

### 2. Serveur notify simplifié

```python
# servers/notify/server.py
from servers.common.base_server import BaseMCPServer
from mcp.types import TextContent, Tool
from .notifier import Notifier

class NotifyServer(BaseMCPServer):
    def __init__(self):
        super().__init__("notify")
        self.notifier = Notifier()
    
    def get_tools(self) -> list[Tool]:
        return [
            Tool(
                name="notify",
                description="Send a system notification",
                inputSchema={...},
            ),
            Tool(
                name="ask_user",
                description="Ask user a question",
                inputSchema={...},
            ),
        ]
    
    async def handle_tool(self, name: str, arguments: dict) -> list[TextContent]:
        if name == "notify":
            result = self.notifier.send_notification(...)
        elif name == "ask_user":
            result = self.notifier.ask_user(...)
        return [TextContent(type="text", text=result)]

def run():
    NotifyServer().run()

if __name__ == "__main__":
    run()
```

### 3. Structure finale

```
servers/
├── common/
│   ├── __init__.py
│   ├── config.py           # MCPConfigurator (Plan 13)
│   └── base_server.py      # BaseMCPServer (ce plan)
├── notify/
│   └── server.py           # NotifyServer(BaseMCPServer)
└── screenshot/
    └── server.py           # ScreenshotServer(BaseMCPServer)
```

## Fichiers à modifier

| Fichier | Action |
|---------|--------|
| `servers/common/base_server.py` | Créer (nouveau) |
| `servers/notify/server.py` | Refactorer |
| `servers/screenshot/server.py` | Refactorer |

## Dépendances

- **Requiert** : Plan 13 (pour avoir `servers/common/` créé)

## Critères de validation

- [ ] `BaseMCPServer` implémenté
- [ ] `NotifyServer` hérite de `BaseMCPServer`
- [ ] `ScreenshotServer` hérite de `BaseMCPServer`
- [ ] Les deux serveurs fonctionnent identiquement
- [ ] Tests manuels : invoquer chaque outil MCP

## Estimation

- **Effort** : Faible (2-3h)
- **Risque** : Faible (refactoring interne)
- **Impact** : Faible (amélioration structure, pas de nouvelle fonctionnalité)

## Notes

Ce plan est optionnel. Le gain est principalement en termes de structure et de facilité pour ajouter de nouveaux serveurs MCP à l'avenir.
