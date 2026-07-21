from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Depends

from face_recognition_app.inference.service import RecognitionService
from face_recognition_app.presentation.api.dependencies import (
    get_recognition_service,
)
from face_recognition_app.presentation.api.schemas import HealthResponse


router = APIRouter(tags=["health"])
Service = Annotated[RecognitionService, Depends(get_recognition_service)]


@router.get("/health", response_model=HealthResponse)
def health(service: Service) -> HealthResponse:
    return HealthResponse(
        status="ready" if service.ready else "not_ready",
        ready=service.ready,
        detail=service.error,
    )
