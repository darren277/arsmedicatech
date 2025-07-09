""""""
import datetime
from mcp_init import mcp

# --- import side‑effect modules that register tools ---
#from tools import ...

if __name__ == "__main__":
    ts = datetime.datetime.now().isoformat()
    print(f"Starting MCP server at {ts}...")

    mcp.run(
        transport="http",
        host="0.0.0.0",
        port=9000,
        path="/mcp",
        log_level="debug"
    )
