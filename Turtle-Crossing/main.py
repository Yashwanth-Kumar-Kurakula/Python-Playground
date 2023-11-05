from turtle import Screen
from tim import Tim
from blocks import Blocks
from scoreboard import Score
import time

# Create a Turtle graphics screen.
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("white")
screen.tracer(0)

# Initialize Tim (the player), Blocks (obstacles), and Score (score tracking).
tim = Tim()
blocks = Blocks()
score = Score()

# Listen for keyboard input to control Tim's movement.
screen.listen()
screen.onkey(tim.move_forward, "w")
screen.onkey(tim.move_backward, "s")

# Initialize game-related variables.
is_game_true = True  # Flag to control the game loop.
car_speed = 1  # Initial speed of Tim's movement.

# Main game loop.
while is_game_true:
    screen.update()
    time.sleep(0.01)
    blocks.create_block()
    blocks.move(speed=car_speed)

    # Check for collisions between Tim and the blocks.
    for block in blocks.all_blocks:
        if block.distance(tim) < 20:
            is_game_true = False  # End the game if a collision occurs.

    # Check if Tim reaches the top of the screen, update the score, and increase the speed.
    if tim.ycor() > 330:
        tim.goto(0, -280)
        car_speed += 1
        score.update_score()

# Close the game window when the game is over.
screen.exitonclick()
