from __future__ import annotations

from unittest.mock import Mock, patch

import numpy as np
import pytest

from face_recognition_app.capture.face_detector import FaceDetection
from face_recognition_app.capture.webcam_capture import (
    WebcamCapture,
    build_parser,
    draw_detections,
)


def test_draw_detections_returns_annotated_copy() -> None:
    frame = np.zeros((80, 80, 3), dtype=np.uint8)

    annotated = draw_detections(frame, [FaceDetection((10, 20, 40, 60), 0.91)])

    assert annotated is not frame
    assert np.count_nonzero(frame) == 0
    assert np.count_nonzero(annotated) > 0


def test_parser_accepts_detector_camera_and_device() -> None:
    args = build_parser().parse_args(
        ["--detector", "yolo", "--camera", "2", "--device", "cpu"]
    )

    assert args.detector == "yolo"
    assert args.camera == 2
    assert args.device == "cpu"


@patch("face_recognition_app.capture.webcam_capture.cv2.VideoCapture")
def test_run_rejects_unavailable_camera(video_capture: Mock) -> None:
    capture = video_capture.return_value
    capture.isOpened.return_value = False
    app = WebcamCapture(detector=Mock(), camera_index=3)

    with pytest.raises(RuntimeError, match="camera 3"):
        app.run()

    capture.release.assert_called_once_with()


@patch("face_recognition_app.capture.webcam_capture.cv2.destroyAllWindows")
@patch("face_recognition_app.capture.webcam_capture.cv2.waitKey", return_value=ord("q"))
@patch("face_recognition_app.capture.webcam_capture.cv2.imshow")
@patch("face_recognition_app.capture.webcam_capture.cv2.VideoCapture")
def test_run_detects_one_frame_and_releases_camera(
    video_capture: Mock,
    imshow: Mock,
    wait_key: Mock,
    destroy_windows: Mock,
) -> None:
    frame = np.zeros((40, 40, 3), dtype=np.uint8)
    capture = video_capture.return_value
    capture.isOpened.return_value = True
    capture.read.return_value = (True, frame)
    detector = Mock()
    detector.detect_faces.return_value = [FaceDetection((5, 5, 20, 20))]

    WebcamCapture(detector=detector).run()

    detector.detect_faces.assert_called_once_with(frame)
    imshow.assert_called_once()
    wait_key.assert_called_once_with(1)
    capture.release.assert_called_once_with()
    destroy_windows.assert_called_once_with()
