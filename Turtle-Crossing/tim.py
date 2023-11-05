from turtle import Turtle

class Tim(Turtle):
    """
    A class representing the player character 'Tim' in a Turtle graphics game.
    Tim is a turtle that can move forward and backward on the screen.
    """
    def __init__(self):
        """
        Initializes a Tim object with default attributes and initial position.
        """
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.speed = 10  # The speed at which Tim moves.
        self.setheading(90)  # Set Tim's initial orientation (facing upward).
        self.goto(0, -280)  # Set Tim's initial position at the bottom of the screen.

    def move_forward(self):
        """
        Move Tim forward by a distance determined by the 'speed' attribute.
        """
        self.forward(self.speed)

    def move_backward(self):
        """
        Move Tim backward by a distance determined by the 'speed' attribute.
        """
        self.backward(self.speed)
