import turtle
import random
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]
"""
jimmy_the_turtle = turtle.Turtle()
screen = turtle.Screen()
times = 3
for i in range(0, 10):
    jimmy_the_turtle.color(random.choice(colours))
    for o in range(0, times):
        jimmy_the_turtle.forward(100)
        jimmy_the_turtle.right(360 / times)
    times += 1

screen.exitonclick()
"""

direction = [0, 90, 180, 270]
jimmy = turtle.Turtle()
jimmy.pensize(12)
jimmy.speed(0)
Screen = turtle.Screen()
for i in range(0, 10000):
    jimmy.color(random.choice(colours))
    jimmy.left(random.choice(direction))
    jimmy.forward(30)

jimmy.home()
Screen.exitonclick()
