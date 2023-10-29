import turtle

# Create a Turtle object
tim = turtle.Turtle()
# Create a Screen object
screen = turtle.Screen()

def move_forward():
    """Move the turtle forward by 10 units."""
    tim.forward(10)

def move_backward():
    """Move the turtle backward by 10 units."""
    tim.backward(10)

def turn_clockwise():
    """Turn the turtle to the right by 10 degrees and move forward when 'w' key is pressed."""
    tim.right(10)
    screen.onkey(key="w", fun=move_forward)

def turn_anti_clockwise():
    """Turn the turtle to the left by 10 degrees."""
    tim.left(10)

def reset_turtle():
    """Reset the turtle to its initial state."""
    tim.reset()

# Listen for keyboard events
screen.listen()
# Map keyboard keys to their respective functions
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_clockwise)
screen.onkey(key="d", fun=turn_anti_clockwise)
screen.onkey(key="c", fun=reset_turtle)

# Exit the program when clicking anywhere on the screen
screen.exitonclick()

# Start the main event loop
turtle.mainloop()
