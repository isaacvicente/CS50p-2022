from response import validate_email


def test_valid_emails():
    assert validate_email("malan@harvard.edu") == "Valid"
    assert validate_email("abc@example.co.uk") == "Valid"
    assert validate_email("disposable.style.email.with+symbol@example.com") == "Valid"
    assert validate_email("other.email-with-hyphen@example.com") == "Valid"
    assert validate_email("example-indeed@strange-example.com") == "Valid"
    assert validate_email("simple@example.com") == "Valid"


def test_invalid_emails():
    assert validate_email("email.example.com") == "Invalid"
    assert validate_email(".email@example.com") == "Invalid"
    assert validate_email("email@-example.com") == "Invalid"
    assert validate_email("email@example..com") == "Invalid"
    assert validate_email("@example.com") == "Invalid"
    assert validate_email("Abc..123@example.com") == "Invalid"
