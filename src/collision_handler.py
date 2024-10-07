# src/collision_handler.py

from typing import Optional, Dict
from src.events.collision_event import CollisionEvent
from src.collision_strategies.collision_strategy import CollisionStrategy

class CollisionHandler:
    """
    The CollisionHandler class is responsible for detecting collisions between cars
    based on a given collision detection strategy. This class follows the Strategy
    Pattern, which allows the collision detection algorithm to be selected
    at runtime.

    Attributes:
        strategy (CollisionStrategy): The collision detection strategy to use.
    """

    def __init__(self, strategy: CollisionStrategy):
        """
        Initializes the CollisionHandler with a specific collision detection strategy.

        Args:
            strategy (CollisionStrategy): The collision detection strategy to use.
        """
        self.strategy = strategy

    def detect_collisions(self, positions: Dict[str, tuple], step: int) -> Optional[CollisionEvent]:
        """
        Detects collisions based on the current positions of the cars and the simulation step.

        Args:
            positions (Dict[str, tuple]): A dictionary mapping car identifiers to their positions.
            step (int): The current simulation step.

        Returns:
            Optional[CollisionEvent]: A CollisionEvent if a collision is detected, otherwise None.
        """
        return self.strategy.detect_collisions(positions, step)
