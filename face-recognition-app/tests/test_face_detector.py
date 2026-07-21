from __future__ import annotations

import numpy as np
import pytest

from face_recognition_app.capture.face_detector import (
    FaceDetection,
    _clip_bbox,
    _validate_frame,
    create_face_detector,
)


def test_face_detection_properties() -> None:
    detection = FaceDetection((10, 20, 40, 70), confidence=0.9)

    assert (detection.x1, detection.y1, detection.x2, detection.y2) == (10, 20, 40, 70)
    assert detection.width == 30
    assert detection.height == 50


def test_crop_adds_margin_and_clips_to_frame() -> None:
    frame = np.zeros((100, 100, 3), dtype=np.uint8)
    detection = FaceDetection((5, 10, 25, 30))

    crop = detection.crop(frame, margin=0.5)

    assert crop.shape == (40, 35, 3)
    assert not np.shares_memory(crop, frame)


@pytest.mark.parametrize("margin", [-0.1, -1.0])
def test_crop_rejects_negative_margin(margin: float) -> None:
    frame = np.zeros((10, 10, 3), dtype=np.uint8)

    with pytest.raises(ValueError, match="non-negative"):
        FaceDetection((1, 1, 5, 5)).crop(frame, margin)


def test_crop_rejects_bbox_outside_frame() -> None:
    frame = np.zeros((10, 10, 3), dtype=np.uint8)

    with pytest.raises(ValueError, match="does not overlap"):
        FaceDetection((20, 20, 30, 30)).crop(frame)


@pytest.mark.parametrize(
    ("frame", "exception"),
    [
        (None, TypeError),
        ([], TypeError),
        (np.empty((0, 0, 3)), ValueError),
        (np.zeros((10, 10)), ValueError),
        (np.zeros((10, 10, 4)), ValueError),
    ],
)
def test_validate_frame_rejects_invalid_input(
    frame: object, exception: type[Exception]
) -> None:
    with pytest.raises(exception):
        _validate_frame(frame)  # type: ignore[arg-type]


def test_clip_bbox_clips_and_rejects_empty_boxes() -> None:
    assert _clip_bbox(-5, 2, 12, 20, 10, 15) == (0, 2, 10, 15)
    assert _clip_bbox(20, 20, 30, 30, 10, 10) is None


def test_factory_rejects_unknown_detector() -> None:
    with pytest.raises(ValueError, match="Unsupported detector"):
        create_face_detector("unknown")
