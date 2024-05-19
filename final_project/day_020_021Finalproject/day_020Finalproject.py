import time
from turtle import Screen
from Foods import Food, Big_food
from Score_board import Score
from Snake import Snake

screen = Screen()
# The width and the height of the screen
screen.screensize(300, 300)
# The title of the game
screen.title("Snake game")
# Prevent the screen to update all the segments
screen.tracer(0)

score_board = Score()
snake = Snake()
food = Food()
big_food = Big_food()
time_to_disappear = 0

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(food.update_speed)
    snake.move(15)
    if snake.head.distance(food) < 20:
        snake.more_segments()
        score_board.score += 1
        score_board.last_score += 1
        score_board.update()
        food.refresh()
    if snake.head.xcor() > 620 or snake.head.xcor() < -620 or snake.head.ycor() > 620 or snake.head.ycor() < -620:
        game_is_on = False
        score_board.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) <= 10:
            game_is_on = False
            score_board.game_over()

    if score_board.last_score == 10:
        big_food.big_food()
        score_board.last_score = 0
        time_to_disappear = int(time.time()) - 20

    if snake.head.distance(big_food) < 40:
        big_food.big_food_disappear()
        score_board.score += (int(time.time()) - time_to_disappear) * 6
        print((int(time.time()) - time_to_disappear) * 5)
        print(score_board.score)
        score_board.update()
    elif int(time.time()) == time_to_disappear:
        big_food.big_food_disappear()

screen.exitonclick()
