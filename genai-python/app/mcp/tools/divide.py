from app.mcp.schemas.divide_schema import DivideSchema

def divide_tool(input: DivideSchema):
    if input.b == 0:
        return {
            "error": "Division by zero is not allowed",
            "isError": True
        }

    return {
        "result": input.a / input.b
    }