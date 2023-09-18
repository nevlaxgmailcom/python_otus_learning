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
    c = Circle(radius)
    assert c.name == f'Circle с радиусом {radius}'
    assert c.area == area
    assert c.perimeter == perimeter


@pytest.mark.parametrize("radius",
                         [-1, 0, '-1', [0]
                          ])
def test_circle_negative(radius):
    with pytest.raises(ValueError) as e:
        c = Circle(radius)
        assert c.name == f'Circle с радиусом {radius}'
    assert f'Circle создать нельзя' == str(e.value)


@pytest.mark.parametrize(("side_a", "side_b", "area", "perimeter"),
                         [(1, 2, 2, 6),
                          (1.5, 2.5, 3.75, 8)
                          ])
def test_rectangle(side_a, side_b, area, perimeter):
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
    with pytest.raises(ValueError) as e:
        r = Rectangle(side_a, side_b)
        assert r.name == f'Rectangle со сторонами {side_a} и {side_b}'
    assert f'Rectangle создать нельзя' == str(e.value)


@pytest.mark.parametrize(("side", "area", "perimeter"),
                         [(1, 1, 4),
                          (1.5, 2.25, 6)
                          ])
def test_square(side, area, perimeter):
    s = Square(side)
    assert s.name == f'Square со стороной {side}'
    assert s.area == area
    assert s.perimeter == perimeter


@pytest.mark.parametrize("side",
                         [-1, 0, '12', [1, 2]
                          ])
def test_square_negative(side):
    with pytest.raises(ValueError) as e:
        s = Square(side)
        assert s.name == f'Square со стороной {side}'
    assert f'Square создать нельзя' == str(e.value)


@pytest.mark.parametrize(("side_a", "side_b", "side_c", "area", "perimeter"),
                         [(1, 2, 2, 0.9682458365518543, 5),
                          (1.5, 2.5, 3.75, 1.257691182037546, 7.75)
                          ])
def test_triangle(side_a, side_b, side_c, area, perimeter):
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
    with pytest.raises(ValueError) as e:
        t = Triangle(side_a, side_b, side_c)
        assert t.name == f'Triangle со сторонами ' \
                         f'{side_a}, {side_b}, {side_c}'
    assert f'Triangle создать нельзя' == str(e.value)


def test_add_area():
    c = Circle(2)
    r = Rectangle(2, 5)
    s = Square(5)
    t = Triangle(1, 2, 2.5)
    assert c.add_area(r) == 22.560000000000002
    assert r.add_area(s) == 35
    assert s.add_area(t) == 25.949917759598165
    assert t.add_area(c) == 13.509917759598167


def test_add_area_negative():
    with pytest.raises(ValueError) as e:
        c = Circle(2)
        r = Rectangle(2, 5)
        s = Square(5)
        t = Triangle(1, 2, 2.5)
        assert c.add_area(25) == 22.560000000000002
        assert r.add_area('s') == 35
        assert s.add_area([t]) == 25.949917759598165
        assert t.add_area({c}) == 13.509917759598167
    assert f'Передана не геометрическая фигура' == str(e.value)
