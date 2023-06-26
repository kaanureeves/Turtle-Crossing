import time
from turtle import Screen
from player import Player
from scoreboard import Scoreboard
from car_manager import Car

screen = Screen()
screen.bgcolor("white")
screen.setup(600, 600)
screen.title("TURTLE CROSSING")
screen.tracer(0)

player1=Player()
player1.create_player()

scoreboard=Scoreboard()

cars=Car()

screen.listen()
screen.onkey(player1.move, "w")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move()

    for car in cars.all_cars:
        if car.distance(player1)<20:
            game_is_on=False
            scoreboard.game_over()

    if player1.is_finished():
        player1.go_default_pos()
        cars.lvl_up()
        scoreboard.score_point()





screen.exitonclick()
