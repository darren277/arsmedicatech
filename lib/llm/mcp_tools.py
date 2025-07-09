""""""
from fastmcp.client import Client

async def fetch_mcp_tool_defs(mcp_url: str) -> tuple[list[dict], dict]:
    """
    • Pull the tool list from an MCP server
    • Convert each tool's JSON-Schema → OpenAI 'tool' format
    • Return (openai_tool_defs, {tool_name: call_function})
    """
    async with Client(mcp_url) as c:
        tools = (await c.tools.list()).tools   # dict[name → Tool]

    openai_defs: list[dict] = []
    func_lookup: dict[str, callable] = {}

    # Per‑tool wrapper that calls MCP via the Python client
    def wrap(tool_name):
        async def _call(**kwargs):
            async with Client(mcp_url) as c:
                result = await c.tools.call(name=tool_name, arguments=kwargs)
                return result.structured_content or result.content
        return _call

    for name, tool in tools.items():
        openai_defs.append({
            "type": "function",
            "function": {
                "name": name,
                "description": tool.description or "",
                "parameters": tool.parameters
            }
        })
        func_lookup[name] = wrap(name)

    return openai_defs, func_lookup
