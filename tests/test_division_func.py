import pytest
from utils import division

@pytest.mark.parametrize()
def test_division_good():
    assert division(10,5) == 2
    assert division(20,5) == 4
    assert division(20,2) == 10
    assert division(10,-5) == -2
