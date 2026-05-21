from pydantic import BaseModel, Field

class DivideSchema(BaseModel):
    a: float
    b: float = Field(..., description="Must not be zero")