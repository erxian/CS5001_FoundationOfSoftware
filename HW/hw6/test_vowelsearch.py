from vowelsearch import vowel_in_string
from vowelsearch import contains_vowel


def test_vowel_in_string():
    assert(vowel_in_string("") is False)
    assert(vowel_in_string("garge") is True)
    assert(vowel_in_string("ffff") is False)
    assert(vowel_in_string("12345") is False)
    assert(vowel_in_string("!ABC") is True)


def test_contains_vowel():
    assert(contains_vowel([]) is False)
    assert(contains_vowel(["garge", "him", "And"]) is True)
    assert(contains_vowel(["ffff", "this", "and"]) is False)
