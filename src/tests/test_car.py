# tests/test_car.py

import pytest
from src.car import Car
from src.utils.direction_utils import Direction

def test_car_initialization():
    car = Car(identifier="A", x=1, y=2, direction=Direction.NORTH, commands=[])
    assert car.identifier == "A"
    assert car.x == 1
    assert car.y == 2
    assert car.direction == Direction.NORTH
    assert car.commands == []
