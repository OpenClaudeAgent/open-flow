# Plan 13 - Factoriser configure.py des serveurs MCP

**Statut** : En attente  
**Phase** : Maintenance  
**Priorité** : P1  
**Date** : 2026-01-03  
**Branche** : `feature/refactor-configure`

## Contexte

Les trois serveurs MCP (notify, screenshot, lsmcp) ont chacun leur propre fichier `configure.py` avec du code dupliqué :

| Fichier | Lignes | Code dupliqué |
|---------|--------|---------------|
| `servers/notify/configure.py` | 105 | ~60 lignes |
| `servers/screenshot/configure.py` | 77 | ~60 lignes |
| `servers/lsmcp/configure.py` | 218 | ~60 lignes |

**Code dupliqué identifié** :
- `get_opencode_config_path()` : Chemin vers `~/.config/opencode/opencode.json`
- `load_config()` : Lecture du fichier JSON
- `save_config()` : Écriture du fichier JSON
- Logique de base pour ajouter un serveur MCP

## Objectif

Créer un module partagé `servers/common/config.py` avec une classe `MCPConfigurator` qui factorise le code commun, puis refactorer les 3 fichiers `configure.py` pour l'utiliser.

## Comportement attendu

### 1. Nouveau module partagé

```python
# servers/common/config.py
from pathlib import Path
import json
from typing import Optional

class MCPConfigurator:
    """Base configurator for MCP servers."""
    
    def __init__(self, server_name: str):
        self.server_name = server_name
    
    @staticmethod
    def get_config_path() -> Path:
        """Get path to opencode config file."""
        return Path.home() / ".config" / "opencode" / "opencode.json"
    
    def load_config(self) -> dict:
        """Load config from JSON file."""
        path = self.get_config_path()
        if path.exists():
            with open(path, "r") as f:
                return json.load(f)
        return {}
    
    def save_config(self, config: dict) -> None:
        """Save config to JSON file."""
        path = self.get_config_path()
        path.parent.mkdir(parents=True, exist_ok=True)
        with open(path, "w") as f:
            json.dump(config, f, indent=2)
    
    def configure(
        self,
        command: list[str],
        env: Optional[dict[str, str]] = None,
        args: Optional[list[str]] = None,
    ) -> bool:
        """Add or update MCP server configuration."""
        config = self.load_config()
        
        if "mcpServers" not in config:
            config["mcpServers"] = {}
        
        server_config = {"command": command[0], "args": command[1:]}
        if env:
            server_config["env"] = env
        if args:
            server_config["args"].extend(args)
        
        config["mcpServers"][self.server_name] = server_config
        self.save_config(config)
        return True
    
    def is_configured(self) -> bool:
        """Check if server is already configured."""
        config = self.load_config()
        return self.server_name in config.get("mcpServers", {})
```

### 2. Refactoring des configure.py

Chaque `configure.py` devient simplifié :

```python
# servers/notify/configure.py (exemple)
from servers.common.config import MCPConfigurator

def configure():
    configurator = MCPConfigurator("notify")
    
    if configurator.is_configured():
        print("notify already configured")
        return
    
    # Logique spécifique au serveur
    command = ["uv", "run", "python", "-m", "servers.notify.server"]
    configurator.configure(command)
    print("notify configured successfully")

if __name__ == "__main__":
    configure()
```

### 3. Structure finale

```
servers/
├── common/
│   ├── __init__.py
│   └── config.py          # MCPConfigurator
├── notify/
│   └── configure.py       # Simplifié (~30 lignes)
├── screenshot/
│   └── configure.py       # Simplifié (~30 lignes)
└── lsmcp/
    └── configure.py       # Simplifié (~50 lignes, logique spécifique)
```

## Fichiers à modifier

| Fichier | Action |
|---------|--------|
| `servers/common/__init__.py` | Créer (nouveau) |
| `servers/common/config.py` | Créer (nouveau) |
| `servers/notify/configure.py` | Refactorer |
| `servers/screenshot/configure.py` | Refactorer |
| `servers/lsmcp/configure.py` | Refactorer |

## Critères de validation

- [ ] `MCPConfigurator` fonctionne pour les 3 serveurs
- [ ] Chaque `configure.py` utilise le module commun
- [ ] Les 3 serveurs se configurent correctement
- [ ] ~150 lignes de code dupliqué éliminées
- [ ] Tests manuels : `python -m servers.notify.configure`

## Estimation

- **Effort** : Faible (2-3h)
- **Risque** : Faible (pas de changement fonctionnel)
- **Impact** : Moyen (meilleure maintenabilité)
