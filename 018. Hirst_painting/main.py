import turtle as t
import random
tim=t.Turtle()

screen=t.Screen()
screen.screensize(canvwidth=300, canvheight=300) 
t.colormode(255)
hirst_color=[(245, 243, 238), (246, 242, 244), (202, 164, 110), (240, 245, 241),
             (236, 239, 243), (149, 75, 50), (222, 201, 136), (53, 93, 123),
             (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73),
             (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
             (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77),
             (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19),
             (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

tim.penup()
tim.hideturtle()
x=-220
y=-220
tim.setposition(x,y)

number_dot=100
for dot_count in range(1,number_dot+1):

    tim.dot(20,random.choice(hirst_color))
    tim.forward(50)
    if dot_count%10==0:
        y+=50
        tim.setposition(-220,y)

screen.exitonclick()
