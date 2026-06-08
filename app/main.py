from fastapi import FastAPI

from app.config import get_settings
from app.routes.health import router as health_router


def create_app() -> FastAPI:
    """
    Create and configure the FastAPI application.

    The application factory pattern keeps the project easy to test and prepares
    it for future routers, middleware, database connections, and storage
    integrations.
    """
    settings = get_settings()

    app = FastAPI(
        title=settings.app_name,
        version=settings.app_version,
        description=(
            "API base for a Personal RAW Data Lake. "
            "This service will store raw files, catalog metadata, "
            "and prepare data for future ETL processes."
        ),
    )

    # Register API routers.
    # Future routers will include file upload, metadata catalog, storage, and ETL.
    app.include_router(health_router)

    return app


# ASGI application instance used by Uvicorn.
app = create_app()
