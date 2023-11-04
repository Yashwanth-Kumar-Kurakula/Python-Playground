from turtle import Screen
from tim import Tim
from blocks import Blocks
from scoreboard import Score
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("white")
screen.tracer(0)

tim = Tim()
blocks = Blocks()
score = Score()


screen.listen()
screen.onkey(tim.move_forward, "w")
screen.onkey(tim.move_backward, "s")


is_game_true = True
car_speed = 1


while is_game_true:
    screen.update()
    time.sleep(0.01)
    blocks.create_block()
    blocks.move(speed=car_speed)


    for block in blocks.all_blocks:
        if block.distance(tim) < 20:
            is_game_true = False


    if tim.ycor() > 330:
        tim.goto(0, -280)
        car_speed += 1
        score.update_score()


screen.exitonclick()
