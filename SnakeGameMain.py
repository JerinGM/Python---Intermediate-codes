from turtle import Screen
from snake import Snake
from foodClassSnakeGame import Food
from ScoreSnakeGame import Score
import time
screen = Screen()
screen.setup(width=1000, height=750)
screen.bgcolor("black")
screen.title("Jerin's Snake Game")
gameOn = True
screen.tracer(0)

snake_object = Snake()
snake_object.snake_create()
food_object = Food()
score_object = Score()


screen.listen()
screen.onkey(fun=snake_object.up, key="Up")
screen.onkey(fun=snake_object.down, key="Down")
screen.onkey(fun=snake_object.left, key="Left")
screen.onkey(fun=snake_object.right, key="Right")


while gameOn:
    screen.update()
    time.sleep(0.1)
    snake_object.snake_move()
    if snake_object.empty_list[0].distance(food_object) < 15:
        food_object.refresh()
        score_object.score_update()
        snake_object.snake_extend(snake_object.empty_list[-1].position())
    #collision detection
    if snake_object.empty_list[0].xcor() < -495 or snake_object.empty_list[0].xcor() > 480 or snake_object.empty_list[0].ycor() < -360 or snake_object.empty_list[0].ycor() > 360:
        gameOn = False
        score_object.game_over()

    for item in snake_object.empty_list:
        if snake_object.empty_list[0].distance(item) < 10 and item != snake_object.empty_list[0]:
            gameOn = False
            score_object.game_over()

screen.exitonclick()

