# create the snake
# one idea is to draw
# Bugs

# code Improv
## Inheritance
## use of distance
## write constants outsde
## food in wrong position
##


from turtle import Screen,Turtle
import time
from snake import Snake
from food import Food
from brain import Brain
from screen import SnakeScreen
from score_board import ScoreBoard

snake_Screen = SnakeScreen()
screen = snake_Screen.screen

snake = Snake(screen)
food = Food(screen)
snake_Screen.draw_box()
snake_Screen.axis()

screen.update()
brain = Brain(snake, food, screen)
score_b = ScoreBoard()

screen.listen()
snake.key_controls()
food.rd_pos()

while 1:
    time.sleep(0.1)
    snake.move_snake()
    if brain.is_collision_food():
        snake.add_seg(snake.last_seg_pos)
        food.rd_pos()
        score_b.score += 1
        score_b.update()
    if brain.is_collision_wall() or brain.is_collision_tail():
        score_b.game_over()
        break
    screen.update()
screen.exitonclick()

# move the Snake
# control the
# create food
# create scoreboard
# collision with food

# collision with tail
# collision with wall
