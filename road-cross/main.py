from turtle import Screen
from player import Player
from cars import Cars
from score import Score
import time

new_screen=Screen()
new_screen.title("my road crossing game - umesh")
new_screen.setup(width=600,height=600)
new_screen.bgcolor("grey")
new_screen.tracer(0)
player=Player()
car=Cars()
score=Score()

new_screen.listen()
new_screen.onkey(player.go_up,"Up")

is_on=True
while is_on:
    time.sleep(0.04)
    new_screen.update()
    car.create_cars()
    car.move()

    for i in car.all_cars:
        if i.distance(player)<25:
            score.over()
            is_on=False
    #successful cross
    if player.at_finish():
        player.goto_start()
        car.lvl_up()
        score.update_board()


new_screen.exitonclick()
