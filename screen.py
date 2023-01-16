from turtle import Screen, Turtle


class SnakeScreen:
    def __init__(self):
        self.screen = Screen()
        self.customize()
        self.x = self.screen.window_width() - 20
        self.y = self.screen.window_height() - 20

    def customize(self):
        self.screen.tracer(0)
        self.screen.setup(width=620, height=420)

    def draw_box(self):
        box = Turtle()
        box.shape("turtle")
        box.hideturtle()
        box.penup()
        box.pensize(10)
        box.setposition((-self.x // 2 + 5, -self.y // 2 + 5))
        box.pendown()
        box.forward(self.x - 10)
        box.setheading(90)
        box.forward(self.y - 10)
        box.setheading(180)
        box.forward(self.x - 10)
        box.setheading(270)
        box.forward(self.y - 10)

    def axis(self, color="grey"):
        axis = Turtle()
        axis.shape("turtle")
        axis.hideturtle()
        axis.penup()
        axis.color(color)
        axis.pensize(1)
        axis.setposition((-self.x // 2 + 10, -self.y // 2 + 10))

        for i in range(20):
            axis.setheading(0)
            axis.pendown()
            axis.forward(self.x - 20)
            axis.penup()
            axis.setheading(90)
            axis.forward(20)
            axis.setheading(180)
            axis.forward(self.x - 20)
        axis.setposition((-self.x // 2 + 10, -self.y // 2 + 10))

        for i in range(30):
            axis.setheading(90)
            axis.pendown()
            axis.forward(self.y - 20)
            axis.penup()
            axis.setheading(0)
            axis.forward(20)
            axis.setheading(270)
            axis.forward(self.y - 20)

    def show_score(self, turtle, score):
        turtle.penup()
        turtle.hideturtle()
        turtle.setposition((0, self.y // 2 - 35))
        turtle.color("blue")
        turtle.write(f"Score - {score}", True, align="center", font=('Arial', 16, 'bold'))

    def show_game_over(self):
        turtle=Turtle()
        turtle.penup()
        turtle.hideturtle()
        turtle.setposition((-30,0))
        turtle.color("red")
        turtle.write(f"Game Over", True, align="center", font=('Arial', 20, 'bold'))
if __name__ == "__main__":
    scr = SnakeScreen()
    scr.draw_box()
    scr.axis()
    sc_tr = Turtle()
    scr.show_score(sc_tr, 3)
    sc_tr.clear()
    scr.show_score(sc_tr, 5)

    scr.screen.update()
    scr.screen.exitonclick()
