# Connect 4 Game

This is a simple implementation of the classic game Connect 4 using the Python library Pygame. The game features a graphical user interface with a welcome screen, game grid, and an exit screen to display the winner or a draw.

## How to Play

1. **Welcome Screen:**
   - The game starts with a welcome screen displaying the title "Connect 4" and game rules.
   - To start the game, click the "PLAY!" button.

2. **Game Grid:**
   - The main game grid consists of 7 columns and 6 rows.
   - Players take turns choosing a column to drop their colored piece.
   - The goal is to connect four pieces of the same color either horizontally, vertically, or diagonally.

3. **Exit Screen:**
   - The game ends when a player connects four pieces or if the grid is full without a winner.
   - The exit screen displays the game result - either a winner or a draw.
   - Click the "EXIT" button to close the game.

## Code Structure

- **WelcomeScreen Class:**
  - Displays the welcome screen with the game title, rules, and a "PLAY!" button.
  - Uses Pygame to handle the graphical interface.

- **Grid Class:**
  - Represents the game grid and manages the state of the board.
  - Handles drawing the grid and checking for win conditions.

- **Player Class:**
  - Represents a player with a specified color.

- **Game Class:**
  - Manages the game loop, player turns, and checks for game results.
  - Uses the Grid and Player classes to handle the game logic.

- **ExitScreen Class:**
  - Displays the exit screen with the game result message and an "EXIT" button.

## How to Run

1. Ensure that Python and Pygame are installed on your machine.
2. Run the `connect4.py` script.

Feel free to modify and extend the code to add additional features or customize the game further. Enjoy playing Connect 4!

## Prerequisites

### Python

Make sure that Python is installed on your computer with:

```sh
python --version
```

### Pygame

Install pygame with pip:

```sh
pip install pygame
```

## Play the game

To play the game, clone this repository with `git clone https://github.com/Yashwanth-Kumar-Kurakula/Python-Playground.git` and go to the game folder:

```sh
cd Python-Playground/Connect-4
```

Then, run:

```sh
python main.py
```

ENJOY THE GAME!!!
