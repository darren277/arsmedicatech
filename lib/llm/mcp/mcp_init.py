""""""
import json
from fastmcp import FastMCP
from fastmcp.server.middleware.timing import TimingMiddleware
from fastmcp.server.middleware.logging import LoggingMiddleware
from starlette.responses import PlainTextResponse
from starlette.requests import Request

mcp = FastMCP("Webhook API")

# plug‑in generic middleware
mcp.add_middleware(TimingMiddleware())
mcp.add_middleware(LoggingMiddleware())


@mcp.custom_route("/health", methods=["GET"])
async def health_check(request: Request) -> PlainTextResponse:
    print(f'Health check received from {request.client.host}')
    print(request.__dir__())
    return PlainTextResponse("OK")

@mcp.tool
def hello(name: str = "world") -> str:
    """
    Return a greeting.
    """
    return json.dumps(dict(msg=f"Hello, {name}!"))

#register_openai_tool(mcp, blood_pressure_decision_tree_lookup, tool_definition_bp)
