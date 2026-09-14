from mcp.server.fastmcp import FastMCP

mcp = FastMCP("weather")


@mcp.tool()
async def get_weather(location: str) -> str:
    """Get the weather for location"""
    return "Its always raining in the california"


if __name__ == "__main__":
    mcp.run(transport="streamable-http")
