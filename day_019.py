import turtle

jimmy = turtle.Turtle()
Screen = turtle.Screen()
Screen.listen()
jimmy.pensize(3)


def move_forward():
    jimmy.forward(10)


def turn_left():
    jimmy.left(10)


def move_backward():
    jimmy.forward(-10)


def turn_right():
    jimmy.right(10)


Screen.onkey(key="w", fun=move_forward)
Screen.onkey(key="s", fun=move_backward)
Screen.onkey(key="a", fun=turn_left)
Screen.onkey(key="d", fun=turn_right)
Screen.onkey(key="i", fun=jimmy.hideturtle)
Screen.onkey(key="o", fun=jimmy.showturtle)

Screen.exitonclick()
