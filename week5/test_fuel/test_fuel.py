from fuel import gauge, convert
import pytest


def test_not_integers():
    with pytest.raises(ValueError):
        convert("cat/dog")
        convert("me/you")
        convert("x/y")


def test_wrong_fraction():
    with pytest.raises(ValueError):
        convert("4/3")
        convert("2/1")
        convert("101/100")


def test_convert():
    assert convert("1/4") == 25
    assert convert("1/3") == 33
    assert convert("1/100") == 1
    assert convert("1/2") == 50
    assert convert("3/4") == 75


def test_zero_div_error():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
        convert("42/0")
        convert("100/0")


def test_full_gauge():
    assert gauge(99) == "F"
    assert gauge(100) == "F"


def test_empty_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"


def test_gauge():
    assert gauge(50) == "50%"
    assert gauge(42) == "42%"
    assert gauge(10) == "10%"
