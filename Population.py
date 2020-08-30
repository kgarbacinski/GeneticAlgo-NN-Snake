from typing import *
from Snake import *
import copy


class Population:
    def __init__(self, pop_size):
        self.score_sum = 0
        self.pop_size = pop_size
        self.snakes = [Snake() for _ in range(pop_size)]
        self.fitnesses = [0 for _ in range(len(self.snakes))]
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
        #self.calc_curr_best_idx()
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

        self.calc_score_sum()
        self.calc_fitnesses()
        for idx in range(1, len(self.snakes)):
            parent_first = self.select_from_fitness()
            parent_second = self.select_from_fitness()

            child = parent_first.do_crossover(parent_second) # made some sex here : )

    def calc_score_sum(self):
        self.score_sum = 0
        for idx, snake in enumerate(self.snakes):
            self.score_sum += snake.score

    def calc_fitnesses(self):
        # Normalize
        for idx in range(len(self.fitnesses)):
            self.fitnesses[idx] = self.snakes[idx].score / self.score_sum

    # made with improved pool selection
    def select_from_fitness(self):
        rand_value = random.random(1)
        idx = -1
        while rand_value > 0:
            idx += 1
            rand_value -= self.fitnesses[idx]

        return self.snakes[idx]
