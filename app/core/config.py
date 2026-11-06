from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


# Project root directory
BASE_DIR = Path(__file__).resolve().parents[2]


class Settings(BaseSettings):

    # Qdrant Configuration
    QDRANT_URL: str
    QDRANT_API_KEY: str

    # Gemini Configuration
    GEMINI_API_KEY: str

    # OpenRouter Configuration
    OPENROUTER_API_KEY: str

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        env_file_encoding="utf-8",
        extra="ignore"
    )




settings = Settings()