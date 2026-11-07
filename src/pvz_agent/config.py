"""User-calibrated screen geometry.

Coordinates are desktop pixels. Keep these unset until the game window is open
and its screen position and board bounds have been measured.
"""
from dataclasses import dataclass


@dataclass
class ScreenConfig:
    monitor: int = 1
    # Optional crop: (left, top, width, height), in desktop coordinates.
    game_region: tuple[int, int, int, int] | None = None

    # Board rectangle: (left, top, right, bottom), in desktop coordinates.
    board_bounds: tuple[int, int, int, int] | None = None

    rows: int = 5
    columns: int = 9

    # Seed packet center points, in desktop coordinates, left-to-right.
    seed_centers: tuple[tuple[int, int], ...] = ()

    # Safety switch: mouse actions remain disabled until calibration is done.
    allow_mouse_control: bool = False
