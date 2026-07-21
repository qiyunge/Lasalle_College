from __future__ import annotations

from typing import Annotated

from fastapi import APIRouter, Body, Depends, HTTPException

from face_recognition_app.inference.service import RecognitionService
from face_recognition_app.presentation.api.dependencies import (
    get_recognition_service,
)
from face_recognition_app.presentation.api.schemas import (
    FaceResult,
    RecognitionResponse,
)


router = APIRouter(tags=["recognition"])
Service = Annotated[RecognitionService, Depends(get_recognition_service)]


@router.post("/recognize", response_model=RecognitionResponse)
def recognize(
    service: Service,
    image: bytes = Body(media_type="image/jpeg"),
) -> RecognitionResponse:
    if not service.ready:
        raise HTTPException(status_code=503, detail=service.error)
    try:
        frame, faces = service.recognize(image)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc

    return RecognitionResponse(
        width=frame.shape[1],
        height=frame.shape[0],
        faces=[
            FaceResult(
                label=face.prediction.label,
                confidence=face.prediction.confidence,
                bbox=face.detection.bbox,
            )
            for face in faces
        ],
    )
