from app.mcp.schemas.user_schema import UserSchema

def get_user_tool(input: UserSchema):
    try:
        if input.user_id == "fail":
            raise Exception("Simulated database failure")

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