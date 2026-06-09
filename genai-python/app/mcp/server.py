from mcp.server.fastmcp import FastMCP

from app.mcp.tools.add import add_tool
from app.mcp.tools.divide import divide_tool
from app.mcp.tools.get_user import get_user_tool

from app.mcp.schemas.add_schema import AddSchema
from app.mcp.schemas.divide_schema import DivideSchema
from app.mcp.schemas.user_schema import UserSchema

mcp = FastMCP("demo-mcp-server")


@mcp.tool()
def add(input: AddSchema):
    return add_tool(input)


@mcp.tool()
def divide(input: DivideSchema):
    return divide_tool(input)


@mcp.tool()
def get_user(input: UserSchema):
    return get_user_tool(input)


if __name__ == "__main__":
    print("🚀 MCP server starting...")
    # print(add_tool(AddSchema(a=2, b=3)))
    mcp.run()