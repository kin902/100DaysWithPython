import time
import turtle

screen = turtle.Screen()
# The width and the height of thhe screen
screen.screensize(600, 600)
# The coordination that three first segments can appear
start_position = [(0, 0), (-20, 0), (-40, 0)]
# The title of the game
screen.title("Snake game")
# Prevent the screen to update all the segments
screen.tracer(0)
# A list contain all segments
segments = []

for body in range(0, 3):
    segment = turtle.Turtle("square")
    segment.penup()
    segment.goto(start_position[body])
    segments.append(segment)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg in segments:
        seg.forward(20)

screen.exitonclick()
