from turtle import*
import time
from carmanager import CarManager
from player import Player
from scoreboard import ScoreBoard

player = Player()
car_manager = CarManager()
screen = Screen()
screen.setup(width=600, height=600)

screen.tracer(0)

scoreboard = ScoreBoard()

screen.listen()
screen.onkey(player.go_up, "space ")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level() 
screen.exitonclick()
