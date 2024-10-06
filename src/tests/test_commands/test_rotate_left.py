# tests/test_commands/test_rotate_left.py

import pytest
from src.commands.rotate_left import RotateLeftCommand
from src.car import Car
from src.utils.direction_utils import Direction
from src.grid import Grid


def test_rotate_left_command():
    grid = Grid(width=10, height=10)
    car = Car(identifier="A", x=1, y=1, direction=Direction.NORTH, commands=[])
    command = RotateLeftCommand()
    command.execute(car, grid)
    assert car.direction == Direction.WEST
    command.execute(car, grid)
    assert car.direction == Direction.SOUTH
    command.execute(car, grid)
    assert car.direction == Direction.EAST
    command.execute(car, grid)
    assert car.direction == Direction.NORTH
