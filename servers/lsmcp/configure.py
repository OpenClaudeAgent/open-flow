#!/usr/bin/env python3
"""Configure MCP lsmcp server in OpenCode."""

import json
import sys
from pathlib import Path


def get_opencode_config_path() -> Path:
    """Get the OpenCode config file path."""
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


def configure_lsmcp(config: dict) -> tuple[dict, bool]:
    """
    Add MCP lsmcp configuration.

    Returns:
        Tuple of (updated config, whether changes were made)
    """
    # Ensure mcp section exists
    if "mcp" not in config:
        config["mcp"] = {}

    expected_command = ["npx", "@nicepkg/lsmcp"]

    # Check if lsmcp already configured correctly
    if "lsmcp" in config["mcp"]:
        existing = config["mcp"]["lsmcp"]
        if (
            existing.get("type") == "local"
            and existing.get("command") == expected_command
            and existing.get("enabled") is True
        ):
            return config, False  # Already configured correctly

    # Add lsmcp configuration
    # Uses npx to run the package directly (no local install needed)
    config["mcp"]["lsmcp"] = {
        "type": "local",
        "command": expected_command,
        "enabled": True,
    }

    return config, True


def main():
    """Main entry point."""
    if len(sys.argv) > 1 and sys.argv[1] == "--help":
        print("Configure MCP lsmcp server for OpenCode")
        print()
        print("Usage: python configure.py")
        print()
        print("This will add the lsmcp server to your OpenCode config at:")
        print(f"  {get_opencode_config_path()}")
        print()
        print("Requirements:")
        print("  - Node.js >= 22")
        print(
            "  - LSP servers for your languages (typescript-language-server, pyright, etc.)"
        )
        return 0

    config_path = get_opencode_config_path()

    print("MCP lsmcp Configuration")
    print("=======================")
    print(f"Config file: {config_path}")
    print()

    # Load existing config
    config = load_config(config_path)

    # Add MCP lsmcp
    config, changed = configure_lsmcp(config)

    if changed:
        save_config(config_path, config)
        print("✅ MCP lsmcp configured successfully")
        print()
        print("Configuration added:")
        print(json.dumps({"mcp": {"lsmcp": config["mcp"]["lsmcp"]}}, indent=2))
        print()
        print("Restart OpenCode to use LSP tools.")
    else:
        print("ℹ️  MCP lsmcp already configured")

    return 0


if __name__ == "__main__":
    sys.exit(main())
