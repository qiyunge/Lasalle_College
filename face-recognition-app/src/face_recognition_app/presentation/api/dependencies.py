from __future__ import annotations

from fastapi import Request

from face_recognition_app.inference.service import RecognitionService


def get_recognition_service(request: Request) -> RecognitionService:
    """Return the application-scoped recognition service."""
    return request.app.state.recognition_service
