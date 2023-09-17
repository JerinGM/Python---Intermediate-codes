from turtle import Turtle


class Net(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")

    def move_up(self):
        self.left(90)
        for i in range(19):
            self.forward(10)
            self.penup()
            self.forward(10)
            self.pendown()

    def move_down(self):
        self.right(90)
        for i in range(19):
            self.forward(10)
            self.penup()
            self.forward(10)
            self.pendown()
