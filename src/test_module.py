from src.utils import add


def test_assert():
    assert True


def test_two_plus_two_is_four():
    assert add(2, 2) == 4
