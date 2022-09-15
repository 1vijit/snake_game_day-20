import random
from turtle import Turtle


class Food(Turtle) :
    def __init__(self) :
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        x_pos = random.randint(-260,260)
        y_pos = random.randint(-260, 260)
        self.goto(x_pos, y_pos)

    def refresh(self):
        x_pos = random.randint(-260,260)
        y_pos = random.randint(-260, 260)
        self.goto(x_pos, y_pos)
