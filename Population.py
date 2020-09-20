from typing import *
from Snake import *
import copy
from constants import MUTATION_RATE


class Population:
    def __init__(self, pop_size):
        self.no_generations = 1
        self.score_sum = 0
        self.pop_size = pop_size
        self.snakes = [Snake() for _ in range(pop_size)]
        self.fitnesses = [0 for _ in range(len(self.snakes))]
        self.curr_best_idx = 0 # idx of the best snake that should be shown on the board
        self.global_best_snake = self.snakes[0] # init with random snake
        self.mutation_rate = MUTATION_RATE
        self.best_len = 4

    def is_extinct(self) -> bool:
        for snake in self.snakes:
            if snake.is_alive:
                return False
        return True

    def update_alive(self):
        for idx, snake in enumerate(self.snakes):
            if snake.is_alive:
                snake.set_input() # get input for nn
                snake.set_velocity() # determine v based on output
                snake.move()

                if self.snakes[0].is_alive and idx == 0:
                    self.snakes[0].show()

        # after each tour, find the temp best one
        self.calc_curr_best_idx()
        # TODO: set current best for showing only one snake

    def calc_score(self):
        for snake in self.snakes:
            snake.calc_score() # calculate fitness for each snake

    def calc_curr_best_idx(self):
        # lifetime is same, therefore calc only len
        max_len = 0
        max_idx = 0
        for idx, snake in enumerate(self.snakes):
            if snake.is_alive and snake.len > max_len:
                max_len = snake.len
                max_idx = idx

        if not self.snakes[self.curr_best_idx].is_alive:# or max_len > self.snakes[self.curr_best_idx].len + 5:
            self.curr_best_idx = max_idx

        if max_len > self.best_len:
            self.best_len = max_len

    def set_global_best_snake(self):
        max_score = 0
        max_idx = 0
        for idx, snake in enumerate(self.snakes):
            if snake.score > max_score:
                max_score = snake.score
                max_idx = idx

        if max_score > self.global_best_snake.score:
            self.global_best_snake = self.snakes[max_idx].clone()

    def do_natural_selection(self):
        next_snakes = []

        self.set_global_best_snake()
        next_snakes.append(self.global_best_snake.clone())

        self.calc_score_sum()
        self.calc_fitnesses()
        for idx in range(1, len(self.snakes)):
            parent_first = self.select_from_fitness()
            parent_second = self.select_from_fitness()

            child = parent_first.do_crossover(parent_second) # make some sex here : )
            child.mutate(self.mutation_rate) # officer down

            next_snakes.append(child)

        self.snakes = next_snakes[:]
        self.no_generations += 1



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
        rand_value = random.random() # from (0 to 1>
        idx = -1
        while rand_value > 0:
            idx += 1
            rand_value -= self.fitnesses[idx]

        return self.snakes[idx]


    def clear_snakes(self):
        for snake in self.snakes:
            snake.clear_snake()
            snake.clear_apples()