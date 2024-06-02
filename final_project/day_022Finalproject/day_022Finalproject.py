from turtle import Screen
from day_022_Ball import Ball
from day_022_Paddle import Paddle
from day_022_Score_board import Score_board
import time

screen = Screen()
screen.tracer(0)
screen.setup(800, 600)
screen.title("Pong Game")
screen.bgcolor("black")

score_board = Score_board()
ball = Ball()
R_paddle = Paddle((350, 0))
L_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(R_paddle.up, "Up")
screen.onkey(R_paddle.down, "Down")
screen.onkey(L_paddle.up, "w")
screen.onkey(L_paddle.down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    score_board.update_scoreboard()

    if ball.ycor() > 280 or ball.ycor() < -260:
        ball.bounce_y()

    if ball.distance(R_paddle) < 50 and ball.xcor() > 320 or ball.distance(L_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        score_board.L_point()
        ball.reset_position()

    elif ball.xcor() < -380:
        score_board.R_point()
        ball.reset_position()

screen.exitonclick()
