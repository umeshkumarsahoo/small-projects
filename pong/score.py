from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score=0
        self.r_score=0
        self.update()

    def update(self):
        self.clear()
        self.goto(-80,200)
        self.write(self.l_score,align="center",font=("poppins",50,"italic"))
        self.goto(80,200)
        self.write(self.r_score,align="center",font=("poppins",50,"italic"))

    def l_inc(self):
        self.l_score+=1
        self.update()
    def r_inc(self):
        self.r_score+=1
        self.update()
