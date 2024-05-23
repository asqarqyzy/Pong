from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.tracer(0)
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Arcade Game")

r_paddle = Paddle((375, 0))
screen.listen()
screen.onkeypress(fun=r_paddle.move_down, key="Down")
screen.onkeypress(fun=r_paddle.move_up, key="Up")

l_paddle = Paddle((-375, 0))
screen.onkeypress(fun=l_paddle.move_down, key="s")
screen.onkeypress(fun=l_paddle.move_up, key="w")

ball = Ball()
scoreboard = Scoreboard()


game_is_on = True
while game_is_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if (ball.distance(r_paddle) <= 50 and ball.xcor() > 355) or (ball.distance(l_paddle) <= 50 and ball.xcor() < -355):
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.restart()
        ball.bounce_x()
        scoreboard.add_l_score()
    if ball.xcor() < -380:
        ball.restart()
        ball.bounce_x()
        scoreboard.add_r_score()
screen.exitonclick()
