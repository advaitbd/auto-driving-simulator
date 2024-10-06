# src/car.py

from dataclasses import dataclass
from typing import List
from src.utils.direction_utils import Direction
from src.grid import Grid
from src.commands.base_command import BaseCommand

@dataclass
class Car:
    identifier: str
    x: int
    y: int
    direction: Direction
    commands: List[BaseCommand]

    def get_position(self):
        """
        Returns the current position and direction of the car.

        Returns:
            tuple: A tuple containing the x-coordinate, y-coordinate, and direction as a string.
        """
        direction_str = {
            Direction.NORTH: "N",
            Direction.EAST: "E",
            Direction.SOUTH: "S",
            Direction.WEST: "W",
        }[self.direction]
        return self.x, self.y, direction_str
