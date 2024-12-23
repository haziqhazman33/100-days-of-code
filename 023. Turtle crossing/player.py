STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.goto(0,-280)
        self.setheading(90)
        self.move_distance=MOVE_DISTANCE
    
    def moveup(self):
        self.forward(self.move_distance)

    def reset_position(self):
        self.goto(0,-280)
