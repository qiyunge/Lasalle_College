from __future__ import annotations

import cv2
import numpy as np
import pytest
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV

from face_recognition_app.training.evaluate import evaluate_classifier
from face_recognition_app.training.mlp_model import (
    create_hyperparameter_search,
    create_mlp_pipeline,
    training_history,
)
from face_recognition_app.training.train import load_classification_dataset


def test_load_classification_dataset_uses_parent_folder_as_label(tmp_path) -> None:
    for label, value in (("Ada", 0), ("Linus", 255)):
        class_dir = tmp_path / label
        class_dir.mkdir()
        assert cv2.imwrite(
            str(class_dir / "face.jpg"), np.full((8, 8, 3), value, np.uint8)
        )

    features, labels = load_classification_dataset(tmp_path)

    assert features.shape == (2, 100 * 100 * 3)
    assert set(labels) == {"Ada", "Linus"}


def test_load_classification_dataset_requires_two_classes(tmp_path) -> None:
    class_dir = tmp_path / "Ada"
    class_dir.mkdir()
    assert cv2.imwrite(str(class_dir / "face.jpg"), np.zeros((8, 8, 3), np.uint8))

    with pytest.raises(ValueError, match="at least two classes"):
        load_classification_dataset(tmp_path)


def test_pipeline_trains_and_evaluates() -> None:
    features = np.asarray([[0.0], [0.1], [0.9], [1.0]] * 5)
    labels = np.asarray(["a", "a", "b", "b"] * 5)
    model = create_mlp_pipeline(hidden_layer_sizes=(4,), max_iter=100, random_state=3)
    assert model.named_steps["classifier"].early_stopping is False
    model.fit(features, labels)

    metrics = evaluate_classifier(model, features, labels)

    assert 0.0 <= metrics["accuracy"] <= 1.0
    assert metrics["classes"] == ["a", "b"]
    assert np.asarray(metrics["confusion_matrix"]).shape == (2, 2)
    assert training_history(model)["validation_score"] == []


def test_evaluation_supports_multiple_classes() -> None:
    model = create_mlp_pipeline(
        hidden_layer_sizes=(6,), max_iter=100, random_state=3
    )
    features = np.asarray([[0.0], [0.1], [0.5], [0.6], [0.9], [1.0]] * 10)
    labels = np.asarray(
        ["Ada", "Linus", "Grace", "Grace", "Ken", "Ken"] * 10
    )
    model.fit(features, labels)

    metrics = evaluate_classifier(model, features, labels)

    assert metrics["classes"] == ["Ada", "Grace", "Ken", "Linus"]
    assert np.asarray(metrics["confusion_matrix"]).shape == (4, 4)


@pytest.mark.parametrize(
    ("search_kind", "expected_type"),
    [("random", RandomizedSearchCV), ("grid", GridSearchCV)],
)
def test_create_hyperparameter_search(search_kind, expected_type) -> None:
    pipeline = create_mlp_pipeline(max_iter=10)

    search = create_hyperparameter_search(
        pipeline,
        search_kind=search_kind,
        cv=2,
        n_iter=2,
        n_jobs=1,
    )

    assert isinstance(search, expected_type)


def test_create_hyperparameter_search_rejects_unknown_kind() -> None:
    with pytest.raises(ValueError, match="grid.*random"):
        create_hyperparameter_search(create_mlp_pipeline(), search_kind="other")
