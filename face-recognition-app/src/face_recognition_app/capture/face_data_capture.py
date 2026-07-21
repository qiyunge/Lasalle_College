from __future__ import annotations

from collections.abc import Sequence
from email import parser
from pathlib import Path
import argparse

import cv2
import time
import numpy as np  

from face_recognition_app.capture.face_detector import FaceDetection, FaceDetector, create_face_detector
   

from face_recognition_app.common.config import config

Video_source = int | str | Path

class FaceDataCapture:
    def __init__(self,
                 detector: FaceDetector,
                 source: Video_source,
                 person_name:str,
                 output_dir: str|Path|None = None,
                 *,
                 sample_count: int = 200,
                 frame_interval: int = 5,
                 crop_margin: float = 0.2,
                 preview: bool = True,
                 ) -> None:
        
        if not person_name.strip():
            raise ValueError("Person name cannot be empty or whitespace.")
        if sample_count <= 0:
            raise ValueError("Sample count must be a positive integer.")
        if frame_interval <= 0:
            raise ValueError("Frame interval must be a positive integer.")
        if crop_margin < 0:
            raise ValueError("Crop margin must be a non-negative float.")
        
        self.detector = detector
        self.source = normalize_video_source(source)
        self.person_name = sanitize_name(person_name)

        base_dir = Path(output_dir or config.paths.raw_data_dir).expanduser().resolve()

        self.person_dir = base_dir / self.person_name
        self.sample_count = sample_count
        self.frame_interval = frame_interval
        self.crop_margin = crop_margin
        self.preview = preview

    def run(self)->int:
        self.person_dir.mkdir(parents=True, exist_ok=True)
        cap = cv2.VideoCapture(self.source)

        if not cap.isOpened():
            cap.release()
            raise RuntimeError(f"Failed to open video source: {self.source}")
        
        frame_count = 0
        saved_count = self._existing_sample_count()

        try:
            while saved_count < self.sample_count:
                success, frame = cap.read()
                if not success:
                    print("Failed to read frame from video source.")
                    break

                frame_count += 1
                if frame_count % self.frame_interval != 0:
                    continue

                detections: Sequence[FaceDetection] = self.detector.detect_faces(frame)
                selected_face = select_largest_face(detections)

                if selected_face is not None:
                    face_image = selected_face.crop(frame, margin=self.crop_margin)
                    saved_count += 1
                    self._save_face_image(face_image, saved_count)

                if self.preview:
                    preview_frame = draw_capture_status(
                        frame,
                        selected_face,
                        frame_number = frame_count,
                        saved_count = saved_count,
                        sample_count = self.sample_count,
                    )

                    cv2.imshow("Face Data Capture", preview_frame)

                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break
        finally:
            cap.release()
            if self.preview:
                cv2.destroyAllWindows()
        return saved_count

               
    def _existing_sample_count(self) -> int:
        return len(list(self.person_dir.glob("*.jpg")))
    
    def _save_face_image(self, face_image: np.ndarray, count: int) -> Path:
        timestamp = time.time_ns()
        output_path = self.person_dir / f"{self.person_name}_{count:05d}_{timestamp}.jpg"

        if not cv2.imwrite(str(output_path), face_image):
            raise RuntimeError(f"Failed to save face image to {output_path}")

        return output_path


#  ------ #
def select_largest_face(detections: Sequence[FaceDetection]) -> FaceDetection | None:
    if not detections:
        return None
    return max(detections, key=lambda d: d.width * d.height)
# ----- #   
def normalize_video_source(source: Video_source) -> int | str :
    if isinstance(source, int):
        if source < 0:
            raise ValueError("Video source index must be a non-negative integer.")
        return source
    
    source_str = str(source).strip()
    if not source_str:
        raise ValueError("Video source string cannot be empty or whitespace.")
    
    if source_str.isdigit():
        return int(source_str)
    
    if "://" in source_str:
        return source_str

    file_path = Path(source_str).expanduser().resolve()

    if not file_path.is_file():
        raise ValueError(f"Video source file does not exist: {file_path}")

    return str(file_path)  
#-----#
def draw_capture_status(frame: np.ndarray, detection: FaceDetection | None, frame_number: int, saved_count: int, sample_count: int) -> np.ndarray:
    output_frame = frame.copy()

    if detection is not None:
        x1, y1, x2, y2 = detection.bbox
        cv2.rectangle(output_frame, (x1, y1), (x2, y2), (0, 255, 0), 2)

        confidence_text = f""

        if detection.confidence is not None:
            confidence_text = f"Confidence: {detection.confidence:.2f}"
        cv2.putText(output_frame, confidence_text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 1)

    cv2.putText(
        output_frame,
        f"Frame: {frame_number}",
        (20, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (255, 255, 255),
        2,
    )

    cv2.putText(
        output_frame,
        f"Saved: {saved_count}/{sample_count}",
        (20, 60),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.7,
        (0, 255, 255),
        2,
    )

    cv2.putText(
        output_frame,
        "Press Q to stop",
        (20, 90),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.65,
        (255, 255, 255),
        2,
    )

    return output_frame

# ----- #
def sanitize_name(name: str) -> str:
    cleaned_name = name.strip()
    if not cleaned_name:
        raise ValueError("Person name cannot be empty or whitespace.")
    
    invalid_chars = set(r'\/:*?"<>|')

    for char in invalid_chars:
        cleaned_name = cleaned_name.replace(char, '_')

    # Windows 文件夹名称不能以空格或句点结尾。
    cleaned_name = cleaned_name.strip(". ")
    reserved_names = {
            "CON",
            "PRN",
            "AUX",
            "NUL",
            "COM1",
            "COM2",
            "COM3",
            "COM4",
            "COM5",
            "COM6",
            "COM7",
            "COM8",
            "COM9",
            "LPT1",
            "LPT2",
            "LPT3",
            "LPT4",
            "LPT5",
            "LPT6",
            "LPT7",
            "LPT8",
            "LPT9",
        }

    if not cleaned_name:
        raise ValueError(
            "Person name does not contain valid characters."
        )

    if cleaned_name.upper() in reserved_names:
        cleaned_name = f"person_{cleaned_name}"

    return cleaned_name



def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Capture face images for the training dataset."
    )

    parser.add_argument(
        "--person",
        required=True,
        help="Name of the person being captured.",
    )

    parser.add_argument(
        "--output-dir",
        type=Path,
        default=config.paths.raw_data_dir,
        help="Base directory where face images will be saved.",
    )

    parser.add_argument(
        "--samples",
        type=int,
        default=100,
        help="Total number of images to collect.",
    )

    parser.add_argument(
        "--detector",
        choices=("haar", "yunet", "yolo"),
        default=config.detection.default_detector,
    )

    parser.add_argument(
    "--source",
    required=True,
    help="Camera index, video file, RTSP URL, or HTTP URL.",
)

    parser.add_argument(
    "--frame-interval",
    type=int,
    default=5,
    help="Save one face every N frames.",
)

    parser.add_argument(
        "--margin",
        type=float,
        default=0.2,
        help="Additional margin around the detected face.",
    )

    parser.add_argument(
        "--device",
        help="YOLO device, for example cpu, cuda, or 0.",
    )

    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)

    detector = create_face_detector(
        detector_name=args.detector,
        device=args.device,
    )

    face_capture = FaceDataCapture(
    detector=detector,
    source=args.source,
    person_name=args.person,
    output_dir=args.output_dir,
    sample_count=args.samples,
    frame_interval=args.frame_interval,
    crop_margin=args.margin,
)

    saved_count = face_capture.run()

    print(
        f"Saved {saved_count} face images to "
        f"{face_capture.person_dir}"
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())