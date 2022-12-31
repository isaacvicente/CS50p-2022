from jar import Jar
import pytest


def test_valid_init():
    Jar()
    Jar(1)
    Jar(100)
    Jar(50)
    Jar(2)


def test_invalid_init():
    with pytest.raises(ValueError):
        Jar(-1)
        Jar("foo")
        Jar(3.14)
        Jar(True)
        Jar([12])


def test_size():
    jar = Jar()
    jar.size = 1
    jar.size = 10
    jar.size = 12  # The default capacity is 12

    with pytest.raises(ValueError):
        jar.size = 13  # Excedes the capacity
        jar.size = True
        jar.size = "one"
        jar.size = 0.5
        jar.size = [5]


def test_deposit():
    jar = Jar()
    jar.deposit(1)
    jar.deposit(2)
    jar.deposit(5)

    with pytest.raises(ValueError):
        jar.deposit(jar.capacity + 1)  # Excedes the capacity
        jar.deposit(-1)
        jar.deposit("bar")
        jar.deposit(True)
        jar.deposit({"cookie": 1})
        jar.deposit("🍪")


def test_withdraw():
    jar = Jar()
    jar.deposit(10)
    jar.withdraw(3)
    jar.withdraw(6)

    with pytest.raises(ValueError):
        jar.withdraw(4)  # Theres only one cookie in the jar
        jar.withdraw(-1)
        jar.withdraw("foobar")
        jar.withdraw(False)
        jar.withdraw("🍪")


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    jar.withdraw(2)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"
    jar.withdraw(7)
    assert str(jar) == "🍪🍪🍪"
