from turtle import Turtle,Screen
new_screen=Screen()
Starting_pos=[(0,0),(-20,0),(-40,0)]
move_distance=20
Up=90
Down=270
Right=0
Left=180
class Snake:
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]



    def create_snake(self):
        for position in Starting_pos:
            self.add_segments(position)

    def add_segments(self,position):
            segment=Turtle()
            segment.shape("square")
            segment.shapesize(stretch_len=1.0,stretch_wid=1.0)
            segment.color("black")
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)

    def extent(self):
        self.add_segments(self.segments[-1].position())

    def snake_move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x=self.segments[seg_num-1].xcor()
            new_y=self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(move_distance)

    def up(self):
        if self.head.heading()!=Down:
            self.head.setheading(Up)

    def down(self):
        if self.head.heading()!=Up:
            self.head.setheading(Down)

    def left(self):
        if self.head.heading()!=Right:
            self.head.setheading(Left)

    def right(self):
        if self.head.heading()!=Left:
            self.head.setheading(Right)
