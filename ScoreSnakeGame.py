from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(x=0, y=350)
        self.score_update()

    def score_update(self):
        self.clear()
        self.write(f"Score: {self.score}", False, "center", ("Arial", 15, "normal"))
        self.score += 1

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!!!", False, "center", ("Arial", 15, "normal"))
