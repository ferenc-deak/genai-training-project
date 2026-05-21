from mcp.server.fastmcp import FastMCP
from pydantic import BaseModel, Field

mcp = FastMCP("frontend-mcp-python-server")

# -------------------------
# TOOL 1: ADD
# -------------------------
class AddInput(BaseModel):
    a: float = Field(..., description="First number")
    b: float = Field(..., description="Second number")

@mcp.tool()
def add(input: AddInput):
    return {"result": input.a + input.b}


# -------------------------
# TOOL 2: DIVIDE (safe)
# -------------------------
class DivideInput(BaseModel):
    a: float
    b: float

@mcp.tool()
def divide(input: DivideInput):
    if input.b == 0:
        return {
            "error": "Division by zero is not allowed",
            "isError": True
        }

    return {"result": input.a / input.b}


# -------------------------
# TOOL 3: GET USER (failure simulation)
# -------------------------
class UserInput(BaseModel):
    user_id: str

@mcp.tool()
def get_user(input: UserInput):
    try:
        if input.user_id == "fail":
            raise Exception("Database connection failed")

        return {
            "result": {
                "id": input.user_id,
                "name": "Demo User"
            }
        }

    except Exception as e:
        return {
            "error": str(e),
            "isError": True
        }


if __name__ == "__main__":
    mcp.run()