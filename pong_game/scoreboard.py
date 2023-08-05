from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.update_scareboard()


    def update_scareboard(self):
        self.clear()
        self.goto(x=-100, y= 280)
        self.write(arg= self.l_score, align="center", font=("arial", 12, "normal"))
        self.goto(x=100, y=280)
        self.write(arg=self.r_score, align="center", font=("arial", 12, "normal"))


    def add_left(self):
        self.l_score += 1
        self.update_scareboard()

    def add_right(self):
        self.r_score += 1
        self.update_scareboard()



    def game_over(self):
        self.clear()
        self.write(arg=f"GAME OVER, SCORE: {self.score - 1}", align="center", font=("arial", 12, "normal"))
