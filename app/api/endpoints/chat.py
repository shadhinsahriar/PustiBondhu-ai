
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

from app.services.llm_service import generate_response

router = APIRouter()


class ChatRequest(BaseModel):
    message: str


@router.post("/test-openrouter")
async def test_openrouter(request: ChatRequest):

    try:
        response = await generate_response(request.message)

        return {
            "provider": "OpenRouter",
            "response": response
        }

    except RuntimeError as error:
        raise HTTPException(
            status_code=502,
            detail=str(error)
        )
