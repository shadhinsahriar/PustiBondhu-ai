from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.api.router import api_router
from app.vector_store.qdrant import close_qdrant_connection


@asynccontextmanager
async def lifespan(app: FastAPI):

    print("PustiBondhu AI Service Starting...")

    yield

    await close_qdrant_connection()

    print("PustiBondhu AI Service Stopped.")


app = FastAPI(
    title="PustiBondhu AI Service",
    description="AI and RAG Backend for PustiBondhu",
    version="1.0.0",
    lifespan=lifespan
)


app.include_router(
    api_router,
    prefix="/api/v1"
)


@app.get("/")
async def root():

    return {
        "message": "Welcome to PustiBondhu AI Service",
        "status": "running"
    }