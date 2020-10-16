from convert import convert_to_decimal


def test_convert_to_decimal():
    assert(convert_to_decimal("1101") == 13)
    assert(convert_to_decimal("101101101") == 365)