from hangman import combine, initial
from hangman import compare_letter, compare_word


def test_compare_word():
    assert(compare_word("APPLE", "APPLE") is True)
    assert(compare_word("OVISE", "OBVIOUS") is False)


def test_compare_letter():
    assert(compare_letter("A", "APPLE") == ['A', '_', '_', '_', '_'])
    assert(compare_letter("H", "APPLE") == ['_', '_', '_', '_', '_'])
    assert(
        compare_letter("B", "OBVIOUS") ==
        ['_', 'B', '_', '_', '_', '_', '_'])


def test_combine():
    assert(
        combine(['A', '_', '_', '_', '_'], ['_', 'P', 'P', '_', '_']) ==
        ['A', 'P', 'P', '_', '_'])
    assert(
        combine(['_', '_', '_', '_', '_'], ['_', '_', '_', 'L', 'E']) ==
        ['_', '_', '_', 'L', 'E'])


def test_initial():
    assert(initial("APPLE") == ['_', '_', '_', '_', '_'])
    assert(initial("OBVIOUS") == ['_', '_', '_', '_', '_', '_', '_'])
