# Endless Runner Game

Welcome to the Endless Runner Game! This game is a simple yet engaging runner implemented using the Pygame library. It is designed to help beginner programmers understand the fundamentals of game development. Let's dive into the details of the game and its logic.

## Table of Contents
1. [Installation](#installation)
2. [Game Controls](#game-controls)
3. [Game Logic](#game-logic)
4. [Customization](#customization)
5. [Contributing](#contributing)
6. [License](#license)

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Yashwanth-Kumar-Kurakula/Python-Playground 
   ```
2. **Navigate to the __Runner-Game__ Folder**
   
3. **Install Dependencies:**
   Ensure you have Python and Pygame installed. You can install Pygame using:
   ```bash
   pip install pygame
   ```

4. **Run the Game:**
   ```bash
   python runner.py
   ```

## Game Controls

- **Jump**: Press the spacebar to make the character jump over obstacles.
- **Quit**: Press 'Q' to exit the game.

## Game Logic

### Character Movement

- The character automatically moves forward.
- The player can make the character jump by pressing the spacebar.
- The longer the spacebar is held, the higher the character jumps.

### Obstacles

- Snails and flies serve as obstacles and appear randomly on the screen.
- Snails move along the ground, while flies move at a higher altitude.
- Jump over obstacles to avoid collisions.

### Scoring

- Players earn points for every second survived.
- The score is displayed on the screen.

### Game Over

- The game ends when the character collides with an obstacle.
- The final score is displayed along with instructions to restart.

## Customization

- The game can be customized by modifying the source code.
- Change character appearances, obstacle types, or background.
- Experiment with different parameters to adjust difficulty levels.

## Contributing

Contributions are welcome! If you find a bug or have an idea for an improvement, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details. Feel free to use, modify, and distribute the game as you see fit.
