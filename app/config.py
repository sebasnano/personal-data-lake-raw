from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Central application settings.

    This class reads configuration values from environment variables or from a
    local `.env` file. Keeping configuration centralized makes the project
    easier to run in development, quality, and production environments.
    """

    app_name: str = "personal-data-lake-api"
    app_env: str = "development"
    app_version: str = "0.1.0"

    # Used when the API runs behind a reverse proxy with a path prefix.
    # Example in code-server: /proxy/8000
    app_root_path: str = ""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )


@lru_cache
def get_settings() -> Settings:
    """
    Return cached application settings.

    The cache prevents reading the environment repeatedly on every request.
    This will also be useful later for database and object storage settings.
    """
    return Settings()
