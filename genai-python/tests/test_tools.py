from app.mcp.tools.add import add_tool
from app.mcp.schemas.add_schema import AddSchema


def test_add_basic():
    assert add_tool(AddSchema(a=1, b=1))["result"] == 2