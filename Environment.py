from typing import *
from Population import *

class Environment:
    no_generations = 0
    populations = List[Population]

    def __init__(self, no_populations: int, pop_size: int):
        self.populations = [Population(pop_size)] * no_populations