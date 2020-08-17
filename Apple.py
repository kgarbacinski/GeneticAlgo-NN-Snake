from Vector import *
from random import randint
from constants import WINDOW_HEIGHT, WINDOW_WIDTH, PLAYABLE_AREA_HEIGHT, PLAYABLE_AREA_WIDTH
import pygame
from pygame import Rect
from main import DISPLAY


class Apple:
    def __init__(self):
        self.pos = Vector(randint(1, PLAYABLE_AREA_WIDTH - 10), randint(1, PLAYABLE_AREA_HEIGHT - 10))

    def show(self):
        pygame.draw.rect(DISPLAY, pygame.Color("Red"), (self.pos.x, self.pos.y, 10, 10))
        pygame.display.update(self.pos.x, self.pos.y, 10, 10)