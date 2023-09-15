# import colorgram
# emptyList = []
# colors = colorgram.extract('image.jpg', 30)
# for color in range(30):
#     rgb = colors[color].rgb
#     r = rgb.r
#     g = rgb.g
#     b = rgb.b
#     my_tuple = (r,g,b)
#     emptyList.append(my_tuple)

#print(emptyList)

import random
import turtle
from turtle import Turtle
from turtle import Screen
color_list = [(244, 228, 79), (162, 75, 42), (216, 146, 90), (23, 30, 61), (124, 160, 218), (54, 89, 145), (45, 36, 30), (40, 48, 114), (29, 44, 34), (147, 56, 81), (131, 31, 43), (203, 82, 120), (146, 31, 25), (214, 80, 55), (69, 31, 41), (67, 113, 77), (133, 182, 164), (94, 105, 200), (193, 140, 155), (72, 79, 40), (96, 162, 82), (153, 207, 220), (156, 186, 235), (48, 87, 32), (171, 165, 69), (229, 169, 185)]
turtle.colormode(255)

turtle_object = Turtle()
turtle_object.speed("fastest")
turtle_object.pensize(8)

turtle_object.penup()
turtle_object.backward(200)
turtle_object.right(90)
turtle_object.penup()
turtle_object.forward(200)
#print(turtle_object.position())
turtle_object.left(90)
for pos in range(17):
    for i in range(10):
        turtle_object.hideturtle()
        turtle_object.pendown()
        turtle_object.dot(13, random.choice(color_list))
        turtle_object.penup()
        turtle_object.forward(40)
    turtle_object.penup()
    turtle_object.left(90)
    turtle_object.forward(25)
    turtle_object.left(90)
    turtle_object.forward(400)
    turtle_object.right(180)


















screen = Screen()
screen.exitonclick()


