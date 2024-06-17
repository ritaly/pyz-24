import pytest
from .fields import rectangle, triangle, trapezoid

@pytest.fixture
def sides():
    """return side A & B """
    return 10, 50


def test_rectangle_with_correct_values(sides):
    a, b = sides
    result = rectangle(a, b)
    assert result == 500


def test_rectangle_with_incorrect_values():
    a, b = 5, 'b'
    with pytest.raises(ValueError, match="Wartość musi być numeryczna!"):
        rectangle(a, b)


def test_triangle_with_correct_values(sides):
    a, b = sides
    result = triangle(a, b)
    assert result == 250


def test_trapezoit_with_correct_values(sides):
    a, b = sides
    result = trapezoid(a, b, 5)
    assert result == 150
