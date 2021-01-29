import turtle
import pandas
from state import State

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
screen.tracer(0)

data = pandas.read_csv("50_states.csv")
states = data.state.tolist()
x = data.x.tolist()
y = data.y.tolist()
turtles = []

for i in range(len(states)):
    temp_state = State(x[i], y[i], states[i])
    turtles.append(temp_state)

print(states)

correct_guesses = 0
correct_states = []
cond = 1
while cond:
    answer_state = screen.textinput(f"{correct_guesses}/50 States Correct", "What's another state's name?")
    for state in turtles:
        if answer_state is None or correct_guesses == 50:
            cond = 0
        elif state.match(answer_state.title()):
            correct_guesses += 1
            correct_states.append(answer_state.title())
            state.reveal()

missing_states = [state for state in states if state not in correct_states]

retval = pandas.DataFrame(missing_states)
retval.to_csv("missing_states.csv")


screen.exitonclick()
