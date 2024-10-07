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
