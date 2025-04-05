from typing import List
from game.snake import Snake
import random
from config.constants import MUTATION_RATE

class Population:
    def __init__(self, pop_size: int):
        self.no_generations = 1
        self.score_sum = 0
        self.pop_size = pop_size
        self.snakes: List[Snake] = [Snake() for _ in range(pop_size)]
        self.fitnesses = [0.0 for _ in range(len(self.snakes))]
        self.curr_best_idx = 0
        self.global_best_snake = self.snakes[0]
        self.mutation_rate = MUTATION_RATE
        self.best_snake_len = 4

    def is_extinct(self) -> bool:
        return all(not snake.is_alive for snake in self.snakes)

    def update_alive(self):
        for idx, snake in enumerate(self.snakes):
            if snake.is_alive:
                snake.set_input()
                snake.set_velocity()
                snake.move()

                if idx == 0 and snake.is_alive:
                    snake.show()
                    self.best_snake_len = snake.len

        self.calc_curr_best_idx()

    def calc_score(self):
        for snake in self.snakes:
            snake.calc_score()

    def calc_curr_best_idx(self):
        max_len = 0
        max_idx = 0
        for idx, snake in enumerate(self.snakes):
            if snake.is_alive and snake.len > max_len:
                max_len = snake.len
                max_idx = idx

        if not self.snakes[self.curr_best_idx].is_alive:
            self.curr_best_idx = max_idx

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
        next_snakes = [self.global_best_snake]
        self.set_global_best_snake()
        self.calc_score_sum()
        self.calc_fitnesses()

        for _ in range(1, len(self.snakes)):
            parent_first = self.select_from_fitness()
            parent_second = self.select_from_fitness()
            child = parent_first.do_crossover(parent_second)
            child.mutate(self.mutation_rate)
            next_snakes.append(child)

        self.snakes = next_snakes
        self.no_generations += 1
        self.best_snake_len = 4

    def calc_score_sum(self):
        self.score_sum = sum(snake.score for snake in self.snakes)

    def calc_fitnesses(self):
        for idx in range(len(self.fitnesses)):
            self.fitnesses[idx] = self.snakes[idx].score / self.score_sum

    def select_from_fitness(self) -> Snake:
        rand_value = random.random()
        idx = -1
        while rand_value > 0:
            idx += 1
            rand_value -= self.fitnesses[idx]
        return self.snakes[idx]

    def clear_snakes(self):
        for snake in self.snakes:
            snake.clear_snake()
            snake.clear_apples()