
from turtle import Turtle, Screen
import random

timmy = Turtle()
turtle.colormode(255)
def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

timmy.shape("turtle")
timmy.width(1)
timmy.speed(0)
# for i in range(2):
#     timmy.forward(100)
#     timmy.right(90)
#     timmy.forward(100)
#     timmy.right(90)
lines = 3

# while lines < 11:
#     list_color = ["red", "yellow", "blue", "gold", "green", "black"]
#     colour = random.choice(list_color)
#     timmy.color(colour)
#     angle = 360 / lines
#     for i in range(lines):
#         timmy.forward(50)
#         timmy.right(angle)
#     lines += 1
# turn =[ 0, 90, 180, 270]
# for i in range(500):
#     timmy.color(random_colour())
#     timmy.forward(20)
#     timmy.setheading(random.choice(turn))
y = 0
x = 0
def draw(size):
    for i in range(int(360 / size)):
        timmy.circle(50)
        timmy.right(size)
        timmy.color(random_colour())
draw(5)


    # timmy.tilt(1)






screen = Screen()
screen.exitonclick()