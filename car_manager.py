import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE  # Initialize car speed
        self.counter = 0

    def create_car(self):
        new_car = Turtle("square")
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.color(random.choice(COLORS))
        new_car.penup()
        # Randomize the y position within a reasonable range
        new_car.goto(x=280, y=random.randint(-230, 230))
        self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            car.setheading(180)  # Move leftward
            car.forward(self.car_speed)

    def manage_cars(self):
        self.counter += 1
        # Create a new car every 6 frames
        if self.counter % 6 == 0:
            self.create_car()
        self.move_car()

    def speed_up(self):
        # Increment car speed
        self.car_speed += MOVE_INCREMENT
