# tests/test_simulator.py

import pytest
from src.parsers.input_parser import InputParser
from src.utils.direction_utils import Direction
from src.grid import Grid
from src.car import Car
from src.simulator.single_car_simulator import SingleCarSimulator
from src.simulator.multi_car_simulator import MultiCarSimulator
from src.collision_handler import CollisionHandler
from src.collision_strategies.simple_collision_strategy import SimpleCollisionStrategy
from src.events.collision_event import CollisionEvent

def test_simulate_single_car():
    input_lines = [
        "10 10",  # Grid dimensions: width=10, height=10
        "1 2 N",  # Car information: x=1, y=2, direction=NORTH
        "FFRFFFRRLF",  # Command sequence
    ]

    grid, car, commands = InputParser.parse_single_car_input(input_lines)
    simulator = SingleCarSimulator(grid, car)
    final_position = simulator.simulate()

    expected_position = (4, 3)
    expected_direction = "S"

    assert final_position[0] == expected_position[0], f"Expected x={expected_position[0]}, got x={final_position[0]}"
    assert final_position[1] == expected_position[1], f"Expected y={expected_position[1]}, got y={final_position[1]}"
    assert final_position[2] == expected_direction, f"Expected direction={expected_direction}, got direction={final_position[2]}"

def test_simulate_multiple_cars_with_collision():
    input_lines = [
        "10 10",  # Grid dimensions: width=10, height=10
        "A",  # Car A Identifier
        "1 2 N",  # Car A Information: x=1, y=2, direction=NORTH
        "FFRFFFFRL",  # Car A Commands
        "B",  # Car B Identifier
        "7 8 W",  # Car B Information: x=7, y=8, direction=WEST
        "FFLFFFFFF",  # Car B Commands
    ]

    grid, cars = InputParser.parse_multiple_cars_input(input_lines)
    collision_strategy = SimpleCollisionStrategy()
    collision_handler = CollisionHandler(collision_strategy)
    simulator = MultiCarSimulator(grid, cars, collision_handler)
    collision = simulator.simulate()

    assert collision is not None, "Expected a collision, but none was detected."
    assert set(collision.collided_cars) == {"A", "B"}, f"Expected cars A and B to collide, but got {collision.collided_cars}."
    assert collision.position == (5, 4), f"Expected collision at (5,4), but got {collision.position}."
    assert collision.step == 7, f"Expected collision at step 7, but got {collision.step}."

def test_simulate_multiple_cars_edge_collision():
    input_lines = [
        "5 5",  # Grid dimensions: width=5, height=5
        "A",  # Car A Identifier
        "0 0 E",  # Car A Information: x=0, y=0, direction=EAST
        "FFFF",  # Car A Commands
        "B",  # Car B Identifier
        "4 0 W",  # Car B Information: x=4, y=0, direction=WEST
        "FFFF",  # Car B Commands
    ]

    grid, cars = InputParser.parse_multiple_cars_input(input_lines)
    collision_strategy = SimpleCollisionStrategy()
    collision_handler = CollisionHandler(collision_strategy)
    simulator = MultiCarSimulator(grid, cars, collision_handler)
    collision = simulator.simulate()

    assert collision is not None, "Expected a collision, but none was detected."
    assert set(collision.collided_cars) == {"A", "B"}, f"Expected cars A and B to collide, but got {collision.collided_cars}."
    assert collision.position == (2, 0), f"Expected collision at (2,0), but got {collision.position}."
    assert collision.step == 2, f"Expected collision at step 2, but got {collision.step}."
