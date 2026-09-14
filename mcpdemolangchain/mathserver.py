from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Math")


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b


@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiple two numbers"""
    return a * b


## The"transport="stdio" argument tells the server to:
##Use the standard input output (stdin /stdio) to recieve and respond the tool calls

if __name__ == "__main__":
    mcp.run(transport="stdio")
