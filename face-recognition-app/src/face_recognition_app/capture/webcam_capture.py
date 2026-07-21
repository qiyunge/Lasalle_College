from __future__ import annotations

import argparse
from collections.abc import Sequence

import cv2
import numpy as np

from face_recognition_app.capture.face_detector import (
    FaceDetection,
    FaceDetector,
    create_face_detector,
)
from face_recognition_app.common.config import config


class WebcamCapture:
    """Capture webcam frames and display face detections in real time."""

    def __init__(
        self,
        detector: FaceDetector,
        camera_index: int | None = None,
        frame_width: int | None = None,
        frame_height: int | None = None,
        window_name: str | None = None,
    ) -> None:
        self.detector = detector
        self.camera_index = (
            config.camera.camera_index if camera_index is None else camera_index
        )
        self.frame_width = frame_width or config.camera.frame_width
        self.frame_height = frame_height or config.camera.frame_height
        self.window_name = window_name or config.camera.window_name

    def run(self) -> None:
        """Run until the user presses q or the camera stops returning frames."""
        capture = cv2.VideoCapture(self.camera_index)
        if not capture.isOpened():
            capture.release()
            raise RuntimeError(f"Could not open camera {self.camera_index}.")

        capture.set(cv2.CAP_PROP_FRAME_WIDTH, self.frame_width)
        capture.set(cv2.CAP_PROP_FRAME_HEIGHT, self.frame_height)

        try:
            while True:
                success, frame = capture.read()
                if not success:
                    break

                detections = self.detector.detect_faces(frame)
                annotated_frame = draw_detections(frame, detections)
                cv2.imshow(self.window_name, annotated_frame)

                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
        finally:
            capture.release()
            cv2.destroyAllWindows()


def draw_detections(
    frame: np.ndarray,
    detections: Sequence[FaceDetection],
) -> np.ndarray:
    """Return a copy of a frame annotated with face boxes and confidence."""
    annotated = frame.copy()
    for detection in detections:
        cv2.rectangle(
            annotated,
            (detection.x1, detection.y1),
            (detection.x2, detection.y2),
            (0, 255, 0),
            2,
        )
        label = "Face"
        if detection.confidence is not None:
            label = f"Face: {detection.confidence:.2f}"

        label_y = max(20, detection.y1 - 10)
        cv2.putText(
            annotated,
            label,
            (detection.x1, label_y),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (0, 255, 0),
            2,
        )
    return annotated


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run real-time face detection.")
    parser.add_argument(
        "--detector",
        choices=("haar", "yunet", "yolo"),
        default=config.detection.default_detector,
    )
    parser.add_argument("--camera", type=int, default=config.camera.camera_index)
    parser.add_argument(
        "--device",
        help="Ultralytics device for YOLO, for example 'cpu', '0', or 'cuda'.",
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    detector = create_face_detector(
        detector_name=args.detector,
        device=args.device,
    )
    app = WebcamCapture(detector=detector, camera_index=args.camera)
    app.run()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
