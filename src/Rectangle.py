from Figure import Figure


class Rectangle(Figure):
    """Класс Rectangle"""

    def __init__(self, side_a, side_b):
        super().__init__(side_a, side_b, side_a, side_b)
        self.side_a = side_a
        self.side_b = side_b
        self.name = f'Rectangle со сторонами {self.side_a} и {self.side_b}'

    @property
    def area(self):
        return self.side_b * self.side_a
