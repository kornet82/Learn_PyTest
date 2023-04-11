import pytest
from utils import division

@pytest.mark.parametrize("a, b, expected_result", [(10, 5, 2),
                                                   (10, -2, -5),
                                                   (30, -3, -10),
                                                   (5, 2, 2.5)])
def test_division_good(a, b, expected_result):
    assert division(a, b) == expected_result

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        division(10,0)


def test_type_error():
    with pytest.raises(TypeError):
        division(10, 'abc')
