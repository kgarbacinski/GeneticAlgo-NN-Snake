from dataclasses import dataclass

@dataclass
class Vision:
    wall_dist: float = 0.0
    tail_dist: float = 0.0
    is_apple: int = 0