import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen() #create a screen object 
screen.setup(width=600, height=600)
screen.tracer(0) #turn off the automatic update, you need to use screen.update 

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up,"Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1) #after the actions, the program will pause for 0.1 seconds
    screen.update()
    # during every refresh 
    car_manager.create_car()
    car_manager.move_cars()
    
    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False # end the loop 
            scoreboard.game_over()
    
    # Detect reach of the final
    if player.is_at_finish_line():
        player.go_to_start()#  go back to the start point
        car_manager.level_up()
        scoreboard.increase_level()
