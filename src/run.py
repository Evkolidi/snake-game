import random

import pygame

from src.constants import SIZE, FPS, RES, BACKGROUND_IMAGE
from src.snake import Snake
from src.apple import Apple
from src.score import Score


def close_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

def main():
    pygame.init()
    surface = pygame.display.set_mode([RES, RES])
    clock = pygame.time.Clock()
    font_score = pygame.font.SysFont('Arial', 26, bold=True)
    font_end = pygame.font.SysFont('Arial', 66, bold=True)

    snake = Snake()
    apple = Apple()
    score = Score()

    bg_image = pygame.image.load(BACKGROUND_IMAGE).convert()

    while True:
        surface.blit(bg_image, (0, 0))

        # drawing snake, apple
        [pygame.draw.rect(surface, pygame.Color(snake.color), (i, j, SIZE, SIZE)) for i, j in (snake.get_all_positions())]
        pygame.draw.rect(surface, pygame.Color(apple.color), (*(apple.get_position()), SIZE, SIZE))

        # show score
        render_score = font_score.render(f'SCORE: {score.get_score()}', 1, pygame.Color(score.color))
        surface.blit(render_score, (5, 5))

        snake.update_position()
        score.update_score()

        if snake.get_head_position() == apple.get_position():
            apple.replace()
            snake.grow()
            score.apple_eaten()

        snake.die_check()

        if not snake.alive():
            while True:
                render_end = font_end.render('GAME OVER', 1, pygame.Color(score.color))
                surface.blit(render_end, (RES // 2 - 200, RES // 3))
                pygame.display.flip()
                close_game()


        pygame.display.flip()
        clock.tick(FPS)
        close_game()

        snake.change_direction()
