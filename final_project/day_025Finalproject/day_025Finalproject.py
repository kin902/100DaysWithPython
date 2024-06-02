import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.setup(725, 491)
screen.addshape("blank_states_img.gif")
screen.tracer(0)
turtle.shape("blank_states_img.gif")

states_data = pandas.read_csv("50_states.csv")
states_name = states_data.state.to_list()
states_xcor = states_data.x.to_list()
states_ycor = states_data.y.to_list()

answer_state = str()
game_is_on = True
guessed_states = list()
missed_states = []

"""
# It will give the user's mouse cor when click random on some point on the screen
def get_mouse_click_cor(x, y):
    print(x, y)

turtle.onscreenclick(get_mouse_click_cor)
# Mainloop with not close the screen when click on it
turtle.mainloop()
"""

while game_is_on:
    screen.update()
    if len(guessed_states) == 50:
        game_is_on = False
    else:
        answer_state = screen.textinput(title="Guess the states",
                                        prompt=f"What's another state's name? {50 - len(guessed_states)} more to go")

    if answer_state == "exit":
        for state in states_name:
            if state not in guessed_states:
                missed_states.append(state)
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("missing_states")
        break
    elif answer_state in states_name and answer_state not in guessed_states:
        state_index = states_name.index(answer_state)
        guessed_states.append(answer_state)
        turtle.goto(states_xcor[state_index], states_ycor[state_index])
        turtle.write(answer_state, align="center", font=("Courier", 10, "normal"))
        turtle.goto(0, 0)
