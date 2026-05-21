from app.mcp.tools.divide import divide_tool
from app.mcp.tools.get_user import get_user_tool

from app.mcp.schemas.divide_schema import DivideSchema
from app.mcp.schemas.user_schema import UserSchema


def test_divide_by_zero():
    res = divide_tool(DivideSchema(a=10, b=0))
    assert res["isError"] is True


def test_user_failure():
    res = get_user_tool(UserSchema(user_id="fail"))
    assert res["isError"] is True