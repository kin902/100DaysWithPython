# Import all the class from the file
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

# Create all the object by OPP
score_board = Score()
snake = Snake()
food = Food()
big_food = Big_food()
# A variable for the big food ( the big red one )
time_to_disappear = 0

# Make the screen listen to the user key
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

# The game is on when the snake didn't touch the end of the screen, or it's body
game_is_on = True
while game_is_on:
    # make the screen update in a ratio with the segments of the snake
    screen.update()
    time.sleep(food.update_speed)
    # Move the snake ( it's head ) by 10 distance
    snake.move(15)
    # If the snake's head is near the food
    if snake.head.distance(food) < 20:
        # Make the snake longer
        snake.more_segments()
        # Add the score to the scoreboard
        score_board.score += 1
        # A variable for counting the food the snake need to eat before the bid food appear ( by 10 point )
        score_board.last_score += 1
        # Update the scoreboard
        score_board.update()
        # Refresh the food
        food.refresh()
    # If the snake head touch the edge of the screen
    if snake.head.xcor() > 620 or snake.head.xcor() < -620 or snake.head.ycor() > 620 or snake.head.ycor() < -620:
        # The game will stop and print GAME OVER
        snake.reset_game()
        score_board.reset_game()
        food.update_speed = 0.12
    # List throw all snake's segments if the snake's head is touching one of them
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) <= 10:
            # The game will stop and print GAME OVER
            snake.reset_game()
            food.update_speed = 0.12
            score_board.reset_game()

    # If the player has eaten 10 foods recently so the big food will appear
    if score_board.last_score == 10:
        big_food.big_food()
        # Reset the last_score ( food )
        score_board.last_score = 0
        # Start to counting the time
        time_to_disappear = int(time.time()) - 15

    # If the snake's head is near the big food so delete the big food and add the point
    if snake.head.distance(big_food) < 40:
        big_food.big_food_disappear()
        # Add the point by multiply by 6 ( so the maximum point is 90 )
        score_board.score += (int(time.time()) - time_to_disappear) * 6

        # Two print function for checking the score because bug
        # print((int(time.time()) - time_to_disappear) * 5)
        # print(score_board.score)

        # Update the score again
        score_board.update()
    # If it runs out of time so it will disappear
    elif int(time.time()) == time_to_disappear:
        big_food.big_food_disappear()

# The screen will close when the player click on it
screen.exitonclick()
