from typing import *
from constants import INPUT_NODES, HIDDEN_NODES, OUTPUT_NODES, VELOCITY
from NeuralNetwork import *
from main import DISPLAY
import pygame

class Snake:
    def __init__(self, x_pos: int, y_pos: int):
        # Snake attributes
        self.x = x_pos
        self.y = y_pos
        self.len = 0
        self.isAlive = True

        # Create vector of position and velocity
        pos = list([self.x, self.y])
        vel = list([VELOCITY, 0])

        # Init snake with 4 body segments
        self.tail = []
        self.tail.append([self.x - 30, self.y])  # Add first segment of body
        self.tail.append(list([self.x - 20, self.y]))  # Add second segment of body
        self.tail.append(list([self.x - 10, self.y]))  # Add third segment of body
        self.len += 3 # Increase a body length

        # Get DNA as snake's brain
        DNA = NeuralNetwork(INPUT_NODES, HIDDEN_NODES, OUTPUT_NODES)

        self.show()



    def show(self):
        # Show whole snake's body
        DISPLAY.fill(pygame.Color("Black"))
