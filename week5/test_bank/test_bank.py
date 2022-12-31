from bank import value


def test_hellos():
    assert value("hello") == 0
    assert value("Hello, Newman") == 0
    assert value("hello, david") == 0


def test_return_20():
    assert value("hey man") == 20
    assert value("Hi!") == 20
    assert value("How it's going there?") == 20


def test_return_100():
    assert value("ooi") == 100
    assert value("Good morning") == 100
    assert value("Excuse me") == 100


def test_capitalization():
    assert value("What's Up?") == 100
    assert value("How You Doing?") == 20


def test_all_upper():
    assert value("HELLO, NEWMAN") == 0
    assert value("WHAT'S UP?") == 100
