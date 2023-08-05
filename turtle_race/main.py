from turtle import Turtle, Screen
import random

tim = Turtle(shape="turtle")
tom = Turtle(shape="turtle")
john = Turtle(shape="turtle")
tam = Turtle(shape="turtle")
nni = Turtle(shape="turtle")
han = Turtle(shape="turtle")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtle_list = [tim,tom, john, tam, nni, han]
is_game = False
for i in range(6):
    for j in range(6):
        if i == j:
            turtle_list[j].color(colors[i])
screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="make your bet", prompt="which turtle will win?: ")
if user_bet:
    is_game = True
tim.penup()
tim.goto(x=-230, y=150)
tom.penup()
tom.goto(x=-230, y=100)
john.penup()
john.goto(x=-230, y=50)
tam.penup()
tam.goto(x=-230, y=0)
nni.penup()
nni.goto(x=-230, y=-50)
han.penup()
han.goto(x=-230, y=-100)
while is_game:

    for turtlex in turtle_list:
        if turtlex.xcor() > 230:
            win_colour = turtlex.pencolor()
            is_game = False
            if win_colour == user_bet:
                print("you win")
            else:
                print("you loose")
        move = random.randint(0, 10)
        turtlex.forward(move)










screen.exitonclick()