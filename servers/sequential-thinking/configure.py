#!/usr/bin/env python3
"""Configure MCP sequential-thinking server in opencode.json."""

import json
import sys
from pathlib import Path


def get_opencode_config_path() -> Path:
    """Get the path to opencode.json."""
    return Path.home() / ".config" / "opencode" / "opencode.json"


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


def configure_sequential_thinking(config: dict) -> tuple[dict, bool]:
    """
    Add MCP sequential-thinking configuration.

    Returns:
        Tuple of (updated config, whether changes were made)
    """
    # Ensure mcp section exists
    if "mcp" not in config:
        config["mcp"] = {}

    expected_command = ["npx", "-y", "@modelcontextprotocol/server-sequential-thinking"]

    # Check if already configured correctly
    if "sequential-thinking" in config["mcp"]:
        existing = config["mcp"]["sequential-thinking"]
        if (
            existing.get("type") == "local"
            and existing.get("command") == expected_command
            and existing.get("enabled") is True
        ):
            return config, False  # Already configured correctly

    # Add sequential-thinking configuration
    config["mcp"]["sequential-thinking"] = {
        "type": "local",
        "command": expected_command,
        "enabled": True,
    }

    return config, True


def main():
    """Main entry point."""
    config_path = get_opencode_config_path()

    print("MCP Sequential Thinking Configuration")
    print("=====================================")
    print(f"Config file: {config_path}")
    print()

    # Load existing config
    config = load_config(config_path)

    # Add MCP sequential-thinking
    config, changed = configure_sequential_thinking(config)

    if changed:
        save_config(config_path, config)
        print("MCP sequential-thinking configured successfully")
        print()
        print("Configuration added:")
        print(
            json.dumps(
                {"mcp": {"sequential-thinking": config["mcp"]["sequential-thinking"]}},
                indent=2,
            )
        )
    else:
        print("MCP sequential-thinking already configured")

    return 0


if __name__ == "__main__":
    sys.exit(main())
