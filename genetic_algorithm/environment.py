from typing import List
from genetic_algorithm.population import Population


class Environment:
    def __init__(self, no_populations: int, pop_size: int):
        self.no_generations = 0
        self.best_snake_len = 4
        self.populations: List[Population] = [
            Population(pop_size) for _ in range(no_populations)
        ]

    def is_pop_extinct(self) -> bool:
        return all(pop.is_extinct() for pop in self.populations)

    def update(self):
        for pop in self.populations:
            pop.update_alive()
            self.best_snake_len = pop.best_snake_len

    def run_genetic(self):
        for pop in self.populations:
            pop.clear_snakes()
            pop.calc_score()
            pop.do_natural_selection()
            self.no_generations += 1
