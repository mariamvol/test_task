# geometry/base.py
from abc import ABC, abstractmethod

class Shape(ABC):
    """Базовый интерфейс для всех фигур"""

    @abstractmethod
    def area(self) -> float:
        """Вычислить площадь фигуры"""
        pass
