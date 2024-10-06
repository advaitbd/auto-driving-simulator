# src/commands/move_forward.py

from src.commands.base_command import BaseCommand
from src.car import Car
from src.grid import Grid


class MoveForwardCommand(BaseCommand):
    def execute(self, car: "Car", grid: Grid):
        new_x, new_y = car.direction.move_forward(car.x, car.y)
        if grid.is_within_bounds(new_x, new_y):
            car.x, car.y = new_x, new_y
