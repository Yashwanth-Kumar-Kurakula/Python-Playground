# Snake Game

This Python program implements a simple Snake Game using the Pygame library. The game consists of a snake that moves around the screen, eating apples to grow longer. The goal is to survive as long as possible without colliding with the boundaries of the screen or the snake's own body.

## Table of Contents

- [Installation](#installation)
- [Game Controls](#game-controls)
- [Game Rules](#game-rules)
- [Game Elements](#game-elements)
- [Customization](#customization)
- [Acknowledgments](#acknowledgments)

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Yashwanth-Kumar-Kurakula/Python-Playground 
   ```
2. **Navigate to the __Snake_GUI__ Folder**
   
3. **Install Dependencies:**
   Ensure you have Python and Pygame installed. You can install Pygame using:
   ```bash
   pip install pygame
   ```

4. **Run the Game:**
   ```bash
   python snake_game.py
   ```

## Game Controls

- **Up Arrow:** Move the snake up.
- **Right Arrow:** Move the snake to the right.
- **Down Arrow:** Move the snake down.
- **Left Arrow:** Move the snake to the left.
- **Close Window:** Click the close button to exit the game.

## Game Rules

1. **Eat Apples:** The snake must eat apples to grow longer.
2. **Avoid Collisions:** Do not collide with the screen boundaries or the snake's own body.
3. **Scoring:** The score is based on the length of the snake (number of body segments).

## Game Elements

### Snake
- The snake is composed of a head and a body of connected segments.
- The head's direction is controlled by the player.
- The body grows longer when the snake eats an apple.

### Fruit
- Apples appear randomly on the screen.
- The snake must eat apples to grow.
- Eating an apple increases the player's score.

### Score
- The player's score is displayed on the screen.
- It is determined by the length of the snake's body (excluding the head).

### Graphics and Sound
- The game includes graphics for the snake, apples, and the game background.
- Sound effects, such as a "crunch" sound, enhance the gaming experience.

## Customization

1. **Graphics:**
   - You can replace the graphics in the "Graphics" folder with your own images.
   - Ensure the new images have the same dimensions as the original ones.

2. **Sound:**
   - Replace the "crunch.wav" file in the "Sound" folder with your own sound file.

3. **Font:**
   - Replace the "PoetsenOne-Regular.ttf" font file with your preferred font.

## Acknowledgments

- This game is inspired by the tutorial provided by Clear Code, which can be found [here](https://www.youtube.com/watch?v=QFvqStqPCRU&t=6105s).

Feel free to explore and modify the code to suit your preferences. Enjoy playing the Snake Game!
