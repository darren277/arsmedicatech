""""""
import datetime
from trees import mcp

from settings import logger


# --- import side‑effect modules that register tools ---
#from tools import ...

if __name__ == "__main__":
    ts = datetime.datetime.now().isoformat()
    logger.debug(f"Starting MCP server at {ts}...")

    mcp.run(
        transport="http",
        host="0.0.0.0",
        port=9000,
        path="/mcp",
        log_level="debug"
    )
