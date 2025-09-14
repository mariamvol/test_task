#triangle.py
import math
from .base import Shape


class Triangle(Shape):
    def __init__(self, a: float, b: float, c: float):
        for side in (a, b, c):
            if side <= 0 or math.isinf(side) or math.isnan(side):
                raise ValueError("All sides must be positive finite numbers")

        if a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Triangle inequality violated")

        self.a, self.b, self.c = a, b, c

    def area(self) -> float:
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right(self, eps: float = 1e-9) -> bool:
        sides = sorted([self.a, self.b, self.c])
        lhs = sides[0] ** 2 + sides[1] ** 2
        rhs = sides[2] ** 2
        tol = max(eps * rhs, eps)
        return abs(lhs - rhs) <= tol

    def __repr__(self):
        return f"Triangle({self.a}, {self.b}, {self.c})"
