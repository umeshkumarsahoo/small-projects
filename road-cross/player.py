from turtle import Turtle
start_pos=(0,-280)
move_distance=10
finish_line_y=280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.goto_start()
        self.setheading(90)

    def goto_start(self):
        self.goto(start_pos)

    def go_up(self):
        self.forward(move_distance)

    def at_finish(self):
        if self.ycor()>finish_line_y:
            return True
