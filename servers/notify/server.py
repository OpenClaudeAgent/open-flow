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
        ),
        Tool(
            name="notify_commit",
            description="Notify the user that a commit was made. Use this after committing changes.",
            inputSchema={
                "type": "object",
                "properties": {
                    "branch": {
                        "type": "string",
                        "description": "Branch name where the commit was made.",
                    },
                    "message": {
                        "type": "string",
                        "description": "Commit message (first line).",
                    },
                    "files": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List of modified files.",
                    },
                    "hash": {
                        "type": "string",
                        "description": "Short commit hash (7 chars).",
                    },
                    "agent": {
                        "type": "string",
                        "description": "Name of the agent that made the commit.",
                    },
                },
                "required": ["branch", "message"],
            },
        ),
        Tool(
            name="notify_merge",
            description="Notify the user that a branch was merged to main. Use this after merging.",
            inputSchema={
                "type": "object",
                "properties": {
                    "source_branch": {
                        "type": "string",
                        "description": "Branch that was merged.",
                    },
                    "commits_count": {
                        "type": "integer",
                        "description": "Number of commits merged.",
                    },
                    "files_count": {
                        "type": "integer",
                        "description": "Number of files changed.",
                    },
                    "version": {
                        "type": "string",
                        "description": "Version tag if any (e.g., v0.5.0).",
                    },
                    "repo": {
                        "type": "string",
                        "description": "Repository name.",
                    },
                    "agent": {
                        "type": "string",
                        "description": "Name of the agent that performed the merge.",
                    },
                },
                "required": ["source_branch"],
            },
        ),
        Tool(
            name="notify_sync",
            description="Notify the user that worktrees were synchronized. Use after sync-worktrees.",
            inputSchema={
                "type": "object",
                "properties": {
                    "worktrees": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List of worktrees that were synchronized.",
                    },
                    "source": {
                        "type": "string",
                        "description": "Source branch (default: main).",
                    },
                    "repo": {
                        "type": "string",
                        "description": "Repository name.",
                    },
                    "conflicts": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List of conflicts if any.",
                    },
                },
                "required": ["worktrees"],
            },
        ),
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    """Handle tool calls."""
    if name == "ask_user":
        return await _handle_ask_user(arguments)
    elif name == "notify_commit":
        return await _handle_notify_commit(arguments)
    elif name == "notify_merge":
        return await _handle_notify_merge(arguments)
    elif name == "notify_sync":
        return await _handle_notify_sync(arguments)
    else:
        return [TextContent(type="text", text=f"Unknown tool: {name}")]


async def _handle_ask_user(arguments: dict) -> list[TextContent]:
    """Handle ask_user tool call."""
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


async def _handle_notify_commit(arguments: dict) -> list[TextContent]:
    """Handle notify_commit tool call."""
    branch = arguments.get("branch", "unknown")
    message = arguments.get("message", "")
    files = arguments.get("files", [])
    commit_hash = arguments.get("hash", "")
    agent = arguments.get("agent")

    # Build notification body
    body_parts = [message]
    if files:
        files_str = ", ".join(files[:5])  # Limit to 5 files
        if len(files) > 5:
            files_str += f" (+{len(files) - 5} more)"
        body_parts.append(f"Files: {files_str}")

    body = "\n".join(body_parts)

    # Send notification with low urgency (info type)
    success = send_notification(
        title="Commit",
        message=body,
        type="info",  # low urgency = info (Ping sound)
        sound=True,
        agent=agent,
        repo=branch,  # Branch as subtitle
    )

    if success:
        hash_info = f" {commit_hash}" if commit_hash else ""
        return [
            TextContent(type="text", text=f"Commit notified:{hash_info} on {branch}")
        ]
    else:
        return [
            TextContent(
                type="text",
                text="Failed to send notification. Platform may not be supported.",
            )
        ]


async def _handle_notify_merge(arguments: dict) -> list[TextContent]:
    """Handle notify_merge tool call."""
    source_branch = arguments.get("source_branch", "unknown")
    commits_count = arguments.get("commits_count")
    files_count = arguments.get("files_count")
    version = arguments.get("version")
    repo = arguments.get("repo")
    agent = arguments.get("agent")

    # Build notification body
    body_parts = [f"{source_branch} → main"]

    stats = []
    if commits_count:
        stats.append(f"{commits_count} commit{'s' if commits_count > 1 else ''}")
    if files_count:
        stats.append(f"{files_count} file{'s' if files_count > 1 else ''}")
    if stats:
        body_parts.append(", ".join(stats))

    if version:
        body_parts.append(f"Version: {version}")

    body = "\n".join(body_parts)

    # Send notification with normal urgency (warning type)
    success = send_notification(
        title="Merge sur main",
        message=body,
        type="warning",  # normal urgency = warning (Funk sound)
        sound=True,
        agent=agent,
        repo=repo,  # Repo as subtitle
    )

    if success:
        return [
            TextContent(type="text", text=f"Merge notified: {source_branch} → main")
        ]
    else:
        return [
            TextContent(
                type="text",
                text="Failed to send notification. Platform may not be supported.",
            )
        ]


async def _handle_notify_sync(arguments: dict) -> list[TextContent]:
    """Handle notify_sync tool call."""
    worktrees = arguments.get("worktrees", [])
    source = arguments.get("source", "main")
    repo = arguments.get("repo")
    conflicts = arguments.get("conflicts", [])

    # Build notification body
    count = len(worktrees)
    body_parts = [f"{count} worktree{'s' if count > 1 else ''} updated from {source}"]

    if worktrees:
        worktrees_str = ", ".join(worktrees[:5])  # Limit to 5
        if len(worktrees) > 5:
            worktrees_str += f" (+{len(worktrees) - 5} more)"
        body_parts.append(worktrees_str)

    if conflicts:
        body_parts.append(f"⚠️ Conflicts: {', '.join(conflicts)}")

    body = "\n".join(body_parts)

    # Determine urgency based on conflicts
    ntype = "warning" if conflicts else "info"  # Conflicts = normal, no conflicts = low

    # Send notification
    success = send_notification(
        title="Worktrees synchronisés",
        message=body,
        type=ntype,
        sound=True,
        repo=repo,  # Repo as subtitle
    )

    if success:
        return [
            TextContent(type="text", text=f"Sync notified: {count} worktrees updated")
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
