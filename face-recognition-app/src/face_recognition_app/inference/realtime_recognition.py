from __future__ import annotations

import argparse
from collections.abc import Sequence
from dataclasses import dataclass

import cv2
import numpy as np

from face_recognition_app.capture.face_detector import (
    FaceDetection,
    FaceDetector,
    create_face_detector,
)
from face_recognition_app.common.config import config
from face_recognition_app.inference.predictor import FacePrediction, FacePredictor


@dataclass(frozen=True)
class RecognizedFace:
    detection: FaceDetection
    prediction: FacePrediction


def recognize_faces(
    frame: np.ndarray,
    detector: FaceDetector,
    predictor: FacePredictor,
    *,
    crop_margin: float = 0.2,
) -> list[RecognizedFace]:
    """Detect and classify every valid face in one frame."""
    recognized: list[RecognizedFace] = []
    for detection in detector.detect_faces(frame):
        try:
            face_image = detection.crop(frame, margin=crop_margin)
        except ValueError:
            continue
        recognized.append(
            RecognizedFace(detection, predictor.predict(face_image))
        )
    return recognized


def draw_recognized_faces(
    frame: np.ndarray, faces: Sequence[RecognizedFace]
) -> np.ndarray:
    """Return a copy of a frame annotated with identity predictions."""
    output = frame.copy()
    for face in faces:
        detection = face.detection
        prediction = face.prediction
        known = prediction.label != config.recognition.unknown_label
        color = (0, 200, 0) if known else (0, 165, 255)
        cv2.rectangle(
            output,
            (detection.x1, detection.y1),
            (detection.x2, detection.y2),
            color,
            2,
        )
        cv2.putText(
            output,
            f"{prediction.label}: {prediction.confidence:.0%}",
            (detection.x1, max(20, detection.y1 - 10)),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.65,
            color,
            2,
        )
    return output


class RealtimeRecognizer:
    def __init__(
        self,
        detector: FaceDetector,
        predictor: FacePredictor,
        *,
        camera_index: int | None = None,
        crop_margin: float = 0.2,
    ) -> None:
        if crop_margin < 0:
            raise ValueError("Crop margin must be non-negative.")
        self.detector = detector
        self.predictor = predictor
        self.camera_index = (
            config.camera.camera_index if camera_index is None else camera_index
        )
        self.crop_margin = crop_margin

    def run(self) -> None:
        capture = cv2.VideoCapture(self.camera_index)
        if not capture.isOpened():
            capture.release()
            raise RuntimeError(f"Could not open camera {self.camera_index}.")

        capture.set(cv2.CAP_PROP_FRAME_WIDTH, config.camera.frame_width)
        capture.set(cv2.CAP_PROP_FRAME_HEIGHT, config.camera.frame_height)
        try:
            while True:
                success, frame = capture.read()
                if not success:
                    break
                faces = recognize_faces(
                    frame,
                    self.detector,
                    self.predictor,
                    crop_margin=self.crop_margin,
                )
                cv2.imshow(
                    config.camera.window_name,
                    draw_recognized_faces(frame, faces),
                )
                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
        finally:
            capture.release()
            cv2.destroyAllWindows()


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Run real-time face recognition.")
    parser.add_argument(
        "--detector",
        choices=("haar", "yunet", "yolo"),
        default=config.detection.default_detector,
    )
    parser.add_argument("--camera", type=int, default=config.camera.camera_index)
    parser.add_argument("--model", default=config.paths.classifier_model_path)
    parser.add_argument(
        "--threshold", type=float, default=config.recognition.unknown_threshold
    )
    parser.add_argument("--margin", type=float, default=0.2)
    parser.add_argument("--device")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    detector = create_face_detector(args.detector, device=args.device)
    predictor = FacePredictor(args.model, unknown_threshold=args.threshold)
    RealtimeRecognizer(
        detector,
        predictor,
        camera_index=args.camera,
        crop_margin=args.margin,
    ).run()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
