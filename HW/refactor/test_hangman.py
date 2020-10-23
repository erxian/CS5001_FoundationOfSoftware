from hangman import letter_in_word
from hangman import compare_word, already_guessed


def test_letter_in_word():
    assert(letter_in_word("A", "APPLE") is True)
    assert(letter_in_word("M", "APPLE") is False)


def test_compare_word():
    assert(compare_word("APPLE", "APPLE") is True)
    assert(compare_word("APPLY", "APPLE") is False)


def test_already_guessed():
    assert(already_guessed("A", "APO") is True)
    assert(already_guessed("E", "APO") is False)
