from password import check_length, check_chars
from password import check_special_chars, secure_password


def test_check_length():
    assert(check_length("532384Lmy@"))
    assert(not check_length("532384"))
    assert(not check_length("532384mmmy@mmmmmm"))


def test_check_chars():
    assert(check_chars("532384Lmy@", {"$", "#", "@", "!"}))
    assert(not check_chars("532384LLY", {"$", "#", "@", "!"}))
    assert(not check_chars("kdndhbhdmy@", {"$", "#", "@", "!"}))


def test_check_special_chars():
    assert(check_special_chars("532384Lmy@", {"$", "#", "@", "!"}))
    assert(not check_special_chars("532384Lmy&", {"$", "#", "@", "!"}))


def test_secure_password():
    assert(secure_password("532384Lmy@") is True)
    assert(secure_password("532384") is False)
    assert(secure_password("532384mmmy@") is True)
    assert(secure_password("532384LLY") is False)
    assert(secure_password("532384Lmy&") is False)
    assert(secure_password("kdndhbhdmy@") is False)
