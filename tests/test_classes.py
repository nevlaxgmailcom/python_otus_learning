from src.Rectangle import Rectangle
from src.Square import Square
from src.Circle import Circle
from src.Triangle import Triangle
import pytest


@pytest.mark.parametrize(("radius", "area", "perimeter"),
                         [(1, 3.14, 6.28),
                          (1.5, 7.065, 9.42)
                          ])
def test_circle(radius, area, perimeter):
    """Проверка вычисления площади, периметра фигуры Circle"""

    c = Circle(radius)
    assert c.name == f'Circle с радиусом {radius}'
    assert c.area == area
    assert c.perimeter == perimeter


@pytest.mark.parametrize("radius",
                         [-1, 0, '-1', [0]
                          ])
def test_circle_negative(radius):
    """Проверка исключения при невозможности создания фигуры Circle"""

    with pytest.raises(ValueError) as e:
        c = Circle(radius)
        assert c.name == f'Circle с радиусом {radius}'
    assert f'Circle создать нельзя' == str(e.value)


@pytest.mark.parametrize(("side_a", "side_b", "area", "perimeter"),
                         [(1, 2, 2, 6),
                          (1.5, 2.5, 3.75, 8)
                          ])
def test_rectangle(side_a, side_b, area, perimeter):
    """Проверка вычисления площади, периметра фигуры Rectangle"""

    r = Rectangle(side_a, side_b)
    assert r.name == f'Rectangle со сторонами {side_a} и {side_b}'
    assert r.area == area
    assert r.perimeter == perimeter


@pytest.mark.parametrize(("side_a", "side_b"),
                         [(-1, -2),
                          (0, 0),
                          ('0', {"side_b": 0})
                          ])
def test_rectangle_negative(side_a, side_b):
    """Проверка исключения при невозможности создания фигуры Rectangle"""

    with pytest.raises(ValueError) as e:
        r = Rectangle(side_a, side_b)
        assert r.name == f'Rectangle со сторонами {side_a} и {side_b}'
    assert f'Rectangle создать нельзя' == str(e.value)


@pytest.mark.parametrize(("side", "area", "perimeter"),
                         [(1, 1, 4),
                          (1.5, 2.25, 6)
                          ])
def test_square(side, area, perimeter):
    """Проверка вычисления площади, периметра фигуры Square"""

    s = Square(side)
    assert s.name == f'Square со стороной {side}'
    assert s.area == area
    assert s.perimeter == perimeter


@pytest.mark.parametrize("side",
                         [-1, 0, '12', [1, 2]
                          ])
def test_square_negative(side):
    """Проверка исключения при невозможности создания фигуры Square"""

    with pytest.raises(ValueError) as e:
        s = Square(side)
        assert s.name == f'Square со стороной {side}'
    assert f'Square создать нельзя' == str(e.value)


@pytest.mark.parametrize(("side_a", "side_b", "side_c", "area", "perimeter"),
                         [(1, 2, 2, 0.9682458365518543, 5),
                          (1.5, 2.5, 3.75, 1.257691182037546, 7.75)
                          ])
def test_triangle(side_a, side_b, side_c, area, perimeter):
    """Проверка вычисления площади, периметра фигуры Triangle"""

    t = Triangle(side_a, side_b, side_c)
    assert t.name == f'Triangle со сторонами ' \
                     f'{side_a}, {side_b}, {side_c}'
    assert t.area == area
    assert t.perimeter == perimeter


@pytest.mark.parametrize(("side_a", "side_b", "side_c"),
                         [(-1, -2, -2),
                          (0, 0, 0),
                          (1, 2, 3),
                          ('1', [2], 3)
                          ])
def test_triangle_negative(side_a, side_b, side_c):
    """Проверка исключения при невозможности создания фигуры Triangle"""

    with pytest.raises(ValueError) as e:
        t = Triangle(side_a, side_b, side_c)
        assert t.name == f'Triangle со сторонами ' \
                         f'{side_a}, {side_b}, {side_c}'
    assert f'Triangle создать нельзя' == str(e.value)


@pytest.mark.parametrize(("fig_a", "fig_b", "result"),
                         [(Circle(2), Rectangle(2, 5), 22.560000000000002),
                          (Rectangle(2, 5), Square(5), 35),
                          (Square(5), Triangle(1, 2, 2.5), 25.949917759598165),
                          (Triangle(1, 2, 2.5), Circle(2), 13.509917759598167)
                          ])
def test_add_area(fig_a, fig_b, result):
    """Проверка вычисления суммы площадей двух геометрических фигур"""

    a = fig_a
    b = fig_b
    assert a.add_area(b) == result


@pytest.mark.parametrize(("fig_a", "fig_b"),
                         [(Circle(2), 25),
                          (Rectangle(2, 5), 's'),
                          (Square(5), [15]),
                          (Triangle(1, 2, 2.5), {"c": 15})
                          ])
def test_add_area_negative(fig_a, fig_b):
    """Проверка исключения вычисления суммы площадей двух фигур, если передана не фигура"""

    with pytest.raises(ValueError) as e:
        a = fig_a
        b = fig_b
        assert a.add_area(b)
    assert f'Передана не геометрическая фигура' == str(e.value)
