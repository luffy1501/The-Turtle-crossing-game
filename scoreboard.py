from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()


    def score(self):
        self.color("white")
        self.level = 0
        self.hideturtle()
        self.penup()
        self.goto(-230, 250)
        self.move_speed = 0.1
        self.update_score()


    def update_score(self):
        self.clear()
        self.level += 1
        self.move_speed *= 0.9
        self.write(f"Level:{self.level}", align="center", font=FONT)

    def end(self):
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 0)
        self.write("You Won", align="center", font=FONT)
