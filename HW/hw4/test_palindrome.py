from palindrome import is_palindrome


def test_is_palindrome():
    assert(is_palindrome("c") is False)
    assert(is_palindrome("madam Im adam") is True)
    assert(is_palindrome("RADar") is True)
