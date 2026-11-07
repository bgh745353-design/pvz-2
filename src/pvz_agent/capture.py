"""Desktop screenshot capture using MSS; no game memory or process inspection."""
from __future__ import annotations

import cv2
import mss
import numpy as np

from .config import ScreenConfig


class ScreenCapture:
    def __init__(self, config: ScreenConfig):
        self.config = config
        self._sct = mss.mss()

    def grab(self) -> np.ndarray:
        monitors = self._sct.monitors
        if self.config.monitor >= len(monitors):
            raise ValueError(
                f"Monitor {self.config.monitor} is unavailable; "
                f"detected {len(monitors) - 1} monitor(s)."
            )

        region = self.config.game_region or monitors[self.config.monitor]
        shot = np.asarray(self._sct.grab({
            "left": region[0],
            "top": region[1],
            "width": region[2],
            "height": region[3],
        }))
        return cv2.cvtColor(shot, cv2.COLOR_BGRA2RGB)

    def close(self) -> None:
        self._sct.close()
