from __future__ import annotations

from unittest.mock import Mock

import numpy as np
import pytest

from face_recognition_app.capture.face_detector import FaceDetection
from face_recognition_app.inference.predictor import FacePrediction, FacePredictor
from face_recognition_app.inference.realtime_recognition import (
    draw_recognized_faces,
    recognize_faces,
)


def classifier(classes: list[str], probabilities: list[float]) -> Mock:
    model = Mock()
    model.classes_ = np.asarray(classes)
    model.predict_proba.return_value = np.asarray([probabilities])
    return model


def test_predictor_returns_best_known_identity() -> None:
    model = classifier(["Ada", "Linus"], [0.85, 0.15])
    predictor = FacePredictor(model=model, unknown_threshold=0.7)

    prediction = predictor.predict(np.zeros((20, 20, 3), dtype=np.uint8))

    assert prediction == FacePrediction("Ada", 0.85)
    assert model.predict_proba.call_args.args[0].shape == (1, 100 * 100 * 3)


def test_predictor_marks_low_confidence_face_unknown() -> None:
    model = classifier(["Ada", "Linus"], [0.55, 0.45])
    predictor = FacePredictor(model=model, unknown_threshold=0.7)

    assert predictor.predict(np.zeros((10, 10, 3), np.uint8)).label == "Unknown"


def test_predictor_rejects_invalid_threshold() -> None:
    with pytest.raises(ValueError, match="between 0 and 1"):
        FacePredictor(model=Mock(), unknown_threshold=1.1)


def test_recognize_faces_crops_each_detection() -> None:
    frame = np.zeros((50, 50, 3), np.uint8)
    detector = Mock()
    detector.detect_faces.return_value = [FaceDetection((10, 10, 30, 30))]
    predictor = Mock()
    predictor.predict.return_value = FacePrediction("Ada", 0.9)

    faces = recognize_faces(frame, detector, predictor, crop_margin=0)

    assert len(faces) == 1
    assert faces[0].prediction.label == "Ada"
    assert predictor.predict.call_args.args[0].shape == (20, 20, 3)


def test_draw_recognized_faces_does_not_mutate_input() -> None:
    frame = np.zeros((40, 40, 3), np.uint8)
    faces = [
        Mock(
            detection=FaceDetection((5, 5, 25, 25)),
            prediction=FacePrediction("Ada", 0.9),
        )
    ]

    output = draw_recognized_faces(frame, faces)

    assert np.count_nonzero(frame) == 0
    assert np.count_nonzero(output) > 0
