import pytest

from util import is_even


@pytest.mark.parametrize("number, result", [
    (0, True),
    (1, False),
    (2, True),
    (3, False),
    (4, True),
    (5, False)
])
def test_many(number, result):
    assert is_even(number) is result


def test_exception():
    with pytest.raises(TypeError) as e:
        is_even("abc")
        assert e.value.args[0] == "Invalid input type, only integers allowed."
