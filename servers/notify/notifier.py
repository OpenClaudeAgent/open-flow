"""Cross-platform notification abstraction."""

import platform
import subprocess
import shutil
from dataclasses import dataclass
from enum import Enum
from typing import Optional, Any
from pathlib import Path

# Conditional PyObjC import for macOS
PYOBJC_AVAILABLE = False
NSUserNotification: Any = None
NSUserNotificationCenter: Any = None
NSImage: Any = None

if platform.system() == "Darwin":
    try:
        from Foundation import (  # type: ignore[import-not-found]
            NSUserNotification,
            NSUserNotificationCenter,
        )
        from AppKit import NSImage  # type: ignore[import-not-found]

        PYOBJC_AVAILABLE = True
    except ImportError:
        pass


class NotificationType(Enum):
    """Type of notification, affects emoji and sound."""

    INFO = "info"
    SUCCESS = "success"
    WARNING = "warning"
    ERROR = "error"


@dataclass
class NotificationConfig:
    """Configuration for a notification."""

    title: str
    message: str
    type: NotificationType = NotificationType.INFO
    sound: bool = True
    timeout: int = 10
    agent: Optional[str] = None
    task: Optional[str] = None
    repo: Optional[str] = None


# Emoji mapping for notification types
EMOJIS = {
    NotificationType.INFO: "ℹ️",
    NotificationType.SUCCESS: "✅",
    NotificationType.WARNING: "⚠️",
    NotificationType.ERROR: "❌",
}

# macOS sound mapping
MACOS_SOUNDS = {
    NotificationType.INFO: "Blow",
    NotificationType.SUCCESS: "Glass",
    NotificationType.WARNING: "Basso",
    NotificationType.ERROR: "Sosumi",
}


def _get_icon_path() -> Optional[str]:
    """Get the path to the notification icon."""
    # Look for icon in assets folder relative to this file
    module_dir = Path(__file__).parent
    icon_path = module_dir / "assets" / "icon.png"
    if icon_path.exists():
        return str(icon_path)
    return None


class Notifier:
    """Cross-platform notification sender."""

    def __init__(self):
        self.system = platform.system()

    def send(self, config: NotificationConfig) -> bool:
        """
        Send a notification to the system.

        Returns:
            True if notification was sent successfully.
        """
        if self.system == "Darwin":
            return self._send_macos(config)
        elif self.system == "Linux":
            return self._send_linux(config)
        elif self.system == "Windows":
            return self._send_windows(config)
        else:
            return False

    def _send_macos(self, config: NotificationConfig) -> bool:
        """Send notification on macOS, preferring PyObjC over osascript."""
        if PYOBJC_AVAILABLE:
            return self._send_macos_pyobjc(config)
        else:
            return self._send_macos_osascript(config)

    def _send_macos_pyobjc(self, config: NotificationConfig) -> bool:
        """Send notification on macOS using PyObjC (native API)."""
        try:
            # Create notification
            notification = NSUserNotification.alloc().init()

            # Build title with emoji
            emoji = EMOJIS.get(config.type, "")
            title = f"{emoji} {config.title}"
            notification.setTitle_(title)

            # Set subtitle: repo name if provided
            if config.repo:
                notification.setSubtitle_(config.repo)

            # Build message with agent and task context
            message_parts = []
            if config.agent:
                message_parts.append(config.agent.capitalize())
            if config.task:
                message_parts.append(config.task)

            if message_parts:
                prefix = " | ".join(message_parts)
                message = f"{prefix} - {config.message}"
            else:
                message = config.message
            notification.setInformativeText_(message)

            # Note: setContentImage_ displays a large image (not suitable)
            # The app icon (Python) is shown automatically

            # Play sound if requested
            if config.sound:
                sound_name = MACOS_SOUNDS.get(config.type, "default")
                notification.setSoundName_(sound_name)

            # Disable actions - notification does nothing when clicked
            # By not setting any action buttons, the notification just dismisses on click
            notification.setHasActionButton_(False)

            # Deliver notification
            center = NSUserNotificationCenter.defaultUserNotificationCenter()
            center.deliverNotification_(notification)

            return True
        except Exception:
            # Fallback to osascript if PyObjC fails
            return self._send_macos_osascript(config)

    def _send_macos_osascript(self, config: NotificationConfig) -> bool:
        """Send notification on macOS using osascript (fallback)."""
        emoji = EMOJIS.get(config.type, "")
        title = f"{emoji} {config.title}"
        sound_name = MACOS_SOUNDS.get(config.type, "default") if config.sound else ""

        # Build message with context
        message_parts = []
        if config.repo:
            message_parts.append(f"[{config.repo}]")
        if config.agent:
            message_parts.append(config.agent.capitalize())
        if config.task:
            message_parts.append(config.task)

        if message_parts:
            prefix = " | ".join(message_parts)
            message = f"{prefix} - {config.message}"
        else:
            message = config.message

        # Escape quotes for AppleScript
        title_escaped = title.replace('"', '\\"')
        message_escaped = message.replace('"', '\\"')

        script = (
            f'display notification "{message_escaped}" with title "{title_escaped}"'
        )
        if config.sound:
            script += f' sound name "{sound_name}"'

        try:
            subprocess.run(["osascript", "-e", script], check=True, capture_output=True)
            return True
        except subprocess.CalledProcessError:
            return False

    def _send_linux(self, config: NotificationConfig) -> bool:
        """Send notification on Linux using notify-send."""
        if not shutil.which("notify-send"):
            return False

        emoji = EMOJIS.get(config.type, "")
        title = f"{emoji} {config.title}"

        # Build message with context
        message_parts = []
        if config.repo:
            message_parts.append(f"[{config.repo}]")
        if config.agent:
            message_parts.append(config.agent.capitalize())
        if config.task:
            message_parts.append(config.task)

        if message_parts:
            prefix = " | ".join(message_parts)
            message = f"{prefix} - {config.message}"
        else:
            message = config.message

        # Map type to urgency
        urgency_map = {
            NotificationType.INFO: "normal",
            NotificationType.SUCCESS: "normal",
            NotificationType.WARNING: "normal",
            NotificationType.ERROR: "critical",
        }
        urgency = urgency_map.get(config.type, "normal")

        try:
            cmd = [
                "notify-send",
                "--urgency",
                urgency,
                "--expire-time",
                str(config.timeout * 1000),
                title,
                message,
            ]
            subprocess.run(cmd, check=True, capture_output=True)

            # Play sound if requested
            if config.sound:
                self._play_linux_sound(config.type)

            return True
        except subprocess.CalledProcessError:
            return False

    def _play_linux_sound(self, ntype: NotificationType) -> None:
        """Play a sound on Linux using paplay or aplay."""
        # Try common sound paths
        sound_files = {
            NotificationType.INFO: "/usr/share/sounds/freedesktop/stereo/message.oga",
            NotificationType.SUCCESS: "/usr/share/sounds/freedesktop/stereo/complete.oga",
            NotificationType.WARNING: "/usr/share/sounds/freedesktop/stereo/dialog-warning.oga",
            NotificationType.ERROR: "/usr/share/sounds/freedesktop/stereo/dialog-error.oga",
        }

        sound_file = sound_files.get(ntype)
        if not sound_file:
            return

        # Try paplay first (PulseAudio), then aplay (ALSA)
        for player in ["paplay", "aplay"]:
            if shutil.which(player):
                try:
                    subprocess.run(
                        [player, sound_file], check=True, capture_output=True
                    )
                    break
                except subprocess.CalledProcessError:
                    continue

    def _send_windows(self, config: NotificationConfig) -> bool:
        """Send notification on Windows using PowerShell."""
        emoji = EMOJIS.get(config.type, "")
        title = f"{emoji} {config.title}"

        # Build message with context
        message_parts = []
        if config.repo:
            message_parts.append(f"[{config.repo}]")
        if config.agent:
            message_parts.append(config.agent.capitalize())
        if config.task:
            message_parts.append(config.task)

        if message_parts:
            prefix = " | ".join(message_parts)
            message = f"{prefix} - {config.message}"
        else:
            message = config.message

        # PowerShell script for toast notification
        ps_script = f'''
        [Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime] | Out-Null
        [Windows.Data.Xml.Dom.XmlDocument, Windows.Data.Xml.Dom.XmlDocument, ContentType = WindowsRuntime] | Out-Null
        
        $template = @"
        <toast duration="short">
            <visual>
                <binding template="ToastText02">
                    <text id="1">{title}</text>
                    <text id="2">{message}</text>
                </binding>
            </visual>
            <audio silent="{str(not config.sound).lower()}"/>
        </toast>
"@
        
        $xml = New-Object Windows.Data.Xml.Dom.XmlDocument
        $xml.LoadXml($template)
        $toast = [Windows.UI.Notifications.ToastNotification]::new($xml)
        [Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier("OpenFlow").Show($toast)
        '''

        try:
            subprocess.run(
                ["powershell", "-Command", ps_script], check=True, capture_output=True
            )
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            return False


def send_notification(
    title: str,
    message: str,
    type: str = "info",
    sound: bool = True,
    timeout: int = 10,
    agent: Optional[str] = None,
    task: Optional[str] = None,
    repo: Optional[str] = None,
) -> bool:
    """
    Convenience function to send a notification.

    Args:
        title: Notification title
        message: Notification body
        type: One of 'info', 'success', 'warning', 'error'
        sound: Whether to play a sound
        timeout: Display duration in seconds (Linux/Windows)
        agent: Name of the agent sending the notification (optional)
        task: Name or number of the current task (optional)
        repo: Name of the repository/project (optional, shown as subtitle on macOS)

    Returns:
        True if notification was sent successfully.
    """
    try:
        ntype = NotificationType(type)
    except ValueError:
        ntype = NotificationType.INFO

    config = NotificationConfig(
        title=title,
        message=message,
        type=ntype,
        sound=sound,
        timeout=timeout,
        agent=agent,
        task=task,
        repo=repo,
    )

    notifier = Notifier()
    return notifier.send(config)
