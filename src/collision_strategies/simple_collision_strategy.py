# src/collision_strategies/simple_collision_strategy.py

from collections import defaultdict
from typing import Optional, Dict
from src.events.collision_event import CollisionEvent
from src.collision_strategies.collision_strategy import CollisionStrategy

class SimpleCollisionStrategy(CollisionStrategy):
    def detect_collisions(self, positions: Dict[str, tuple], step: int) -> Optional[CollisionEvent]:
        """
        Detects collisions based on the positions of cars.

        Args:
            positions (Dict[str, tuple]): A dictionary mapping car identifiers to their positions (x, y).
            step (int): The current simulation step.

        Returns:
            Optional[CollisionEvent]: A CollisionEvent if a collision is detected, otherwise None.
        """
        position_to_cars = defaultdict(list)
        for car_id, pos in positions.items():
            position_to_cars[pos].append(car_id)

        collision_positions = [
            pos for pos, cars_at_pos in position_to_cars.items() if len(cars_at_pos) > 1
        ]

        if collision_positions:
            collision_pos = collision_positions[0]
            collided_cars = position_to_cars[collision_pos]
            return CollisionEvent(
                collided_cars=collided_cars, position=collision_pos, step=step
            )

        return None
