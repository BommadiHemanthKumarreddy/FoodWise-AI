"""
FoodWiseAI — Application Configuration

Loads environment variables using Pydantic Settings.
"""

try:
    from pydantic_settings import BaseSettings, SettingsConfigDict
    class Settings(BaseSettings):
        """Application settings loaded from environment variables."""
        model_config = SettingsConfigDict(
            env_file=".env",
            env_file_encoding="utf-8",
            case_sensitive=False,
            extra="ignore",
        )
        APP_NAME: str = "FoodWiseAI"
        DEBUG: bool = False
        API_V1_PREFIX: str = "/api/v1"
        DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/foodwiseai"
        SECRET_KEY: str = "change-me-to-a-random-secret-key"
except ImportError:
    from pydantic import BaseSettings
    class Settings(BaseSettings):
        """Application settings loaded from environment variables (Pydantic v1 fallback)."""
        class Config:
            env_file = ".env"
            env_file_encoding = "utf-8"
            case_sensitive = False
            extra = "ignore"
        APP_NAME: str = "FoodWiseAI"
        DEBUG: bool = False
        API_V1_PREFIX: str = "/api/v1"
        DATABASE_URL: str = "postgresql+asyncpg://postgres:postgres@localhost:5432/foodwiseai"
        SECRET_KEY: str = "change-me-to-a-random-secret-key"


# Singleton settings instance
settings = Settings()
