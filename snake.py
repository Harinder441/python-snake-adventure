from turtle import Turtle


class Snake:

    def __init__(self, screen):
        self.segments = []
        for i in range(3):
            self.add_seg((-20 * i, 0))
        self.last_seg_pos = (-20 * 2, 0)
        self.scr = screen

    @staticmethod
    def my_turtle(turtle):
        turtle.shape("square")
        turtle.speed(10)
        turtle.penup()

    def add_seg(self, pos):
        snake_seg = Turtle()
        self.my_turtle(snake_seg)
        snake_seg.setposition(pos)
        self.segments.append(snake_seg)

    def move_snake(self):
        # print(self.segments[0].pos())
        self.last_seg_pos = self.segments[-1].pos()
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(self.segments[i - 1].pos())
        self.scr.update()
        self.segments[0].forward(20)
        return self.last_seg_pos

    def move_left(self):
        if self.segments[0].heading() == 90:
            self.segments[0].left(90)
        elif self.segments[0].heading() == 270:
            self.segments[0].right(90)

    def move_right(self):
        if self.segments[0].heading() == 270:
            self.segments[0].left(90)
        elif self.segments[0].heading() == 90:
            self.segments[0].right(90)

    def move_up(self):
        if self.segments[0].heading() == 0:
            self.segments[0].left(90)
        elif self.segments[0].heading() == 180:
            self.segments[0].right(90)

    def move_down(self):
        if self.segments[0].heading() == 180:
            self.segments[0].left(90)
        elif self.segments[0].heading() == 0:
            self.segments[0].right(90)

    def key_controls(self):
        self.scr.onkey(self.move_right, "Right")
        self.scr.onkey(self.move_left, "Left")
        self.scr.onkey(self.move_up, "Up")
        self.scr.onkey(self.move_down, "Down")

    def translate(self, axis):
        x0 = self.segments[0].pos()[0]
        y0 = self.segments[0].pos()[1]
        if axis == 'x':
            self.segments[0].setposition((-x0, y0))
        elif axis == 'y':
            self.segments[0].setposition((x0, -y0))


if __name__ == "__main__":
    pass
