from turtle import Turtle,Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time
screen=Screen()
WIDTH=600
HEIGH=600
screen.setup(width=WIDTH,height=HEIGH)
screen.bgcolor('black')
screen.title("Snake Game v1")
screen.tracer(0)
# Constants
def draw_border():
    """Draws a border/frame for the game."""
    border = Turtle()
    border.pencolor("green")
    border.pensize(width=5)
    border.hideturtle()
    # border.speed("fastest")
    border.penup()
    border.goto(-300,300)  # Start top-left corner
    border.pendown()
    for _ in range(4):
        border.forward(300*2)
        border.right(90)

border=draw_border()
snake=Snake()
food=Food()
scoreboard=Scoreboard()
game_on=True
snake.create_snake()

screen.listen()
screen.onkey(snake.up,'w')
screen.onkey(snake.down,'s')
screen.onkey(snake.left,'a')
screen.onkey(snake.right,'d')
while game_on:
    screen.update() #require tracer
    time.sleep(0.1)
    snake.move()
    scoreboard.updatescoreboard()
  
    if snake.head.distance(food)<15:
        food.refresh()
        snake.grow()
        scoreboard.increase_score()

    if snake.head.xcor()>280 or snake.head.xcor()< -280 or snake.head.ycor()>280 or snake.head.ycor()< -280:
        game_on= False
        scoreboard.game_over()

    for segment in snake.segments[2:]:
        if snake.head.distance(segment)<10:
            game_on=False
            scoreboard.game_over()

screen.exitonclick()
