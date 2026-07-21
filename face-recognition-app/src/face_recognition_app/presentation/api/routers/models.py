from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Depends

from face_recognition_app.inference.service import RecognitionService
from face_recognition_app.presentation.api.dependencies import (
    get_recognition_service,
)
from face_recognition_app.presentation.api.schemas import ModelResponse


router = APIRouter(tags=["models"])
Service = Annotated[RecognitionService, Depends(get_recognition_service)]


@router.get("/model", response_model=ModelResponse)
def model_information(service: Service) -> ModelResponse:
    return ModelResponse(
        ready=service.ready,
        path=str(service.model_path),
        detector=service.detector_name,
        threshold=service.threshold,
        classes=service.classes,
        detail=service.error,
    )
