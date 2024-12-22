import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

FONT = ("Courier", 24, "normal")

#screen building
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

#player building
timmy = Player()

#car building
car = CarManager()

#initializing scoreboard
score = Scoreboard()

#game over initializing
game_ending = Turtle()
game_ending.hideturtle()

screen.listen()
screen.onkey(key="Up", fun=timmy.move_forward)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.manage_cars()

    if timmy.ycor() == timmy.finish_line_y:
        timmy.start_moving()
        score.level_up()
        car.speed_up()

    for random_car in car.all_cars:
        if timmy.distance(random_car) < 15:
            game_is_on= False
            game_ending.write(arg="Game over", align="center", font=FONT)

screen.exitonclick()