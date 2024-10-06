# tests/test_commands/test_move_forward.py

import pytest
from src.commands.move_forward import MoveForwardCommand
from src.car import Car
from src.utils.direction_utils import Direction
from src.grid import Grid


def test_move_forward_command_within_bounds():
    grid = Grid(width=5, height=5)
    car = Car(identifier="C", x=2, y=2, direction=Direction.NORTH, commands=[])
    command = MoveForwardCommand()
    command.execute(car, grid)
    assert car.x == 2
    assert car.y == 3

def test_move_forward_command_out_of_bounds():
    grid = Grid(width=5, height=5)
    car = Car(identifier="D", x=4, y=4, direction=Direction.NORTH, commands=[])
    command = MoveForwardCommand()
    command.execute(car, grid)
    assert car.x == 4
    assert car.y == 4  # Move ignored
