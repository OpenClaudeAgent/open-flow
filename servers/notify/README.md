# MCP Notify Server

MCP server for sending native macOS notifications to interact with users.

## Features

- **Native macOS notifications**: Uses PyObjC for native API access
- **Customizable urgency levels**: Low, normal, and high with different sounds
- **Options display**: Show choices/options in the notification
- **Context info**: Include repo, branch, agent, and task metadata
- **Cross-platform support**: Fallback to osascript on macOS, notify-send on Linux, PowerShell on Windows

## Installation

### Requirements

- macOS 12+ (or Linux/Windows with respective notification systems)
- Python 3.10+
- Notification permissions

### Setup

```bash
cd servers/notify

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install mcp pyobjc

# Configure OpenCode
python configure.py
```

### Permissions

On macOS, notifications require the "Notifications" permission:

1. Go to **System Settings** > **Notifications**
2. Enable notifications for your terminal app or Python

## Usage

The server provides 4 tools:

| Tool | Purpose | Urgency |
|------|---------|---------|
| `ask_user` | Ask user a question or request a decision | Configurable |
| `notify_commit` | Notify that a commit was made | Low |
| `notify_merge` | Notify that a branch was merged to main | Normal |
| `notify_sync` | Notify that worktrees were synchronized | Low |

---

### Tool: `ask_user`

Send a notification to ask the user a question or request a decision.

#### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `title` | string | Yes | - | Short title summarizing what you need from the user |
| `question` | string | Yes | - | The question or decision you need the user to answer |
| `options` | array | No | - | List of possible options or choices for the user |
| `urgency` | string | No | `normal` | `low`, `normal`, or `high` (affects sound) |
| `repo` | string | No | - | Name of the repository or project |
| `branch` | string | No | - | Current git branch |
| `agent` | string | No | - | Name of the agent asking the question |
| `task` | string | No | - | Name or number of the current task |

#### Urgency Levels

| Level | Sound | Emoji | Use Case |
|-------|-------|-------|----------|
| `low` | Ping | ℹ️ | Informational questions |
| `normal` | Funk | ⚠️ | Standard decisions |
| `high` | Submarine | 🚨 | Urgent attention needed |

#### Examples

**Simple question:**
```
Send a notification asking "Should I proceed with the refactoring?"
```

**Question with options:**
```
Ask the user to choose between "Continue", "Abort", or "Review first"
```

**Full context:**
```
Notify the user with:
- title: "Merge Conflict"
- question: "How should I resolve the conflict in app.py?"
- options: ["Keep ours", "Keep theirs", "Manual merge"]
- urgency: "high"
- repo: "my-project"
- branch: "feature/auth"
```

#### Output

The tool returns a confirmation message with:
- Urgency emoji (ℹ️, ⚠️, or 🚨)
- Agent name (if provided)
- Title of the notification sent

Example: `⚠️ Question sent [Executor]: Merge Conflict`

---

### Tool: `notify_commit`

Notify the user that a commit was made. Use this after committing changes.

#### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `branch` | string | Yes | Branch name where the commit was made |
| `message` | string | Yes | Commit message (first line) |
| `files` | array | No | List of modified files |
| `hash` | string | No | Short commit hash (7 chars) |
| `agent` | string | No | Name of the agent that made the commit |

#### Example Notification

```
+-----------------------------------------------+
| [Icon]                                        |
| feature/notify-actions              subtitle  |
| ℹ️ Commit                             title   |
| fix(notify): add action button support        |
| Files: server.py, notifier.py           body  |
+-----------------------------------------------+
```

#### Output

Returns: `Commit notified: <hash> on <branch>`

---

### Tool: `notify_merge`

Notify the user that a branch was merged to main. Use this after merging.

#### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `source_branch` | string | Yes | Branch that was merged |
| `commits_count` | integer | No | Number of commits merged |
| `files_count` | integer | No | Number of files changed |
| `version` | string | No | Version tag if any (e.g., v0.5.0) |
| `repo` | string | No | Repository name |
| `agent` | string | No | Name of the agent that performed the merge |

#### Example Notification

```
+-----------------------------------------------+
| [Icon]                                        |
| open-flow                             subtitle |
| ⚠️ Merge sur main                      title  |
| feature/notify-actions → main                 |
| 3 commits, 5 files                      body  |
+-----------------------------------------------+
```

#### Output

Returns: `Merge notified: <source_branch> → main`

---

### Tool: `notify_sync`

Notify the user that worktrees were synchronized. Use after sync-worktrees.

#### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `worktrees` | array | Yes | List of worktrees that were synchronized |
| `source` | string | No | Source branch (default: main) |
| `repo` | string | No | Repository name |
| `conflicts` | array | No | List of conflicts if any |

#### Example Notification

```
+-----------------------------------------------+
| [Icon]                                        |
| open-flow                             subtitle |
| ℹ️ Worktrees synchronisés              title  |
| 3 worktrees updated from main                 |
| roadmap, executor, quality              body  |
+-----------------------------------------------+
```

#### Output

Returns: `Sync notified: <count> worktrees updated`

**Note:** If conflicts are detected, urgency is elevated to `normal` and conflicts are listed.

## Troubleshooting

### Notifications not appearing

1. Check that notifications are enabled in System Settings > Notifications
2. Ensure your terminal app has notification permissions
3. Check "Do Not Disturb" is not enabled

### Sound not playing

1. Verify system volume is not muted
2. Check that notification sounds are enabled for your terminal app
3. Try a different urgency level to test different sounds

### PyObjC import error

If PyObjC is not available, the server falls back to osascript. To use native notifications:

```bash
pip install pyobjc
```

## Development

```bash
# Run server directly
python -m server

# Test notification
python -c "from notifier import send_notification; send_notification('Test', 'Hello World', type='info')"
```
