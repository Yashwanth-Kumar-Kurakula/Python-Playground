from turtle import Turtle
import random

class Blocks(Turtle):
    """
    A class for managing a collection of blocks in a Turtle graphics environment.
    """
    def __init__(self):
        """
        Initializes a Blocks object with attributes for managing blocks.
        """
        super().__init__()
        self.hideturtle()
        self.all_blocks = []
        self.block_colors = ["orange", "green", "red", "black", "blue", "yellow", "pink", "violet"]

    def create_block(self):
        """
        Create a new block with random characteristics and add it to the collection of blocks.

        The chance of creating a new block is determined by a random integer between 1 and 15.
        """
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
        """
        Move all blocks in the collection backward by the specified speed.

        Args:
            speed (int): The speed at which the blocks should move backward.
        """
        for b in self.all_blocks:
            b.backward(speed)
