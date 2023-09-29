from turtle import Turtle

ALINGNMENT = "center"
FONT = ('courier', 24, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        f = open("data.txt", "r").read()
        self.high_score = f
        self.penup()
        self.goto(x=0, y=270)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}, High Score: {self.high_score}", align=ALINGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALINGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        if int(self.high_score) < self.score:
            self.high_score = self.score
            f = open("data.txt", "w")
            f.write(str(self.high_score))
        self.clear()
        self.update_scoreboard()
