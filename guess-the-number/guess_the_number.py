import random

def guess_the_number(min_value, max_value):
    """
    Play the "Guess the Number" game.

    Args:
        min_value (int): The minimum number in the range (inclusive).
        max_value (int): The maximum number in the range (inclusive).

    Returns:
        None
    """
    # Generate a random number within the specified range
    secret_number = random.randint(min_value, max_value)
    
    # Initialize variables to keep track of the number of attempts
    attempts = 0

    print(f"Welcome to the Guess the Number game! I'm thinking of a number between {min_value} and {max_value}.")
    
    while True:
        # Get the player's guess
        try:
            player_guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if player_guess < min_value or player_guess > max_value:
            print(f"Please guess a number between {min_value} and {max_value}.")
        elif player_guess < secret_number:
            print("Try a higher number.")
        elif player_guess > secret_number:
            print("Try a lower number.")
        else:
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")
            break

def main():
    """
    Main function to start the game.
    """
    min_value = 1
    max_value = 100  # You can adjust the range as needed.

    guess_the_number(min_value, max_value)


main()
