from turtle import Turtle
import random
shapes=["circle","square","triangle"]
colors=["red","green","blue","violet"]
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.color(random.choice(colors))
        self.penup()
        self.shape(random.choice(shapes))
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.speed("fastest")
        random_x=random.randint(-280,280)
        random_y=random.randint(-280,260)
        self.goto(random_x,random_y)

    def refresh(self):
            self.shapesize(stretch_len=0.5,stretch_wid=0.5)
            self.color(random.choice(colors))
            self.shape(random.choice(shapes))
            random_x=random.randint(-280,280)
            random_y=random.randint(-280,280)
            self.goto(random_x,random_y)
