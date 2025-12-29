# MCP Screenshot Server

MCP server for capturing screenshots on macOS.

## Features

- **Full screen capture**: Capture the entire screen
- **Window capture**: Capture a specific window by title
- **Multi-monitor support**: Select which screen to capture
- **Configurable format**: PNG or JPG output
- **Delayed capture**: Optional delay before capturing

## Installation

### Requirements

- macOS 12+
- Python 3.10+
- Screen Recording permission

### Setup

```bash
cd servers/screenshot

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install mcp

# Configure OpenCode
python configure.py
```

### Permissions

On macOS, screen capture requires the "Screen Recording" permission:

1. Go to **System Settings** > **Privacy & Security** > **Screen Recording**
2. Enable permission for your terminal app (Terminal, iTerm2, etc.)

## Usage

The server provides a single tool: `screenshot`

### Parameters

| Parameter | Type | Required | Default | Description |
|-----------|------|----------|---------|-------------|
| `mode` | string | No | `screen` | `screen` or `window` |
| `window_title` | string | If mode=window | - | Window title (partial match) |
| `screen_index` | integer | No | `0` | Screen index (0 = main) |
| `format` | string | No | `png` | `png` or `jpg` |
| `delay` | number | No | `0` | Seconds to wait before capture |

### Examples

**Capture full screen:**
```
Use the screenshot tool to capture my screen
```

**Capture a specific window:**
```
Use the screenshot tool to capture the "Terminal" window
```

**Capture with delay:**
```
Use the screenshot tool with a 3 second delay
```

### Output

The tool returns:
- File path to the captured image
- Image dimensions (width x height)
- Format (png/jpg)
- Window title (if capturing a window)

Screenshots are saved to `/tmp/mcp-screenshot/` and automatically cleaned up after 24 hours.

## Troubleshooting

### "Screenshot file was not created"

Screen Recording permission is not granted. Go to System Settings > Privacy & Security > Screen Recording and enable your terminal app.

### "Window not found"

The window title doesn't match any open window. The error message will show available windows to help you find the correct title.

### Window capture returns wrong window

Try using a more specific window title. The search does partial matching, so "Terminal" might match multiple windows.

## Development

```bash
# Run server directly
python -m server

# Test capture
python -c "from screenshotter import capture_screen; print(capture_screen())"
```
