from __future__ import annotations

from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from face_recognition_app.inference.service import RecognitionService
from face_recognition_app.presentation.api.routers import (
    health,
    models,
    recognition,
)
from face_recognition_app.presentation.web.routers.pages import (
    STATIC_DIRECTORY,
    router as pages_router,
)


def create_app(service: RecognitionService | None = None) -> FastAPI:
    recognition_service = service or RecognitionService()

    @asynccontextmanager
    async def lifespan(application: FastAPI):
        recognition_service.load()
        application.state.recognition_service = recognition_service
        yield

    application = FastAPI(
        title="Face Recognition App",
        version="0.1.0",
        lifespan=lifespan,
        docs_url="/api/docs",
        openapi_url="/api/openapi.json",
        redoc_url="/api/redoc",
    )
    application.include_router(health.router, prefix="/api/v1")
    application.include_router(models.router, prefix="/api/v1")
    application.include_router(recognition.router, prefix="/api/v1")
    application.mount(
        "/static",
        StaticFiles(directory=STATIC_DIRECTORY),
        name="static",
    )
    application.include_router(pages_router)
    return application


app = create_app()
