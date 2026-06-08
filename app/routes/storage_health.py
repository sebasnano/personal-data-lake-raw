from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.storage.minio_client import get_minio_client
from app.storage.storage_service import ObjectStorageService


router = APIRouter(
    prefix="/health/storage",
    tags=["health"],
)


class StorageHealthResponse(BaseModel):
    """
    Response model for the object storage health check.
    """

    status: str
    bucket: str
    available: bool
    message: str


@router.get(
    "",
    response_model=StorageHealthResponse,
    summary="Check object storage health",
    description="Validates MinIO connectivity and ensures the RAW bucket exists.",
)
def storage_health() -> StorageHealthResponse:
    """
    Validate the RAW object storage layer.

    This endpoint is useful for checking whether the API can communicate with
    MinIO before implementing file upload.
    """
    service = ObjectStorageService(client=get_minio_client())
    result = service.ensure_raw_bucket_exists()

    return StorageHealthResponse(
        status=result.status,
        bucket=result.bucket,
        available=result.available,
        message=result.message,
    )
