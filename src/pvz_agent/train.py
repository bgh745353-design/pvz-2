"""PPO entry point; requires explicit calibration before training."""
from __future__ import annotations

import argparse

from stable_baselines3 import PPO
from stable_baselines3.common.env_checker import check_env

from .config import ScreenConfig
from .env import PvZScreenEnv


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--timesteps", type=int, default=50_000)
    parser.add_argument("--check-only", action="store_true")
    args = parser.parse_args()

    config = ScreenConfig()
    if not config.allow_mouse_control:
        raise SystemExit(
            "Training is blocked by default. First calibrate ScreenConfig "
            "and explicitly enable mouse control in your local config."
        )

    env = PvZScreenEnv(config=config)
    try:
        if args.check_only:
            check_env(env, warn=True)
            print("Gymnasium environment check passed.")
            return

        model = PPO("CnnPolicy", env, verbose=1, tensorboard_log="./runs/tensorboard")
        model.learn(total_timesteps=args.timesteps)
        model.save("./checkpoints/pvz_ppo")
    finally:
        env.close()


if __name__ == "__main__":
    main()
