from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor('orange')
screen.title("Pong game")
screen.tracer(0) #control animation, turnoffanimation=0
paddle=Turtle()
ball=Ball()
scoreboard=Scoreboard()
r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))

screen.listen() 
screen.onkey(fun=r_paddle.go_up,key='Up')
screen.onkey(fun=r_paddle.go_down,key='Down')
screen.onkey(fun=l_paddle.go_up,key='w')
screen.onkey(fun=l_paddle.go_down,key='s')
game_on=True
while game_on:
        time.sleep(0.1)
        screen.update()
        ball.move()        
        
        # detect collision with wall
        if ball.ycor()>280 or ball.ycor()<-280:
                ball.bounce_y()
        #detect collision with paddle        
        if ball.distance(r_paddle) <50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320:
                ball.bounce_x()
                ball.move_speed*=0.9
        
        #Detect R paddle misses        
        if ball.xcor()>350:
                ball.reset_position()
                scoreboard.l_point()
                
        #Detect l paddle misses
        if ball.xcor()<-350:
                ball.reset_position()
                scoreboard.r_point()
screen.exitonclick()
