from turtle import Turtle
from constants import *

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.customize()
        self.score = 0
        with open("high_score.txt") as file:
            self.high_Score = int(file.read())

        self.update()
    def customize(self):
        self.penup()
        self.hideturtle()
        self.setposition((0, HEIGHT // 2 - 45))
        self.color("blue")

    def update(self):
        self.clear()
        self.setposition((0, HEIGHT // 2 - 45))
        self.write(f"Score - {self.score}", True, align="center", font=('Arial', 16, 'bold'))

    def game_over(self):
        self.clear()
        self.setposition((-30,0))
        self.color("red")
        if self.high_Score < self.score:
            self.high_Score = self.score
            self.update_file()
        self.write(f"Your Score {self.score} \n High score {self.high_Score}", True, align="center", font=('Arial', 20, 'bold'))

    def update_file(self):
        with open("high_score.txt", mode = "w") as file:
            file.write(str(self.high_Score))
    # def __del__(self):
    #     self.file.close()


if __name__ == "__main__":
    sc = ScoreBoard()
