from turtle import Turtle
MOVE_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.pad = Turtle(shape="square")
        self.pad.color("white")
        self.pad.penup()
        self.pad.shapesize(stretch_wid=5, stretch_len=1)
        self.pad.goto(position)


    def move_up(self):
        new_y = self.pad.ycor() + 20
        self.pad.goto(self.pad.xcor(), new_y)



    def move_down(self):
        new_y = self.pad.ycor() - 20
        self.pad.goto(self.pad.xcor(), new_y)

