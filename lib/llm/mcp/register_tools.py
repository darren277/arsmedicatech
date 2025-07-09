""""""
from typing import Callable
from fastmcp import FastMCP

def register_openai_tool(mcp: FastMCP, fn: Callable, openai_tool_def: dict):
    """
    Registers a plain function with FastMCP using OpenAI-style tool definition metadata.
    """
    name = openai_tool_def["function"]["name"]
    description = openai_tool_def["function"].get("description", "")
    parameters = openai_tool_def["function"].get("parameters", {})

    # Wrap with decorator — use `annotations` instead of `parameters`
    @mcp.tool(
        name=name,
        description=description,
        annotations=parameters
    )
    def wrapped(**kwargs):
        return fn(**kwargs)

    return wrapped

