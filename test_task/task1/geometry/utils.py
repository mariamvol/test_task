#utils.py
from .base import Shape


def compute_area(shape: Shape) -> float:
    """Полиморфный расчёт площади фигуры без знания её типа в compile-time."""
    return shape.area()

