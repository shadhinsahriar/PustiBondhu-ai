from qdrant_client import AsyncQdrantClient

from app.core.config import settings


# Initialize Qdrant client
qdrant_client = AsyncQdrantClient(
    url=settings.QDRANT_URL,
    api_key=settings.QDRANT_API_KEY,
    timeout=30
)


async def check_qdrant_connection():

    try:

        # Fetch available collections
        response = await qdrant_client.get_collections()

        collections = [
            collection.name
            for collection in response.collections
        ]

        return {
            "status": "connected",
            "database": "Qdrant Cloud",
            "collections": collections,
            "total_collections": len(collections)
        }

    except Exception as error:

        return {
            "status": "disconnected",
            "database": "Qdrant Cloud",
            "error": str(error)
        }


async def close_qdrant_connection():

    await qdrant_client.close()