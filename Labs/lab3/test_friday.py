from friday import greeting, day_convert_digit, count

def test_greeting():
    assert(greeting('evelyn') == "Hello, evelyn")
    assert(greeting('joseph') == "Hello, joseph")


def test_day_convert_digit():
    assert(day_convert_digit('M') == 2)
    assert(day_convert_digit('Su') == 1)
    assert(day_convert_digit('W') == 4)


def test_count():
    assert(count('M') == 4)
    assert(count('Su') == 5)
    assert(count('W') == 2)