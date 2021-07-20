from turtle import Screen, Turtle
import pandas

screen = Screen()
screen.title("U.S MAP QUIZ GAME")
screen.bgpic("blank_states_img.gif")


# from this functionality I've added the co-ordinates of states on the screen to the csv file.
# ---------------------------------------------
# def click_co_ordindates(x, y):
#     print(x, y)
#
# screen.onscreenclick(click_co_ordindates)
# ----------------------------------------------
class WriteStateName(Turtle):

    def __init__(self, state, x, y):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(x, y)
        self.write(arg=state, align="center")



data = pandas.read_csv("50_states.csv")
states = data["states"]
correct_guess = 0
guessed_states = []

while len(guessed_states) < 50:
    user_input = screen.textinput(title=f"States corrected {correct_guess}/50",
                                  prompt="What's the other state name?").title()

    if user_input == "Exit":
        break

    for state in states:
        if user_input == state:
            x_cor = data[data.states == state].x
            y_cor = data[data.states == state].y
            x_cor = int(x_cor)
            y_cor = int(y_cor)
            write_state = WriteStateName(state, x_cor, y_cor)
            correct_guess += 1
            guessed_states.append(state)


not_answered_states = []
for state in states:
    if state not in guessed_states:
        not_answered_states.append(state)

data_not_answered_dict = {"states": not_answered_states, }

data_not_answered = pandas.DataFrame(data_not_answered_dict)
data_not_answered.to_csv("Missing_states.csv")

screen.exitonclick()
