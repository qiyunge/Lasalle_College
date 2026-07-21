from __future__ import annotations

from unittest.mock import Mock

import cv2
import numpy as np
import pytest

from face_recognition_app.capture.face_detector import FaceDetection
from face_recognition_app.inference.predictor import FacePrediction
from face_recognition_app.inference.service import RecognitionService


def test_service_decodes_and_recognizes_image() -> None:
    detector = Mock()
    detector.detect_faces.return_value = [FaceDetection((5, 5, 20, 20))]
    predictor = Mock()
    predictor.model.classes_ = np.asarray(["Ada", "Linus"])
    predictor.predict.return_value = FacePrediction("Ada", 0.9)
    service = RecognitionService(detector=detector, predictor=predictor)
    success, encoded = cv2.imencode(
        ".jpg", np.zeros((30, 40, 3), dtype=np.uint8)
    )
    assert success

    frame, faces = service.recognize(encoded.tobytes())

    assert frame.shape == (30, 40, 3)
    assert len(faces) == 1
    assert faces[0].prediction.label == "Ada"


def test_service_rejects_invalid_image() -> None:
    service = RecognitionService(detector=Mock(), predictor=Mock())

    with pytest.raises(ValueError, match="valid encoded image"):
        service.recognize(b"not an image")
