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
    a = s[0] #the first letter of string s
    b = s[-1] #the last letter of string s
    l = len(s)
    minimum_charactor = 2
    while a == b and l >= minimum_charactor:
        return True
    return False


#result = is_palindrome("rr")
#print(result)
