# tests/test_commands/test_rotate_right.py

import pytest
from src.commands.rotate_right import RotateRightCommand
from src.car import Car
from src.utils.direction_utils import Direction
from src.grid import Grid


def test_rotate_right_command():
    grid = Grid(width=10, height=10)
    car = Car(identifier="B", x=2, y=2, direction=Direction.NORTH, commands=[])
    command = RotateRightCommand()
    command.execute(car, grid)
    assert car.direction == Direction.EAST
    command.execute(car, grid)
    assert car.direction == Direction.SOUTH
    command.execute(car, grid)
    assert car.direction == Direction.WEST
    command.execute(car, grid)
    assert car.direction == Direction.NORTH
