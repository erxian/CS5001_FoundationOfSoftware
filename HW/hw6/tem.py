    assert(vowel_in_string("garge") is True)
    assert(vowel_in_string("ffff") is False)
    assert(vowel_in_string("12345") is False)
    assert(vowel_in_string("!abc") is True)



def test_contains_vowel():
    assert(contains_vowel([]) is False)
    assert(contains_vowel(["garge", "him", "and"]) is True)
    assert(contains_vowel(["ffff", "this", "and"]) is False)