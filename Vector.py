from dataclasses import dataclass


@dataclass(unsafe_hash=True)
class Vector:
    x: float
    y: float