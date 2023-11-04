from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 0
        self.update_scoreboard(level=self.level)


    def update_scoreboard(self, level):
        self.clear()
        self.goto(-320, 250)
        self.write(f"Level = {level}", align="center", font=("courier", 20, "normal"))


    def update_score(self):
        self.level += 1
        self.update_scoreboard(level=self.level)
