"""
ArsMedicaTech MCP Server Initialization
"""
import json

from fastmcp import Context, FastMCP
from fastmcp.server.dependencies import get_http_request
from fastmcp.server.middleware.logging import LoggingMiddleware
from fastmcp.server.middleware.timing import TimingMiddleware
from openai import AsyncOpenAI
from starlette.requests import Request
from starlette.responses import PlainTextResponse

from lib.services.encryption import get_encryption_service
from settings import logger

mcp: FastMCP[Context] = FastMCP("ArsMedicaTech MCP Server")

# plug‑in generic middleware
mcp.add_middleware(TimingMiddleware())
mcp.add_middleware(LoggingMiddleware())


@mcp.custom_route("/health", methods=["GET"])  # type: ignore[misc]
async def health_check(request: Request) -> PlainTextResponse:
    """
    Health check endpoint to verify server status.
    :param request: Request object containing client information.
    :return: PlainTextResponse indicating server health.
    """
    client_host: str = "unknown"
    if request.client is not None:
        client_host = request.client.host
    logger.debug(f'Health check received from {client_host}')
    logger.debug(str(request.__dir__()))
    return PlainTextResponse("OK")


@mcp.tool
def hello(name: str = "world") -> str:
    """
    Return a greeting.
    :param name: Name to greet, defaults to "world".
    :return: JSON string containing the greeting message.
    """
    return json.dumps(dict(msg=f"Hello, {name}!"))

# register_openai_tool(mcp, blood_pressure_decision_tree_lookup, tool_definition_bp)


@mcp.tool
async def rag(query: str) -> str:
    """
    Perform a retrieval-augmented generation (RAG) query.
    :param query: The query string to search for relevant information.
    :return: JSON string containing the response message.
    """
    req: Request = get_http_request()

    enc_key = req.headers.get("x-session-token")
    logger.debug('ACTUAL HEADERS:', req.headers, req.headers.__dir__())
    logger.debug(f"===> Encrypted key from context: {enc_key}")
    if not enc_key:
        raise ValueError("No encrypted key provided in header.")

    key = get_encryption_service().decrypt_api_key(enc_key)

    if not key:
        raise ValueError("No OpenAI API key provided in the request headers.")

    logger.debug(f"===> Using OpenAI API key: {key}")

    client = AsyncOpenAI(api_key=key)

    from lib.db.vec import Vec
    vec = Vec(client)
    logger.debug(f"RAG query: {query}")
    msg = await vec.rag_chat(query)
    logger.debug(f"RAG response: {msg}")
    return json.dumps(dict(msg=msg))
