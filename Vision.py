from dataclasses import dataclass


@dataclass(unsafe_hash=False,)
class Vision:
    wall_dist: object = 0
    tail_dist: object = 0 # as False
    is_apple: bool = 0
