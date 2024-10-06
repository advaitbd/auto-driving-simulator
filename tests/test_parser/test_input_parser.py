# tests/test_parsers/test_input_parser.py

import pytest
from src.parsers.input_parser import InputParser
from src.utils.direction_utils import Direction
from src.commands.move_forward import MoveForwardCommand
from src.commands.rotate_right import RotateRightCommand
from src.commands.rotate_left import RotateLeftCommand

def test_parse_single_car_input():
    input_lines = ["10 10", "1 2 N", "FFRFFFRRLF"]
    grid, car, commands = InputParser.parse_single_car_input(input_lines)
    assert grid.width == 10
    assert grid.height == 10
    assert car.identifier == "A"
    assert car.x == 1
    assert car.y == 2
    assert car.direction == Direction.NORTH

    expected_commands = [
        MoveForwardCommand(),
        MoveForwardCommand(),
        RotateRightCommand(),
        MoveForwardCommand(),
        MoveForwardCommand(),
        MoveForwardCommand(),
        RotateRightCommand(),
        RotateRightCommand(),
        RotateLeftCommand(),
        MoveForwardCommand(),
    ]
    assert commands == expected_commands

def test_parse_multiple_cars_input():
    input_lines = ["10 10", "A", "1 2 N", "FFRFFFRRL", "B", "7 8 W", "FFLFFFFFF"]
    grid, cars = InputParser.parse_multiple_cars_input(input_lines)
    assert grid.width == 10
    assert grid.height == 10
    assert len(cars) == 2
    car_a, car_b = cars

    assert car_a.identifier == "A"
    assert car_a.x == 1
    assert car_a.y == 2
    assert car_a.direction == Direction.NORTH
    expected_commands_a = [
        MoveForwardCommand(),
        MoveForwardCommand(),
        RotateRightCommand(),
        MoveForwardCommand(),
        MoveForwardCommand(),
        MoveForwardCommand(),
        RotateRightCommand(),
        RotateRightCommand(),
        RotateLeftCommand(),
    ]
    assert car_a.commands == expected_commands_a

    assert car_b.identifier == "B"
    assert car_b.x == 7
    assert car_b.y == 8
    assert car_b.direction == Direction.WEST
    expected_commands_b = [
        MoveForwardCommand(),
        MoveForwardCommand(),
        RotateLeftCommand(),
        MoveForwardCommand(),
        MoveForwardCommand(),
        MoveForwardCommand(),
        MoveForwardCommand(),
        MoveForwardCommand(),
        MoveForwardCommand(),
    ]
    assert car_b.commands == expected_commands_b
