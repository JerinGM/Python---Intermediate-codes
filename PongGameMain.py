from turtle import Screen
import time
from PongPaddle import Paddle
from netPong import Net
from Pongball import Ball
from scorePong import Score
gameOn = True

screen = Screen()
screen.setup(width=1300, height=700)
screen.title("Legendary Pong Game - by Jerin")
screen.bgcolor("black")
screen.tracer(0)

paddleone = Paddle((630, 0))
paddletwo = Paddle((-630, 0))
ball = Ball()
netup = Net()
netdown = Net()
scoreL = Score((-30, 300))
scoreR = Score((30, 300))

netup.move_up()
netdown.move_down()
screen.listen()
screen.onkey(fun=paddleone.up, key="Up")
screen.onkey(fun=paddleone.down, key="Down")
screen.onkey(fun=paddletwo.up, key="w")
screen.onkey(fun=paddletwo.down, key="s")

while gameOn:
    time.sleep(0.04)
    screen.update()
    ball.move()

    # collision with top and bottom walls
    if ball.ycor() > 330 or ball.ycor() < -330:
        ball.bounce()
    # collision with either paddle
    elif (ball.distance(paddleone) < 50 and ball.xcor() > 600) or (ball.distance(paddletwo) < 50 and ball.xcor() < -600):
        ball.bouncegame()
    # collision with right wall
    elif ball.xcor() > 640:
        ball.reset()
        scoreL.score_update()
    # collision with left wall
    elif ball.xcor() < -640:
        ball.reset()
        scoreR.score_update()
screen.exitonclick()
