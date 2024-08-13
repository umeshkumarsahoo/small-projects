from turtle import Turtle
Font=("courier",24,"bold")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.level=1
        self.hideturtle()
        self.penup()
        self.goto(-280,250)
        self.write(f"level:{self.level}",align="left",font=Font)
    def update_board(self):
        self.clear()
        self.update()
        self.write(f"level:{self.level}",align="left",font=Font)

    def  update(self):
        self.level+=1
    def over(self):
        self.goto(0,0)
        self.color("white")
        self.write("🤣Game over!!",align="center",font=("Arial",30,"bold"))
