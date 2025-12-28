# OpenFlow - OpenCode Configuration Repository

Configuration repository for OpenCode agents, skills, and workflows.

## Structure

```
open-flow/
├── agents/                          # Custom agents
│   ├── quality.md                   # Quality assurance agent
│   ├── executeur.md                 # Task executor agent
│   ├── roadmap.md                   # Roadmap planning agent
│   ├── ui-designer.md               # UI/UX design agent
│   ├── tester.md                    # Testing agent
│   └── refactoring.md               # Code refactoring agent
├── skills/                          # Custom skills
│   ├── qml-blueplayer/SKILL.md      # QML/Qt best practices
│   └── functional-testing/SKILL.md  # Qt Quick Test patterns
├── config/
│   └── opencode.template.json       # Config template (no secrets)
└── install.sh                       # Installation script
```

## Quick Start

```bash
# Clone the repository
git clone <your-repo-url> ~/Projects/open-flow
cd ~/Projects/open-flow

# Install agents and skills
./install.sh
```

## Commands

| Command | Description |
|---------|-------------|
| `./install.sh` | Install all agents and skills |
| `./install.sh agents` | Install only agents |
| `./install.sh skills` | Install only skills |
| `./install.sh status` | Show current installation |
| `./install.sh diff` | Compare with installed versions |
| `./install.sh backup` | Create backup of current config |
| `./install.sh restore` | Restore from backup |

## Agents

### Quality Agent
Generates manual test plans, validates test changes, and maintains quality history.

### Executeur Agent
Executes roadmap tasks - implements, validates with user, updates and merges.

### Roadmap Agent
Planning agent - creates and manages task plans without touching code.

### UI Designer Agent
Creates visually elegant, modern, and harmonious interfaces.

### Tester Agent
Improves test coverage, quality, and maintainability.

### Refactoring Agent
Improves testability and maintainability via recognized patterns.

## Skills

### qml-blueplayer
Best practices for QML/Qt development - conventions, patterns, and theme system.

### functional-testing
Functional UI testing patterns for Qt Quick Test - SignalSpy, scenarios, debugging.

## Workflow

1. **Edit** agents/skills in this repository
2. **Test** changes with `./install.sh diff`
3. **Install** with `./install.sh`
4. **Iterate** based on feedback
5. **Commit** improvements

## Backup System

Backups are automatically created before each installation in:
```
~/.opencode-backups/
├── agents-YYYYMMDD_HHMMSS/
├── skills-YYYYMMDD_HHMMSS/
└── config-YYYYMMDD_HHMMSS/
```

## Installation Paths

| Type | Location |
|------|----------|
| Agents | `~/.config/opencode/agent/` |
| Skills | `~/.opencode/skill/` |
| Config | `~/.config/opencode/opencode.json` |

## Configuration

Copy the template and add your API keys:

```bash
cp config/opencode.template.json ~/.config/opencode/opencode.json
# Edit and add your keys
```

## Development

To improve an agent:

1. Edit the `.md` file in `agents/`
2. Run `./install.sh diff` to see changes
3. Run `./install.sh agents` to install
4. Test in OpenCode
5. Commit when satisfied

## License

Personal configuration - adapt to your needs.
