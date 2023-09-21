from Figure import Figure


class Triangle(Figure):
    """Класс Triangle"""

    def __init__(self, side_a, side_b, side_c):
        super().__init__(side_a, side_b, side_c)
        if side_a + side_b <= side_c or side_a + side_c <= side_b or side_b + side_c <= side_a:
            raise ValueError(f'Triangle создать нельзя')
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.name = f'Triangle со сторонами ' \
                    f'{self.side_a}, {self.side_b}, {self.side_c}'

    @property
    def area(self):
        p = self.perimeter / 2
        return (p
                * (p - self.side_a)
                * (p - self.side_b)
                * (p - self.side_c)
                ) ** 0.5
