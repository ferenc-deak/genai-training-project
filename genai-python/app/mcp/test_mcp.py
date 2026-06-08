# test_mcp.py
from app.mcp.tools.add import add_tool
from app.mcp.schemas.add_schema import AddSchema

input = AddSchema(a=2, b=3)
print(add_tool(input))