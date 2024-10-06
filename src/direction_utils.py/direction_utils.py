# src/utils/direction_utils.py

from enum import Enum, auto

class Direction(Enum):
    NORTH = auto()
    EAST = auto()
    SOUTH = auto()
    WEST = auto()

    @staticmethod
    def from_string(direction_str: str):
        mapping = {
            "N": Direction.NORTH,
            "E": Direction.EAST,
            "S": Direction.SOUTH,
            "W": Direction.WEST,
        }
        return mapping.get(direction_str.upper())

    def to_string(self) -> str:
        mapping = {
            Direction.NORTH: "N",
            Direction.EAST: "E",
            Direction.SOUTH: "S",
            Direction.WEST: "W",
        }
        return mapping[self]

    def move_forward(self, x: int, y: int) -> tuple:
        if self == Direction.NORTH:
            return x, y + 1
        elif self == Direction.EAST:
            return x + 1, y
        elif self == Direction.SOUTH:
            return x, y - 1
        elif self == Direction.WEST:
            return x - 1, y

    def _rotate(self, rotation_order):
        current_index = rotation_order.index(self)
        return rotation_order[(current_index + 1) % 4]

    def rotate_left(self):
        return self._rotate([Direction.NORTH, Direction.WEST, Direction.SOUTH, Direction.EAST])

    def rotate_right(self):
        return self._rotate([Direction.NORTH, Direction.EAST, Direction.SOUTH, Direction.WEST])
