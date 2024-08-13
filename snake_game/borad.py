from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        self.penup()
        self.goto(0,270)
        self.color("black")
        self.write(f"score😎:{self.score}",align="center",font=("poppins",24,"bold"))
        self.hideturtle()
        self.update()

    def update(self):
        self.write(f"score😎:{self.score}",align="center",font=("poppins",24,"bold"))

    def increase(self):
        self.score+=1
        self.clear()
        self.write(f"score😎:{self.score}",align="center",font=("poppins",24,"bold"))

    def over(self):
        self.goto(0,0)
        self.write("Game is over lol🤣",align="center",font=("poppins",50,"bold"))
