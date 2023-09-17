from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("pink")
        self.speed(0)
        self.refresh()

    def refresh(self):
        self.goto(((random.randint(-490, 490)), (random.randint(-335, 335))))
