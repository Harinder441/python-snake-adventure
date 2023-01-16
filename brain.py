class Brain:
    def __init__(self, snake, food, screen):
        self.snake = snake
        self.food = food
        self.scr = screen
        self.y = screen.window_height() - 20
        self.x = screen.window_width() - 20
        self.score = 0

    def is_collision_food(self):
        cond1 = abs(self.snake.segments[0].pos()[0] - self.food.pos[0]) < 0.1
        cond2 = abs(self.snake.segments[0].pos()[1] - self.food.pos[1]) < 0.1
        if cond2 and cond1:
            self.update_score()
            return 1
        else:
            return 0

    def is_collision_wall(self):
        x0 = self.snake.segments[0].pos()[0]
        y0 = self.snake.segments[0].pos()[1]
        if abs(x0 - self.x // 2) < 15 or abs(x0 + self.x // 2) < 15:

            return 'x'
        elif abs(y0 - self.y // 2) < 15 or abs(y0 + self.y // 2) < 15:

            return 'y'
        else:
            return 0

    def is_collision_tail(self):
        for i in range(1, len(self.snake.segments)):
            if self.snake.segments[0].distance(self.snake.segments[i]) < 2:
                return 1
        else:
            return 0

    def update_score(self):
        self.score += 1
