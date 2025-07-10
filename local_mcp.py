""""""
import datetime

import os

# add pwd to path...
import sys
sys.path.append(os.path.join(os.getcwd(), 'lib', 'llm', 'mcp'))

from lib.llm.mcp.mcp_server import mcp


if __name__ == "__main__":
    ts = datetime.datetime.now().isoformat()
    print(f"Starting MCP server at {ts}...")

    mcp.run(
        transport="http",
        host="0.0.0.0",
        port=9000,
        path="/mcp",
        log_level="debug",
    )
