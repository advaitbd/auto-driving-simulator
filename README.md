# Auto Driving Car Simulation

## Overview

This project simulates the movement of self-driving cars on a rectangular grid. It supports both single-car and multiple-car simulations, including collision detection. The enhanced implementation introduces further modularization, utilizing design patterns such as the Command Pattern and an event-driven architecture to improve scalability and maintainability.

## Setup Instructions

### Installation

1. **Create a Virtual Environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. **Install the Required Packages**

   ```bash
   pip install -e .
   pip install -r requirements.txt
   ```

3. **Running the Tests**

    ```bash
    pytest
    ```
