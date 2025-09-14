# circle.py
import math
from .base import Shape


class Circle(Shape):
    def __init__(self, radius: float):
        if radius <= 0 or math.isinf(radius) or math.isnan(radius):
            raise ValueError("Radius must be a positive finite number")
        self.radius = radius

    def area(self) -> float:
        return math.pi * self.radius ** 2

    def __repr__(self):
        return f"Circle(r={self.radius})"
