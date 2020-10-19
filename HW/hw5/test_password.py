from password import secure_password


def test_secure_password():
    assert(secure_password("532384Lmy@") is True)
    assert(secure_password("532384") is False)
    assert(secure_password("532384mmmy@") is True)
    assert(secure_password("532384LLY") is False)
    assert(secure_password("532384Lmy&") is False)
    assert(secure_password("kdndhbhdmy@") is False)
