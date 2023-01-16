from turtle import Turtle
import random as rd


class Food:
    def __init__(self, screen):
        self.scr = screen
        self.y = screen.window_height()-20
        self.x = screen.window_width()-20
        self.food = Turtle()
        self.customize_food()
        self.pos = self.food.pos()

    def customize_food(self):
        self.food.shape("circle")
        self.food.penup()

    def rd_pos(self):
        x0 = rd.choice(list(range(-self.x // 2+20, self.x // 2 - 20, 20)))
        y0 = rd.choice(list(range(-self.y // 2+20, self.y // 2 - 20, 20)))
        self.food.setposition((x0, y0))
        self.pos = self.food.pos()
