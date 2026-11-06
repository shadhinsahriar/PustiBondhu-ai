from openai import AsyncOpenAI

from app.core.config import settings


# Initialize OpenRouter client
client = AsyncOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=settings.OPENROUTER_API_KEY
)


async def generate_response(prompt: str) -> str:
    """
    Generate an AI response using OpenRouter.
    """

    try:
        response = await client.chat.completions.create(
            model="openrouter/free",
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        return response.choices[0].message.content or ""

    except Exception as error:
        raise RuntimeError(f"OpenRouter API error: {error}")