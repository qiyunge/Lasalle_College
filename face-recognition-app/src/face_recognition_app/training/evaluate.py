from __future__ import annotations

import argparse
import json
from collections.abc import Sequence
from pathlib import Path
from typing import Any

import joblib
import numpy as np
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

from face_recognition_app.common.config import config


def evaluate_classifier(
    model: Any, features: np.ndarray, labels: np.ndarray
) -> dict[str, Any]:
    """Evaluate a fitted classifier and return JSON-serializable metrics."""
    if len(features) != len(labels):
        raise ValueError("Features and labels must contain the same number of samples.")
    if len(labels) == 0:
        raise ValueError("Cannot evaluate an empty dataset.")

    predictions = model.predict(features)
    classes = [str(value) for value in model.classes_]
    return {
        "accuracy": float(accuracy_score(labels, predictions)),
        "classes": classes,
        "confusion_matrix": confusion_matrix(
            labels, predictions, labels=model.classes_
        ).tolist(),
        "classification_report": classification_report(
            labels,
            predictions,
            labels=model.classes_,
            output_dict=True,
            zero_division=0,
        ),
    }


def evaluate_saved_model(
    test_dir: str | Path,
    *,
    model_path: str | Path | None = None,
    report_path: str | Path | None = None,
) -> dict[str, Any]:
    """Evaluate a persisted classifier against an independent class-folder set."""
    from face_recognition_app.training.train import load_classification_dataset

    classifier_path = Path(model_path or config.paths.classifier_model_path)
    if not classifier_path.is_file():
        raise FileNotFoundError(f"Classifier model not found: {classifier_path}")

    features, labels = load_classification_dataset(
        test_dir, require_multiple_classes=False
    )
    model = joblib.load(classifier_path)
    metrics = evaluate_classifier(model, features, labels)
    metrics["test_samples"] = int(len(labels))

    output_path = Path(report_path or config.paths.evaluation_report_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(json.dumps(metrics, indent=2), encoding="utf-8")
    return metrics


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Evaluate a trained face classifier on the test dataset."
    )
    parser.add_argument("--test-dir", type=Path, default=config.paths.test_data_dir)
    parser.add_argument(
        "--model-path", type=Path, default=config.paths.classifier_model_path
    )
    parser.add_argument(
        "--report-path", type=Path, default=config.paths.evaluation_report_path
    )
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    metrics = evaluate_saved_model(
        args.test_dir,
        model_path=args.model_path,
        report_path=args.report_path,
    )
    print(
        f"Evaluation complete: {metrics['test_samples']} samples; "
        f"accuracy={metrics['accuracy']:.4f}"
        
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
