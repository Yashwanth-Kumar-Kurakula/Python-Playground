from turtle import Turtle

class Tim(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.speed = 10
        self.setheading(90)
        self.goto(0, -280)


    def move_forward(self):
        self.forward(self.speed)


    def move_backward(self):
        self.backward(self.speed)
