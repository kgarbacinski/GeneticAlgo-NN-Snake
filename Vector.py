from dataclasses import dataclass


@dataclass(unsafe_hash=False)
class Vector:
    x: int
    y: int
