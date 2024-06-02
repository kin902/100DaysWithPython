from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.current_level = 1
        self.goto(-180, 270)
        self.write(arg=f"Current level: {self.current_level}", align="center", font=FONT)

    def update_level(self):
        self.current_level += 1
        self.goto(-180, 270)
        self.clear()
        self.write(arg=f"Current level: {self.current_level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align="center", font=FONT)
