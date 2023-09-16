from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=525, height=525)

user_input = screen.textinput(title="Welcome to the turtle race",
                              prompt="Which turtle will win this race, Input a color")

y_axis_positions = [-150, -100, -50, 0, 50, 100, 150]
color = ["pink", "red", "black", "purple", "green", "yellow", "blue"]
all_turtles = []
raceOn = True

for i in range(7):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-250, y=y_axis_positions[i])
    new_turtle.color(color[i])
    all_turtles.append(new_turtle)
#print(all_turtles)

while raceOn == True:
    for turtle in all_turtles:
        if turtle.xcor() > 240:
            raceOn = False
            if turtle.pencolor() == user_input:
                print(f"Your turtle wins the race!! {turtle.pencolor()} is the winner")
            else:
                print(f"Your turtle lost the race. The winner is {turtle.pencolor()}")
        else:
            turtle.forward(random.randint(0,10))

screen.exitonclick()
