from turtle import Turtle
import random

class Blocks(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.all_blocks = []
        self.block_colors = ["orange", "green", "red", "black", "blue", "yellow", "pink", "violet"]


    def create_block(self):
        chance = random.randint(1, 15)
        if chance == 1:
            new_block = Turtle("square")
            new_block.penup()
            new_block.color(random.choice(self.block_colors))
            new_block.shapesize(stretch_wid=1, stretch_len=3)
            y_rand = random.randint(-250, 250)
            new_block.goto(350, y_rand)
            self.all_blocks.append(new_block)


    def move(self, speed):
        for b in self.all_blocks:
            b.backward(speed)
