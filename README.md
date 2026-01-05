# OpenFlow - BMAD Method for OpenCode

> **Note** : Ce projet implémente la méthodologie **BMAD** (Build More, Architect Dreams) pour [OpenCode](https://github.com/sst/opencode) ❤️

Configuration repository implementing BMAD methodology with specialized agents, skills, and MCP servers for AI-driven agile development.

## Quick Start

```bash
# Clone the repository
git clone <your-repo-url> ~/Projects/open-flow
cd ~/Projects/open-flow

# Install everything (agents, skills, MCP servers)
./install.sh

# Or install in a specific language
./install.sh install --lang=en   # English
./install.sh install --lang=fr   # French (default)
```

## Structure

```
open-flow/
├── agents/                          # Custom agents (i18n)
│   ├── fr/                          # French agents
│   │   ├── executeur.md
│   │   ├── quality.md
│   │   └── ...
│   └── en/                          # English agents
│       ├── executor.md
│       ├── quality.md
│       └── ...
├── skills/                          # Custom skills (i18n)
│   ├── fr/                          # French skills
│   │   └── <skill-name>/SKILL.md
│   └── en/                          # English skills
│       └── <skill-name>/SKILL.md
├── servers/                         # MCP servers
│   ├── notify/                      # Notification MCP server
│   │   ├── server.py                # MCP server (tool: ask_user)
│   │   ├── notifier.py              # PyObjC native notifications
│   │   └── configure.py             # Auto-configuration script
│   └── screenshot/                  # Screenshot MCP server
│       ├── server.py                # MCP server (tool: screenshot)
│       ├── screenshotter.py         # PyObjC screen capture
│       └── configure.py             # Auto-configuration script
├── roadmap/                         # Project roadmap
│   ├── README.md                    # Task tracking + methodology
│   └── plan-XX-*.md                 # Immutable implementation plans
├── maintenance/                     # Project health monitoring
│   ├── reports/                     # Generated health reports
│   ├── templates/                   # Report templates
│   └── metrics/                     # Metrics history (JSON)
├── install.sh                       # Installation script
├── AGENTS.fr.md                     # Global rules (French)
└── AGENTS.en.md                     # Global rules (English)
```

## BMAD Methodology (4 Phases)

**BMAD** = Build More, Architect Dreams - AI-driven agile development methodology

```
Phase 1: ANALYSIS (Optional)
    └─> Analyst → Product Brief, Research

Phase 2: PLANNING  
    └─> PM → PRD (Product Requirements Document)

Phase 3: SOLUTIONING
    ├─> UX Designer → UX Design
    ├─> Architect → Architecture Document
    └─> PM → Epics & User Stories

Phase 4: IMPLEMENTATION
    ├─> SM (Scrum Master) → Sprint Planning, Stories
    ├─> Dev (Developer) → Implementation (TDD)
    ├─> TEA (Test Architect) → Test Framework, Automation
    └─> Tech Writer → Documentation

QUICK FLOW (Alternative rapide)
    └─> Quick Flow → Tech Spec → Quick Dev → Code Review
```

### BMAD Lifecycle

1. **Analysis** (Optional) : Brainstorming, research, product brief
2. **Planning** : User interviews → PRD creation
3. **Solutioning** : UX → Architecture → Epics & Stories
4. **Implementation** : Sprint planning → Story creation → TDD → Tests → Review
5. **Quick Flow** : Tech spec → Implementation → Review (pour petites features)

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

## Agents BMAD

| Agent | Role | Phase | Key Workflows |
|-------|------|-------|---------------|
| **Analyst** | Business Analysis | 1 - Analysis | Brainstorming, Research, Product Brief |
| **PM** | Product Manager | 2 - Planning | PRD Creation, Epics & Stories |
| **UX Designer** | User Experience | 3 - Solutioning | UX Design, Wireframes |
| **Architect** | System Architecture | 3 - Solutioning | Architecture Document |
| **SM** | Scrum Master | 4 - Implementation | Sprint Planning, Story Creation |
| **Dev** | Developer | 4 - Implementation | TDD Implementation, Story Execution |
| **TEA** | Test Architect | 4 - Implementation | Test Framework, Automation, CI/CD |
| **Tech Writer** | Documentation | All phases | Project Docs, Diagrams, Explanations |
| **Quick Flow** | Full-Stack Solo | Quick Flow | Tech Spec → Implementation → Review |
| **BMad Master** | Orchestrator | All phases | Task/Workflow lists, Guidance |

### How to invoke

```bash
# Analysis Phase
/analyst          # Business analysis, research, product brief

# Planning Phase
/pm               # Create PRD, epics & stories

# Solutioning Phase
/ux-designer      # UX design and wireframes
/architect        # Architecture document

# Implementation Phase
/sm               # Sprint planning, story creation
/dev              # TDD implementation
/tea              # Test framework, automation

# Documentation
/tech-writer      # Documentation, diagrams

# Quick Flow (alternative)
/quick-flow       # Rapid tech spec → implementation → review

# Orchestration
/bmad-master      # Guidance, task lists, workflow orchestration
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

### Screenshot Server

Native macOS screenshot tool for capturing screens and windows.

**Tool**: `screenshot`

**Parameters**:
| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `mode` | string | No | `screen` or `window` (default: screen) |
| `window_title` | string | If mode=window | Window title to capture |
| `screen_index` | integer | No | Screen index for multi-monitor (default: 0) |
| `format` | string | No | `png` or `jpg` (default: png) |
| `delay` | number | No | Seconds to wait before capture |

**Requirements**: macOS Screen Recording permission.

## Skills BMAD

Skills provide specialized knowledge and workflows loaded via `/skill <name>`.

### BMAD Core Skills

| Skill | Description | Used By |
|-------|-------------|---------|
| `bmad-workflow-status` | Track project progress through BMAD phases | All agents |
| `bmad-prd` | Create Product Requirements Document | PM |
| `bmad-architecture` | Design scalable architecture | Architect |
| `bmad-ux-design` | UX Design and UI planning | UX Designer |
| `bmad-epics-stories` | Create Epics and User Stories | PM |
| `bmad-sprint-planning` | Generate sprint-status from epics | SM |
| `bmad-create-story` | Create developer-ready stories | SM |
| `bmad-dev-story` | TDD implementation workflow | Dev |
| `bmad-code-review` | Thorough code review process | Dev, Quick Flow |
| `bmad-tech-spec` | Create technical specification | Quick Flow |
| `bmad-quick-dev` | Rapid implementation workflow | Quick Flow |

### OpenFlow Infrastructure Skills

| Skill | Description |
|-------|-------------|
| `clean-code` | Clean code principles (naming, DRY, KISS) |
| `testability-patterns` | SOLID, dependency injection patterns |
| `git-conventions` | Conventional commits, branching strategy |
| `notify` | When to use ask_user MCP tool |

## Commands

| Command | Description |
|---------|-------------|
| `./install.sh` | Install all (agents, skills, MCP servers) |
| `./install.sh install --lang=en` | Install in English |
| `./install.sh install --lang=fr` | Install in French (default) |
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
