from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('blue')
        self.speed('fastest')
        self.shape("circle")
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)


class Big_food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color('red')
        self.speed('fastest')
        self.shape("circle")
        self.shapesize(stretch_len=2, stretch_wid=2)
        self.goto(1000, 1000)

    def big_food(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

    def big_food_disappear(self):
        self.goto(1000, 1000)