from typing import *
from constants import INPUT_NODES, HIDDEN_NODES, OUTPUT_NODES, PLAYABLE_AREA_HEIGHT, PLAYABLE_AREA_WIDTH, \
    LEFT_DOWN_VECTOR, LEFT_UP_VECTOR, LEFT_VECTOR, RIGHT_DOWN_VECTOR, RIGHT_UP_VECTOR, RIGHT_VECTOR, UP_VECTOR, DOWN_VECTOR
from NeuralNetwork import *
from main import DISPLAY
import pygame
from Vector import Vector
from Apple import Apple
from Vision import Vision


class Snake:
    def __init__(self, x_pos: int, y_pos: int):
        # Snake attributes
        self.x_start = PLAYABLE_AREA_WIDTH / 2
        self.y_start = PLAYABLE_AREA_HEIGHT / 2
        self.len = 1
        self.is_alive = True
        self.time_left = 200
        self.life_time = 0

        # Create vector of position and velocity
        self.head = Vector(self.x_start, self.y_start) # actual position
        self.vel = Vector(RIGHT_VECTOR.x, RIGHT_VECTOR.y)

        # Init snake with 4 body segments
        self.tail = []
        self.tail.append(Vector(self.x_start - 30, self.y_start)) # Add last segment of body
        self.tail.append(Vector(self.x_start - 20, self.y_start))  # Add second segment of body
        self.tail.append(Vector(self.x_start - 10, self. y_start)) # Add first segment of body
        self.len += 3 # Increase a body length

        # Vision for input
        self.visions = [Vision() for _ in range(8)]
        self.visions_array = []

        # Get DNA as snake's brain
        self.DNA = NeuralNetwork(INPUT_NODES, HIDDEN_NODES, OUTPUT_NODES)
        self.apple = Apple()

        self.show()

    def fitness(self):
        pass

    def is_on_tail(self, x: int, y: int) -> bool:
        for segment in self.tail:
            if segment.x == x and segment.y == y:
                return True

        return False

    def check_dir_and_get_vision(self, direction: Vector) -> Vision:
        vision = Vision()
        distance = 0

        head_buff = Vector(self.head.x, self.head.y)

        # Move once
        head_buff.x += direction.x
        head_buff.y += direction.y
        distance += 1

        # Looks in 8 direction and checks where's food, wall and body's segment
        while 0 < head_buff.x <= PLAYABLE_AREA_WIDTH and 0 < head_buff.y <= PLAYABLE_AREA_HEIGHT:
            if head_buff.x == self.apple.pos.x and head_buff.y == self.apple.pos.y:
                vision.is_apple = 1

            if self.is_on_tail(head_buff.x, head_buff.y):
                vision.tail_dist = 1 / distance

            head_buff.x += direction.x
            head_buff.y += direction.y
            distance += 1

        vision.wall_dist = 1 / distance

        return vision

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

        self.visions_array = self.visions_to_array()

    def visions_to_array(self):
        array = []
        for vision in self.visions:
            array.append(vision.is_apple)
            array.append(vision.tail_dist)
            array.append(vision.wall_dist)

        return array

    # Set v from output
    def set_velocity(self):
        output_array = self.DNA.get_output(self.visions_array)
        max_idx = self.find_max_val_index(output_array)

        # Set direction
        if max_idx == 0 and self.vel.x != RIGHT_VECTOR.x and self.vel.y != RIGHT_VECTOR.y:
            self.vel.x = LEFT_VECTOR.x
            self.vel.y = LEFT_VECTOR.y
        elif max_idx == 1 and self.vel.x != DOWN_VECTOR.x and self.vel.y != DOWN_VECTOR.y:
            self.vel.x = UP_VECTOR.x
            self.vel.y = UP_VECTOR.y
        elif max_idx == 2 and self.vel.x != LEFT_VECTOR.x and self.vel.y != LEFT_VECTOR.y:
            self.vel.x = RIGHT_VECTOR.x
            self.vel.y = RIGHT_VECTOR.y
        elif max_idx == 3 and self.vel.x != UP_VECTOR.x and self.vel.y != UP_VECTOR.y:
            self.vel.x = DOWN_VECTOR.x
            self.vel.y = DOWN_VECTOR.y

    @staticmethod
    def find_max_val_index(array: list) -> int:
        return array.index(max(array))

    def check_if_dies(self) -> bool:
        if self.head.x + self.vel.x >= PLAYABLE_AREA_WIDTH or self.head.x + self.vel.x < 0 or\
           self.head.y + self.vel.y < 0 or self.head.y + self.vel.y >= PLAYABLE_AREA_HEIGHT:
            return True

        return False

    def check_if_eats(self):
        if self.head.x + self.vel.x == self.apple.pos.x and self.head.y + self.vel.y == self.apple.pos.y:
            return True

        return False

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

        if self.check_if_dies() or self.is_on_tail(self.head.x + self.vel.x, self.head.y + self.vel.y) or self.time_left < 0:
            self.is_alive = False
            return

        if self.check_if_eats():
            self.eat()

        # Move the snake's head
        self.clear_snake()
        self.tail.pop(0)
        self.tail.append(Vector(self.head.x, self.head.y))
        self.head.x += self.vel.x
        self.head.y += self.vel.y

    def clear_snake(self):
        for segment in self.tail:
            pygame.draw.rect(DISPLAY, pygame.Color("White"), (segment.x, segment.y, 10, 10))

        pygame.draw.rect(DISPLAY, pygame.Color("White"), (self.head.x, self.head.y, 10, 10))

    def show(self):
        #DISPLAY.fill(pygame.Color("White"))

        # Show whole snake's body
        for segment in self.tail:
            pygame.draw.rect(DISPLAY, pygame.Color("Black"), (segment.x, segment.y, 10, 10))

        # Draw head
        pygame.draw.rect(DISPLAY, pygame.Color("Black"), (self.head.x, self.head.y, 10, 10))

        pygame.display.update(0, 0, PLAYABLE_AREA_WIDTH, PLAYABLE_AREA_HEIGHT)

        # Draw apple
        self.apple.show()