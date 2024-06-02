import time
from turtle import Screen
from day_23Player import Player
from day_23Car_manager import CarManager
from day_23Scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
player = Player()
car_manager = CarManager()
score_board = Scoreboard()

screen.listen()
screen.onkey(fun=player.move_forward, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.new_car()
    car_manager.move_car()
    for car in car_manager.all_car:
        if player.distance(car) < 20:
            game_is_on = False
            score_board.game_over()

    if player.ycor() >= 280:
        player.goto_start()
        car_manager.level_up()
        score_board.update_level()

screen.exitonclick()
