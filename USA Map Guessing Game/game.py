import turtle, pandas

data = pandas.read_csv("50_states.csv")
states_name = data.state.to_list()


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

game_active = True
guessed_states = []

while game_active and len(guessed_states) < 50:
    guess = screen.textinput("US States Game", "Enter the name of state: ")
    guess = str(guess).strip().capitalize()
    if guess == "Exit":
        game_active = False

    if guess in states_name:
            guessed_states.append(guess)
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
