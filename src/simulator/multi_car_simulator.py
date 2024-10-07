# src/simulator/multi_car_simulator.py

from typing import List, Optional
from src.grid import Grid
from src.car import Car
from src.events.collision_event import CollisionEvent
from src.collision_handler import CollisionHandler

class MultiCarSimulator:
    def __init__(self, grid: Grid, cars: List[Car], collision_handler: CollisionHandler):
        """
        Initializes the MultiCarSimulator with a grid, a list of cars, and a collision handler.

        Args:
            grid (Grid): The grid on which the cars will move.
            cars (List[Car]): A list of Car objects to be simulated.
            collision_handler (CollisionHandler): The handler to detect and manage collisions.
        """
        self.grid = grid
        self.cars = cars
        self.collision_handler = collision_handler

    def simulate(self) -> Optional[CollisionEvent]:
        """
        Simulates the movement of cars on the grid and checks for collisions.

        Returns:
            Optional[CollisionEvent]: A CollisionEvent if a collision occurs, otherwise None.
        """
        max_commands = max(len(car.commands) for car in self.cars)
        for step in range(1, max_commands + 1):
            positions = self._move_cars(step)
            collision_event = self.collision_handler.detect_collisions(positions, step)
            if collision_event:
                return collision_event
        return None

    def _move_cars(self, step: int) -> dict:
        """
        Moves the cars based on their commands for the given step.

        Args:
            step (int): The current simulation step.

        Returns:
            dict: A dictionary mapping car identifiers to their new positions (x, y).
        """
        positions = {}
        for car in self.cars:
            if step <= len(car.commands):
                command = car.commands[step - 1]
                command.execute(car, self.grid)
            positions[car.identifier] = car.x, car.y
        return positions
