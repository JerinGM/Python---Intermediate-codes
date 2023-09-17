from turtle import Turtle


class Snake:

    def __init__(self):
        self.empty_list = []

    def snake_create(self):
        x_position = [0, -20, -40]
        # STARTING SNAKE
        for item in range(3):
            new_square = Turtle("square")
            new_square.color("white")
            new_square.penup()
            new_square.goto(x=x_position[item], y=0)
            self.empty_list.append(new_square)

    # Adding snake segment to -1(the last value)
    def snake_extend(self, position):
        new_square = Turtle("square")
        new_square.color("white")
        new_square.penup()
        new_square.goto(position)
        self.empty_list.append(new_square)


    def snake_move(self):
        # 3rd square to be in 2's position, 2 in 1's and so on. Achieving this by the below for loop. MOVING SNAKE
        for item in range(len(self.empty_list) - 1, 0, -1):
            x_pos = self.empty_list[item - 1].xcor()
            y_pos = self.empty_list[item - 1].ycor()
            self.empty_list[item].goto(x_pos, y_pos)
        # forward should be 20 as that is the size of our turtle
        self.empty_list[0].forward(20)

    def up(self):
        if self.empty_list[0].heading() != 270:
            self.empty_list[0].setheading(90)

    def down(self):
        if self.empty_list[0].heading() != 90:
            self.empty_list[0].setheading(270)

    def left(self):
        if self.empty_list[0].heading() != 0:
            self.empty_list[0].setheading(180)

    def right(self):
        if self.empty_list[0].heading() != 180:
            self.empty_list[0].setheading(0)
