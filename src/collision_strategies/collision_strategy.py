# src/collision_strategies/collision_strategy.py

from abc import ABC, abstractmethod
from typing import Optional, Dict
from src.events.collision_event import CollisionEvent

class CollisionStrategy(ABC):
    @abstractmethod
    def detect_collisions(self, positions: Dict[str, tuple], step: int) -> Optional[CollisionEvent]:
        pass
