"""
Register OpenAI-style tools with FastMCP.
"""
from typing import Callable
from fastmcp import FastMCP

def register_openai_tool(mcp: FastMCP, fn: Callable, openai_tool_def: dict) -> None:
    """
    NOTE: CURRENTLY DOES NOT WORK DUE TO COMPLICATIONS WITH INJECTING CONTEXT (`ctx`).

    Registers a plain function with FastMCP using OpenAI-style tool definition metadata.

    :param: mcp (FastMCP): The FastMCP instance to register the tool with.
    :param: fn (Callable): The function to register as a tool.
    :param: openai_tool_def (dict): OpenAI-style tool definition containing metadata.
    :returns: None
    """
    name = openai_tool_def["function"]["name"]

    meta = openai_tool_def["function"]
    description = meta.get("description", None)
    mcp.tool(name=name, description=description)(fn)
