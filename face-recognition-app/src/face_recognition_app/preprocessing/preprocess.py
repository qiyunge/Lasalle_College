from __future__ import annotations

import argparse
from collections.abc import Iterable, Sequence
from pathlib import Path

import cv2
import numpy as np

from face_recognition_app.common.config import config


SUPPORTED_IMAGE_SUFFIXES = frozenset({".bmp", ".jpeg", ".jpg", ".png", ".webp"})


def preprocess_image(
    image: np.ndarray,
    image_size: tuple[int, int] | None = None,
    *,
    grayscale: bool | None = None,
    normalize: bool | None = None,
) -> np.ndarray:
    """Convert a BGR image to the shape and value range used by the classifier."""
    if not isinstance(image, np.ndarray):
        raise TypeError("Image must be a NumPy array.")
    if image.size == 0:
        raise ValueError("Image is empty.")
    if image.ndim not in (2, 3) or (image.ndim == 3 and image.shape[2] not in (1, 3)):
        raise ValueError("Image must be grayscale or a BGR image with 3 channels.")

    width, height = image_size or config.preprocessing.image_size
    if width <= 0 or height <= 0:
        raise ValueError("Image dimensions must be positive.")

    use_grayscale = config.preprocessing.grayscale if grayscale is None else grayscale
    use_normalization = (
        config.preprocessing.normalize_pixels if normalize is None else normalize
    )

    processed = image
    if use_grayscale and processed.ndim == 3:
        processed = cv2.cvtColor(processed, cv2.COLOR_BGR2GRAY)
    elif not use_grayscale and processed.ndim == 2:
        processed = cv2.cvtColor(processed, cv2.COLOR_GRAY2BGR)

    processed = cv2.resize(processed, (width, height), interpolation=cv2.INTER_AREA)
    if use_grayscale and processed.ndim == 2:
        processed = processed[..., np.newaxis]

    if use_normalization:
        processed = processed.astype(np.float32) / 255.0
    return processed


def iter_image_files(directory: str | Path) -> Iterable[Path]:
    """Yield supported images below a directory in deterministic order."""
    root = Path(directory).expanduser().resolve()
    if not root.is_dir():
        raise FileNotFoundError(f"Image directory not found: {root}")
    return (
        path
        for path in sorted(root.rglob("*"))
        if path.is_file() and path.suffix.lower() in SUPPORTED_IMAGE_SUFFIXES
    )


def preprocess_directory(
    input_dir: str | Path,
    output_dir: str | Path,
    *,
    image_size: tuple[int, int] | None = None,
    grayscale: bool | None = None,
) -> int:
    """Preprocess a class-folder dataset while preserving its directory layout."""
    source = Path(input_dir).expanduser().resolve()
    destination = Path(output_dir).expanduser().resolve()
    if source == destination:
        raise ValueError("Input and output directories must be different.")

    count = 0
    for image_path in iter_image_files(source):
        image = cv2.imread(str(image_path), cv2.IMREAD_COLOR)
        if image is None:
            continue
        processed = preprocess_image(
            image,
            image_size=image_size,
            grayscale=grayscale,
            normalize=False,
        )
        output_path = destination / image_path.relative_to(source)
        output_path.parent.mkdir(parents=True, exist_ok=True)
        if not cv2.imwrite(str(output_path), processed):
            raise RuntimeError(f"Failed to write processed image: {output_path}")
        count += 1
    return count


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Resize and standardize face images.")
    parser.add_argument("--input-dir", type=Path, default=config.paths.raw_data_dir)
    parser.add_argument("--output-dir", type=Path, default=config.paths.processed_data_dir)
    parser.add_argument("--width", type=int, default=config.preprocessing.image_size[0])
    parser.add_argument("--height", type=int, default=config.preprocessing.image_size[1])
    parser.add_argument("--grayscale", action="store_true")
    return parser


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    count = preprocess_directory(
        args.input_dir,
        args.output_dir,
        image_size=(args.width, args.height),
        grayscale=args.grayscale,
    )
    print(f"Processed {count} images into {args.output_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
