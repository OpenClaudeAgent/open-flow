#!/usr/bin/env python3
"""Configure MCP screenshot server in OpenCode."""

import json
import sys
from pathlib import Path


def get_opencode_config_path() -> Path:
    """Get the OpenCode config file path."""
    return Path.home() / ".config" / "opencode" / "opencode.json"


def get_server_path() -> Path:
    """Get the path to this server directory."""
    return Path(__file__).parent.resolve()


def configure_opencode():
    """Add screenshot server to OpenCode MCP configuration."""
    config_path = get_opencode_config_path()
    server_path = get_server_path()
    venv_python = server_path / ".venv" / "bin" / "python"

    # Read existing config
    if config_path.exists():
        with open(config_path) as f:
            config = json.load(f)
    else:
        config = {}

    # Ensure mcp section exists
    if "mcp" not in config:
        config["mcp"] = {}

    # Add screenshot server configuration
    config["mcp"]["screenshot"] = {
        "type": "local",
        "command": [str(venv_python), "-m", "server"],
        "args": [],
        "cwd": str(server_path),
    }

    # Write config
    config_path.parent.mkdir(parents=True, exist_ok=True)
    with open(config_path, "w") as f:
        json.dump(config, f, indent=2)

    print(f"✅ Screenshot server configured in {config_path}")
    print(f"   Server path: {server_path}")
    print(f"   Python: {venv_python}")
    print()
    print("Restart OpenCode to use the screenshot tool.")


def main():
    """Main entry point."""
    if len(sys.argv) > 1 and sys.argv[1] == "--help":
        print("Configure MCP screenshot server for OpenCode")
        print()
        print("Usage: python configure.py")
        print()
        print("This will add the screenshot server to your OpenCode config at:")
        print(f"  {get_opencode_config_path()}")
        return

    configure_opencode()


if __name__ == "__main__":
    main()
