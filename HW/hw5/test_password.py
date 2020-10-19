from password import check_length, check_chars
from password import check_special_chars, secure_password


def test_check_length():
    assert(check_length("532384Lmy@") is True)
    assert(check_length("532384") is False)
    assert(check_length("532384mmmy@mmmmmm") is False)


def test_check_chars():
    assert(check_chars("532384Lmy@", {"$", "#", "@", "!"}) is True)
    assert(check_chars("532384LLY", {"$", "#", "@", "!"}) is False)
    assert(check_chars("kdndhbhdmy@", {"$", "#", "@", "!"}) is False)


def test_check_special_chars():
    assert(check_special_chars("532384Lmy@", {"$", "#", "@", "!"}) is True)
    assert(check_special_chars("532384Lmy&", {"$", "#", "@", "!"}) is False)


def test_secure_password():
    assert(secure_password("532384Lmy@") is True)
    assert(secure_password("532384") is False)
    assert(secure_password("532384mmmy@") is True)
    assert(secure_password("532384LLY") is False)
    assert(secure_password("532384Lmy&") is False)
    assert(secure_password("kdndhbhdmy@") is False)
