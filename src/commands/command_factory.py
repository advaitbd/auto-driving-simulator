from src.commands.move_forward import MoveForwardCommand
from src.commands.rotate_left import RotateLeftCommand
from src.commands.rotate_right import RotateRightCommand

class CommandFactory:
    """
    Factory class to create command instances based on a given command string.

    This class encapsulates the logic for creating different command objects,
    making the code more modular and easier to maintain. By centralizing the
    creation logic, we adhere to the Single Responsibility Principle and
    ensure that the rest of the codebase remains decoupled from the specifics
    of command instantiation.
    """

    @staticmethod
    def create_command(command_str: str):
        """
        Create a command instance based on the provided command string.

        Args:
            command_str (str): A single character representing the command.
                               'F' for MoveForwardCommand,
                               'L' for RotateLeftCommand,
                               'R' for RotateRightCommand.

        Returns:
            BaseCommand: An instance of a command class.

        Raises:
            ValueError: If the command string is invalid.
        """
        command_mapping = {
            "F": MoveForwardCommand,
            "L": RotateLeftCommand,
            "R": RotateRightCommand,
        }
        command_class = command_mapping.get(command_str)
        if command_class:
            return command_class()
        raise ValueError(f"Invalid command: {command_str}")
