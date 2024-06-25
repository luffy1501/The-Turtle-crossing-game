import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("THE TURTLE CROSSING GAME")
screen.tracer(0)
player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()
car_manager.create_cars()
scoreboard.score()
screen.listen()
screen.onkey(player.move_up, "w")
screen.onkey(player.move_down, "s")
screen.onkey(player.move_right(), "d")
screen.onkey(player.move_left(), "a")


game_is_on = True
while game_is_on:
    time.sleep(scoreboard.move_speed)
    car_manager.create_cars()
    car_manager.move()

    for cars in car_manager.all_cars:
        if player.distance(cars) < 20:
            game_is_on = False

    if player.ycor() > 280:
        player.finish()
        scoreboard.update_score()



    screen.update()
screen.exitonclick()
