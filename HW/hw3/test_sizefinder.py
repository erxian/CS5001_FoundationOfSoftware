from sizefinder import size_calculate, check_valid


def test_size_calculate():
    assert(size_calculate(32.5, 26, 2) == "XL")
    assert(size_calculate(32.5, 30, 2) == "M")
    assert(size_calculate(41.2, 34, 3) == "L")


def test_check_valid():
    assert(check_valid(32.5, 26, 36) is True)
    assert(check_valid(32.5, 30, 42) is True)
    assert(check_valid(32.5, 34, 52) is False)
