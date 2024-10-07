# Auto Driving Simulator

## Overview

The Auto Driving Simulator is a Python application that simulates the movement of cars on a grid. The cars can move forward, rotate left, and rotate right based on a series of commands. The simulator supports both single-car and multi-car modes, with collision detection in the multi-car mode.

## Features

- Part 1: Simulate the movement of a single car on a grid.
- Part 2: Simulate the movement of multiple cars on a grid with collision detection.
- Dockerized: Easily build and run the application using Docker.

## Design

The Auto Driving Simulator is designed using several object-oriented design principles and patterns to ensure modularity, flexibility, and maintainability. Below is a table summarizing the key classes and the design patterns they implement:

| Class/Module | Description| Design Pattern(s) Implemented |
|---|---|---|
| `Car`                                 | Represents a car with its position, direction, and commands.                | Data Class                             |
| `CollisionHandler`                    | Handles collision detection using a specified strategy.                     | Strategy Pattern                       |
| `CollisionStrategy`                   | Abstract base class for collision detection strategies.                     | Strategy Pattern                       |
| `SimpleCollisionStrategy`             | A simple implementation of collision detection strategy.                    | Strategy Pattern                       |
| `BaseCommand`                         | Abstract base class for commands that can be executed by a car.             | Command Pattern                        |
| `MoveForwardCommand`                  | Command to move the car forward.                                            | Command Pattern                        |
| `RotateLeftCommand`                   | Command to rotate the car to the left.                                      | Command Pattern                        |
| `RotateRightCommand`                  | Command to rotate the car to the right.                                     | Command Pattern                        |
| `CommandFactory`                      | Factory class to create command instances based on a given command string.  | Factory Pattern                        |
| `CollisionEvent`                      | Represents a collision event with details about the collision.              | Data Class                             |
| `Grid`                                | Represents the grid on which cars move.                                     | Data Class                             |
| `InputParser`                         | Parses input to create grid, car, and command instances.                    | -                                      |
| `MultiCarSimulator`                   | Simulates the movement of multiple cars on the grid with collision detection.| -                                      |
| `SingleCarSimulator`                  | Simulates the movement of a single car on the grid.                         | -                                      |
| `Direction`                           | Enum representing the direction of the car and provides movement utilities. | Enum, Utility Class                    |

### Design Patterns Explained

1. **Strategy Pattern**:
   - Allows the algorithm to be selected at runtime.
   - Example: `CollisionHandler` uses `CollisionStrategy` to detect collisions. `SimpleCollisionStrategy` is one implementation of this strategy.

2. **Command Pattern**:
   - Encapsulates a request as an object, thereby allowing for parameterization of clients with queues, requests, and operations.
   - Examples: `BaseCommand` and its subclasses (`MoveForwardCommand`, `RotateLeftCommand`, `RotateRightCommand`).

3. **Factory Pattern**:
   - Provides an interface for creating objects in a superclass but allows subclasses to alter the type of objects that will be created.
   - Example: `CommandFactory` creates command instances based on a given command string.

4. **Enum**:
   - Represents a fixed set of constants.
   - Example: `Direction` enum represents the four possible directions (NORTH, EAST, SOUTH, WEST).

### Class Interactions

- **Car**:
  - Holds its position, direction, and a list of commands.
  - Uses `Direction` for movement and rotation.
  - Executes commands using instances of `BaseCommand`.

- **CollisionHandler**:
  - Detects collisions using a specified `CollisionStrategy`.
  - Can be configured with different strategies like `SimpleCollisionStrategy`.

- **Simulators**:
  - `SingleCarSimulator` and `MultiCarSimulator` handle the simulation of car movements.
  - `MultiCarSimulator` also handles collision detection using `CollisionHandler`.

- **InputParser**:
  - Parses input to create instances of `Grid`, `Car`, and commands.
  - Uses `CommandFactory` to create command instances.

This design ensures that the simulator is modular, making it easy to extend and maintain. For example, new collision detection strategies can be added without modifying the existing `CollisionHandler` class. Similarly, new commands can be added by extending the `BaseCommand` class and updating the `CommandFactory`.

## Getting Started

### Build the Docker Image

To build the Docker image, run the following command in the root directory of the project:

```sh
docker build -t gic-assignment .
```

### Run the Tests

To run the tests and generate a coverage report, use the following command:

```sh
docker run -it --rm gic-assignment pytest
```

### Run the Application

To run the application, you can use the following commands:

1. Run the Docker container:

   ```sh
   docker run -it --rm gic-assignment python main.py
   ```

2. Input the grid size, car positions, and commands.

    For example, you can use the following input for Part 1 (Single Car):

    ```
    10 10
    1 2 N
    FFRFFFRRLF

    ```

    Or the following input for Part 2 (Multiple Cars):

    ```
    10 10
    A
    1 2 N
    FFRFFFFRRL
    B
    7 8 W
    FFLFFFFFFF

    ```

### Setup Locally

To set up the project locally, follow these steps:

1. Setup your virtual env and install the required packages:

   ```sh
   python3 -m venv venv
   source venv/bin/activate
   pip install -e .
   pip install -r requirements.txt
   ```

2. Run the application:

   ```sh
   python main.py
   ```
