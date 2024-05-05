import time
import turtle
from Snake import Snake
from Foods import Food
from Score_board import Score
screen = turtle.Screen()
# The width and the height of the screen
screen.screensize(300, 300)
# The title of the game
screen.title("Snake game")
# Prevent the screen to update all the segments
screen.tracer(0)

score_board = Score()
snake = Snake()
food = Food()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move(20)
    if snake.head.distance(food) < 20:
        score_board.score += 1
        score_board.update()
        food.refresh()

screen.exitonclick()
