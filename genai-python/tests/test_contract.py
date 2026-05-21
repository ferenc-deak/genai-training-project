from app.mcp.tools.add import add_tool
from app.mcp.tools.divide import divide_tool
from app.mcp.tools.get_user import get_user_tool

from app.mcp.schemas.add_schema import AddSchema
from app.mcp.schemas.divide_schema import DivideSchema
from app.mcp.schemas.user_schema import UserSchema


def test_add_contract():
    res = add_tool(AddSchema(a=2, b=3))
    assert res["result"] == 5


def test_divide_contract():
    res = divide_tool(DivideSchema(a=10, b=2))
    assert res["result"] == 5


def test_user_contract():
    res = get_user_tool(UserSchema(user_id="123"))
    assert res["result"]["id"] == "123"