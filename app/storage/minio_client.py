from functools import lru_cache

from minio import Minio

from app.config import get_settings


@lru_cache
def get_minio_client() -> Minio:
    """
    Create and cache the MinIO client.

    The client is configured from environment variables. Caching avoids creating
    a new connection object on every request while keeping the configuration in
    one centralized place.
    """
    settings = get_settings()

    return Minio(
        endpoint=settings.minio_endpoint,
        access_key=settings.minio_access_key,
        secret_key=settings.minio_secret_key,
        secure=settings.minio_secure,
    )
