import turtle
from turtle import Turtle, Screen
import random
# Extracting all the color from a random picture
"""
import colorgram
rgb_colors = []
colors = colorgram.extract('download (1).jpg', 25)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b

    rgb_colors.append((r, g, b))
"""
# All possible colors the turtle can be
colors = [(199, 175, 119), (124, 36, 24), (187, 158, 51), (169, 106, 56), (6, 56, 84), (206, 219, 209), (223, 223, 226), (108, 67, 85), (39, 36, 35), (20, 122, 176), (88, 142, 55), (9, 67, 47), (63, 153, 137), (76, 39, 48), (110, 161, 175), (134, 41, 43), (183, 97, 80), (209, 199, 127), (179, 202, 186), (147, 171, 158), (170, 159, 163), (212, 184, 175), (30, 77, 60)]
# Color mode = RGB
turtle.colormode(255)
jimmy = Turtle()
screen = Screen()
y = -190
# Hide the turtle anh change the speed to fastest
jimmy.hideturtle()
jimmy.speed("fastest")
times = 0
# Coordinate for 9 row
for i in range(0, 7):
    jimmy.penup()
    jimmy.goto((-190, y))
    y += 60
    times += 1
    # Draw 9 dots ong that row
    for o in range(0, 8):
        jimmy.pendown()
        jimmy.dot(30,colors[i + o])
        jimmy.penup()
        jimmy.forward(50)
        times += 1
# Exit when the user clik on the window
screen.exitonclick()
