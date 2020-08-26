from typing import *
from Population import *


class Environment:
    def __init__(self, no_populations: int, pop_size: int):
        self.no_generations = 0
        self.populations = List[Population]
        self.populations = [Population(pop_size) for _ in range(no_populations)]

    def is_pop_extinct(self):
        for pop in self.populations:
            if not pop.is_extinct():
                return False
        return True

    def update(self):
        for pop in self.populations:
            pop.update_alive()

    def run_genetic(self):
        # Runs when whole population is dead
        for pop in self.populations:
            pop.fitness() # calculate fitness for each snake in each population