"""Cross-platform notification abstraction."""

import platform
import subprocess
import shutil
from dataclasses import dataclass
from enum import Enum
from typing import Optional


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
        emoji = EMOJIS.get(config.type, "")
        title = f"{emoji} {config.title}"

        if self.system == "Darwin":
            return self._send_macos(title, config.message, config.type, config.sound)
        elif self.system == "Linux":
            return self._send_linux(
                title, config.message, config.type, config.sound, config.timeout
            )
        elif self.system == "Windows":
            return self._send_windows(
                title, config.message, config.type, config.sound, config.timeout
            )
        else:
            return False

    def _send_macos(
        self, title: str, message: str, ntype: NotificationType, sound: bool
    ) -> bool:
        """Send notification on macOS using osascript."""
        sound_name = MACOS_SOUNDS.get(ntype, "default") if sound else ""

        # Escape quotes for AppleScript
        title_escaped = title.replace('"', '\\"')
        message_escaped = message.replace('"', '\\"')

        script = (
            f'display notification "{message_escaped}" with title "{title_escaped}"'
        )
        if sound:
            script += f' sound name "{sound_name}"'

        try:
            subprocess.run(["osascript", "-e", script], check=True, capture_output=True)
            return True
        except subprocess.CalledProcessError:
            return False

    def _send_linux(
        self,
        title: str,
        message: str,
        ntype: NotificationType,
        sound: bool,
        timeout: int,
    ) -> bool:
        """Send notification on Linux using notify-send."""
        if not shutil.which("notify-send"):
            return False

        # Map type to urgency
        urgency_map = {
            NotificationType.INFO: "normal",
            NotificationType.SUCCESS: "normal",
            NotificationType.WARNING: "normal",
            NotificationType.ERROR: "critical",
        }
        urgency = urgency_map.get(ntype, "normal")

        try:
            cmd = [
                "notify-send",
                "--urgency",
                urgency,
                "--expire-time",
                str(timeout * 1000),
                title,
                message,
            ]
            subprocess.run(cmd, check=True, capture_output=True)

            # Play sound if requested
            if sound:
                self._play_linux_sound(ntype)

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

    def _send_windows(
        self,
        title: str,
        message: str,
        ntype: NotificationType,
        sound: bool,
        timeout: int,
    ) -> bool:
        """Send notification on Windows using PowerShell."""
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
            <audio silent="{str(not sound).lower()}"/>
        </toast>
"@
        
        $xml = New-Object Windows.Data.Xml.Dom.XmlDocument
        $xml.LoadXml($template)
        $toast = [Windows.UI.Notifications.ToastNotification]::new($xml)
        [Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier("OpenCode").Show($toast)
        '''

        try:
            subprocess.run(
                ["powershell", "-Command", ps_script], check=True, capture_output=True
            )
            return True
        except (subprocess.CalledProcessError, FileNotFoundError):
            return False


def send_notification(
    title: str, message: str, type: str = "info", sound: bool = True, timeout: int = 10
) -> bool:
    """
    Convenience function to send a notification.

    Args:
        title: Notification title
        message: Notification body
        type: One of 'info', 'success', 'warning', 'error'
        sound: Whether to play a sound
        timeout: Display duration in seconds (Linux/Windows)

    Returns:
        True if notification was sent successfully.
    """
    try:
        ntype = NotificationType(type)
    except ValueError:
        ntype = NotificationType.INFO

    config = NotificationConfig(
        title=title, message=message, type=ntype, sound=sound, timeout=timeout
    )

    notifier = Notifier()
    return notifier.send(config)
