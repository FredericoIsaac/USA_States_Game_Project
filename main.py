import turtle
import pandas
from state_class import State

# Screen configuration's
screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# Initialising
guesses_list = []
states_data = pandas.read_csv("50_states.csv")

number_of_states = len(states_data.axes[0])

while len(guesses_list) < 50:

    answer_state = screen.textinput(title=f"{len(guesses_list)}/{number_of_states} States Correct",
                                    prompt="What's another state name?").title()

    if answer_state == "Exit":
        states_missed = states_data[states_data["state"] != guesses_list[0]]

        for index_guessed in range(1, len(guesses_list)):
            states_missed = states_missed[states_missed["state"] != guesses_list[index_guessed]]

        states_missed.to_csv("states_to_learn.csv", index=False)

        break

    search_answer_data = states_data[states_data["state"] == answer_state]

    if search_answer_data.empty or answer_state in guesses_list:
        continue

    state_text_turtle = State(search_answer_data)
    guesses_list.append(answer_state)


screen.exitonclick()


