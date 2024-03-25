from turtle import Turtle 
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()
        


    def refresh(self):
        random_location_of_food_x = random.randint(-280, 280)
        random_location_of_food_y = random.randint(-280, 280)
        self.goto(random_location_of_food_x, random_location_of_food_y)


