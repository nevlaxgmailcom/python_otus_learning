from abc import ABC, abstractmethod


class Figure(ABC):
    """Базовый класс Figure геометрических фигур"""

    def __init__(self, *args):
        if [side for side in args if not isinstance(side, (int, float)) or side <= 0]:
            raise ValueError(f'{self.__class__.__name__} создать нельзя')
        if len(args) > 1:
            self.perimeter = sum(args)

    @property
    @abstractmethod
    def area(self):
        pass

    def add_area(self, figure):
        if not isinstance(figure, Figure):
            raise ValueError("Передана не геометрическая фигура")
        return self.area + figure.area
