import time
import turtle
count_space_click = 0
Screen = turtle.Screen()
user_bet = int(Screen.textinput("How long do you want to sleep", "Please input the number(second)").lower())
print("Going to sleep...")
time.sleep(user_bet)
print("Wake up!!!")
time.sleep(1)
print("WAKE UP!!!")
Screen.exitonclick()
