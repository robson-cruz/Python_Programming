import pytest

from util import is_even


@pytest.mark.parametrize("number, result", zip(range(6), [True, False, True, False, True, False]))
def test_many(number, result):
    assert is_even(number) is result
