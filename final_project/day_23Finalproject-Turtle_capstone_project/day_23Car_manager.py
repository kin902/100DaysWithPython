import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 10
MOVE_INCREMENT = 2.5


class CarManager:
    def __init__(self):
        self.all_car = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def new_car(self):
        chance_create_new_car = random.randint(1, 6)
        if chance_create_new_car == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            random_y = random.randint(-230, 230)
            new_car.goto(x=280, y=random_y)
            self.all_car.append(new_car)

    def move_car(self):
        for car in self.all_car:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
