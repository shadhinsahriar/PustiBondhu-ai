from fastapi import APIRouter

from app.api.endpoints import health, chat

api_router = APIRouter()

# Health endpoints
api_router.include_router(
    health.router,
    prefix="/health",
    tags=["Health"]
)

# Chat endpoints
api_router.include_router(
    chat.router,
    prefix="/chat",
    tags=["Chat"]
)