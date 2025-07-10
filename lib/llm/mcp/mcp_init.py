""""""
import json
from fastmcp import FastMCP
from fastmcp.server.middleware.timing import TimingMiddleware
from fastmcp.server.middleware.logging import LoggingMiddleware
from openai import AsyncOpenAI
from starlette.responses import PlainTextResponse
from starlette.requests import Request
from fastmcp.server.dependencies import get_http_request

from lib.services.encryption import get_encryption_service

mcp = FastMCP("ArsMedicaTech MCP Server")

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

@mcp.tool
async def rag(query: str) -> str:
    """
    Perform a retrieval-augmented generation (RAG) query.
    :param query:
    :return:
    """
    request: Request = get_http_request()

    openai_api_key = request.headers.get("x-user-openai-key")
    key = get_encryption_service().decrypt_api_key(openai_api_key)

    client = AsyncOpenAI(api_key=key)

    from lib.db.vec import Vec
    vec = Vec(client)
    print(f"RAG query: {query}")
    msg = await vec.rag_chat(query)
    print(f"RAG response: {msg}")
    return json.dumps(dict(msg=msg))
