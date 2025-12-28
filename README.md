# OpenFlow - OpenCode Configuration Repository

Configuration repository for OpenCode agents, skills, MCP servers, and workflows.

## Structure

```
open-flow/
├── agents/                          # Custom agents
│   ├── executeur.md                 # Task executor agent
│   ├── quality.md                   # Quality assurance agent
│   ├── refactoring.md               # Code refactoring agent
│   ├── roadmap.md                   # Roadmap planning agent
│   └── tester.md                    # Testing agent
├── skills/                          # Custom skills
│   ├── agentic-flow/SKILL.md        # Agentic workflow patterns
│   ├── clean-code/SKILL.md          # Clean code principles
│   ├── code-review/SKILL.md         # Code review checklist
│   ├── functional-testing/SKILL.md  # Qt Quick Test patterns
│   ├── git-conventions/SKILL.md     # Git conventions
│   ├── notify/SKILL.md              # Notification tool usage
│   ├── qml/SKILL.md                 # QML best practices
│   ├── qml-blueplayer/SKILL.md      # QML BluePlayer specifics
│   ├── qt-cpp/SKILL.md              # Qt/C++ patterns
│   ├── testability-patterns/SKILL.md # Testability patterns
│   └── ui-design-principles/SKILL.md # UI design principles
├── servers/                         # MCP servers
│   └── notify/                      # Notification MCP server
│       ├── server.py                # MCP server (tool: ask_user)
│       ├── notifier.py              # PyObjC native notifications
│       ├── configure.py             # Auto-configuration script
│       └── assets/                  # Icons
├── roadmap/                         # Project roadmaps
│   └── README.md                    # Current plans
├── install.sh                       # Installation script
└── AGENTS.md                        # Global agent rules
```

## Quick Start

```bash
# Clone the repository
git clone <your-repo-url> ~/Projects/open-flow
cd ~/Projects/open-flow

# Install everything (agents, skills, MCP servers)
./install.sh
```

## Commands

| Command | Description |
|---------|-------------|
| `./install.sh` | Install all (agents, skills, MCP servers) |
| `./install.sh agents` | Install only agents |
| `./install.sh skills` | Install only skills |
| `./install.sh mcp` | Configure MCP servers only |
| `./install.sh status` | Show current installation |
| `./install.sh diff` | Compare with installed versions |
| `./install.sh backup` | Create backup of current config |
| `./install.sh restore` | Restore from backup |

## MCP Servers

### Notify Server (ask_user)

Native macOS notification tool for agent-user communication.

**Tool**: `ask_user`

**Parameters**:
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `title` | string | Yes | Short title (notification header) |
| `question` | string | Yes | The question to ask |
| `options` | array | No | List of possible choices |
| `urgency` | string | No | `low`, `normal`, `high` |
| `repo` | string | No | Repository name |
| `branch` | string | No | Current branch |
| `agent` | string | No | Agent name |
| `task` | string | No | Task identifier |

**Usage Policy**: Only use when explicitly instructed in agent instructions.

**Installation**:
```bash
./install.sh mcp
```

This will:
1. Create a virtual environment in `servers/notify/.venv`
2. Install dependencies (`mcp`, `pyobjc`)
3. Configure `~/.config/opencode/opencode.json`

## Agents

### Executeur Agent
Executes roadmap tasks - implements, validates with user, updates and merges.

### Quality Agent
Generates manual test plans, validates test changes, and maintains quality history.

### Roadmap Agent
Planning agent - creates and manages task plans without touching code.

### Tester Agent
Improves test coverage, quality, and maintainability.

### Refactoring Agent
Improves testability and maintainability via recognized patterns.

## Skills

Skills provide specialized knowledge and step-by-step guidance for specific tasks.

| Skill | Description |
|-------|-------------|
| `agentic-flow` | Agentic workflow patterns |
| `clean-code` | Clean code principles |
| `code-review` | Code review checklist |
| `functional-testing` | Qt Quick Test patterns |
| `git-conventions` | Git commit conventions |
| `notify` | When to use ask_user tool |
| `qml` | QML best practices |
| `qml-blueplayer` | QML for BluePlayer project |
| `qt-cpp` | Qt/C++ patterns |
| `testability-patterns` | SOLID, DI patterns |
| `ui-design-principles` | UI/UX guidelines |

## Installation Paths

| Type | Location |
|------|----------|
| Agents | `~/.config/opencode/agent/` |
| Skills | `~/.config/opencode/skill/` |
| Config | `~/.config/opencode/opencode.json` |
| Backups | `~/.opencode-backups/` |

## Backup System

Backups are automatically created before each installation:
```
~/.opencode-backups/
├── agents-YYYYMMDD_HHMMSS/
├── skills-YYYYMMDD_HHMMSS/
└── config-YYYYMMDD_HHMMSS/
```

Maximum backup size: 20MB (oldest removed first).

## Workflow

1. **Edit** agents/skills/servers in this repository
2. **Test** changes with `./install.sh diff`
3. **Install** with `./install.sh`
4. **Iterate** based on feedback
5. **Commit** improvements

## Development

### Improve an Agent

1. Edit the `.md` file in `agents/`
2. Run `./install.sh diff` to see changes
3. Run `./install.sh agents` to install
4. Test in OpenCode
5. Commit when satisfied

### Improve a Skill

1. Edit `SKILL.md` in `skills/<name>/`
2. Run `./install.sh skills` to install
3. Test with `/skill <name>` in OpenCode

### Improve MCP Server

1. Edit files in `servers/notify/`
2. Run `./install.sh mcp` to reconfigure
3. Restart OpenCode to reload MCP server

## License

Personal configuration - adapt to your needs.
