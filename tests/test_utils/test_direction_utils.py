# tests/test_utils/test_direction_utils.py

import pytest
from src.utils.direction_utils import Direction


def test_direction_from_string():
    assert Direction.from_string("N") == Direction.NORTH
    assert Direction.from_string("E") == Direction.EAST
    assert Direction.from_string("S") == Direction.SOUTH
    assert Direction.from_string("W") == Direction.WEST
    assert Direction.from_string("n") == Direction.NORTH
    assert Direction.from_string("invalid") is None


def test_direction_to_string():
    assert Direction.NORTH.to_string() == "N"
    assert Direction.EAST.to_string() == "E"
    assert Direction.SOUTH.to_string() == "S"
    assert Direction.WEST.to_string() == "W"


def test_direction_move_forward():
    assert Direction.NORTH.move_forward(1, 1) == (1, 2)
    assert Direction.EAST.move_forward(1, 1) == (2, 1)
    assert Direction.SOUTH.move_forward(1, 1) == (1, 0)
    assert Direction.WEST.move_forward(1, 1) == (0, 1)


def test_direction_rotate_left():
    assert Direction.NORTH.rotate_left() == Direction.WEST
    assert Direction.WEST.rotate_left() == Direction.SOUTH
    assert Direction.SOUTH.rotate_left() == Direction.EAST
    assert Direction.EAST.rotate_left() == Direction.NORTH


def test_direction_rotate_right():
    assert Direction.NORTH.rotate_right() == Direction.EAST
    assert Direction.EAST.rotate_right() == Direction.SOUTH
    assert Direction.SOUTH.rotate_right() == Direction.WEST
    assert Direction.WEST.rotate_right() == Direction.NORTH
