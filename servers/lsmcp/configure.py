#!/usr/bin/env python3
"""Configure MCP lsmcp servers in OpenCode."""

import json
import shutil
import sys
from pathlib import Path

# Available language presets with their descriptions
PRESETS = {
    "python": {
        "preset": "pyright",
        "description": "Python (pyright)",
    },
    "typescript": {
        "preset": "typescript",
        "description": "TypeScript/JavaScript",
    },
    "go": {
        "preset": "gopls",
        "description": "Go",
    },
    "rust": {
        "preset": "rust-analyzer",
        "description": "Rust",
    },
    "cpp": {
        "preset": "clangd",
        "description": "C/C++ (clangd)",
        "check_command": "clangd",
    },
}

# Default presets to install
DEFAULT_PRESETS = ["python", "typescript", "cpp"]


def get_opencode_config_path() -> Path:
    """Get the OpenCode config file path."""
    return Path.home() / ".config" / "opencode" / "opencode.json"


def check_lsp_server(preset_name: str, preset_info: dict) -> bool:
    """
    Check if the LSP server for a preset is available.

    Returns True if available, False otherwise.
    Prints a warning if not available.
    """
    check_cmd = preset_info.get("check_command")
    if not check_cmd:
        return True  # No check needed

    if shutil.which(check_cmd):
        return True

    # Print warning with installation instructions
    print(
        f"⚠️  {check_cmd} not found - {preset_info['description']} support may not work"
    )

    if preset_name == "cpp":
        print("   Install clangd:")
        print("   - macOS: brew install llvm (or Xcode Command Line Tools)")
        print("   - Linux: apt install clangd (or equivalent)")
        print("   - Windows: Install LLVM from https://llvm.org")
    print()

    return False


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


def configure_lsmcp(config: dict, presets: list[str]) -> tuple[dict, list[str]]:
    """
    Add MCP lsmcp configurations for specified presets.

    Returns:
        Tuple of (updated config, list of configured presets)
    """
    if "mcp" not in config:
        config["mcp"] = {}

    configured = []

    for lang in presets:
        if lang not in PRESETS:
            print(f"⚠️  Unknown preset: {lang}")
            continue

        preset_info = PRESETS[lang]
        server_name = f"lsmcp-{lang}"
        expected_command = ["npx", "@mizchi/lsmcp", "-p", preset_info["preset"]]

        # Check if already configured correctly
        if server_name in config["mcp"]:
            existing = config["mcp"][server_name]
            if (
                existing.get("type") == "local"
                and existing.get("command") == expected_command
                and existing.get("enabled") is True
            ):
                continue  # Already configured

        # Add configuration
        config["mcp"][server_name] = {
            "type": "local",
            "command": expected_command,
            "enabled": True,
        }
        configured.append(lang)

    return config, configured


def main():
    """Main entry point."""
    if len(sys.argv) > 1 and sys.argv[1] == "--help":
        print("Configure MCP lsmcp servers for OpenCode")
        print()
        print("Usage: python configure.py [presets...]")
        print()
        print("Available presets:")
        for lang, info in PRESETS.items():
            default = " (default)" if lang in DEFAULT_PRESETS else ""
            print(f"  {lang:12} - {info['description']}{default}")
        print()
        print("Examples:")
        print(
            "  python configure.py              # Install defaults (python, typescript, cpp)"
        )
        print("  python configure.py python       # Install only Python")
        print("  python configure.py python go    # Install Python and Go")
        print("  python configure.py all          # Install all presets")
        print()
        print(f"Config file: {get_opencode_config_path()}")
        print()
        print("Requirements:")
        print("  - Node.js >= 22")
        print(
            "  - LSP servers for your languages (pyright, typescript, gopls, clangd, etc.)"
        )
        return 0

    # Determine which presets to install
    if len(sys.argv) > 1:
        if sys.argv[1] == "all":
            presets = list(PRESETS.keys())
        else:
            presets = sys.argv[1:]
    else:
        presets = DEFAULT_PRESETS

    config_path = get_opencode_config_path()

    print("MCP lsmcp Configuration")
    print("=======================")
    print(f"Config file: {config_path}")
    print(f"Presets: {', '.join(presets)}")
    print()

    # Load existing config
    config = load_config(config_path)

    # Add MCP lsmcp servers
    config, configured = configure_lsmcp(config, presets)

    if configured:
        save_config(config_path, config)
        print(f"✅ Configured {len(configured)} lsmcp server(s):")
        for lang in configured:
            info = PRESETS[lang]
            print(f"   - lsmcp-{lang} ({info['description']})")
        print()

        # Check LSP server availability for configured presets
        for lang in configured:
            check_lsp_server(lang, PRESETS[lang])

        print("Restart OpenCode to use LSP tools.")
    else:
        print("ℹ️  All requested lsmcp servers already configured")

    return 0


if __name__ == "__main__":
    sys.exit(main())
