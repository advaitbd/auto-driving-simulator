# src/main.py

from src.parsers.input_parser import InputParser
from src.simulator.single_car_simulator import SingleCarSimulator
from src.simulator.multi_car_simulator import MultiCarSimulator
from src.collision_handler import CollisionHandler
from src.collision_strategies.simple_collision_strategy import SimpleCollisionStrategy

def main():
    input_lines = []
    print("Enter input (end with an empty line):")

    # Read input lines until an empty line is encountered
    while True:
        line = input().strip()
        if line == "":
            break
        input_lines.append(line)

    try:
        if len(input_lines) == 3:
            # Single Car Mode
            # Parse the input for single car simulation
            grid, car, commands = InputParser.parse_single_car_input(input_lines)
            # Initialize the single car simulator
            simulator = SingleCarSimulator(grid, car)
            # Run the simulation and get the final position of the car
            final_position = simulator.simulate()
            # Print the final position of the car
            print(f"{final_position[0]} {final_position[1]} {final_position[2]}")

        else:
            # Multiple Cars Mode
            # Parse the input for multiple cars simulation
            grid, cars = InputParser.parse_multiple_cars_input(input_lines)
            # Initialize the collision strategy and handler
            collision_strategy = SimpleCollisionStrategy()
            collision_handler = CollisionHandler(collision_strategy)
            # Initialize the multiple cars simulator
            simulator = MultiCarSimulator(grid, cars, collision_handler)
            # Run the simulation and check for collision events
            collision_event = simulator.simulate()

            if collision_event:
                # If a collision occurred, print the details
                collided_cars = " ".join(collision_event.collided_cars)
                print(f"{collided_cars}")
                print(f"{collision_event.position[0]} {collision_event.position[1]}")
                print(f"{collision_event.step}")
            else:
                # If no collision occurred, print "no collision"
                print("no collision")

    except ValueError as e:
        # Handle any value errors that occur during parsing or simulation
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
