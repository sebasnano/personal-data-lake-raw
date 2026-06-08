from fastapi import APIRouter, Depends
from pydantic import BaseModel

from app.config import Settings, get_settings


router = APIRouter(
    prefix="/health",
    tags=["health"],
)


class HealthResponse(BaseModel):
    """
    Public response model for the health check endpoint.

    Using a response model makes the API contract explicit and improves the
    generated Swagger documentation.
    """

    status: str
    service: str
    environment: str
    version: str


@router.get(
    "",
    response_model=HealthResponse,
    summary="Check API health",
    description="Returns the current status of the Personal Data Lake API.",
)
def health_check(settings: Settings = Depends(get_settings)) -> HealthResponse:
    """
    Confirm that the API is running.

    This endpoint is intentionally simple. It will be used during development,
    deployment validation, and future monitoring checks.
    """
    return HealthResponse(
        status="ok",
        service=settings.app_name,
        environment=settings.app_env,
        version=settings.app_version,
    )
