import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("my snake game")
screen.tracer(0)

tim = Snake()
food = Food()
score = Scoreboard()


screen.listen()
screen.onkey(tim.up, "Up")
screen.onkey(tim.down, "Down")
screen.onkey(tim.left, "Left")
screen.onkey(tim.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    tim.move()

    # detect collision with food
    if tim.head.distance(food) < 15:
        food.refresh()
        score.add()
        tim.add_segment()
    # detect collision with wall
    if tim.head.xcor() > 280 or tim.head.xcor() < -280 or tim.head.ycor() > 280 or tim.head.ycor() < -280:
        score.reset_scoreboard()
        tim.reset()
    # detect collision with snake segment
    for segment in tim.segments[1:len(tim.segments) - 1]:
        if tim.head.distance(segment) < 10:
            score.reset_scoreboard()
            tim.reset()









screen.exitonclick()