import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("ping_pong")
screen.tracer(0)

# turtle_line = Turtle()
# turtle_line.color("white")
# turtle_line.penup()
# turtle_line.goto(x=0, y=300)
# turtle_line.pendown()
# turtle_line.goto(x=0, y=-290)

score = Scoreboard()
r_player = Paddle((350, 0))
l_player = Paddle((-350, 0))
ball = Ball()
screen.listen()
screen.onkey(r_player.move_up, "Up")
screen.onkey(r_player.move_down, "Down")
screen.onkey(l_player.move_up, "w")
screen.onkey(l_player.move_down, "s")



game_on = True
while game_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < - 280:
        ball.bounce_y()
    if ball.distance(r_player) < 50 and ball.xcor() > 340 or ball.distance(l_player) < 50 and ball.xcor() > -340:
        ball.bounce_x()
    if ball.xcor() > 380:
        score.add_left()
        ball.reset_ball()
        ball.increase_speed()
    if ball.xcor() < - 360:
        score.add_right()
        ball.reset_ball()














screen.exitonclick()