from working import convert
import pytest


def test_valid_hours_without_minutes():
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"
    assert convert("7 AM to 12 PM") == "07:00 to 12:00"
    assert convert("9 PM to 9 AM") == "21:00 to 09:00"


def test_valid_hours_with_minutes():
    assert convert("9:23 AM to 3:12 PM") == "09:23 to 15:12"
    assert convert("8:50 PM to 1:10 AM") == "20:50 to 01:10"
    assert convert("1:30 PM to 8:25 PM") == "13:30 to 20:25"
    assert convert("7 AM to 6:01 PM") == "07:00 to 18:01"
    assert convert("7:30 AM to 8 PM") == "07:30 to 20:00"


def test_invalid_hours():
    with pytest.raises(ValueError):
        convert("0 AM to 2 PM")
        convert("13 AM to 8 PM")
        convert("23 AM to 24 PM")
        convert("15 PM to 1 AM")


def test_invalid_minutes():
    with pytest.raises(ValueError):
        convert("9:60 AM to 8 PM")
        convert("8:99 AM to 4 PM")
        convert("7 AM to 9:99 PM")
        convert("3 AM to 8:61 PM")


def test_invalid_time_format():
    with pytest.raises(ValueError):
        convert("9 AJ to 5 PM")
        convert("8 BC to 11 PM")
        convert("9:09 LK to 2 PM")
        convert("3 AM to 1 HJ")
        convert("6 AM to 6 PJ")

        convert("7 aM to 5:14 pM")
        convert("6:32 Pm to 9 Am")
        convert("8 AM to 4 pm")
        convert("9 am to 4:30 PM")

        convert("nine AM to five PM")
        convert("9 o'clock AM to 5 o'clock PM")


def test_invalid_conjunction():
    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
        convert("2:12 AM --> 7 PM")
        convert("4 PM -> 10:56 PM")


def test_non_hours():
    with pytest.raises(ValueError):
        convert("hello world")
        convert("my name is not David Malan")
        convert("this string is invalid")
