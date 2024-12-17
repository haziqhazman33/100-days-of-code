
from turtle import Turtle,Screen
from snake import Snake
import time
screen=Screen()
screen.title('Snake Game')

screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title("snake_game v2")
screen.tracer(0) #

game_on=True
snake=Snake()

screen.listen()
screen.onkey(snake.up,"w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left,"a")
screen.onkey(snake.right,"d")

while game_on:
    screen.update() 
    time.sleep(0.1)
    snake.move()

screen.exitonclick()
