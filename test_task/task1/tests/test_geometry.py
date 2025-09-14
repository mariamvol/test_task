import math
import pytest
from geometry.circle import Circle
from geometry.triangle import Triangle
from geometry.utils import compute_area


def test_circle_area():
    c = Circle(2)
    assert math.isclose(c.area(), 4 * math.pi, rel_tol=1e-12)


@pytest.mark.parametrize("r", [0, -1, float("inf"), float("nan")])
def test_circle_invalid(r):
    with pytest.raises(ValueError):
        Circle(r)


def test_triangle_area_345():
    t = Triangle(3, 4, 5)
    assert math.isclose(t.area(), 6.0, rel_tol=1e-12)


def test_triangle_invalid():
    with pytest.raises(ValueError):
        Triangle(1, 2, 3)  # нарушение неравенства
    with pytest.raises(ValueError):
        Triangle(0, 1, 1)


def test_triangle_right_angle():
    t = Triangle(3, 4, 5)
    assert t.is_right()
    t2 = Triangle(2, 3, 4)
    assert not t2.is_right()


def test_polymorphism():
    shapes = [Circle(1), Triangle(3, 4, 5)]
    total = sum(compute_area(s) for s in shapes)
    assert math.isclose(total, math.pi + 6.0, rel_tol=1e-12)
