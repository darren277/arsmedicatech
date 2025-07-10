""""""
import httpx
from fastmcp.client import Client

class CustomHeaderAuth(httpx.Auth):
    def __init__(self, headers: dict[str, str]):
        self.headers = headers

    def auth_flow(self, request):
        for key, value in self.headers.items():
            request.headers[key] = value
        yield request



async def fetch_mcp_tool_defs(mcp_url: str) -> tuple[list[dict], dict]:
    """
    • Pull the tool list from an MCP server
    • Convert each tool's JSON-Schema → OpenAI 'tool' format
    • Return (openai_tool_defs, {tool_name: call_function})
    """
    async with Client(mcp_url) as c:
        print('Fetching tools from MCP server:', mcp_url)
        print(c.__dir__())
        #tools = (await c.tools.list()).tools   # dict[name → Tool]
        tools = (await c.list_tools())  # [Tool]
        print('tools', tools)

    openai_defs: list[dict] = []
    func_lookup: dict[str, callable] = {}

    # Per‑tool wrapper that calls MCP via the Python client
    def wrap(tool_name):
        async def _call(*, session_id: str, **kwargs):
            custom_auth = CustomHeaderAuth({
                "x-user-id": "optional to add later...",
                "x-session-token": session_id
            })

            async with Client(mcp_url, auth=custom_auth) as c:
                # 'call_tool_mcp', 'call_tool'
                #result = await c.tools.call(name=tool_name, arguments=kwargs)
                # result = await client.call_tool("my_tool", {"param": "value"})
                print(f"[DEBUG] Calling tool: {tool_name} with args:", kwargs)
                result = await c.call_tool(tool_name, kwargs)
                print(f"[DEBUG] Tool call result for {tool_name}:", result)
                if hasattr(result, 'structured_content'):
                    return result.structured_content or result.content
                else:
                    return result.content or result
        return _call

    tool_dict = {tool.name: tool for tool in tools}

    for name, tool in tool_dict.items():
        openai_defs.append({
            "type": "function",
            "function": {
                "name": name,
                "description": tool.description or "",
                #"parameters": tool.parameters
                "parameters": {
                    "type": "object",
                    "properties": tool.inputSchema.get("properties", {}),
                    "required": tool.inputSchema.get("required", []),
                }
            }
        })
        func_lookup[name] = wrap(name)

    return openai_defs, func_lookup
