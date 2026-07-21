from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import joblib
import numpy as np

from face_recognition_app.common.config import config
from face_recognition_app.preprocessing.preprocess import preprocess_image


@dataclass(frozen=True)
class FacePrediction:
    """Classifier result for one cropped face image."""

    label: str
    confidence: float


class FacePredictor:
    """Load a trained classifier and predict identities from face crops."""

    def __init__(
        self,
        model_path: str | Path | None = None,
        *,
        unknown_threshold: float | None = None,
        unknown_label: str | None = None,
        model: Any | None = None,
    ) -> None:
        self.unknown_threshold = (
            config.recognition.unknown_threshold
            if unknown_threshold is None
            else unknown_threshold
        )
        if not 0.0 <= self.unknown_threshold <= 1.0:
            raise ValueError("Unknown threshold must be between 0 and 1.")
        self.unknown_label = unknown_label or config.recognition.unknown_label

        if model is not None:
            self.model = model
            return

        path = Path(model_path or config.paths.classifier_model_path)
        if not path.is_file():
            raise FileNotFoundError(f"Classifier model not found: {path}")
        self.model = joblib.load(path)

    def predict(self, face_image: np.ndarray) -> FacePrediction:
        """Predict one face, applying the configured unknown-person threshold."""
        features = preprocess_image(face_image).reshape(1, -1)
        probabilities = np.asarray(self.model.predict_proba(features)[0])
        if probabilities.size == 0:
            raise RuntimeError("Classifier returned no class probabilities.")

        best_index = int(np.argmax(probabilities))
        confidence = float(probabilities[best_index])
        label = str(self.model.classes_[best_index])
        if confidence < self.unknown_threshold:
            label = self.unknown_label
        return FacePrediction(label=label, confidence=confidence)
