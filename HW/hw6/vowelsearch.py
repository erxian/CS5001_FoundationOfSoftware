'''
Zengping Xu
CS 5001 Fall 2020

This program check a given list of strings, True if
every string in the list contains a vowel, and False
otherwise.
'''


VOWEL = ("a", "e", "i", "o", "u")


def vowel_in_string(s):
    '''
    Function -- vowel_in_string
        check if string contains a vowel
    Parameters:
        s -- a string
    Retruns:
        a boolean, True if the string contains a
        vowel, False otherwise
    '''
    if len(s) == 0:
        return False
    else:
        if s[-1].lower() in VOWEL:
            return True
        else:
            return vowel_in_string(s[:-1])


def contains_vowel(lst):
    '''
    Function -- contains_vowel
        check if every string in a list contains a vowel
    Parameters:
        lst -- a list of strings
    Returns:
        a boolean, True if every string contains a vowel,
        False otherwise
    '''
    if len(lst) == 0:
        return False
    elif len(lst) == 1:
        return vowel_in_string(lst[-1])
    else:
        return vowel_in_string(lst[-1]) and contains_vowel(lst[:-1])
