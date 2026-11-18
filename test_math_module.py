import pytest

from math_module import factorial


@pytest.mark.parametrize("n, expected", [
    (0, 1), (1, 1), (2, 2), (5, 120), (10, 3628800),
])
def test_factorial_values(n, expected):
    assert factorial(n) == expected


def test_negative_integer():
    with pytest.raises(ValueError):
        factorial(-1)


@pytest.mark.parametrize("value", [2.5, "5", True])
def test_invalid_type(value):
    with pytest.raises(TypeError):
        factorial(value)
