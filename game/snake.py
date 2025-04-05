from __future__ import annotations
from typing import List
from config.constants import (
    INPUT_NODES,
    HIDDEN_NODES,
    OUTPUT_NODES,
    PLAYABLE_AREA_HEIGHT,
    PLAYABLE_AREA_WIDTH,
    LEFT_DOWN_VECTOR,
    LEFT_UP_VECTOR,
    LEFT_VECTOR,
    RIGHT_DOWN_VECTOR,
    RIGHT_UP_VECTOR,
    RIGHT_VECTOR,
    UP_VECTOR,
    DOWN_VECTOR,
)
from neural_network.neural_network import NeuralNetwork
from game.vector import Vector
from game.apple import Apple
from game.vision import Vision
from copy import copy
import pygame


class Snake:
    def __init__(self):
        self.x_start = PLAYABLE_AREA_WIDTH / 2
        self.y_start = PLAYABLE_AREA_HEIGHT / 2
        self.len = 1
        self.is_alive = True
        self.time_left = 200
        self.life_time = 0
        self.score = 0

        self.head = Vector(self.x_start, self.y_start)
        self.vel = Vector(RIGHT_VECTOR.x, RIGHT_VECTOR.y)

        self.tail: List[Vector] = [
            Vector(self.x_start - 30, self.y_start),
            Vector(self.x_start - 20, self.y_start),
            Vector(self.x_start - 10, self.y_start),
        ]
        self.len += 3

        self.visions: List[Vision] = [Vision() for _ in range(8)]
        self.visions_array = []

        self.DNA = NeuralNetwork(INPUT_NODES, HIDDEN_NODES, OUTPUT_NODES)
        self.apple = Apple()

    def calc_score(self):
        if self.len > 10:
            self.score = pow(self.life_time, 2) * pow(2, 10) * (self.len - 9)
        else:
            self.score = pow(self.life_time, 2) * pow(2, self.len)

    def is_on_tail(self, x: int, y: int) -> bool:
        return any(segment.x == x and segment.y == y for segment in self.tail)

    def check_dir_and_get_vision(self, direction: Vector) -> Vision:
        vision = Vision()
        distance = 0
        head_buff = Vector(self.head.x, self.head.y)

        while (
            0 <= head_buff.x <= PLAYABLE_AREA_WIDTH
            and 0 <= head_buff.y <= PLAYABLE_AREA_HEIGHT
        ):
            if head_buff.x == self.apple.pos.x and head_buff.y == self.apple.pos.y:
                vision.is_apple = 1

            if self.is_on_tail(head_buff.x, head_buff.y):
                vision.tail_dist = 1 / distance

            head_buff.x += direction.x
            head_buff.y += direction.y
            distance += 1

        vision.wall_dist = 1 / distance
        return vision

    def set_input(self):
        directions = [
            LEFT_VECTOR,
            UP_VECTOR,
            RIGHT_VECTOR,
            DOWN_VECTOR,
            LEFT_UP_VECTOR,
            RIGHT_UP_VECTOR,
            RIGHT_DOWN_VECTOR,
            LEFT_DOWN_VECTOR,
        ]
        self.visions = [
            self.check_dir_and_get_vision(direction) for direction in directions
        ]
        self.visions_array = self.visions_to_array()

    def visions_to_array(self) -> List[float]:
        return [
            value
            for vision in self.visions
            for value in (vision.is_apple, vision.tail_dist, vision.wall_dist)
        ]

    def set_velocity(self):
        output_array = self.DNA.get_output(self.visions_array)
        max_idx = self.find_max_val_index(output_array)

        if max_idx == 0 and self.vel.x != RIGHT_VECTOR.x:
            self.vel = LEFT_VECTOR
        elif max_idx == 1 and self.vel.y != DOWN_VECTOR.y:
            self.vel = UP_VECTOR
        elif max_idx == 2 and self.vel.x != LEFT_VECTOR.x:
            self.vel = RIGHT_VECTOR
        elif max_idx == 3 and self.vel.y != UP_VECTOR.y:
            self.vel = DOWN_VECTOR

    @staticmethod
    def find_max_val_index(array: List[float]) -> int:
        return array.index(max(array))

    def check_if_dies(self) -> bool:
        return (
            self.head.x + self.vel.x >= PLAYABLE_AREA_WIDTH
            or self.head.x + self.vel.x < 0
            or self.head.y + self.vel.y < 0
            or self.head.y + self.vel.y >= PLAYABLE_AREA_HEIGHT
        )

    def check_if_eats(self) -> bool:
        return (
            self.head.x + self.vel.x == self.apple.pos.x
            and self.head.y + self.vel.y == self.apple.pos.y
        )

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
        self.life_time += 1
        self.time_left -= 1

        if (
            self.check_if_dies()
            or self.is_on_tail(self.head.x + self.vel.x, self.head.y + self.vel.y)
            or self.time_left < 0
        ):
            self.is_alive = False
            return

        self.clear_snake()
        pygame.draw.rect(
            DISPLAY, pygame.Color("White"), (self.head.x, self.head.y, 10, 10)
        )

        if self.check_if_eats():
            self.eat()
        else:
            self.tail.pop(0)
            self.tail.append(Vector(self.head.x, self.head.y))

        self.head.x += self.vel.x
        self.head.y += self.vel.y

    def clear_snake(self):
        for segment in self.tail:
            pygame.draw.rect(
                DISPLAY, pygame.Color("White"), (segment.x, segment.y, 10, 10)
            )
        pygame.draw.rect(
            DISPLAY, pygame.Color("White"), (self.head.x, self.head.y, 10, 10)
        )

    def clear_apples(self):
        pygame.draw.rect(
            DISPLAY, pygame.Color("White"), (self.apple.pos.x, self.apple.pos.y, 10, 10)
        )

    def do_crossover(self, other_snake: Snake) -> Snake:
        child_snake = Snake()
        child_snake.DNA = self.DNA.do_crossover(other_snake.DNA)
        return child_snake

    def mutate(self, mutation_rate: float):
        self.DNA.mutate(mutation_rate)

    def clone(self) -> Snake:
        clone = Snake()
        clone.DNA = copy(self.DNA)
        clone.is_alive = True
        return clone

    def show(self, display):
        for segment in self.tail:
            pygame.draw.rect(display, pygame.Color("Black"), (segment.x, segment.y, 10, 10))
        pygame.draw.rect(display, pygame.Color("Black"), (self.head.x, self.head.y, 10, 10))
        pygame.display.update(0, 0, PLAYABLE_AREA_WIDTH, PLAYABLE_AREA_HEIGHT)
        self.apple.show()
