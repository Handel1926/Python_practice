from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.color("red")
        self.goto(x=0, y= 280)
        self.hideturtle()
        self.update_scoreboard()

    def add(self):
        self.score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"score {self.score} HIGH_SCORE {self.high_score}", align="center", font=("arial", 12, "normal"))

    def reset_scoreboard(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
        with open("data.txt", "w") as data:
            data.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def game_over(self):
        self.clear()
        self.write(arg=f"GAME OVER, SCORE: {self.score - 1}", align="center", font=("arial", 12, "normal"))



