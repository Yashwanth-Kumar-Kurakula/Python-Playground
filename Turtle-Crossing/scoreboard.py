from turtle import Turtle

class Score(Turtle):
    """
    A class for managing the game's score and displaying it on the screen using Turtle graphics.
    """
    def __init__(self):
        """
        Initializes a Score object and sets up the initial score attributes.
        """
        super().__init()
        self.penup()
        self.hideturtle()
        self.level = 0
        self.update_scoreboard(level=self.level)

    def update_scoreboard(self, level):
        """
        Update the scoreboard on the screen with the current game level.

        Args:
            level (int): The level to be displayed on the scoreboard.
        """
        self.clear()
        self.goto(-320, 250)
        self.write(f"Level = {level}", align="center", font=("courier", 20, "normal"))

    def update_score(self):
        """
        Increase the game level by 1 and update the scoreboard to reflect the new level.
        """
        self.level += 1
        self.update_scoreboard(level=self.level)
