'''
Zengping Xu
CS 5001 Fall 2020

This program gets input from user about a string, and
determine whether the supplied string is a palindrome or not
'''


def is_palindrome(s):
    '''
    Function -- is_palindrome
        determine whether the supplied string is a palindrome
    Parameters:
        s -- the supplied string
    Returns True if the string is a palindrome or False if if not
    '''
    s = s.replace(' ', '')  # delete the space among s
    s = s.lower()  # change all letter to lowercase
    length = len(s)
    # a palindrome should have at least 2 characters,
    minumum_length = 2
    if length < minumum_length:
        return False

    pair = 2
    # calculate possible letter pairs need be compaired
    pairs = length // pair
    default = True
    i = 0
    while i <= pairs:
        if s[i] == s[length - i - 1]:
            i += 1
        else:
            default = False
            break
    return default
