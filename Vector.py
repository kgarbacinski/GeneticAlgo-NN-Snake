from dataclasses import dataclass


@dataclass(unsafe_hash=False)
class Vector:
    x: int = 0
    y: int = 0
