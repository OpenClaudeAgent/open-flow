# Plan 06 - OpenFlow Analytics

## Context

OpenCode stores rich data about each session in `~/.local/share/opencode/storage/`:
- **Sessions**: Metadata (project, title, timestamps)
- **Messages**: Role, agent used, model, tokens, cost
- **Parts**: Message content, tool calls, results

This data enables analysis of agent, skill, and workflow usage defined in this repo (open-flow). Currently, there's no way to visualize these metrics or detect problematic patterns (infinite agent loops, tool overuse, etc.).

## Objective

Create a CLI script that analyzes OpenCode sessions and generates a statistical report on OpenFlow component usage (agents, skills, workflows).

## Expected Behavior

### Invocation

```bash
# Full analysis
./scripts/openflow-analytics

# Analyze a specific project
./scripts/openflow-analytics --project open-flow

# Analyze last N days
./scripts/openflow-analytics --days 7

# JSON export for external processing
./scripts/openflow-analytics --format json > report.json
```

### Generated Report

The script displays a structured report in several sections:

#### 1. Global Summary
```
=== OpenFlow Analytics ===
Period: 2025-12-22 -> 2025-12-29 (7 days)
Sessions analyzed: 42
Total messages: 1,234
Tokens consumed: 2.4M (input: 1.8M, output: 600K)
Estimated cost: $45.23
```

#### 2. Agent Usage
```
=== Agents ===
Agent          | Sessions | Messages | Tokens   | Cost
---------------|----------|----------|----------|--------
executeur      | 15       | 234      | 890K     | $12.50
roadmap        | 8        | 89       | 120K     | $2.30
build (default)| 35       | 567      | 1.2M     | $25.00
explore        | 12       | 156      | 45K      | $1.20
tester         | 3        | 45       | 89K      | $3.10
quality        | 2        | 23       | 34K      | $1.13
```

#### 3. Skill Usage
```
=== Skills ===
Skill                | Invocations | By agent
---------------------|-------------|------------------
agentic-flow         | 23          | executeur (20), build (3)
clean-code           | 5           | quality (5)
notify               | 12          | executeur (12)
(no skill loaded)    | 156         | -
```

#### 4. Tool Usage
```
=== Tools (top 10) ===
Tool      | Invocations | Success | Failures | Avg time
----------|-------------|---------|----------|------------
edit      | 456         | 450     | 6        | 0.2s
read      | 1,234       | 1,234   | 0        | 0.1s
bash      | 345         | 320     | 25       | 2.3s
task      | 89          | 85      | 4        | 45.2s
glob      | 234         | 234     | 0        | 0.3s
```

#### 5. Agent Chain Analysis (nested agents)
```
=== Invocation Chains ===
Max observed depth: 3

Detected patterns:
- executeur -> tester (15 times)
- executeur -> quality (8 times)
- executeur -> refactoring -> tester (2 times)

Sessions with depth > 2:
- ses_abc123: executeur -> tester -> explore (3 levels)
- ses_def456: executeur -> refactoring -> tester (3 levels)
```

#### 6. Alerts and Anomalies
```
=== Alerts ===
[WARN] Session ses_xyz789: 12 cascading 'task' invocations
[WARN] Agent 'explore' invoked 45 times in a single session
[INFO] Skill 'qml' never used during period
```

### Available Filters

| Option | Description |
|--------|-------------|
| `--project <name>` | Filter by project name |
| `--days <n>` | Analyze last N days |
| `--agent <name>` | Focus on a specific agent |
| `--format <txt\|json>` | Output format |
| `--verbose` | Additional details |

### Anomaly Detection

The script automatically detects:
1. **Agent loops**: An agent invoking itself (directly or indirectly)
2. **Overuse**: More than 10 `task` invocations in a session
3. **Excessive depth**: Agent chains > 3 levels
4. **Unused skills**: Skills defined but never loaded
5. **Repetitive failures**: Tools with failure rate > 20%

## Specifications

*(Section reserved for Executor for technical details)*

### OpenCode Data Structure

```
~/.local/share/opencode/storage/
├── session/{project_hash}/{session_id}.json  # Session metadata
├── message/{session_id}/{message_id}.json    # Messages with agent, tokens
├── part/{message_id}/{part_id}.json          # Content, tool calls
└── todo/                                      # Todos
```

### Key Fields

**Session**:
- `id`, `projectID`, `directory`, `title`
- `time.created`, `time.updated`

**Message**:
- `sessionID`, `role` (user/assistant)
- `agent` (executeur, roadmap, build, explore...)
- `modelID`, `providerID`
- `tokens` (input, output, cache.read, cache.write)
- `cost`

**Part (type: tool)**:
- `tool` (edit, read, bash, task, skill, glob...)
- `state.status` (completed, error...)
- `state.input`, `state.output`

## Validation Checklist

- [ ] Script runs without errors with `./scripts/openflow-analytics`
- [ ] Global summary shows correct statistics
- [ ] Custom agents (executeur, roadmap, etc.) are correctly identified
- [ ] Loaded skills are detected via the "skill" tool
- [ ] Agent chains are reconstructed via the "task" tool
- [ ] Loop/overuse alerts display correctly
- [ ] `--project` filter works
- [ ] `--days` filter works
- [ ] `--format json` export produces valid JSON
- [ ] Script works even with 0 sessions (informative message)
