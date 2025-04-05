from game.vector import Vector
from random import randint
from config.constants import PLAYABLE_AREA_HEIGHT, PLAYABLE_AREA_WIDTH, APPLE_SIZE
import pygame


class Apple:
    def __init__(self):
        x_pos = randint(0, (PLAYABLE_AREA_WIDTH - 1) // APPLE_SIZE) * APPLE_SIZE
        y_pos = randint(0, (PLAYABLE_AREA_HEIGHT - 1) // APPLE_SIZE) * APPLE_SIZE
        self.pos = Vector(x_pos, y_pos)

    def show(self):
        pygame.draw.rect(
            DISPLAY,
            pygame.Color("Red"),
            (self.pos.x, self.pos.y, APPLE_SIZE, APPLE_SIZE),
        )
        pygame.display.update(self.pos.x, self.pos.y, APPLE_SIZE, APPLE_SIZE)
