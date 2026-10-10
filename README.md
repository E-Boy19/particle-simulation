# Particle Simulation ✨

A fullscreen particle animation built using Python and Pygame. The project creates a minimalist visual effect with white particles moving diagonally across a black screen.

## ✨ Features

- **Fullscreen Animation:** Runs across the entire display.
- **Dynamic Particles:** Generates 50 particles with randomized positions, sizes, and movement speeds.
- **Continuous Animation:** Replaces particles as they leave the visible screen area.
- **Smooth Rendering:** Targets 60 FPS for fluid animation.
- **Minimalist Design:** White particles against a black background.
- **Keyboard Control:** Press `ESC` to exit the application.

## 🛠️ Tech Stack

- Python 3
- Pygame
- Random module for particle generation
- Sys module for application termination

## 📂 Project Structure

```text
ParticleSimulation/
├── main.py
├── requirements.txt
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3 installed on your system.
- Pygame installed in your Python environment.

### Installation

1. Clone the repository:

   ```bash
   git clone <your-repository-url>
   ```

2. Navigate to the project directory:

   ```bash
   cd ParticleSimulation
   ```

3. (Optional) Create and activate a virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

4. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

5. Run the application:

   ```bash
   python3 main.py
   ```

## ⚙️ How It Works

1. **Particle Initialization:** Each particle receives a random starting position, radius, and horizontal and vertical speed.
2. **Animation Loop:** The application updates and renders particles continuously at a target of 60 FPS.
3. **Movement:** Particles move diagonally across the screen, increasing slightly in radius over time.
4. **Particle Replacement:** Particles that move beyond the screen boundaries are removed, and new particles are generated to maintain the particle count.
5. **Rendering:** The screen is cleared to black before the particles are drawn in white.

## 👨‍💻 Author

**Aaditya Garud**

Built with Python and Pygame 🐍
