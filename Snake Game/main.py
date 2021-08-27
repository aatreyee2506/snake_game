from  turtle import Screen,Turtle
from snake import Snake
import time
from food import Food
from score import Score

screen=Screen()

screen.setup(width=600,height=600)
screen.title('Snake Game')
screen.bgcolor('black')
screen.tracer(0)

snake=Snake()
food=Food()
score=Score()

screen.listen()
screen.onkey(fun=snake.up,key="Up")
screen.onkey(fun=snake.down,key="Down")
screen.onkey(fun=snake.left,key="Left")
screen.onkey(fun=snake.right,key="Right")

game=True   
while game:
    screen.update()
    time.sleep(0.1)  
    snake.move()
    
    if snake.new[0].distance(food)<15:
        food.refresh()
        snake.extend()
        score.inc_score()
        

    if snake.new[0].xcor()>290 or snake.new[0].xcor()< -290 or snake.new[0].ycor() >290 or snake.new[0].ycor() < -290:
        score.reset()
        snake.reset()


for segment in snake.new[1:]:
   
    if snake.new[0].distance(segment)<10:
        score.reset()
        snake.reset()        


screen.exitonclick()