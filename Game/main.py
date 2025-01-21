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

def set_player_guess(game_screen, score):
    if score == 0:
        return game_screen.textinput(title="Guess the State", prompt="What's another state's name?").title()
    else:
        updated_score = f"{score}/{NUMBER_OF_STATES} States Correct"
        return game_screen.textinput(title=updated_score, prompt="What's another state's name?").title()

def check_for_missing_states(states, written_states):
    missing_states_dictionary = {
        "state": []
    }

    for land in states["state"]:
        if land not in written_states:
            missing_states_dictionary["state"].append(land)

    return missing_states_dictionary

def create_csv_file_with_missing_states(missing_states_dictionary):
    missing_states_data = pandas.DataFrame(missing_states_dictionary)
    missing_states_data.to_csv("./missing_states.csv")

def start_game():
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
        answer_state = set_player_guess(screen, right_guesses)

        if answer_state == "Exit":
            break

        for state in states_file["state"]:
            if (answer_state == state) and (answer_state not in guessed_states):
                right_guesses += 1
                write_state(state, states_file)
                guessed_states.append(state)

    missing_states = check_for_missing_states(states_file, guessed_states)
    create_csv_file_with_missing_states(missing_states)

start_game()
