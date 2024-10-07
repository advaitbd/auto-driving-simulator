# src/utils/direction_utils.py

from enum import Enum, auto

class Direction(Enum):
    NORTH = auto()
    EAST = auto()
    SOUTH = auto()
    WEST = auto()

    @staticmethod
    def from_string(direction_str: str):
        """
        Converts a string representation of a direction to a Direction enum.

        Args:
            direction_str (str): The string representation of the direction (e.g., 'N', 'E', 'S', 'W').

        Returns:
            Direction: The corresponding Direction enum value.
        """
        mapping = {
            "N": Direction.NORTH,
            "E": Direction.EAST,
            "S": Direction.SOUTH,
            "W": Direction.WEST,
        }
        return mapping.get(direction_str.upper())

    def to_string(self) -> str:
        """
        Converts a Direction enum to its string representation.

        Returns:
            str: The string representation of the direction (e.g., 'N', 'E', 'S', 'W').
        """
        mapping = {
            Direction.NORTH: "N",
            Direction.EAST: "E",
            Direction.SOUTH: "S",
            Direction.WEST: "W",
        }
        return mapping[self]

    def move_forward(self, x: int, y: int) -> tuple:
        """
        Moves the position forward in the current direction.

        Args:
            x (int): The current x-coordinate.
            y (int): The current y-coordinate.

        Returns:
            tuple: The new (x, y) position after moving forward.
        """
        if self == Direction.NORTH:
            return x, y + 1
        elif self == Direction.EAST:
            return x + 1, y
        elif self == Direction.SOUTH:
            return x, y - 1
        elif self == Direction.WEST:
            return x - 1, y

    def _rotate(self, rotation_order):
        """
        Rotates the direction based on the given rotation order.

        Args:
            rotation_order (list): The list of directions in the order of rotation.

        Returns:
            Direction: The new direction after rotation.
        """
        current_index = rotation_order.index(self)
        return rotation_order[(current_index + 1) % 4]

    def rotate_left(self):
        """
        Rotates the direction 90 degrees to the left.

        Returns:
            Direction: The new direction after rotating left.
        """
        return self._rotate([Direction.NORTH, Direction.WEST, Direction.SOUTH, Direction.EAST])

    def rotate_right(self):
        """
        Rotates the direction 90 degrees to the right.

        Returns:
            Direction: The new direction after rotating right.
        """
        return self._rotate([Direction.NORTH, Direction.EAST, Direction.SOUTH, Direction.WEST])
