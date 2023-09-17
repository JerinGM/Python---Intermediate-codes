from turtle import Turtle
class Score(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(position)
        self.score_update()

    def score_update(self):
        self.clear()
        self.write(f"{self.score}", False, "center", ("Courier", 35, "normal"))
        self.score += 1