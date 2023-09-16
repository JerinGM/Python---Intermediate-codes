from turtle import Turtle, Screen

t_obj = Turtle()
screen = Screen()


def forward():
    t_obj.forward(10)


def backward():
    t_obj.backward(10)


def anti_clockwise():
    t_obj.left(10)


def clockwise():
    t_obj.right(10)


def clear():
    t_obj.clear()
    t_obj.penup()
    t_obj.home()
    t_obj.pendown()



screen.listen()
screen.onkey(key="w", fun=forward)
screen.onkey(key="s", fun=backward)
screen.onkey(key="a", fun=anti_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
