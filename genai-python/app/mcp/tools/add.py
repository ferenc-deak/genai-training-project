from app.mcp.schemas.add_schema import AddSchema

def add_tool(input: AddSchema):
    return {
        "result": input.a + input.b
    }