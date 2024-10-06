# src/parsers/input_parser.py

from typing import List, Tuple
from src.utils.direction_utils import Direction
from src.car import Car
from src.grid import Grid
from src.commands.command_factory import CommandFactory
from src.commands.base_command import BaseCommand

class InputParser:
    @staticmethod
    def parse_single_car_input(input_lines: List[str]) -> Tuple[Grid, Car, List[str]]:
        grid, car, commands = InputParser._parse_car_input(input_lines, 0)
        return grid, car, commands

    @staticmethod
    def parse_multiple_cars_input(input_lines: List[str]) -> Tuple[Grid, List[Car]]:
        grid = InputParser._parse_grid_dimensions(input_lines[0])
        cars = []
        i = 1
        while i < len(input_lines):
            identifier = input_lines[i].strip()
            car_info = input_lines[i + 1].split()
            x, y = int(car_info[0]), int(car_info[1])
            direction = Direction.from_string(car_info[2])

            commands = InputParser._parse_commands(input_lines[i + 2].strip())

            car = InputParser._create_car(identifier=identifier, x=x, y=y, direction=direction, commands=commands)
            cars.append(car)
            i += 3
        return grid, cars

    @staticmethod
    def _parse_grid_dimensions(line: str) -> Grid:
        grid_dimensions = list(map(int, line.split()))
        return Grid(width=grid_dimensions[0], height=grid_dimensions[1])

    @staticmethod
    def _parse_car_input(input_lines: List[str], start_index: int) -> Tuple[Grid, Car, List[BaseCommand]]:
        grid = InputParser._parse_grid_dimensions(input_lines[start_index])
        car_info = input_lines[start_index + 1].split()
        x, y = int(car_info[0]), int(car_info[1])
        direction = Direction.from_string(car_info[2])

        commands = InputParser._parse_commands(input_lines[start_index + 2].strip())

        car = InputParser._create_car(identifier="A", x=x, y=y, direction=direction, commands=commands)
        return grid, car, commands

    @staticmethod
    def _parse_commands(command_line: str) -> List[BaseCommand]:
        return [CommandFactory.create_command(c) for c in command_line.strip()]

    @staticmethod
    def _create_car(identifier: str, x: int, y: int, direction: Direction, commands: List[BaseCommand]) -> Car:
        return Car(identifier=identifier, x=x, y=y, direction=direction, commands=commands)
