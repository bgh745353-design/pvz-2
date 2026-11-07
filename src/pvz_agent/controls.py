"""Mouse control with an explicit calibration safety gate."""
from __future__ import annotations

import pyautogui

from .config import ScreenConfig


class GameControls:
    def __init__(self, config: ScreenConfig):
        self.config = config
        # Prevent PyAutoGUI from moving instantly between points.
        pyautogui.PAUSE = 0.08
        pyautogui.FAILSAFE = True

    def click(self, x: int, y: int) -> None:
        if not self.config.allow_mouse_control:
            raise RuntimeError(
                "Mouse control is disabled. Calibrate the game window and "
                "explicitly set allow_mouse_control=True first."
            )
        pyautogui.click(x=int(x), y=int(y))

    def press_escape(self) -> None:
        if not self.config.allow_mouse_control:
            raise RuntimeError("Mouse/keyboard control is disabled.")
        pyautogui.press("esc")
