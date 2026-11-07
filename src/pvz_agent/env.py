"""Minimal Gymnasium wrapper for real-time screenshot interaction."""
from __future__ import annotations

import time

import gymnasium as gym
import numpy as np
from gymnasium import spaces

from .capture import ScreenCapture
from .config import ScreenConfig
from .controls import GameControls
from .perception import resize_observation


class PvZScreenEnv(gym.Env):
    """A deliberately conservative first environment.

    Action 0 waits for one frame interval. Action 1 clicks the configured
    first seed packet; it is unavailable until a seed center is calibrated
    and mouse control is explicitly enabled. This is a plumbing milestone,
    not yet a complete game-playing policy or reward model.
    """

    metadata = {"render_modes": ["rgb_array"]}

    def __init__(
        self,
        config: ScreenConfig | None = None,
        frame_interval: float = 0.25,
        observation_size: tuple[int, int] = (320, 180),
    ):
        super().__init__()
        self.config = config or ScreenConfig()
        self.capture = ScreenCapture(self.config)
        self.controls = GameControls(self.config)
        self.frame_interval = frame_interval
        self.width, self.height = observation_size

        self.action_space = spaces.Discrete(2)
        self.observation_space = spaces.Box(
            low=0, high=255, shape=(self.height, self.width, 3), dtype=np.uint8
        )

    def _observation(self) -> np.ndarray:
        return resize_observation(self.capture.grab(), self.width, self.height)

    def reset(self, *, seed: int | None = None, options: dict | None = None):
        super().reset(seed=seed)
        time.sleep(self.frame_interval)
        return self._observation(), {"source": "desktop_screenshot"}

    def step(self, action: int):
        if not self.action_space.contains(action):
            raise ValueError(f"Invalid action: {action}")

        if action == 1:
            if not self.config.seed_centers:
                raise RuntimeError("Configure seed_centers before using action 1.")
            x, y = self.config.seed_centers[0]
            self.controls.click(x, y)

        time.sleep(self.frame_interval)
        obs = self._observation()

        # Reward and terminal detection are intentionally not fabricated.
        # Until visual game-state signals are implemented, this is a
        # continuing interaction loop with neutral reward.
        return obs, 0.0, False, False, {"action": int(action)}

    def render(self):
        return self._observation()

    def close(self):
        self.capture.close()
