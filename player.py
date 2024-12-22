from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.finish_line_y = FINISH_LINE_Y
        self.shape("turtle")
        self.penup()
        self.start_moving()
        self.player_speed = 1

    def start_moving(self):
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_forward(self):
        if self.ycor() != FINISH_LINE_Y:
            self.forward(MOVE_DISTANCE)