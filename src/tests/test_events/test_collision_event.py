# tests/test_events/test_collision_event.py

import pytest
from src.events.collision_event import CollisionEvent


def test_collision_event_creation():
    event = CollisionEvent(collided_cars=["A", "B"], position=(5, 5), step=3)
    assert event.collided_cars == ["A", "B"]
    assert event.position == (5, 5)
    assert event.step == 3
