from fastapi import APIRouter, HTTPException

from app.vector_store.qdrant import check_qdrant_connection


router = APIRouter()


@router.get("/qdrant")
async def qdrant_health():

    result = await check_qdrant_connection()

    if result["status"] == "disconnected":
        raise HTTPException(
            status_code=503,
            detail=result
        )

    return result