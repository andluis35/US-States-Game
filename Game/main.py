import pandas
import turtle

NUMBER_OF_STATES = 50

def write_state(land, data):
    state_data = data[data.state == land]
    state_name = turtle.Turtle()
    state_name.hideturtle()
    state_name.penup()
    state_name.color("black")
    state_name.goto(x=state_data.x.item(), y=state_data.y.item())
    state_name.write(land)

screen = turtle.Screen()
screen.setup(width=725, height=491)
screen.title("U.S. States Game")

image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
states_file = pandas.read_csv("./50_states.csv")
right_guesses = 0
guessed_states = []

while right_guesses < NUMBER_OF_STATES:
    if right_guesses == 0:
        answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()
    else:
        updated_score = f"{right_guesses}/{NUMBER_OF_STATES} States Correct"
        answer_state = screen.textinput(title=updated_score, prompt="What's another state's name?").title()

    for state in states_file["state"]:
        if (answer_state == state) and (answer_state not in guessed_states):
            right_guesses += 1
            write_state(state, states_file)
            guessed_states.append(state)

screen.exitonclick()
