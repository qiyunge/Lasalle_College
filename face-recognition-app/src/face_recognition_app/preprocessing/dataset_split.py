from __future__ import annotations

import argparse
import random
import shutil
from collections.abc import Sequence
from pathlib import Path

from face_recognition_app.common.config import config
from face_recognition_app.preprocessing.preprocess import SUPPORTED_IMAGE_SUFFIXES


def validate_split_ratios(train: float, validation: float, test: float) -> None:
    ratios = (train, validation, test)
    if any(ratio < 0 for ratio in ratios):
        raise ValueError("Split ratios cannot be negative.")
    if not abs(sum(ratios) - 1.0) < 1e-9:
        raise ValueError("Split ratios must add up to 1.0.")


def split_counts(total: int, train: float, validation: float) -> tuple[int, int, int]:
    """Return stable counts while assigning rounding remainder to the test set."""
    train_count = int(total * train)
    validation_count = int(total * validation)
    return train_count, validation_count, total - train_count - validation_count


def split_dataset(
    input_dir: str | Path,
    output_dir: str | Path,
    *,
    train_ratio: float = 0.7,
    validation_ratio: float = 0.15,
    test_ratio: float = 0.15,
    seed: int = 42,
) -> dict[str, int]:
    """Copy a class-folder dataset into train, validation, and test folders."""
    validate_split_ratios(train_ratio, validation_ratio, test_ratio)
    source = Path(input_dir).expanduser().resolve()
    destination = Path(output_dir).expanduser().resolve()
    if not source.is_dir():
        raise FileNotFoundError(f"Dataset directory not found: {source}")
    if source == destination or source in destination.parents:
        raise ValueError("Output directory cannot be inside the input directory.")

    totals = {"train": 0, "validation": 0, "test": 0}
    rng = random.Random(seed)
    for class_dir in sorted(path for path in source.iterdir() if path.is_dir()):
        images = sorted(
            path
            for path in class_dir.iterdir()
            if path.is_file() and path.suffix.lower() in SUPPORTED_IMAGE_SUFFIXES
        )
        rng.shuffle(images)
        train_count, validation_count, _ = split_counts(
            len(images), train_ratio, validation_ratio
        )
        groups = {
            "train": images[:train_count],
            "validation": images[train_count : train_count + validation_count],
            "test": images[train_count + validation_count :],
        }
        for split_name, split_images in groups.items():
            class_output = destination / split_name / class_dir.name
            class_output.mkdir(parents=True, exist_ok=True)
            for image_path in split_images:
                shutil.copy2(image_path, class_output / image_path.name)
            totals[split_name] += len(split_images)
    return totals


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Split a face image dataset by class.")
    parser.add_argument("--input-dir", type=Path, default=config.paths.processed_data_dir)
    parser.add_argument("--output-dir", type=Path, default=config.paths.split_data_dir)
    parser.add_argument("--train", type=float, default=0.7)
    parser.add_argument("--validation", type=float, default=0.15)
    parser.add_argument("--test", type=float, default=0.15)
    parser.add_argument("--seed", type=int, default=42)
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    totals = split_dataset(
        args.input_dir,
        args.output_dir,
        train_ratio=args.train,
        validation_ratio=args.validation,
        test_ratio=args.test,
        seed=args.seed,
    )
    print("Split complete: " + ", ".join(f"{key}={value}" for key, value in totals.items()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
