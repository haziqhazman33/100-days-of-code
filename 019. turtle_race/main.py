from turtle import Turtle,Screen,TK
import random
screen=Screen()
screen.title("Turtle Race")
#trackRace
def track():
    sketch_road=Turtle()
    screen.setup(width=500,height=400)
    sketch_road.penup()
    sketch_road.setposition(-200,100)
    sketch_road.speed(0)
  
    for step in range(5):

        for _ in range(10):
            sketch_road.penup()
            sketch_road.forward(20)
            sketch_road.pendown()
            sketch_road.forward(20)
            sketch_road.penup()
            sketch_road.hideturtle()
        sketch_road.setposition(-200,100-(step+1)*40)

track()

#set turtles color and their position
y_start=80
colors=['red','yellow','green','blue']
turtle_list=[]
for index in range(0,4):
    new_turtle=Turtle(shape='turtle')
    new_turtle.color(colors[index])
    new_turtle.penup()
    new_turtle.goto(-230,y_start)
    y_start-=40
    turtle_list.append(new_turtle)

game_on=True
user_bet=screen.textinput(title='turtle guess?',prompt=f'{colors}')
while game_on:
    
    for racer in turtle_list:
        distance=random.randint(1,10)
        racer.forward(distance)
        if racer.xcor() >230:
            game_on=False
            winner=racer.color()[0]
            # print(winner)
            if winner == user_bet: 
                TK.messagebox.showinfo(title="Congratulations You did it!", message=f"{winner.capitalize()} is the winner")
            else:
                TK.messagebox.showinfo(title="Game Over", message=f"{winner.capitalize()} is the winner")

screen.exitonclick()
