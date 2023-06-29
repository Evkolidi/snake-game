import random

import pygame

from src.constants import SIZE, FPS, RES

def get_random_coordinate():
    return random.randrange(SIZE, RES - SIZE, SIZE)


class Snake:
    x = get_random_coordinate()
    y = get_random_coordinate()
    snake = [(x, y)]
    length = 1
    dx = 0
    dy = 0
    allowed_directions = {'W', 'A', 'S', 'D'}
    color = 'green'
    total_frames = 0
    frames_to_move = 10
    is_alive = True

    def update_position(self):
        self.total_frames += 1
        if not self.total_frames % self.frames_to_move:
            self.x += self.dx * SIZE
            self.y += self.dy * SIZE
            self.snake.append((self.x, self.y))
            self.snake = self.snake[-self.length:]

    def change_direction(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_w] or key[pygame.K_UP] and 'W' in self.allowed_directions:
            self.dx, self.dy = 0, -1
            self.allowed_directions = {'A', 'D'}
        elif key[pygame.K_a] or key[pygame.K_LEFT] and 'A' in self.allowed_directions:
            self.dx, self.dy = -1, 0
            self.allowed_directions = {'W', 'S'}
        elif key[pygame.K_s] or key[pygame.K_DOWN] and 'S' in self.allowed_directions:
            self.dx, self.dy = 0, 1
            self.allowed_directions = {'A', 'D'}
        elif key[pygame.K_d] or key[pygame.K_RIGHT] and 'D' in self.allowed_directions:
            self.dx, self.dy = 1, 0
            self.allowed_directions = {'W', 'S'}

    def die_check(self):
        if (min(self.x, self.y) < 0 or max(self.x, self.y) > RES - SIZE or 
                len(self.snake) != len(set(self.snake))):
            self.is_alive = False
            self.dx = 0
            self.dy = 0

    def alive(self):
        return self.is_alive

    def get_head_position(self):
        return self.snake[-1]

    def get_all_positions(self):
        return self.snake

    def grow(self):
        self.length += 1
        self.frames_to_move = max(self.frames_to_move - 1, 4)
