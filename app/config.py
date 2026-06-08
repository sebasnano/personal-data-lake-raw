from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Central application settings.

    Settings are loaded from environment variables or from a local `.env` file.
    This makes the same codebase usable in development, quality, and production
    environments without hardcoding infrastructure values.
    """

    # Application settings
    app_name: str = "personal-data-lake-api"
    app_env: str = "development"
    app_version: str = "0.1.0"

    # Optional root path used when the API runs behind a path-based proxy.
    # Example in code-server: /proxy/8000
    app_root_path: str = ""

    # MinIO settings
    # MinIO is the RAW object storage layer of the data lake.
    minio_endpoint: str = "minio:9000"
    minio_access_key: str = "change_me"
    minio_secret_key: str = "change_me"
    minio_bucket_raw: str = "raw"
    minio_secure: bool = False

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )


@lru_cache
def get_settings() -> Settings:
    """
    Return cached application settings.

    The cache avoids reading environment variables repeatedly during the app
    lifecycle. This is useful for routes, storage clients, and future database
    connections.
    """
    return Settings()
