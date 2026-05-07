from fastapi import APIRouter
from app.models.prompt import PromptRequest
from app.services.ai_service import generate_text

router = APIRouter()

@router.post("/generate")
def generate(request: PromptRequest):
    result = generate_text(request.prompt)
    return {"response": result}