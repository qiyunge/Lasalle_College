from __future__ import annotations

import cv2
import numpy as np


def augment_image(
    image: np.ndarray,
    *,
    rng: np.random.Generator | None = None,
    flip_probability: float = 0.5,
    max_rotation: float = 10.0,
    brightness_range: tuple[float, float] = (0.85, 1.15),
) -> np.ndarray:
    """Apply mild, recognition-safe random transformations to one BGR image."""
    if not isinstance(image, np.ndarray):
        raise TypeError("Image must be a NumPy array.")
    if image.size == 0 or image.ndim != 3 or image.shape[2] != 3:
        raise ValueError("Image must be a non-empty BGR image with 3 channels.")
    if not 0.0 <= flip_probability <= 1.0:
        raise ValueError("Flip probability must be between 0 and 1.")
    if max_rotation < 0:
        raise ValueError("Maximum rotation cannot be negative.")
    minimum_brightness, maximum_brightness = brightness_range
    if minimum_brightness <= 0 or minimum_brightness > maximum_brightness:
        raise ValueError("Brightness range must be positive and ordered.")

    generator = rng or np.random.default_rng()
    result = image.copy()
    if generator.random() < flip_probability:
        result = cv2.flip(result, 1)

    height, width = result.shape[:2]
    angle = float(generator.uniform(-max_rotation, max_rotation))
    matrix = cv2.getRotationMatrix2D((width / 2, height / 2), angle, 1.0)
    result = cv2.warpAffine(
        result,
        matrix,
        (width, height),
        flags=cv2.INTER_LINEAR,
        borderMode=cv2.BORDER_REFLECT_101,
    )

    brightness = float(generator.uniform(minimum_brightness, maximum_brightness))
    return np.clip(result.astype(np.float32) * brightness, 0, 255).astype(image.dtype)
