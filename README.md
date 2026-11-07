# Plants vs. Zombies RL Agent

A Windows-first reinforcement-learning agent for the original PC version of Plants vs. Zombies.

The agent interacts with the game only through screenshots and mouse/keyboard input. It does not read game memory or internal process state.

## Project status

Initial scaffold in progress.

## Planned architecture

- **Screen capture:** MSS
- **Visual perception:** OpenCV
- **Game controls:** PyAutoGUI
- **RL interface:** Gymnasium
- **Training:** Stable-Baselines3 (PPO)
- **Learning input:** screenshot observations; no game-memory access

## Windows 10 setup

Use Python 3.10 or 3.11.

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Safety and interaction

Run the game in windowed mode where possible. The first milestone is a manually verified Day 1 environment: capture a frame, identify the board, and execute a small set of bounded actions. Training should begin only after the observation and action loop is validated.

## Roadmap

1. Capture screenshots and validate coordinates.
2. Implement bounded mouse actions and a Gymnasium environment.
3. Add basic visual features for sun, seed packets, and lawn cells.
4. Train PPO on short episodes and save checkpoints.
5. Expand to additional levels and mechanics.
