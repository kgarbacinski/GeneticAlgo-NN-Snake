from typing import *
from constants import INPUT_NODES, HIDDEN_NODES, OUTPUT_NODES, VELOCITY, PLAYABLE_AREA_HEIGHT, PLAYABLE_AREA_WIDTH, \
    LEFT_DOWN_VECTOR, LEFT_UP_VECTOR, LEFT_VECTOR, RIGHT_DOWN_VECTOR, RIGHT_UP_VECTOR, RIGHT_VECTOR, UP_VECTOR, DOWN_VECTOR
from NeuralNetwork import *
from main import DISPLAY
import pygame
from Vector import Vector
from Apple import *
from Vision import *


class Snake:
    def __init__(self, x_pos: int, y_pos: int):
        # Snake attributes
        self.x_start = x_pos
        self.y_start = y_pos
        self.len = 4
        self.is_alive = True
        self.time_left = 200
        self.life_time = 0

        # Create vector of position and velocity
        self.head = Vector(self.x_start, self.y_start) # actual position
        self.vel = Vector(VELOCITY, 0)

        # Init snake with 4 body segments
        self.tail = []
        self.tail.append(Vector(self.x_start - 30, self.y_start)) # Add last segment of body
        self.tail.append(Vector(self.x_start - 20, self.y_start))  # Add second segment of body
        self.tail.append(Vector(self.x_start - 10, self. y_start)) # Add first segment of body
        self.len += 3 # Increase a body length

        # Vision for input
        self.visions = List[Vision]

        # Get DNA as snake's brain
        self.DNA = NeuralNetwork(INPUT_NODES, HIDDEN_NODES, OUTPUT_NODES)
        self.apple = Apple()

        self.show()

    def fitness(self):
        pass

    def check_dir_and_get_vision(self, direction: Vector) -> Vision:
        vision = Vision()

        head_buff = Vector(self.head.x, self.head.y)
        distance = 0

        # Looks in 8 direction and checks where's food, wall and body's segment
        while head_buff.x > 0 or head_buff.y > 0 or head_buff.x <= PLAYABLE_AREA_WIDTH \
                or head_buff.y <= PLAYABLE_AREA_HEIGHT:
            if head_buff.x == self.apple.pos.x and head_buff.y == self.apple.pos.y:
                vision.is_apple = True

            if self.is_on_tail(head_buff.x, head_buff.y):
                vision.tail_dist = 1 / distance

            head_buff.x += direction.x
            head_buff.y += direction.y
            distance += 1

        vision.wall_dist = 1 / distance

        return vision

    def is_on_tail(self, x: int, y: int)->bool:
        for segment in self.tail:
            if segment.x == x and segment.y == y:
                return True

        return False

    # Get input to determine v
    def set_input(self):
        self.visions[0] = self.check_dir_and_get_vision(LEFT_VECTOR)
        self.visions[1] = self.check_dir_and_get_vision(UP_VECTOR)
        self.visions[2] = self.check_dir_and_get_vision(RIGHT_VECTOR)
        self.visions[3] = self.check_dir_and_get_vision(DOWN_VECTOR)
        self.visions[4] = self.check_dir_and_get_vision(LEFT_UP_VECTOR)
        self.visions[5] = self.check_dir_and_get_vision(RIGHT_UP_VECTOR)
        self.visions[6] = self.check_dir_and_get_vision(RIGHT_DOWN_VECTOR)
        self.visions[7] = self.check_dir_and_get_vision(LEFT_DOWN_VECTOR)

    # Set v from output
    def set_velocity(self):
        self.DNA.array_to_matrix(None, 1)

    def check_if_dies(self) -> bool:
        if self.head.x + self.vel.x >= PLAYABLE_AREA_WIDTH or self.head.x + self.vel.x <= 0 or\
           self.head.y + self.vel.y <= 0 or self.head.y + self.vel.y >= PLAYABLE_AREA_HEIGHT:
            return True

    def check_if_eats(self):
        if self.head.x + self.vel.x == self.apple.pos.x and self.head.y + self.vel.y == self.apple.pos.y:
            return True

    def grow(self):
        new_segment = Vector(self.head.x, self.head.y)
        self.tail.append(new_segment)
        self.len += 1

    def gen_not_in_tail(self):
        while self.apple.pos in self.tail:
            self.apple = Apple()

    def eat(self):
        self.apple = Apple()
        self.gen_not_in_tail()

        self.time_left += 100

        self.grow()

    def move(self):
        # Change attributes to determine fitness
        self.life_time += 1
        self.time_left -= 1

        if self.check_if_dies() or self.time_left < 0:
            self.is_alive = False
            return

        if self.check_if_eats():
            self.eat()

        # Move the snake's head
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
        pygame.display.update(self.head.x, self.head.y, 10, 10)

        # Draw apple
        self.apple.show()