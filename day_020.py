import time
import turtle
screen = turtle.Screen()
# The width and the height of the screen
screen.screensize(600, 600)
# The title of the game
screen.title("Snake game")
# Prevent the screen to update all the segments
screen.tracer(0)
snake = turtle.Turtle("square")
