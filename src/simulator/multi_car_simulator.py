# src/simulator/multi_car_simulator.py

from typing import List, Optional
from src.grid import Grid
from src.car import Car
from src.events.collision_event import CollisionEvent
from src.collision_handler import CollisionHandler

class MultiCarSimulator:
    def __init__(self, grid: Grid, cars: List[Car], collision_handler: CollisionHandler):
        self.grid = grid
        self.cars = cars
        self.collision_handler = collision_handler

    def simulate(self) -> Optional[CollisionEvent]:
        max_commands = max(len(car.commands) for car in self.cars)
        for step in range(1, max_commands + 1):
            positions = self._move_cars(step)
            collision_event = self.collision_handler.detect_collisions(positions, step)
            if collision_event:
                return collision_event
        return None

    def _move_cars(self, step: int) -> dict:
        positions = {}
        for car in self.cars:
            if step <= len(car.commands):
                command = car.commands[step - 1]
                command.execute(car, self.grid)
            positions[car.identifier] = car.x, car.y
        return positions
