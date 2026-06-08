from fastapi import FastAPI

from app.config import get_settings
from app.routes.health import router as health_router


def create_app() -> FastAPI:
    """
    Create and configure the FastAPI application.
    """
    settings = get_settings()

    app = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        root_path=settings.app_root_path,
        description=(
            "API base for a Personal RAW Data Lake. "
            "This service will store raw files, catalog metadata, "
            "and prepare data for future ETL processes."
        ),
    )

    app.include_router(health_router)

    return app


app = create_app()