from words import words

import random


def main():
    # Initialization
    word = random.choice(words)
    guessed_letters = ["_" for i in range(len(word))]
    attempts = 7

    # Main loop
    while True:
        # Display the word to guess
        print("Word to guess:", " ".join(guessed_letters))
        print(f"You have {attempts} attempts left.")

        # Ask the player for a letter
        letter = input("Enter a letter: ")

        # Check the letter
        if letter in word:
            # Letter found
            for i in range(len(word)):
                if word[i] == letter:
                    guessed_letters[i] = letter

            # Check the end of the game
            if "_" not in guessed_letters:
                print(f"\nCongratulations, you won! The word was {word}.")
                break

        else:
            # Letter not found
            attempts -= 1
            print(f"The letter {letter} is not in the word.")

            # Check the end of the game
            if attempts == 0:
                print(f"\nLost! The word was {word}...")
                break

        print("\n")


# Program execution
if __name__ == "__main__":
    main()
