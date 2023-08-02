import turtle
import pandas
from scoreboard import Scoreboard

screen = turtle.Screen()
screen.title("U.S State Guess")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)

scoreboard = Scoreboard()

tit = "Guess the State"
pop = "What's state's name?"
guessed_states = []

while len(guessed_states) < 50:
    screen.update()
    guess = screen.textinput(title=tit, prompt=pop).title()
    data = pandas.read_csv("50_states.csv")
    state_list = data["state"].to_list()

    if guess == "Exit":
        missing_states = [state for state in state_list if state not in guessed_states]
        output = {"state": missing_states}
        print(output)
        pandas.DataFrame(output).to_csv("answer_miss.csv")
        break

    if guess in state_list:

        correct_answer = data[data["state"] == guess]
        x = correct_answer["x"].iloc[0]
        y = correct_answer["y"].iloc[0]
        state_name = correct_answer.state.item()
        guessed_states.append(state_name)

        scoreboard.update((x, y), state_name)

        tit = f"{scoreboard.score}/50 State Correct"

    pop = "What's another state's name?"



