from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('blue')
        # Make the food go really fast so wa can't see it
        self.speed('fastest')
        self.shape("circle")
        # This variable is use for updating the screen later
        self.update_speed = 0.12
        # Create a food with random X and Y
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

    def refresh(self):
        # To refresh the food when the snake eat it
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
        self.update_speed -= 0.002


class Big_food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('red')
        self.speed('fastest')
        self.shape("circle")
        # The big food is double than the size of a regular food
        self.shapesize(stretch_len=2, stretch_wid=2)
        # Make it go out of the screen
        self.goto(1000, 1000)

    def big_food(self):
        # To make the big food appear
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

    def big_food_disappear(self):
        # If it runs out of or the player has eaten it
        self.goto(1000, 1000)