from typing import *
from Snake import *


class Population:
    def __init__(self, pop_size):
        self.snakes = [[Snake(100, 200)] * pop_size]
