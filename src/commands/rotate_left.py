# src/commands/rotate_left.py

from src.commands.base_command import BaseCommand
from src.car import Car
from src.grid import Grid


class RotateLeftCommand(BaseCommand):
    def execute(self, car: "Car", grid: Grid):
        car.direction = car.direction.rotate_left()
