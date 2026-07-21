from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path
from typing import Literal

import cv2
import numpy as np

from face_recognition_app.common.config import config


DetectorName = Literal["haar", "yunet", "yolo"]
BoundingBox = tuple[int, int, int, int]  # (x1, y1, x2, y2)

@dataclass(frozen=True)
class FaceDetection:
    bbox: BoundingBox
    confidence: float | None = None

    @property
    def x1(self) -> int:
        return self.bbox[0]

    @property
    def y1(self) -> int:
        return self.bbox[1]

    @property
    def x2(self) -> int:
        return self.bbox[2]

    @property
    def y2(self) -> int:
        return self.bbox[3]

    @property
    def width(self) -> int:
        return self.x2 - self.x1

    @property
    def height(self) -> int:
        return self.y2 - self.y1

    def crop(self, frame: np.ndarray, margin: float = 0.2) -> np.ndarray:
        """Crop this detection from a frame, optionally adding a relative margin."""
        _validate_frame(frame)
        if margin < 0:
            raise ValueError("Margin must be non-negative.")

        frame_height, frame_width = frame.shape[:2]
        horizontal_margin = int(self.width * margin)
        vertical_margin = int(self.height * margin)
        bbox = _clip_bbox(
            self.x1 - horizontal_margin,
            self.y1 - vertical_margin,
            self.x2 + horizontal_margin,
            self.y2 + vertical_margin,
            frame_width,
            frame_height,
        )
        if bbox is None:
            raise ValueError("Detection bounding box does not overlap the frame.")

        x1, y1, x2, y2 = bbox
        return frame[y1:y2, x1:x2].copy()

class FaceDetector(ABC):
    """Abstract base class for face detectors."""

    @abstractmethod
    def detect_faces(self, frame: np.ndarray) -> list[FaceDetection]:
        """Detect faces in the given frame."""
        raise NotImplementedError
    

class HaarFaceDetector(FaceDetector):
    """Face detector using Haar cascades."""

    def __init__(self,  
                 scale_factor: float = 1.1,
                     min_neighbors: int = 5,
                     minimum_face_size: tuple[int, int] | None = None,
                 cascade_path: str | Path | None = None) -> None:
        cascade_path = Path(cascade_path or config.paths.haar_cascade_path)
        self._detector =  cv2.CascadeClassifier(str(cascade_path))

        if self._detector.empty():
            raise RuntimeError(f"Failed to load Haar cascade from {cascade_path}")
        
        self.scale_factor = scale_factor
        self.min_neighbors = min_neighbors
        self.minimum_face_size = minimum_face_size or config.detection.minimum_face_size

    def detect_faces(self, 
                     frame:np.ndarray
                    ) -> list[FaceDetection]:
        """Detect faces in the given frame."""
        _validate_frame(frame)
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self._detector.detectMultiScale(
            gray_frame, 
            scaleFactor=self.scale_factor, 
            minNeighbors=self.min_neighbors,
            minSize=self.minimum_face_size)
        return [
            FaceDetection(bbox=(x, y, x + w, y + h))
            for (x, y, w, h) in faces
        ]
    

class YuNetFaceDetector(FaceDetector):
    """Face detector using YuNet model."""

    def __init__(self, 
                 model_path: str |Path | None = None,
                 confidence_threshold: float| None = None,
                 nms_threshold: float | None = None,
                 top_k: int | None = None,
                 ) -> None:
        
        self.model_path = (
            Path(model_path or config.paths.yunet_model_path).expanduser().resolve()
        )

        if not self.model_path.is_file():
            raise FileNotFoundError(
                f"YuNet model file not found at {self.model_path}."
            )
        
        self.confidence_threshold = (
            config.detection.confidence_threshold
            if confidence_threshold is None
            else confidence_threshold
        )

        self._detector = cv2.FaceDetectorYN.create(
            str(self.model_path),
            "",
            (320, 320),
            self.confidence_threshold ,
            config.detection.nms_threshold if nms_threshold is None else nms_threshold,
            config.detection.top_k if top_k is None else top_k,
        )
        
        
        if self._detector is None:
            raise RuntimeError(f"Failed to load YuNet model from {self.model_path}")
        
    def detect_faces(self, frame: np.ndarray) -> list[FaceDetection]:
        """Detect faces in the given frame."""

        _validate_frame(frame)
        self._detector.setInputSize((frame.shape[1], frame.shape[0]))
        _, faces = self._detector.detect(frame)
        
        if faces is None:
            return []
        
        detections = []
        for face in faces:
            # YuNet rows contain x, y, width, height, five landmark pairs,
            # and the confidence score as the final value.
            x, y, width, height = face[:4]
            confidence = face[-1]
            detections.append(
                FaceDetection(
                    bbox=(int(x), int(y), int(x + width), int(y + height)),
                    confidence=float(confidence),
                )
            )

        return detections
    
class YoloFaceDetector(FaceDetector):
    """Face detector using YOLOv8 model."""
    
    def __init__(self, 
                 model_path: str | Path | None = None,
                 confidence_threshold: float | None = None,
                device: str | None = None)-> None:
        
        try:
            from ultralytics import YOLO
        except ImportError as exc:
            raise RuntimeError(
                "The 'ultralytics' package is required for YOLOv8 face detection."
            ) from exc
        
        self.model_path = (
            Path(model_path or config.paths.yolo_model_path).expanduser().resolve()
        )

        if not self.model_path.is_file():
            raise FileNotFoundError(
                f"YOLOv8 model file not found at {self.model_path}."
            )
        
        self.confidence_threshold = (
            config.detection.confidence_threshold
            if confidence_threshold is None
            else confidence_threshold
        )
        self.device = device  # Default to CPU if no device is specified
        
        self.detector = YOLO(str(self.model_path))

    def detect_faces(self, frame: np.ndarray) -> list[FaceDetection]:
        """Detect faces in the given frame."""
        _validate_frame(frame)
        
        result = self.detector.predict(
            source=frame, 
            conf=self.confidence_threshold, 
            device=self.device,
            verbose=False
        )[0]
        
        if result.boxes is None:
            return []
        
        frame_height, frame_width = frame.shape[:2]
        detections = []

        for box in result.boxes:
            x1, y1, x2, y2 = map(int, box.xyxy[0].tolist())
            confidence = float(box.conf[0])
            clipped_bbox = _clip_bbox(x1, y1, x2, y2, frame_width, frame_height)
            if clipped_bbox:
                detections.append(
                    FaceDetection(bbox=clipped_bbox, confidence=confidence)
                )
        
        return detections


def create_face_detector(detector_name: DetectorName |str|None = None,*,
                         device: str | None = None)-> FaceDetector:
    """Factory function to create a face detector based on the specified name."""
    normalized_name = (
        detector_name or config.detection.default_detector
    ).strip().lower()

    if normalized_name == "haar":
        return HaarFaceDetector()
    elif normalized_name == "yunet":
        return YuNetFaceDetector()
    elif normalized_name == "yolo":
        return YoloFaceDetector(device=device)
    
    supported_detectors = ["haar", "yunet", "yolo"]
    raise ValueError(
        f"Unsupported detector name '{detector_name}'. Supported detectors are: "
        f"{', '.join(supported_detectors)}"
    )

def _validate_frame(frame: np.ndarray) -> None:
    """Validate the input frame."""
    if not isinstance(frame, np.ndarray):
        raise TypeError("Frame must be a NumPy array.")
    if frame.size == 0:
        raise ValueError("Frame is empty.")
    if frame.ndim != 3 or frame.shape[2] != 3:
        raise ValueError("Frame must be a color image with 3 channels (BGR).")
        
def _clip_bbox(
        x1:int,
        y1:int,
        x2:int,
        y2:int,

        frame_width:int,
        frame_height:int
    ) -> BoundingBox|None:
    """Clip the bounding box to ensure it is within the frame boundaries."""
    
    x1 = max(0, min(x1, frame_width))
    y1 = max(0, min(y1, frame_height))
    x2 = max(0, min(x2, frame_width))   
    y2 = max(0, min(y2, frame_height))
    
    return (x1, y1, x2, y2) if x1 < x2 and y1 < y2 else None
