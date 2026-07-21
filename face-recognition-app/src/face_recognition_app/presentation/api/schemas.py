from __future__ import annotations

from pydantic import BaseModel, Field


class FaceResult(BaseModel):
    label: str
    confidence: float = Field(ge=0.0, le=1.0)
    bbox: tuple[int, int, int, int]


class RecognitionResponse(BaseModel):
    width: int
    height: int
    faces: list[FaceResult]


class HealthResponse(BaseModel):
    status: str
    ready: bool
    detail: str | None = None


class ModelResponse(BaseModel):
    ready: bool
    path: str
    detector: str
    threshold: float
    classes: list[str]
    detail: str | None = None
