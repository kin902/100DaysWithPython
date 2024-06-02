import random
from turtle import Turtle, Screen
name_2 = ["red", "orange", "yellow", "green", "blue", "purple", "pink"]
name = ["Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Pink"]
color = ("Red", "Orange", "Yellow", "Green", "Blue", "Purple", "Pink")
positions = (-150, -100, -50, 0, 50, 100, 150)
win = False
winner = str()
screen = Screen()
winner_name = str()
screen.setup(500, 400)
for i in range(0, 7):
    name[i] = Turtle()
    name[i].penup()
    name[i].shape("turtle")
    name[i].color(color[i])
    name[i].goto(-230, positions[i])
user_bet = str(screen.textinput("Make your bet", "Which turtle will win the race?").lower())
while not win:
    for i in range(0, 7):
        name[i].forward(random.randint(0, 10))
        if name[i].xcor() >= 250.0 and winner == "":
            win = True
            winner = str(name_2[i])
if user_bet == winner:
    print("You guess it right the " + winner + " turtle win!!!")
else:
    print("You guess it wrong the " + winner + " turtle win =(")
