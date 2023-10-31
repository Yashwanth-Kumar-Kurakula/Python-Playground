import random

def welcome_message():
    """Display a welcome message to the user."""
    print("Welcome to the number guessing game:")

def select_difficulty():
    """Prompt the user to select a game difficulty and return the number of tries."""
    while True:
        try:
            difficulty = int(input("Press 1 for Easy Mode\nPress 2 for Normal Mode\nPress 3 for Hard Mode\nEnter the difficulty that you want to play: "))
            if 1 <= difficulty <= 3:
                return [10, 5, 3][difficulty - 1]
            else:
                print("Invalid input. Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter 1, 2, or 3.")

def get_valid_guess():
    """Get a valid numeric guess from the user."""
    while True:
        try:
            guess = int(input("Enter a number between 1 and 100: "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Invalid input. Please enter a number between 1 and 100.")
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 100.")

def main():
    """Main function to run the number guessing game."""
    welcome_message()
    
    game_on = True
    correct_number = random.randint(1, 100)
    
    tries = select_difficulty()
    
    while game_on and tries > 0:
        guess = get_valid_guess()
        if guess == correct_number:
            print("You have guessed correctly!")
            game_on = False
        elif guess > correct_number:
            print("You need to guess a lower number")
        else:
            print("You need to guess a higher number")
        
        tries -= 1

    if tries == 0:
        print(f"Oops! You are out of tries, the correct number was {correct_number}")

if __name__ == "__main__":
    main()
