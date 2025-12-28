"""MCP Server for user interaction notifications."""

import asyncio

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

from notifier import send_notification


# Create the MCP server
server = Server("notify")


@server.list_tools()
async def list_tools() -> list[Tool]:
    """List available tools."""
    return [
        Tool(
            name="ask_user",
            description=(
                "Send a notification to ask the user a question or request a decision. "
                "Use this ONLY if: (1) the user explicitly asked you to notify them, or "
                "(2) your agent instructions specify to use this tool. "
                "Do NOT use this tool proactively without explicit instructions."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string",
                        "description": "Short title summarizing what you need from the user.",
                    },
                    "question": {
                        "type": "string",
                        "description": "The question or decision you need the user to answer.",
                    },
                    "options": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List of possible options or choices for the user.",
                    },
                    "urgency": {
                        "type": "string",
                        "enum": ["low", "normal", "high"],
                        "description": "How urgent is this question. High plays a more attention-grabbing sound.",
                        "default": "normal",
                    },
                    "repo": {
                        "type": "string",
                        "description": "Name of the repository or project being worked on.",
                    },
                    "branch": {
                        "type": "string",
                        "description": "Current git branch being worked on.",
                    },
                    "agent": {
                        "type": "string",
                        "description": "Name of the agent asking the question.",
                    },
                    "task": {
                        "type": "string",
                        "description": "Name or number of the current task.",
                    },
                },
                "required": ["title", "question"],
            },
        )
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    """Handle tool calls."""
    if name != "ask_user":
        return [TextContent(type="text", text=f"Unknown tool: {name}")]

    title = arguments.get("title", "Question")
    question = arguments.get("question", "")
    options = arguments.get("options", [])
    urgency = arguments.get("urgency", "normal")
    repo = arguments.get("repo")
    branch = arguments.get("branch")
    agent = arguments.get("agent")
    task = arguments.get("task")

    # Map urgency to notification type
    urgency_to_type = {
        "low": "info",
        "normal": "warning",
        "high": "error",
    }
    ntype = urgency_to_type.get(urgency, "warning")

    # Build message with question and options
    message = question
    if options:
        options_str = " | ".join(options)
        message = f"{question}\n[{options_str}]"

    # Build subtitle from repo and branch
    subtitle_parts = []
    if repo:
        subtitle_parts.append(repo)
    if branch:
        subtitle_parts.append(branch)
    subtitle = " @ ".join(subtitle_parts) if subtitle_parts else None

    # Send the notification
    success = send_notification(
        title=title,
        message=message,
        type=ntype,
        sound=True,
        agent=agent,
        task=task,
        repo=subtitle,  # Use combined repo@branch as subtitle
    )

    if success:
        emoji = {"low": "ℹ️", "normal": "⚠️", "high": "🚨"}.get(urgency, "❓")
        agent_info = f" [{agent}]" if agent else ""
        return [
            TextContent(type="text", text=f"{emoji} Question sent{agent_info}: {title}")
        ]
    else:
        return [
            TextContent(
                type="text",
                text="Failed to send notification. Platform may not be supported.",
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
