"""Screenshot capture logic for macOS."""

import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path


# Temp directory for screenshots
SCREENSHOT_DIR = Path("/tmp/mcp-screenshot")


def ensure_screenshot_dir() -> Path:
    """Ensure the screenshot directory exists."""
    SCREENSHOT_DIR.mkdir(parents=True, exist_ok=True)
    return SCREENSHOT_DIR


def generate_filename(prefix: str = "screenshot", format: str = "png") -> Path:
    """Generate a timestamped filename for the screenshot."""
    timestamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    filename = f"{prefix}-{timestamp}.{format}"
    return ensure_screenshot_dir() / filename


def check_screen_recording_permission() -> bool:
    """Check if screen recording permission is granted on macOS.

    Returns True if permission is granted or if we can't determine.
    Returns False only if we're certain permission is denied.
    """
    if sys.platform != "darwin":
        return True

    # Try a quick capture to /dev/null to test permission
    try:
        result = subprocess.run(
            ["screencapture", "-x", "-t", "png", "/dev/null"],
            capture_output=True,
            timeout=5,
        )
        # screencapture returns 0 even without permission, but produces empty file
        # We can't reliably detect this, so assume permission is granted
        return True
    except Exception:
        return True


def get_permission_instructions() -> str:
    """Return instructions for granting screen recording permission."""
    return (
        "Screen recording permission required.\n"
        "Go to: System Settings > Privacy & Security > Screen Recording\n"
        "Enable permission for your terminal application (Terminal, iTerm2, etc.)"
    )


def capture_screen(
    screen_index: int = 0,
    format: str = "png",
    delay: float = 0,
) -> dict:
    """Capture the entire screen.

    Args:
        screen_index: Index of the screen to capture (0 = main screen)
        format: Image format (png or jpg)
        delay: Delay in seconds before capture

    Returns:
        dict with path, width, height, format, or error
    """
    if sys.platform != "darwin":
        return {"error": "Screen capture is only supported on macOS"}

    filepath = generate_filename("screen", format)

    # Build screencapture command
    cmd = ["screencapture", "-x"]  # -x = no sound

    # Add delay if specified
    if delay > 0:
        cmd.extend(["-T", str(int(delay))])

    # Add format
    cmd.extend(["-t", format])

    # Add screen selection for multi-monitor
    if screen_index > 0:
        cmd.extend(["-D", str(screen_index + 1)])  # screencapture uses 1-based index

    cmd.append(str(filepath))

    try:
        result = subprocess.run(cmd, capture_output=True, timeout=30)

        if result.returncode != 0:
            return {"error": f"screencapture failed: {result.stderr.decode()}"}

        if not filepath.exists():
            return {
                "error": "Screenshot file was not created. Check screen recording permissions."
            }

        # Get image dimensions using sips
        dimensions = get_image_dimensions(filepath)

        return {
            "path": str(filepath),
            "format": format,
            **dimensions,
        }

    except subprocess.TimeoutExpired:
        return {"error": "Screenshot capture timed out"}
    except Exception as e:
        return {"error": f"Screenshot capture failed: {str(e)}"}


def capture_window(
    window_title: str,
    format: str = "png",
    delay: float = 0,
) -> dict:
    """Capture a window by its title.

    Args:
        window_title: Full or partial window title to match
        format: Image format (png or jpg)
        delay: Delay in seconds before capture

    Returns:
        dict with path, width, height, format, window_title, or error
    """
    if sys.platform != "darwin":
        return {"error": "Window capture is only supported on macOS"}

    # Find window ID by title
    window_info = find_window_by_title(window_title)

    if window_info is None:
        available = list_windows()
        return {
            "error": f"Window not found: '{window_title}'",
            "available_windows": available[:10],  # Limit to 10
        }

    window_id = window_info["id"]
    actual_title = window_info["title"]

    filepath = generate_filename("window", format)

    # Build screencapture command for window
    cmd = ["screencapture", "-x", "-l", str(window_id)]

    if delay > 0:
        cmd.extend(["-T", str(int(delay))])

    cmd.extend(["-t", format])
    cmd.append(str(filepath))

    try:
        result = subprocess.run(cmd, capture_output=True, timeout=30)

        if result.returncode != 0:
            return {"error": f"screencapture failed: {result.stderr.decode()}"}

        if not filepath.exists():
            return {
                "error": "Screenshot file was not created. Check screen recording permissions."
            }

        dimensions = get_image_dimensions(filepath)

        return {
            "path": str(filepath),
            "format": format,
            "window_title": actual_title,
            **dimensions,
        }

    except subprocess.TimeoutExpired:
        return {"error": "Screenshot capture timed out"}
    except Exception as e:
        return {"error": f"Screenshot capture failed: {str(e)}"}


def find_window_by_title(title: str) -> dict | None:
    """Find a window by its title (partial match).

    Returns dict with 'id' and 'title' if found, None otherwise.
    """
    try:
        # Use AppleScript to get window list with IDs
        script = """
        set windowList to ""
        tell application "System Events"
            set allProcesses to every process whose background only is false
            repeat with proc in allProcesses
                try
                    set procName to name of proc
                    set procWindows to every window of proc
                    repeat with win in procWindows
                        set winName to name of win
                        set winId to id of win
                        set windowList to windowList & winId & "|||" & winName & "|||" & procName & "\\n"
                    end repeat
                end try
            end repeat
        end tell
        return windowList
        """

        result = subprocess.run(
            ["osascript", "-e", script],
            capture_output=True,
            timeout=10,
        )

        if result.returncode != 0:
            # Fallback: use CGWindowListCopyWindowInfo via Python (if available)
            return find_window_by_title_fallback(title)

        output = result.stdout.decode().strip()
        title_lower = title.lower()

        for line in output.split("\n"):
            if "|||" not in line:
                continue
            parts = line.split("|||")
            if len(parts) >= 2:
                win_id, win_title = parts[0], parts[1]
                if title_lower in win_title.lower():
                    return {"id": int(win_id), "title": win_title}

        return None

    except Exception:
        return find_window_by_title_fallback(title)


def find_window_by_title_fallback(title: str) -> dict | None:
    """Fallback method using Quartz CGWindowListCopyWindowInfo."""
    try:
        import Quartz

        # Get all windows
        window_list = Quartz.CGWindowListCopyWindowInfo(
            Quartz.kCGWindowListOptionOnScreenOnly
            | Quartz.kCGWindowListExcludeDesktopElements,
            Quartz.kCGNullWindowID,
        )

        title_lower = title.lower()

        for window in window_list:
            window_title = window.get(Quartz.kCGWindowName, "")
            window_owner = window.get(Quartz.kCGWindowOwnerName, "")

            if window_title and title_lower in window_title.lower():
                return {
                    "id": window.get(Quartz.kCGWindowNumber),
                    "title": window_title,
                }
            # Also check owner name (app name)
            if window_owner and title_lower in window_owner.lower():
                return {
                    "id": window.get(Quartz.kCGWindowNumber),
                    "title": f"{window_owner}: {window_title}"
                    if window_title
                    else window_owner,
                }

        return None

    except ImportError:
        # Quartz not available, try simpler approach
        return find_window_simple(title)
    except Exception:
        return None


def find_window_simple(title: str) -> dict | None:
    """Simple window finding using screencapture -C (interactive) info."""
    # This is a last resort - we can list windows but getting IDs is tricky
    # For now, return None and let the caller handle it
    return None


def list_windows() -> list[str]:
    """List available window titles."""
    try:
        import Quartz

        window_list = Quartz.CGWindowListCopyWindowInfo(
            Quartz.kCGWindowListOptionOnScreenOnly
            | Quartz.kCGWindowListExcludeDesktopElements,
            Quartz.kCGNullWindowID,
        )

        titles = []
        for window in window_list:
            window_title = window.get(Quartz.kCGWindowName, "")
            window_owner = window.get(Quartz.kCGWindowOwnerName, "")
            if window_title:
                titles.append(f"{window_owner}: {window_title}")
            elif window_owner:
                titles.append(window_owner)

        return list(set(titles))  # Remove duplicates

    except ImportError:
        return ["(Install pyobjc-framework-Quartz to list windows)"]
    except Exception:
        return []


def get_image_dimensions(filepath: Path) -> dict:
    """Get image dimensions using sips (macOS)."""
    try:
        result = subprocess.run(
            ["sips", "-g", "pixelWidth", "-g", "pixelHeight", str(filepath)],
            capture_output=True,
            timeout=5,
        )

        output = result.stdout.decode()
        width = height = None

        for line in output.split("\n"):
            if "pixelWidth" in line:
                width = int(line.split(":")[-1].strip())
            elif "pixelHeight" in line:
                height = int(line.split(":")[-1].strip())

        return {"width": width, "height": height}

    except Exception:
        return {"width": None, "height": None}


def cleanup_old_screenshots(max_age_hours: int = 24) -> int:
    """Remove screenshots older than max_age_hours.

    Returns the number of files deleted.
    """
    if not SCREENSHOT_DIR.exists():
        return 0

    deleted = 0
    now = datetime.now()

    for filepath in SCREENSHOT_DIR.glob("*.png"):
        try:
            mtime = datetime.fromtimestamp(filepath.stat().st_mtime)
            age_hours = (now - mtime).total_seconds() / 3600

            if age_hours > max_age_hours:
                filepath.unlink()
                deleted += 1
        except Exception:
            pass

    for filepath in SCREENSHOT_DIR.glob("*.jpg"):
        try:
            mtime = datetime.fromtimestamp(filepath.stat().st_mtime)
            age_hours = (now - mtime).total_seconds() / 3600

            if age_hours > max_age_hours:
                filepath.unlink()
                deleted += 1
        except Exception:
            pass

    return deleted
