# src/main.py

from src.parsers.input_parser import InputParser
from src.simulator.single_car_simulator import SingleCarSimulator
from src.simulator.multi_car_simulator import MultiCarSimulator
from src.collision_handler import CollisionHandler
from src.collision_strategies.simple_collision_strategy import SimpleCollisionStrategy

def main():
    print("Select mode:")
    print("1. Single Car")
    print("2. Multiple Cars")
    mode = input("Enter mode (1 or 2): ").strip()

    try:
        if mode == "1":
            print("Enter grid dimensions (width height):")
            grid_line = input().strip()
            print("Enter car position and direction (x y direction):")
            car_line = input().strip()
            print("Enter commands:")
            commands_line = input().strip()

            input_lines = [grid_line, car_line, commands_line]
            grid, car, commands = InputParser.parse_single_car_input(input_lines)
            simulator = SingleCarSimulator(grid, car)
            final_position = simulator.simulate()
            print(f"Final position: {final_position}")

        elif mode == "2":
            print("Enter grid dimensions (width height):")
            grid_line = input().strip()
            input_lines = [grid_line]

            while True:
                print("Enter car identifier (or 'done' to finish):")
                identifier = input().strip()
                if identifier.lower() == 'done':
                    break
                print(f"Enter position and direction for car {identifier} (x y direction):")
                car_line = input().strip()
                print(f"Enter commands for car {identifier}:")
                commands_line = input().strip()

                input_lines.extend([identifier, car_line, commands_line])

            # InputParser will parse the input lines and return the initialised grid and a list of cars
            grid, cars = InputParser.parse_multiple_cars_input(input_lines)

            # We will use the SimpleCollisionStrategy for this example, but we can use different strategies too
            # While SimpleCollisionStrategy just stops the cars, we can implement a different strategy to handle collisions

            collision_strategy = SimpleCollisionStrategy()
            collision_handler = CollisionHandler(collision_strategy)

            simulator = MultiCarSimulator(grid, cars, collision_handler)

            collision_event = simulator.simulate()
            if collision_event:
                print(f"Collision detected: {collision_event}")
            else:
                print("No collision detected")
        else:
            print("Invalid mode. Please choose '1' or '2'.")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
