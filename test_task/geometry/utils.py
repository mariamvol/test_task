#utils.py
from .base import Shape


def compute_area(shape: Shape) -> float:
    """Полиморфный расчeт площади фигуры без знания еe типа в compile-time"""
    return shape.area()


