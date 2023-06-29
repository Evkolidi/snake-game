import random

from src.constants import SIZE, FPS, RES

def get_random_coordinate():
    return random.randrange(SIZE, RES - SIZE, SIZE)


class Apple:
    apple = get_random_coordinate(), get_random_coordinate()
    color = 'red'

    def get_position(self):
        return self.apple

    def replace(self):
        self.apple = get_random_coordinate(), get_random_coordinate()
