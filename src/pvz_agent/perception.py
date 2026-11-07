"""Small, screenshot-only visual helpers; no access to game internals."""
from __future__ import annotations

import cv2
import numpy as np


def resize_observation(frame: np.ndarray, width: int = 320, height: int = 180) -> np.ndarray:
    """Resize RGB screenshot to a fixed-size RGB observation."""
    return cv2.resize(frame, (width, height), interpolation=cv2.INTER_AREA)


def mean_brightness(frame: np.ndarray) -> float:
    """Return normalized mean brightness as a simple diagnostic feature."""
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    return float(np.mean(gray) / 255.0)
