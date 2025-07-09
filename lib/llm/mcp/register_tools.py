""""""
from typing import Callable
from fastmcp import FastMCP

def register_openai_tool(mcp: FastMCP, fn: Callable, openai_tool_def: dict):
    """
    Registers a plain function with FastMCP using OpenAI-style tool definition metadata.
    """
    name = openai_tool_def["function"]["name"]

    meta = openai_tool_def["function"]
    description = meta.get("description", None)
    mcp.tool(name=name, description=description)(fn)
