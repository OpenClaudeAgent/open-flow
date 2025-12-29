"""MCP Server for screenshot capture."""

import asyncio

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

from screenshotter import (
    capture_screen,
    capture_window,
    cleanup_old_screenshots,
    get_permission_instructions,
)


# Create the MCP server
server = Server("screenshot")


@server.list_tools()
async def list_tools() -> list[Tool]:
    """List available tools."""
    return [
        Tool(
            name="screenshot",
            description=(
                "Capture a screenshot of the screen or a specific window on macOS. "
                "Use mode='screen' to capture the entire screen, or mode='window' "
                "with window_title to capture a specific window. "
                "Returns the file path and dimensions of the captured image."
            ),
            inputSchema={
                "type": "object",
                "properties": {
                    "mode": {
                        "type": "string",
                        "enum": ["screen", "window"],
                        "description": "Capture mode: 'screen' for full screen, 'window' for a specific window.",
                        "default": "screen",
                    },
                    "window_title": {
                        "type": "string",
                        "description": "Title (or partial title) of the window to capture. Required when mode='window'.",
                    },
                    "screen_index": {
                        "type": "integer",
                        "description": "Screen index for multi-monitor setups. 0 = main screen.",
                        "default": 0,
                    },
                    "format": {
                        "type": "string",
                        "enum": ["png", "jpg"],
                        "description": "Image format.",
                        "default": "png",
                    },
                    "delay": {
                        "type": "number",
                        "description": "Delay in seconds before capturing.",
                        "default": 0,
                    },
                },
                "required": [],
            },
        )
    ]


@server.call_tool()
async def call_tool(name: str, arguments: dict) -> list[TextContent]:
    """Handle tool calls."""
    if name != "screenshot":
        return [TextContent(type="text", text=f"Unknown tool: {name}")]

    mode = arguments.get("mode", "screen")
    window_title = arguments.get("window_title")
    screen_index = arguments.get("screen_index", 0)
    format = arguments.get("format", "png")
    delay = arguments.get("delay", 0)

    # Cleanup old screenshots (non-blocking, best effort)
    try:
        cleanup_old_screenshots(max_age_hours=24)
    except Exception:
        pass

    # Capture based on mode
    if mode == "window":
        if not window_title:
            return [
                TextContent(
                    type="text",
                    text="Error: window_title is required when mode='window'",
                )
            ]
        result = capture_window(
            window_title=window_title,
            format=format,
            delay=delay,
        )
    else:  # mode == "screen"
        result = capture_screen(
            screen_index=screen_index,
            format=format,
            delay=delay,
        )

    # Handle errors
    if "error" in result:
        error_msg = result["error"]

        # Add available windows if present
        if "available_windows" in result:
            windows = result["available_windows"]
            if windows:
                error_msg += f"\n\nAvailable windows:\n" + "\n".join(
                    f"  - {w}" for w in windows
                )

        # Add permission instructions if relevant
        if "permission" in error_msg.lower():
            error_msg += f"\n\n{get_permission_instructions()}"

        return [TextContent(type="text", text=f"Screenshot failed: {error_msg}")]

    # Success response
    path = result.get("path", "unknown")
    width = result.get("width", "?")
    height = result.get("height", "?")
    fmt = result.get("format", "png")

    response = f"Screenshot captured: {path}\nDimensions: {width}x{height} ({fmt})"

    if "window_title" in result:
        response += f"\nWindow: {result['window_title']}"

    return [TextContent(type="text", text=response)]


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
