# src/commands/base_command.py

from abc import ABC, abstractmethod
from src.grid import Grid


class BaseCommand(ABC):
    @abstractmethod
    def execute(self, car, grid: Grid):
        pass

    def __eq__(self, other):
        """Compare commands based on their class types and attributes."""
        return isinstance(other, self.__class__)
