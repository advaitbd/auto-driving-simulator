# src/grid.py

from dataclasses import dataclass


@dataclass(frozen=True)
class Grid:
    width: int
    height: int

    def __post_init__(self):
        """
        Post-initialization to validate the grid dimensions.

        Raises:
            ValueError: If either width or height is less than or equal to zero.
        """
        if self.width <= 0 or self.height <= 0:
            raise ValueError("Width and height must be greater than 0.")

    def is_within_bounds(self, x: int, y: int) -> bool:
        """
        Checks if the (x, y) position is within the grid boundaries.

        Args:
            x (int): The x-coordinate to check.
            y (int): The y-coordinate to check.

        Returns:
            bool: True if the position (x, y) is within the grid boundaries, False otherwise.
        """
        return 0 <= x < self.width and 0 <= y < self.height
