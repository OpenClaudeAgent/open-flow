# OpenFlow - OpenCode Configuration Repository

Configuration repository for OpenCode agents, skills, MCP servers, and workflows.

## Quick Start

```bash
# Clone the repository
git clone <your-repo-url> ~/Projects/open-flow
cd ~/Projects/open-flow

# Install everything (agents, skills, MCP servers)
./install.sh
```

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

## Agentic Workflow

Five specialized agents collaborate through isolated worktrees:

```
                    UTILISATEUR
                         |
     +----------+--------+--------+----------+
     |          |        |        |          |
     v          v        v        v          v
  Roadmap   Executeur  Quality  Tester  Refactoring
   (Plan)   (Implem)   (QA)    (Tests)  (Testab.)
     |          |        |        |          |
     v          v        v        v          v
  roadmap/    src/    quality/  tests/     src/
```

### Feature Lifecycle

1. **Ideation** : User expresses need
2. **Planning** : Roadmap creates functional plan
3. **Implementation** : Executeur codes according to plan
4. **Tests** : Tester writes automated tests (invoked by Executeur)
5. **Quality** : Quality does code review + tests review (invoked by Executeur)
6. **Validation** : User tests with scenarios checklist
7. **Merge** : Executeur merges to main + tags version (after user approval)

### Validation Phase

When Executeur completes implementation, it:
1. Launches the application (`make run &`)
2. Generates **test scenarios** with concrete actions
3. Presents a validation checklist to the user
4. Notifies via **MCP `ask_user`**
5. Iterates until all scenarios pass

Example validation output:
```
### Scenario 1 : [Main behavior]
1. Click on [element]
2. Enter [value] in field
3. **Expected** : [visible result]

### Scenario 2 : [Edge case]
1. [concrete action]
2. **Expected** : [expected behavior]
```

## Agents

| Agent | Role | Scope | Key Features |
|-------|------|-------|--------------|
| **Executeur** | Implementation | `src/` | Validation scenarios, MCP notifications |
| **Roadmap** | Planning | `roadmap/` | Functional specs, no code |
| **Quality** | Code Review + QA | `quality/` | Code review, tests review, manual test plans |
| **Tester** | Automated tests | `tests/` | Unit/E2E tests, coverage |
| **Refactoring** | Testability | `src/` | SOLID patterns, DI |

### How to invoke

```
/executeur    # Execute next roadmap task
/roadmap      # Plan a new feature
/quality      # Generate manual test plan
/tester       # Write automated tests
/refactoring  # Improve code testability
```

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

## Skills

Skills provide specialized knowledge loaded via `/skill <name>`.

| Skill | Description |
|-------|-------------|
| `agentic-flow` | Agent collaboration and workflow patterns |
| `clean-code` | Clean code principles (naming, DRY, KISS) |
| `code-review` | Code review checklist and feedback |
| `functional-testing` | Qt Quick Test patterns |
| `git-conventions` | Conventional commits, branching |
| `notify` | When to use ask_user tool |
| `qml` | QML/Qt Quick best practices |
| `qt-cpp` | Qt/C++ patterns and conventions |
| `testability-patterns` | SOLID, dependency injection |
| `ui-design-principles` | Visual hierarchy, spacing, colors |

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

## Installation Paths

| Type | Location |
|------|----------|
| Agents | `~/.config/opencode/agent/` |
| Skills | `~/.config/opencode/skill/` |
| Config | `~/.config/opencode/opencode.json` |
| Backups | `~/.opencode-backups/` |

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

## Backup System

Backups are automatically created before each installation:
```
~/.opencode-backups/
├── agents-YYYYMMDD_HHMMSS/
├── skills-YYYYMMDD_HHMMSS/
└── config-YYYYMMDD_HHMMSS/
```

Maximum backup size: 20MB (oldest removed first).

## License

Personal configuration - adapt to your needs.
