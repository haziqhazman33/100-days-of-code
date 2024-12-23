import time
from turtle import Turtle,Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

def draw_road():
    """Draw dashed road lines in the background."""
    road = Turtle()
    road.hideturtle()
    road.penup()
    road.color("gray")
    road.speed("fastest")
    for y in range(-250, 300, 50):  # Draw dashed lines for multiple lanes
        road.goto(-300, y)
        road.setheading(0)
        for _ in range(30):  # Create horizontal dashed lines
            road.pendown()
            road.forward(20)
            road.penup()
            road.forward(20)

def startlabel():
    start=Turtle()
    start.hideturtle()
    start.penup()
    start.goto(-200,-280)
    start.write("start",align="center",font=("Courier", 24, "normal"))

def Endlabel():
    start=Turtle()
    start.hideturtle()
    start.penup()
    start.goto(200,260)
    start.write("Finish",align="center",font=("Courier", 24, "normal"))

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

#draw road
draw_road()
startlabel()
Endlabel()
player=Player()
cars=CarManager()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(player.moveup,'w')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    # Car is created
    cars.create_car()
    cars.move_car()

    #detect collision with car
    for car in cars.all_car:
        if car.distance(player) <20:
            game_is_on=False
            scoreboard.game_over()

    #detect if player has reach finish line
    if player.ycor()>280:
        player.reset_position()
        cars.level_up()
        scoreboard.increase_level()

    screen.update()

screen.exitonclick()
