#!/usr/bin/env python3
"""Configure MCP notify server in opencode.json."""

import json
import os
import sys
from pathlib import Path


def get_opencode_config_path() -> Path:
    """Get the path to opencode.json."""
    return Path.home() / ".config" / "opencode" / "opencode.json"


def get_mcp_notify_path() -> Path:
    """Get the path to the MCP notify server."""
    return Path(__file__).parent.resolve()


def load_config(path: Path) -> dict:
    """Load existing config or return empty dict."""
    if path.exists():
        with open(path, "r") as f:
            return json.load(f)
    return {}


def save_config(path: Path, config: dict) -> None:
    """Save config to file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, "w") as f:
        json.dump(config, f, indent=2)
        f.write("\n")


def configure_mcp_notify(config: dict, mcp_path: Path) -> tuple[dict, bool]:
    """
    Add MCP notify configuration.

    Returns:
        Tuple of (updated config, whether changes were made)
    """
    # Ensure mcp section exists
    if "mcp" not in config:
        config["mcp"] = {}

    # Check if notify already configured
    if "notify" in config["mcp"]:
        existing_cwd = config["mcp"]["notify"].get("cwd", "")
        if str(mcp_path) == existing_cwd:
            return config, False  # Already configured correctly

    # Add notify configuration
    config["mcp"]["notify"] = {
        "command": ["python3", "server.py"],
        "cwd": str(mcp_path),
    }

    return config, True


def main():
    """Main entry point."""
    config_path = get_opencode_config_path()
    mcp_path = get_mcp_notify_path()

    print(f"MCP Notify Configuration")
    print(f"========================")
    print(f"Config file: {config_path}")
    print(f"MCP server:  {mcp_path}")
    print()

    # Load existing config
    config = load_config(config_path)

    # Add MCP notify
    config, changed = configure_mcp_notify(config, mcp_path)

    if changed:
        save_config(config_path, config)
        print("✅ MCP notify configured successfully")
        print()
        print("Configuration added:")
        print(json.dumps({"mcp": {"notify": config["mcp"]["notify"]}}, indent=2))
    else:
        print("ℹ️  MCP notify already configured")

    return 0


if __name__ == "__main__":
    sys.exit(main())
