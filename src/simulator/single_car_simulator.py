# src/simulator/single_car_simulator.py

from typing import Tuple
from src.grid import Grid
from src.car import Car

class SingleCarSimulator:
    def __init__(self, grid: Grid, car: Car):
        """
        Initializes the SingleCarSimulator with a grid and a car.

        Args:
            grid (Grid): The grid on which the car will be simulated.
            car (Car): The car to be simulated.
        """
        self.grid = grid
        self.car = car

    def simulate(self) -> Tuple[int, int, str]:
        """
        Simulates the car's movement based on its commands.

        Executes each command in the car's command list and updates the car's position and direction accordingly.

        Returns:
            Tuple[int, int, str]: The final x-coordinate, y-coordinate, and direction of the car.
        """
        for command in self.car.commands:
            command.execute(self.car, self.grid)
        return self.car.x, self.car.y, self.car.direction.to_string()
