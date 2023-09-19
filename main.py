from turtle import Screen, Turtle
import turtle
import pandas

# screen object
screen = Screen()
screen.title("Guess US states game")
screen.addshape("blank_states_img.gif")

# print(user_input)


# tutle object and print the gif on our screen
turtle.shape("blank_states_img.gif")

# want to get the x and y coordinates upon clicking the image
#
#
# def get_coordinates(x, y):
#     print(x, y)
#
#
# screen.onscreenclick(get_coordinates)

states_data = pandas.read_csv("50_states.csv")

state = states_data.state
#print(state)

# print(states_data.state)

x = states_data.x

# print(x) - prints all s coordinates
# print(x[0]) - prints x coordinate of state at index 0

y = states_data.y
count = 0
guess = 50
while guess !=0:
    guess = guess - 1
    user_input = screen.textinput(title=f" {count}/50 States guessed", prompt="Guess")
    for i in range(50):
        if state[i].lower() == user_input.lower():
            count = count + 1
            turtl = Turtle()
            turtl.hideturtle()
            turtl.color("black")
            turtl.penup()
            turtl.goto(x[i], y[i])
            turtl.write(f"{user_input}", False, "center", ("Arial", 10, "normal"))

screen.mainloop()
