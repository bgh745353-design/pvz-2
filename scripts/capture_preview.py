"""Capture one desktop screenshot to verify MSS setup and game-window framing."""
from pathlib import Path
import argparse

from PIL import Image

from pvz_agent.capture import ScreenCapture
from pvz_agent.config import ScreenConfig


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", default="artifacts/desktop-preview.png")
    args = parser.parse_args()

    capture = ScreenCapture(ScreenConfig())
    try:
        frame = capture.grab()
        output = Path(args.output)
        output.parent.mkdir(parents=True, exist_ok=True)
        Image.fromarray(frame).save(output)
        print(f"Saved screenshot: {output.resolve()}")
        print(f"Frame size: {frame.shape[1]}x{frame.shape[0]}")
    finally:
        capture.close()


if __name__ == "__main__":
    main()
