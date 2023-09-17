from turtle import Turtle
import time

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(1,1)
        self.color("pink")
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        #time.sleep(0.08)
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x, y)

    def bounce(self):
        self.y_move *= -1

    def bouncegame(self):
        self.x_move *= -1

    def reset(self):
        self.goto(0, 0)
        self.bouncegame()
