import time
import turtle
from day_020Snake import Snake
screen = turtle.Screen()
# The width and the height of thhe screen
screen.screensize(600, 600)
# The title of the game
screen.title("Snake game")
# Prevent the screen to update all the segments
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(fun=snake.up, key="w")
screen.onkey(fun=snake.down, key="s")
screen.onkey(fun=snake.left, key="a")
screen.onkey(fun=snake.right, key="d")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move(20)
screen.exitonclick()
