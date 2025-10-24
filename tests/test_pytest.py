import pytest


def test_first_try():
    print("Hello, World!")


class TestUserLogin:
    def test_1(self):
        ...

    def test_2(self):
        ...


def test_assert_positive_case():
    assert (2 + 2) == 4
    assert (2 + 4) == 6
    assert (2 + 6) == 8


def test_assert_negative_case():
    assert (2 + 2) == 5, "(2 + 2) != 5"


def test_greeting():
    greeting = "Hello, world!"
    assert greeting == "Hi, world!"


def test_equal():
    assert 1 == 1


def test_in_list():
    assert 3 in [1, 2, 3, 4]


def test_boolean():
    is_authenticated = True
    assert is_authenticated


def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0
