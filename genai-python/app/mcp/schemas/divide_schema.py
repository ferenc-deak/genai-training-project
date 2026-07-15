from pydantic import BaseModel, Field, field_validator


class DivideSchema(BaseModel):
    a: float
    b: float = Field(..., description="Must not be zero")

    @field_validator("b")
    @classmethod
    def validate_divisor(cls, value):
        if value == 0:
            raise ValueError("b must not be zero")
        return value