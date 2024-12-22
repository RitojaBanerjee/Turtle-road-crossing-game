from turtle import Turtle
FONT = ("Courier", 12, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.show_score()

    def show_score(self):
        self.goto(-270,270)
        self.write(arg=f"Level : {self.level}", font=FONT)

    def level_up(self):
        self.level += 1
        self.clear()
        self.show_score()