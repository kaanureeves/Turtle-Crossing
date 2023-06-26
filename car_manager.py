import turtle
from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Car:
    def __init__(self):
        self.all_cars = []
        self.car_speed=STARTING_MOVE_DISTANCE

    def create_car(self):
        rand_ch = random.randint(1, 6)
        if rand_ch == 1:
            new_car = Turtle("square")
            new_car.shapesize(0.8, 2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            randy = random.randint(-200, 200)
            new_car.goto(300, randy)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def lvl_up(self):
        self.car_speed+=MOVE_INCREMENT
