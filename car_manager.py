from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class Carmanager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
    def create_cars(self):
        random_chance = random.randint(1,6)
        if random_chance ==1:
            new_Car = Turtle("square")
            new_Car.shapesize(stretch_len=2,stretch_wid=1)
            new_Car.penup()
            new_Car.color(random.choice(COLORS))
            random_y = random.randint(-250,250)
            new_Car.goto(300,random_y)
            self.all_cars.append(new_Car)
    def move_car(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def level (self):
        self.car_speed += MOVE_INCREMENT