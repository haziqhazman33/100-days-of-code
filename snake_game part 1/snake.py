from turtle import Screen,Turtle 
import time
screen=Screen()

screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title("snake_game v2")
screen.tracer(0)
start_pos=[(0,0),(-20,0),(-40,0)]
segments=[]
for pos in start_pos:
    new_seg=Turtle(shape='square')
    new_seg.color('white')
    new_seg.penup()
    new_seg.goto(pos)
    segments.append(new_seg)
print(len(segments))
game_on=True
while game_on:

    screen.update() #snake move forward as an entire piece
    time.sleep(1) #snake move bit faster and cut amount time even faster
    # for seg in segments:
    #     seg.forward(20)
    #     #screen.update() #moves piece by piece
    #     #time.sleep(1)  # instead of getting it 
    
    #loop through each segment from last seg to first seg
    
    for seg_num in range(len(segments)-1,0,-1):
        new_x=segments[seg_num-1].xcor()
        new_y=segments[seg_num-1].ycor()
        segments[seg_num].goto(new_x,new_y)
        
    segments[0].forward(20)
    # segments[0].left(90)
screen.exitonclick()
