
# src/simulator/single_car_simulator.py

from typing import Tuple
from src.grid import Grid
from src.car import Car

class SingleCarSimulator:
    def __init__(self, grid: Grid, car: Car):
        self.grid = grid
        self.car = car

    def simulate(self) -> Tuple[int, int, str]:
        for command in self.car.commands:
            command.execute(self.car, self.grid)
        return self.car.x, self.car.y, self.car.direction.to_string()
