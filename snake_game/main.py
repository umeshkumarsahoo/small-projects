import turtle
import time
import snake
from food import Food
from borad import Score
#screen set up
new_screen=turtle.Screen()
new_screen.bgcolor("white")
new_screen.title("snake game ~by umesh")
new_screen.tracer(0)
new_screen.setup(width=600,height=600)
shh=snake.Snake()
food=Food()
score=Score()
#moving
new_screen.listen()
new_screen.onkey(shh.up, "Up")
new_screen.onkey(shh.down, "Down")
new_screen.onkey(shh.left, "Left")
new_screen.onkey(shh.right, "Right")

is_on=True
while is_on:
    new_screen.update()
    shh.snake_move()
    time.sleep(0.1)

    #contact of food with snake
    if shh.head.distance(food)<17:
        food.refresh()
        shh.extent()
        score.increase()
    #contact with wall
    if shh.head.xcor()>295 or shh.head.ycor()< -295 or shh.head.ycor()>295 or shh.head.xcor()< -295:
        is_on=False
        score.over()
    #detect collision with tail
    for segment in shh.segments[1:]:
        if shh.head.distance(segment)<10:
            is_on=False
            score.over()
new_screen.exitonclick()
