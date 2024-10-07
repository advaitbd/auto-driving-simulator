# src/main.py

from src.parsers.input_parser import InputParser
from src.simulator.single_car_simulator import SingleCarSimulator
from src.simulator.multi_car_simulator import MultiCarSimulator
from src.collision_handler import CollisionHandler
from src.collision_strategies.simple_collision_strategy import SimpleCollisionStrategy

def main():
    input_lines = []
    print("Enter input (end with an empty line):")
    while True:
        line = input().strip()
        if line == "":
            break
        input_lines.append(line)

    try:
        if len(input_lines) == 3:
            # Single Car Mode
            grid, car, commands = InputParser.parse_single_car_input(input_lines)
            simulator = SingleCarSimulator(grid, car)
            final_position = simulator.simulate()
            print(f"{final_position[0]} {final_position[1]} {final_position[2]}")
        else:
            # Multiple Cars Mode
            grid, cars = InputParser.parse_multiple_cars_input(input_lines)
            collision_strategy = SimpleCollisionStrategy()
            collision_handler = CollisionHandler(collision_strategy)
            simulator = MultiCarSimulator(grid, cars, collision_handler)
            collision_event = simulator.simulate()

            if collision_event:
                collided_cars = " ".join(collision_event.collided_cars)
                print(f"{collided_cars}")
                print(f"{collision_event.position[0]} {collision_event.position[1]}")
                print(f"{collision_event.step}")
            else:
                # for car in cars:
                #     print(f"{car.x} {car.y}")
                print("no collision")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
