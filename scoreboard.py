from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.goto(0,260)
        self.l_score = 0
        self.r_score = 0
        self.hideturtle()
        self.show_score()

    def show_score(self):
        self.write(f"{self.l_score} vs {self.r_score}", False, "center", ("Courier", 24, "bold"))

    def add_r_score(self):
        self.r_score += 1
        self.clear()
        self.show_score()

    def add_l_score(self):
        self.l_score += 1
        self.clear()
        self.show_score()