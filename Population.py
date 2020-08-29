from typing import *
from Snake import *
import copy


class Population:
    def __init__(self, pop_size):
        self.pop_size = pop_size
        self.snakes = [Snake() for _ in range(pop_size)]
        self.curr_best_idx = 0 # idx of the best snake that should be shown on the board
        self.global_best_snake = self.snakes[0] # init with random snake

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

                if snake == self.snakes[self.curr_best_idx]:
                    snake.show()

        # after each tour, find the temp best one
        self.calc_curr_best_idx()
        # TODO: set current best for showing only one snake

    def calc_score(self):
        for snake in self.snakes:
            snake.calc_score() # calculate fitness for each snake
    '''
    def calc_curr_best_idx(self):
        # lifetime is same, therefore calc only len
        max_len = 0
        max_idx = 0
        for idx, snake in enumerate(self.snakes):
            if snake.is_alive and snake.len > max_len:
                max_len = snake.len
                max_idx = idx

        if not self.snakes[self.curr_best_idx]:
            self.curr_best_idx = max_idx
    '''
    def set_global_best_snake(self):
        max_score = 0
        max_idx = 0
        for idx, snake in enumerate(self.snakes):
            if snake.score > max_score:
                max_score = snake.score
                max_idx = idx

        if max_score > self.global_best_snake.score:
            self.global_best_snake = copy.copy(self.snakes[max_idx])

    def do_natural_selection(self):
        next_snakes = [Snake() for _ in range(self.pop_size)]

        self.set_global_best_snake()
        next_snakes[0] = copy.copy(self.global_best_snake)

        for idx in range(len(self.snakes)):
            parent_first = None
            parent_second = None 
