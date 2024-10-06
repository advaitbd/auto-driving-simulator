# src/collision_handler.py

from typing import Optional, Dict
from src.events.collision_event import CollisionEvent
from src.collision_strategies.collision_strategy import CollisionStrategy

class CollisionHandler:
    def __init__(self, strategy: CollisionStrategy):
        self.strategy = strategy

    def detect_collisions(self, positions: Dict[str, tuple], step: int) -> Optional[CollisionEvent]:
        return self.strategy.detect_collisions(positions, step)
