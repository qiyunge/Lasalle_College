from __future__ import annotations

import cv2
import numpy as np
import pytest

from face_recognition_app.preprocessing.augmentation import augment_image
from face_recognition_app.preprocessing.dataset_split import split_dataset
from face_recognition_app.preprocessing.preprocess import (
    preprocess_directory,
    preprocess_image,
)


def test_preprocess_image_resizes_normalizes_and_preserves_color() -> None:
    image = np.full((20, 30, 3), 255, dtype=np.uint8)

    result = preprocess_image(image, (10, 8))

    assert result.shape == (8, 10, 3)
    assert result.dtype == np.float32
    assert np.all(result == 1.0)


def test_preprocess_image_grayscale_keeps_channel_axis() -> None:
    image = np.zeros((12, 15, 3), dtype=np.uint8)
    result = preprocess_image(image, (6, 5), grayscale=True, normalize=False)
    assert result.shape == (5, 6, 1)
    assert result.dtype == np.uint8


def test_preprocess_directory_preserves_class_folders(tmp_path) -> None:
    source = tmp_path / "raw"
    class_dir = source / "Ada"
    class_dir.mkdir(parents=True)
    assert cv2.imwrite(str(class_dir / "face.jpg"), np.zeros((20, 20, 3), np.uint8))
    (class_dir / "notes.txt").write_text("ignored", encoding="utf-8")

    count = preprocess_directory(source, tmp_path / "output", image_size=(8, 7))

    assert count == 1
    result = cv2.imread(str(tmp_path / "output" / "Ada" / "face.jpg"))
    assert result.shape == (7, 8, 3)


def test_split_dataset_is_complete_and_reproducible(tmp_path) -> None:
    source = tmp_path / "raw"
    for class_name in ("Ada", "Linus"):
        class_dir = source / class_name
        class_dir.mkdir(parents=True)
        for index in range(10):
            (class_dir / f"{index}.jpg").write_bytes(b"image")

    totals = split_dataset(source, tmp_path / "split", seed=7)

    assert totals == {"train": 14, "validation": 2, "test": 4}
    assert sum(totals.values()) == 20


def test_split_dataset_rejects_invalid_ratios(tmp_path) -> None:
    with pytest.raises(ValueError, match="add up"):
        split_dataset(tmp_path, tmp_path / "out", train_ratio=0.8)


def test_augmentation_is_reproducible_and_keeps_shape() -> None:
    image = np.arange(12 * 10 * 3, dtype=np.uint8).reshape(12, 10, 3)
    first = augment_image(image, rng=np.random.default_rng(5))
    second = augment_image(image, rng=np.random.default_rng(5))
    assert first.shape == image.shape
    assert first.dtype == image.dtype
    assert np.array_equal(first, second)
