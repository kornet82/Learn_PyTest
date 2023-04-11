import pytest
from my_funcs.utils import division

@pytest.mark.parametrize("a, b, expected_result", [(10, 5, 2),
                                                   (10, -2, -5),
                                                   (30, -3, -10),
                                                   (5, 2, 2.5)])
def test_division_good(a, b, expected_result):
    assert division(a, b) == expected_result

@pytest.mark.parametrize("expected_exeption, divider, div", [(ZeroDivisionError, 0, 10),
                                                   (TypeError,"abc", 10)])
def test_type_error(expected_exeption, divider, div):
    with pytest.raises(expected_exeption):
        division(div, divider)



