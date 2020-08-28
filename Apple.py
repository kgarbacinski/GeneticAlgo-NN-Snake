from Vector import *
from random import randint
from constants import WINDOW_HEIGHT, WINDOW_WIDTH, PLAYABLE_AREA_HEIGHT, PLAYABLE_AREA_WIDTH
import pygame
from pygame import Rect
from main import DISPLAY
import math


class Apple:
    def __init__(self):
        x_pos = randint(0, math.floor((PLAYABLE_AREA_WIDTH - 1) / 10)) * 10
        y_pos = randint(0, math.floor((WINDOW_HEIGHT - 1) / 10)) * 10
        self.pos = Vector(x_pos, y_pos)

    def show(self):
        pygame.draw.rect(DISPLAY, pygame.Color("Red"), (self.pos.x, self.pos.y, 10, 10))
        pygame.display.update(self.pos.x, self.pos.y, 10, 10)