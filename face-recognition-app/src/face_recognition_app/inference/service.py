from __future__ import annotations

from pathlib import Path
from threading import Lock

import cv2
import numpy as np

from face_recognition_app.capture.face_detector import (
    FaceDetector,
    create_face_detector,
)
from face_recognition_app.common.config import config
from face_recognition_app.inference.predictor import FacePredictor
from face_recognition_app.inference.realtime_recognition import recognize_faces


class RecognitionService:
    """Own the loaded models and serialize access to mutable detector state."""

    def __init__(
        self,
        *,
        model_path: str | Path | None = None,
        detector_name: str | None = None,
        threshold: float | None = None,
        detector: FaceDetector | None = None,
        predictor: FacePredictor | None = None,
    ) -> None:
        self.model_path = Path(model_path or config.paths.classifier_model_path)
        self.detector_name = detector_name or config.detection.default_detector
        self.threshold = (
            config.recognition.unknown_threshold
            if threshold is None
            else threshold
        )
        self.detector = detector
        self.predictor = predictor
        self.error: str | None = None
        self._lock = Lock()

    @property
    def ready(self) -> bool:
        return self.detector is not None and self.predictor is not None

    @property
    def classes(self) -> list[str]:
        if self.predictor is None:
            return []
        return [str(value) for value in self.predictor.model.classes_]

    def load(self) -> None:
        """Load configured models, retaining a useful readiness error on failure."""
        try:
            if self.detector is None:
                self.detector = create_face_detector(self.detector_name)
            if self.predictor is None:
                self.predictor = FacePredictor(
                    self.model_path,
                    unknown_threshold=self.threshold,
                )
            self.error = None
        except Exception as exc:
            self.error = str(exc)

    def recognize(self, image_bytes: bytes) -> tuple[np.ndarray, list]:
        if not self.ready:
            raise RuntimeError(self.error or "Recognition models are not loaded.")
        encoded = np.frombuffer(image_bytes, dtype=np.uint8)
        frame = cv2.imdecode(encoded, cv2.IMREAD_COLOR)
        if frame is None:
            raise ValueError("Request body is not a valid encoded image.")

        with self._lock:
            faces = recognize_faces(frame, self.detector, self.predictor)
        return frame, faces
