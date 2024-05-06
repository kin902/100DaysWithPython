from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.last_score = 0
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 480)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def update(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=("Arial", 30, "normal"))
