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

The server provides a single tool: `ask_user`

### Parameters

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

### Urgency Levels

| Level | Sound | Emoji | Use Case |
|-------|-------|-------|----------|
| `low` | Ping | ℹ️ | Informational questions |
| `normal` | Funk | ⚠️ | Standard decisions |
| `high` | Submarine | 🚨 | Urgent attention needed |

### Examples

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

### Output

The tool returns a confirmation message with:
- Urgency emoji (ℹ️, ⚠️, or 🚨)
- Agent name (if provided)
- Title of the notification sent

Example: `⚠️ Question sent [Executor]: Merge Conflict`

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
