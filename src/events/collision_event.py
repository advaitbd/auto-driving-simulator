# src/events/collision_event.py

from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class CollisionEvent:
    collided_cars: List[str]
    position: Tuple[int, int]
    step: int

    # Method to print the collision event
    def __str__(self):
        return f"Collision at {self.position} at step {self.step} involving cars {self.collided_cars}"
