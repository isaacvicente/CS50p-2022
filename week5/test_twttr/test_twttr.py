from twttr import shorten


def test_all_lower():
    assert shorten("its all lower") == "ts ll lwr"
    assert shorten("this is the output") == "ths s th tpt"


def test_all_upper():
    assert shorten("NOW ITS ALL UPPER") == "NW TS LL PPR"
    assert shorten("TWITTER") == "TWTTR"


def test_all_vowels():
    assert shorten("aeiou") == ""
    assert shorten("ooaaa") == ""


def test_punctuation():
    assert (
        shorten("comma, exclamation!, question mark? and period.")
        == "cmm, xclmtn!, qstn mrk? nd prd."
    )


def test_numbers():
    assert shorten("This is CS50") == "Ths s CS50"
    assert shorten("12345") == "12345"
    assert shorten("You have 100 dolars") == "Y hv 100 dlrs"
