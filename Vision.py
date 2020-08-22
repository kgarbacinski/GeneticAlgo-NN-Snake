from dataclasses import dataclass


@dataclass(unsafe_hash=False, )
class Vision:
    wall_dist: object = None
    tail_dist: object = None
    is_apple: bool = False
