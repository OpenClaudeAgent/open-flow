# MCP lsmcp Server

MCP server providing LSP (Language Server Protocol) tools for Claude.

This integrates the open-source [lsmcp](https://github.com/mizchi/lsmcp) project (MIT License) by @mizchi.

## Features

lsmcp bridges Claude with Language Server Protocol features, enabling:

- **Code Intelligence**: Type information, documentation at hover
- **Navigation**: Go to definition, find all references
- **Diagnostics**: Compiler errors and warnings
- **Refactoring**: Rename symbols across project
- **Completions**: Context-aware suggestions

## Requirements

- **Node.js >= 22** (required for npx execution)
- Language servers for your languages (usually auto-installed by IDEs)

## Installation

The `install.sh` script automatically configures lsmcp for Python, TypeScript, and C/C++.

```bash
# From project root
./install.sh mcp
```

### Manual Installation

```bash
# Install default presets (Python, TypeScript, C/C++)
python3 servers/lsmcp/configure.py

# Install specific languages
python3 servers/lsmcp/configure.py python go rust cpp

# Install all available presets
python3 servers/lsmcp/configure.py all
```

### Available Presets

| Preset | Server Name | LSP Server | Default |
|--------|-------------|------------|---------|
| `python` | `lsmcp-python` | pyright | Yes |
| `typescript` | `lsmcp-typescript` | typescript-language-server | Yes |
| `cpp` | `lsmcp-cpp` | clangd | Yes |
| `go` | `lsmcp-go` | gopls | No |
| `rust` | `lsmcp-rust` | rust-analyzer | No |

Each preset creates a separate MCP server (e.g., `lsmcp-python`, `lsmcp-typescript`).

## Available Tools

Once configured, Claude has access to these LSP tools:

| Tool | Description |
|------|-------------|
| `get_hover` | Type information and documentation at a position |
| `get_definitions` | Navigate to symbol definition |
| `find_references` | Find all usages of a symbol |
| `get_document_symbols` | List symbols in a file (outline) |
| `get_workspace_symbols` | Search symbols across the project |
| `get_diagnostics` | Get errors/warnings for a file |
| `get_all_diagnostics` | Get diagnostics for entire project |
| `get_completion` | Get completion suggestions |
| `get_signature_help` | Get function signature help |
| `format_document` | Format a document |
| `get_code_actions` | Get available quick-fixes and refactorings |
| `rename_symbol` | Rename a symbol across the project |
| `check_capabilities` | Check LSP server capabilities |

## Usage Examples

**Get type information:**
```
Use get_hover on src/server.py at line 42, column 10
```

**Find all references:**
```
Use find_references to find all usages of the "configure" function in configure.py
```

**Get diagnostics:**
```
Use get_diagnostics to check for errors in server.py
```

**Rename a symbol:**
```
Use rename_symbol to rename "old_name" to "new_name" in the project
```

## Troubleshooting

### "Node.js >= 22 required"

lsmcp requires Node.js 22 or higher. Check your version:

```bash
node --version
```

Install/upgrade Node.js from https://nodejs.org or use nvm.

### "Could not find TypeScript installation"

The TypeScript preset requires TypeScript installed in your project:

```bash
npm install typescript
```

### LSP features not working

Ensure the corresponding LSP server is installed:

```bash
# For Python
pip install pyright
# or
npm install -g pyright

# For TypeScript
npm install -g typescript typescript-language-server

# For Go
go install golang.org/x/tools/gopls@latest

# For Rust
rustup component add rust-analyzer

# For C/C++
# macOS (via Homebrew)
brew install llvm
# or install Xcode Command Line Tools (includes clangd)
xcode-select --install

# Linux (Debian/Ubuntu)
sudo apt install clangd

# Windows
# Install LLVM from https://llvm.org/builds/
```

### Slow first request

First request may be slow as lsmcp starts the LSP server. Subsequent requests are faster.

## How It Works

1. Claude calls an lsmcp tool (e.g., `get_hover`)
2. lsmcp starts/connects to the appropriate LSP server
3. LSP server analyzes the code and returns results
4. lsmcp formats results and returns to Claude

## Links

- [lsmcp GitHub](https://github.com/mizchi/lsmcp)
- [Language Server Protocol](https://microsoft.github.io/language-server-protocol/)
