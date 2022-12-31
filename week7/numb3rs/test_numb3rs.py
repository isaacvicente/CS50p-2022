from numb3rs import validate


def test_no_periods():
    assert validate("127001") == False
    assert validate("255255255255") == False


def test_number_range():
    assert validate("255.255.255.0") == True
    assert validate("1.2.0.1000") == False
    assert validate("1.270.128.0") == False
    assert validate("275.3.6.28") == False


def test_ip_format():
    assert validate("127.0.1") == False
    assert validate("83.10.189.18.0") == False
    assert validate("255") == False
    assert validate("123.67") == False


def test_valid_ips():
    assert validate("127.0.0.1") == True
    assert validate("40.89.209.167") == True
    assert validate("103.166.118.136") == True
    assert validate("201.156.8.37") == True
    assert validate("134.124.111.241") == True


def test_invalid_ips():
    assert validate("cat") == False
    assert validate("127,0,0,1") == False
    assert validate("241.123.zero.255") == False
    assert validate("512.512.512.512") == False
