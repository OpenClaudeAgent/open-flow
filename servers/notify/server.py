"""MCP Server for system notifications."""

import asyncio
from typing import Literal

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

from notifier import send_notification, NotificationType


# Create the MCP server
server = Server("notify")


@server.list_tools()
async def list_tools() -> list[Tool]:
    """List available tools."""
    return [
        Tool(
            name="notify",
            description=(
                "Send a system notification to the user. "
                "Use this when you need to alert the user about something important, "
                "such as task completion, errors, or when user input is required. "
                "The notification will appear in the system notification center with a sound."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string",
                        "description": "Short title for the notification",
                    },
                    "message": {
                        "type": "string",
                        "description": "Body text of the notification",
                    },
                    "type": {
                        "type": "string",
                        "enum": ["info", "success", "warning", "error"],
                        "description": (
                            "Type of notification: "
                            "info (general), success (task completed), "
                            "warning (attention needed), error (problem occurred)"
                        ),
                        "default": "info",
                    },
                    "sound": {
                        "type": "boolean",
                        "description": "Whether to play a notification sound",
                        "default": True,
                    },
                },
                "required": ["title", "message"],
            },
        )
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    """Handle tool calls."""
    if name != "notify":
        return [TextContent(type="text", text=f"Unknown tool: {name}")]

    title = arguments.get("title", "Notification")
    message = arguments.get("message", "")
    ntype = arguments.get("type", "info")
    sound = arguments.get("sound", True)

    # Send the notification
    success = send_notification(title=title, message=message, type=ntype, sound=sound)

    if success:
        emoji = {"info": "ℹ️", "success": "✅", "warning": "⚠️", "error": "❌"}.get(
            ntype, "📢"
        )

        return [TextContent(type="text", text=f"{emoji} Notification sent: {title}")]
    else:
        return [
            TextContent(
                type="text",
                text=f"Failed to send notification. Platform may not be supported.",
            )
        ]


async def main():
    """Run the MCP server."""
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream, write_stream, server.create_initialization_options()
        )


def run():
    """Entry point for the server."""
    asyncio.run(main())


if __name__ == "__main__":
    run()
