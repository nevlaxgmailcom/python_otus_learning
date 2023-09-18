from Rectangle import Rectangle


class Square(Rectangle):
    """Класс Square"""

    def __init__(self, side):
        super().__init__(side, side)
        self.side = side
        self.name = f'Square со стороной {self.side}'
