from typing import *
from constants import INPUT_NODES, HIDDEN_NODES, OUTPUT_NODES, VELOCITY
from NeuralNetwork import *
from main import DISPLAY
import pygame
from Vector import Vector

class Snake:
    def __init__(self, x_pos: int, y_pos: int):
        # Snake attributes
        self.x = x_pos
        self.y = y_pos
        self.len = 0
        self.isAlive = True

        # Create vector of position and velocity
        self.head = Vector(self.x, self.y) # actual position
        self.vel = Vector(VELOCITY, 0)

        # Init snake with 4 body segments
        self.tail = []
        self.tail.append(Vector(self.x - 30, self.y)) # Add last segment of body
        self.tail.append(Vector(self.x - 20, self.y))  # Add second segment of body
        self.tail.append(Vector(self.x - 10, self. y)) # Add first segment of body
        self.len += 3 # Increase a body length

        # Get DNA as snake's brain
        self.DNA = NeuralNetwork(INPUT_NODES, HIDDEN_NODES, OUTPUT_NODES)

        self.show()

    def fitness(self):
        pass

    def move(self):
        self.tail.pop(0)
        self.tail.insert(len(self.tail), Vector(self.head.x, self.head.y))
        self.head = Vector(self.head.x + self.vel.x, self.head.y + self.vel.y)

    def show(self):
        DISPLAY.fill(pygame.Color("White"))
        # Show whole snake's body
        for segment in self.tail:
            pygame.draw.rect(DISPLAY, pygame.Color("Black"), (segment.x, segment.y, 10, 10))

        # Draw head
        pygame.draw.rect(DISPLAY, pygame.Color("Black"), (self.head.x, self.head.y, 10, 10))
        pygame.display.update(0, 0, 500, 500)