import pytest
from pydantic import ValidationError

from app.mcp.tools.add import add_tool
from app.mcp.tools.divide import divide_tool
from app.mcp.tools.get_user import get_user_tool

from app.mcp.schemas.add_schema import AddSchema
from app.mcp.schemas.divide_schema import DivideSchema
from app.mcp.schemas.user_schema import UserSchema



# ----------------------------
# Happy-path contract tests
# ----------------------------

def test_add_contract():
    res = add_tool(AddSchema(a=2, b=3))
    assert res["result"] == 5


def test_divide_contract():
    res = divide_tool(DivideSchema(a=10, b=2))
    assert res["result"] == 5


def test_user_contract():
    res = get_user_tool(UserSchema(user_id="123"))
    assert res["result"]["id"] == "123"



# ----------------------------
# Schema validation tests
# ----------------------------

def test_divide_schema_rejects_zero():
    with pytest.raises(ValidationError):
        DivideSchema(a=10, b=0)


def test_add_schema_requires_numeric_values():
    with pytest.raises(ValidationError):
        AddSchema(a="abc", b=2)


def test_user_schema_requires_user_id():
    with pytest.raises(ValidationError):
        UserSchema()