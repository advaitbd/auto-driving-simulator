# tests/test_grid.py

import pytest
from src.grid import Grid


def test_grid_within_bounds():
    grid = Grid(width=10, height=10)
    assert grid.is_within_bounds(0, 0) is True
    assert grid.is_within_bounds(9, 9) is True
    assert grid.is_within_bounds(10, 10) is False
    assert grid.is_within_bounds(-1, 5) is False
    assert grid.is_within_bounds(5, -1) is False


def test_grid_boundary():
    grid = Grid(width=5, height=5)
    assert grid.is_within_bounds(4, 4) is True
    assert grid.is_within_bounds(5, 5) is False
    assert grid.is_within_bounds(5, 4) is False
    assert grid.is_within_bounds(4, 5) is False
