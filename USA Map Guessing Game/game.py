import turtle
import pandas

def load_states_data(file_path):
    """
    Load U.S. states data from a CSV file.

    Parameters:
    - file_path (str): Path to the CSV file.

    Returns:
    - list: List of U.S. states.
    """
    data = pandas.read_csv(file_path)
    return data.state.to_list()

def main():
    """
    Main function to run the U.S. States Guess Game.
    """
    # Load U.S. states data
    states_name = load_states_data("50_states.csv")

    # Set up the turtle screen
    screen = turtle.Screen()
    screen.title("U.S. States Game")

    # Load the U.S. map image
    image = "blank_states_img.gif"
    screen.addshape(image)
    turtle.shape(image)

    # Initialize game variables
    game_active = True
    guessed_states = []

    # Main game loop
    while game_active and len(guessed_states) < 50:
        # Get user input for state name
        guess = screen.textinput("US States Game", "Enter the name of the state: ")
        guess = str(guess).strip().capitalize()

        # Check if the user wants to exit the game
        if guess == "Exit":
            game_active = False

        # Check if the guessed state is correct
        if guess in states_name:
            guessed_states.append(guess)

            # Display the guessed state on the map
            t = turtle.Turtle()
            t.hideturtle()
            t.penup()
            state = data[data.state == guess]
            x_cor = int(state.x.iloc[0])
            y_cor = int(state.y.iloc[0])
            t.goto(x_cor, y_cor)
            t.write(f"*{state.state.item()}", font=("Arial", 8, "normal"))
        else:
            pass

    turtle.mainloop()

# Run the main function
if __name__ == "__main__":
    main()
