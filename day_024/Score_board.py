from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        with open("highest_score") as data:
            self.highest_score = int(data.read())
        self.last_score = 0
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(0, 480)
        # Print the player score
        self.write(f"Score: {self.score}, high score: {self.highest_score}", align="center",
                   font=("Arial", 24, "normal"))

    def update(self):
        # Update the screen when the player's score insecure
        self.clear()
        self.write(f"Score: {self.score}, high score: {self.highest_score}", align="center",
                   font=("Arial", 24, "normal"))
    # def game_over(self):
        # Go to the center of the window and print GAME OVER when the player die or touch the edge of the screen
        # self.goto(0, 0)
        # self.write("GAME OVER", align="center", font=("Arial", 30, "normal"))

    def reset_game(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("highest_score", mode="w") as data:
                data.write(f"{self.highest_score}")
        self.score = 0
        self.last_score = 0
        self.update()
