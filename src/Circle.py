from Figure import Figure


class Circle(Figure):
    """Класс Circle"""

    def __init__(self, radius):
        super().__init__(radius)
        self.radius = radius
        self.__PI = 3.14
        self.name = f'Circle с радиусом {self.radius}'

    @property
    def area(self):
        return self.__PI * (self.radius ** 2)

    @property
    def perimeter(self):
        return self.__PI * (self.radius * 2)
