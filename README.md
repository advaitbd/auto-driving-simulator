# Auto Driving Simulator

## Overview

The Auto Driving Simulator is a Python application that simulates the movement of cars on a grid. The cars can move forward, rotate left, and rotate right based on a series of commands. The simulator supports both single-car and multi-car modes, with collision detection in the multi-car mode.

## Features

- Single Car Mode: Simulate the movement of a single car on a grid.
- Multiple Cars Mode: Simulate the movement of multiple cars on a grid with collision detection.
- Command Line Interface: Interactive input for grid size, car positions, and commands.
- Dockerized: Easily build and run the application using Docker.

## Getting Started

### Build the Docker Image

To build the Docker image, run the following command in the root directory of the project:

```sh
docker build - gic-assignment .
```

### Run the Tests

To run the tests and generate a coverage report, use the following command:

```sh
docker run -it --rm gic-assignment pytest
```

### Run the Application

To run the application, you can use the following commands:

#### Single Car Mode (Part 1)

1. Run the Docker container:

   ```sh
   docker run -it --rm gic-assignment python main.py
   ```

2. Follow the prompts to enter the grid size, car position, and commands:

   ```sh
   Select mode:
   1. Single Car
   2. Multiple Cars
   Enter mode (1 or 2): 1
   Enter grid dimensions (width height): 10 10
   Enter car position and direction (x y direction): 1 2 N
   Enter commands: FFRFFFRRLF
   ```

#### Multiple Cars Mode (Part 2)

1. Run the Docker container:

   ```sh
   docker run -it --rm gic-assignment python main.py
   ```

2. Follow the prompts to enter the grid size, car positions, and commands:

   ```sh
   Select mode:
   1. Single Car
   2. Multiple Cars
   Enter mode (1 or 2): 2
   Enter grid dimensions (width height): 10 10
   Enter car identifier (or 'done' to finish): A
   Enter position and direction for car A (x y direction): 1 2 N
   Enter commands for car A: FFRFFFFRRL
   Enter car identifier (or 'done' to finish): B
   Enter position and direction for car B (x y direction): 7 8 W
   Enter commands for car B: FFLFFFFFFF
   Enter car identifier (or 'done' to finish): done
   ```
