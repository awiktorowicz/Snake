from turtle import Turtle, color

ALIGMENT = "center"
FONT = "Arial"
FONT_SIZE = 24
FONT_TYPE = "normal"
TEXT_COLOR = "white"
class Scoreboard(Turtle):


    def __init__(self):
        super().__init__()
        with open("high_score.txt") as data:
            self.high_score = data.read()
        self.score = 0
        self.color(TEXT_COLOR)
        self.penup()
        self.goto(0,260)
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGMENT, font=(FONT,FONT_SIZE,FONT_TYPE))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open("high_score.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0




