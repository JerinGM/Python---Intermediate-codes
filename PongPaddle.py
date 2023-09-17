from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(7, 2)
        self.color("white")
        self.penup()
        self.goto(position)

    def up(self):
        self.goto(self.xcor(), (self.ycor() + 20))



    def down(self):
        self.goto(self.xcor(), (self.ycor() - 20))
