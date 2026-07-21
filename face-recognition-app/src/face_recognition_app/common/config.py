from __future__ import annotations

import os
from pathlib import Path
from dataclasses import dataclass, field


PROJECT_ROOT = Path(__file__).resolve().parents[3]

def _env_path(variable_name: str, default: Path) -> Path:
    """Get a path from an environment variable or use the default."""
    value = os.getenv(variable_name)

    if not value:
        return default.resolve()
    
    path = Path(value).expanduser()
    if not path.is_absolute():
        path = PROJECT_ROOT / path
    return path.resolve()


@dataclass(frozen=True)
class PathConfig:
    project_root: Path = PROJECT_ROOT
    data_dir: Path = field(default_factory = lambda : _env_path(
        "FACE_APP_DATA_DIR",
         PROJECT_ROOT / "data"))
    
    models_dir:Path = field(default_factory = lambda : _env_path(
        "FACE_APP_MODELS_DIR",
         PROJECT_ROOT / "models"))
    
    @property
    def raw_data_dir(self) -> Path:
        return self.data_dir / "raw"
    
    @property
    def processed_data_dir(self) -> Path:
        return self.data_dir / "processed"
    
    @property
    def split_data_dir(self) -> Path:
        return self.data_dir / "split"

    @property
    def train_data_dir(self) -> Path:
        return self.split_data_dir / "train"
    
    @property
    def validation_data_dir(self) -> Path:
        return self.split_data_dir / "validation"
    
    @property
    def test_data_dir(self) -> Path:
        return self.split_data_dir / "test"
    
    @property
    def yunet_model_path(self) -> Path:
        return self.models_dir / "face_detection_yunet_2023mar.onnx"
    
    @property
    def yolo_model_path(self) -> Path:
        return self.models_dir / "yolov8n-face.pt"
    
    @property
    def classifier_model_path(self) -> Path:
        return self.models_dir / "mlp_classifier.joblib"
    
    @property
    def training_history_path(self) -> Path:
        return self.models_dir / "training_history.json"

    @property
    def evaluation_report_path(self) -> Path:
        return self.models_dir / "evaluation_report.json"
    
    @property
    def haar_cascade_path(self) -> Path:
        return self.models_dir / "haarcascade_frontalface_default.xml"
    

@dataclass(frozen=True)
class DetectionConfig:
    default_detector:str = "yunet"
    confidence_threshold: float = 0.7
    nms_threshold: float = 0.4
    top_k: int = 5000
    minimum_face_size: tuple[int, int] = (30, 30)


@dataclass(frozen=True)
class PreprocessingConfig:
    image_size: tuple[int, int] = (100, 100)
    normalize_pixels: bool = True
    grayscale: bool = False
   
@dataclass(frozen=True)
class RecognitionConfig:
    unknown_threshold: float = 0.7
    unknown_label: str = "Unknown"

@dataclass(frozen=True)
class CameraConfig:
    camera_index: int = 0
    frame_width: int = 1280
    frame_height: int = 720
    window_name: str = "Face Recognition App"

@dataclass(frozen=True)
class AppConfig:
    paths: PathConfig = field(default_factory=PathConfig)
    detection: DetectionConfig = field(default_factory=DetectionConfig)
    preprocessing: PreprocessingConfig = field(default_factory=PreprocessingConfig)
    recognition: RecognitionConfig = field(default_factory=RecognitionConfig)
    camera: CameraConfig = field(default_factory=CameraConfig)


def create_required_directories(config: AppConfig) -> None:
    """Create required directories if they don't exist."""
    directories = [
        config.paths.data_dir,
        config.paths.raw_data_dir,
        config.paths.processed_data_dir,
        config.paths.models_dir,
    ]
    for directory in directories:
        directory.mkdir(parents=True, exist_ok=True)

    
config = AppConfig()
