from turtle import Turtle

FONT = ("Courier", 14, "normal")
GAME_OVER_FONT = ("Courier", 25, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-255, 275)
        self.scoreT = f"Score:{self.score}"
        self.write(self.scoreT, align="center", font=FONT)

    def score_point(self):
        self.score += 1
        self.update()

    def game_over(self):
        self.goto(0, 0)
        self.color("red")
        self.write(f"GAME OVER YOUR SCORE IS {self.score}", align="center", font=GAME_OVER_FONT)
