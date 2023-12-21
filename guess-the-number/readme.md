# Number Guessing Game

Welcome to the Number Guessing Game! This simple Python program allows you to play a number guessing game where you try to guess the correct number within a specified number of tries. Whether you are a beginner or an experienced Python programmer, this game is designed to be easy to follow and fun to play.

## How to Play

1. Run the Python script in your preferred development environment or command line.
2. Follow the instructions to select a difficulty level (Easy, Normal, or Hard).
3. Enter your guesses and receive feedback on whether the correct number is higher or lower.
4. Keep guessing until you either guess the correct number or run out of tries.

## Game Components

### 1. `welcome_message()`

This function displays a welcome message to the user when the game starts.

### 2. `select_difficulty()`

This function prompts the user to select a game difficulty and returns the number of tries allowed based on the chosen difficulty. The difficulty levels are as follows:
- Easy Mode: 10 tries
- Normal Mode: 5 tries
- Hard Mode: 3 tries

### 3. `get_valid_guess()`

This function ensures that the user enters a valid numeric guess between 1 and 100. It prompts the user until a valid guess is provided.

### 4. `main()`

The main function orchestrates the entire game. It calls the `welcome_message()` function, generates a random correct number, and allows the user to make guesses within the specified number of tries based on the selected difficulty.

#### Game Flow:
- User is prompted to select a difficulty level.
- User enters guesses and receives feedback.
- The game continues until the user guesses correctly or runs out of tries.
- A message is displayed based on the outcome of the game.

## How to Run the Game

1. Make sure you have Python installed on your system.
2. Save the provided code in a file, for example, `number_guessing_game.py`.
3. Open a terminal or command prompt and navigate to the directory containing the script.
4. Run the script by entering the following command:
   ```
   python guess_the_number.py
   ```
5. Follow the on-screen instructions to play the game.


Have fun and happy guessing!