from plates import is_valid


def test_two_letters_start():
    assert is_valid("50") == False
    assert is_valid("A1CS25") == False
    assert is_valid("1ABC") == False
    assert is_valid("H3Y") == False


def test_minimum_chars():
    assert is_valid("A") == False
    assert is_valid("5") == False
    assert is_valid("CS") == True


def test_maximum_chars():
    # Seven chars long
    assert is_valid("ABCDEFG") == False
    # Six chars long
    assert is_valid("ABCDEF") == True
    assert is_valid("morethanseven") == False


def test_numbers_not_in_middle():
    assert is_valid("AA22A") == False
    assert is_valid("ABC12DE") == False
    assert is_valid("CS50P") == False


def test_first_number_not_zero():
    assert is_valid("ABC012") == False
    assert is_valid("CS050") == False
    assert is_valid("David01") == False


def test_no_punctuation():
    assert is_valid("CS 50") == False
    assert is_valid("Hi!") == False
    assert is_valid("Really?") == False
    assert is_valid("PI3.14") == False
