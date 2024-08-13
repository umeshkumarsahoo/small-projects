from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time
new_screen=Screen()
new_screen.bgcolor("black")
new_screen.title("pong game ~by umesh")
new_screen.setup(width=800,height=600)
new_screen.tracer(0)
#moving
r_pad=Paddle((350,0))
l_pad=Paddle((-350,0))
#screen setup
new_screen.listen()
new_screen.onkey(r_pad.go_up,"Up")
new_screen.onkey(r_pad.go_down,"Down")
new_screen.onkey(l_pad.go_up,"w")
new_screen.onkey(l_pad.go_down,"s")
#ball setup
ball=Ball()
#score setup
board=Score()
is_on=True
x=0.1
while is_on:
    time.sleep(x)
    new_screen.update()
    ball.move()
    #collision on paddle
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.bounce_y()
    #collision with paddle
    if ball.distance(r_pad) < 50 and ball.xcor() > 320:
        ball.bounce_x()
        x*=0.6

    if ball.distance(l_pad) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        x*=0.6
    #paddle misses the ball
    if ball.xcor()>380:
        ball.reset_pos()
        board.l_inc()
        x=0.1

    if ball.xcor()< -380:
        ball.reset_pos()
        board.r_inc()
        x=0.1


















new_screen.exitonclick()
