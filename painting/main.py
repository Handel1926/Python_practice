import colorgram
from turtle import Turtle, Screen

# colors = colorgram.extract('image.jpg', 30)
# rgb_colors = []
#
# for color in colors:
#     r = color.rgb.r
#     b = color.rgb.b
#     g = color.rgb.g
#     new_color = (r, b, g)
#     rgb_colors.append(new_color)

tim = Turtle()
tim.pensize(5)
color_list = [(195, 120, 165), (140, 59, 81), (218, 143, 201), (66, 121, 98), (142, 181, 164), (156, 60, 150), (130, 24, 35), (74, 28, 36), (55, 89, 114), (187, 83, 96), (144, 153, 176), (24, 70, 89), (33, 72, 56), (164, 154, 142), (106, 82, 78), (223, 169, 179), (21, 56, 66), (124, 30, 27), (68, 39, 36), (180, 176, 204), (88, 132, 146), (165, 105, 100), (47, 83, 64), (215, 181, 176), (43, 79, 71), (75, 49, 63)]
for i in color_list:
    tim.color(i)
    tim.forward(1)
    tim.penup()
    tim.forward(1)


screen = Screen()
screen.exitonclick()
