# import turtle
# import pandas
#
#
# #Screen Setup
# screen = turtle.Screen()
# screen.title("U.S. States Game")
# image = "blank_states_img.gif"
# screen.addshape(image)
# turtle.shape(image)
#
# data = pandas.read_csv("50_states.csv")
# all_states = data.state.to_list()
# guessed_state = []
#
#
# while len(guessed_state) < 50:
#     answer_state = screen.textinput(title=f"{len(guessed_state)}/50 States Correct",
#                                     prompt="what's another state?").title()
#
# #If  answer_state is one of the states in all states of the 50_states.csv
#     #If they got it right:
#         #Create a turtle to write the name of the state at the state's x and y coordinate
#     if answer_state in all_states:
#         guessed_state.append(answer_state)
#         t = turtle.Turtle()
#         t.hideturtle()
#         t.penup()
#         state_data = data[data.state == answer_state]
#         t.goto(int(state_data.x), int(state_data.y))
#         t.write(answer_state)
#
# screen.exitonclick()


