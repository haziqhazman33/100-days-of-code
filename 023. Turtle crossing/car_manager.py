COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

from random import choice,randint
from turtle import Turtle

class CarManager:
    def __init__(self):

        self.all_car=[]
        self.create_car()
        self.car_speed=STARTING_MOVE_DISTANCE
    def create_car(self):
        chance=randint(1,6)
        if chance==1:
            new_car=Turtle()
            new_car.shape('square')
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.penup()
            new_car.color(choice(COLORS))
            new_car.setpos(300,randint(-250,250))
            self.all_car.append(new_car)
    
    def move_car(self):
        for car in self.all_car:
            car.backward(self.car_speed)
        
    def level_up(self):
        self.car_speed+=MOVE_INCREMENT