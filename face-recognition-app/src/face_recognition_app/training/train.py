from __future__ import annotations

import argparse
import json
from collections.abc import Sequence
from pathlib import Path

import cv2
import joblib
import numpy as np

from face_recognition_app.common.config import config
from face_recognition_app.preprocessing.preprocess import (
    iter_image_files,
    preprocess_image,
)
from face_recognition_app.training.evaluate import evaluate_classifier
from face_recognition_app.training.mlp_model import (
    create_hyperparameter_search,
    create_mlp_pipeline,
    training_history,
)


def load_classification_dataset(
    directory: str | Path, *, require_multiple_classes: bool = True
) -> tuple[np.ndarray, np.ndarray]:
    """Load class-folder images as flattened classifier features and labels."""
    root = Path(directory).expanduser().resolve()
    features: list[np.ndarray] = []
    labels: list[str] = []

    for image_path in iter_image_files(root):
        relative = image_path.relative_to(root)
        if len(relative.parts) < 2:
            continue
        image = cv2.imread(str(image_path), cv2.IMREAD_COLOR)
        if image is None:
            continue
        features.append(preprocess_image(image).reshape(-1))
        labels.append(relative.parts[0])

    if not features:
        raise ValueError(f"No readable class-folder images found in {root}.")
    if require_multiple_classes and len(set(labels)) < 2:
        raise ValueError("Training requires images from at least two classes.")
    return np.stack(features), np.asarray(labels)


def train_classifier(
    train_dir: str | Path,
    *,
    validation_dir: str | Path | None = None,
    model_path: str | Path | None = None,
    history_path: str | Path | None = None,
    hidden_layer_sizes: tuple[int, ...] = (128,),
    max_iter: int = 300,
    seed: int = 42,
    search_kind: str = "random",
    cv: int = 5,
    search_iterations: int = 12,
    n_jobs: int = -1,
) -> dict[str, object]:
    """Tune, train, persist, and optionally validate the face classifier."""
    features, labels = load_classification_dataset(train_dir)
    class_counts = np.unique(labels, return_counts=True)[1]
    if int(class_counts.min()) < cv:
        raise ValueError(
            f"Each class needs at least {cv} training images for {cv}-fold CV."
        )

    pipeline = create_mlp_pipeline(
        hidden_layer_sizes=hidden_layer_sizes,
        max_iter=max_iter,
        random_state=seed,
    )
    search = create_hyperparameter_search(
        pipeline,
        search_kind=search_kind,
        cv=cv,
        n_iter=search_iterations,
        random_state=seed,
        n_jobs=n_jobs,
    )
    search.fit(features, labels)
    model = search.best_estimator_

    output_model = Path(model_path or config.paths.classifier_model_path)
    output_model.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, output_model)

    history: dict[str, object] = training_history(model)
    history["training_samples"] = len(labels)
    history["search"] = {
        "kind": search_kind,
        "cv_folds": cv,
        "best_score": float(search.best_score_),
        "best_parameters": search.best_params_,
        "candidates": len(search.cv_results_["params"]),
    }
    if validation_dir is not None:
        validation_features, validation_labels = load_classification_dataset(
            validation_dir
        )
        history["validation"] = evaluate_classifier(
            model, validation_features, validation_labels
        )

    output_history = Path(history_path or config.paths.training_history_path)
    output_history.parent.mkdir(parents=True, exist_ok=True)
    output_history.write_text(json.dumps(history, indent=2), encoding="utf-8")
    return history


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Train the MLP face classifier.")
    parser.add_argument("--train-dir", type=Path, default=config.paths.train_data_dir)
    parser.add_argument("--validation-dir", type=Path,)
    parser.add_argument(
        "--model-path", type=Path, default=config.paths.classifier_model_path
    )
    parser.add_argument(
        "--history-path", type=Path, default=config.paths.training_history_path
    )
    parser.add_argument("--hidden-layers", type=int, nargs="+", default=[128])
    parser.add_argument("--max-iter", type=int, default=300)
    parser.add_argument("--seed", type=int, default=42)
    parser.add_argument("--search", choices=("random", "grid"), default="random")
    parser.add_argument("--cv", type=int, default=5)
    parser.add_argument("--search-iterations", type=int, default=12)
    parser.add_argument("--jobs", type=int, default=-1)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    history = train_classifier(
        args.train_dir,
        validation_dir=args.validation_dir,
        model_path=args.model_path,
        history_path=args.history_path,
        hidden_layer_sizes=tuple(args.hidden_layers),
        max_iter=args.max_iter,
        seed=args.seed,
        search_kind=args.search,
        cv=args.cv,
        search_iterations=args.search_iterations,
        n_jobs=args.jobs,
    )
    search_result = history["search"]
    print(
        f"Training complete: {history['training_samples']} samples; "
        f"best CV accuracy={search_result['best_score']:.4f}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
