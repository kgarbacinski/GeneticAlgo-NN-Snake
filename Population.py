from typing import *
from Snake import *


class Population:
    def __init__(self, pop_size):
        self.snakes = [Snake(350, 200) for _ in range(pop_size)]

    def is_extinct(self) -> bool:
        for snake in self.snakes:
            if snake.is_alive:
                return False
        return True

    def update_alive(self):
        for snake in self.snakes:
            if snake.is_alive:
                snake.set_input() # get input for nn
                snake.set_velocity() # determine v based on output
                snake.move()

                snake.show()
        # TODO: set current best for showing only one snake

    def calc_fitness(self):
        for snake in self.snakes:
            snake.calc_score() # calculate fitness for each snake
