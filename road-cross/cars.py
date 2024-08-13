from turtle import Turtle,Screen
import random
colors=["dark green","violet","blue","red","orange","green","cyan","yellow"]
move_dist=5
move_inc=10
border_color="black"
class Cars():
    def __init__(self):
        self.all_cars=[]
        self.speed=move_dist
    def create_cars(self):
        no=random.randint(1,9)
        if no==3:
            new_car=Turtle("square")
            new_car.shapesize(stretch_len=2,stretch_wid=1)
            new_car.penup()
            new_car.color(random.choice(colors))
            new_car.pencolor(border_color)  
            new_car.pensize(3)
            random_y=random.randint(-250,250)
            new_car.goto(300,random_y)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(move_dist)
    def lvl_up(self):
        self.speed += move_inc
