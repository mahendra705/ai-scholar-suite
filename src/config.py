"""Application configuration using Pydantic BaseSettings.

Settings are loaded from environment variables with sensible defaults.
"""

import os
from dotenv import load_dotenv
from pydantic_settings import BaseSettings

# Load environment variables from .env file
load_dotenv()


class Settings(BaseSettings):
    """Application settings with environment variable overrides."""

    google_api_key: str = ""
    llm_model: str = "gemini-1.5-pro"
    chromadb_path: str = "./chroma_data"
    output_dir: str = "./output"
    api_host: str = "0.0.0.0"
    api_port: int = 8000

    def get_port(self) -> int:
        """Get port from PORT env var (Railway/cloud platforms) or fallback to api_port."""
        return int(os.getenv("PORT", self.api_port))

    model_config = {"env_prefix": ""}


def get_settings() -> Settings:
    """Return a cached Settings instance."""
    return Settings()
