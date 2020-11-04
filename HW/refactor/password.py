'''
Zengping Xu
CS 5001 Fall 2020

This program gets input from user about their password,
and validate if the password is valid or not
'''


def check_length(password):
    '''
    Function -- check_length
        check if the password meet the length requirement
    Parameters:
        password -- password
    Returns:
        a boolean
    '''
    MIN = 9
    MAX = 12
    return len(password) >= MIN and len(password) <= MAX


def check_chars(list_password, special_chars):
    '''
    Function --  check_chars
        check if the password meets at least 3 requirements
    Parameters:
        list_password -- a list, contain all password characters
        special_chars -- a set, contain all valid special characters
    Returns:
        a boolean, True means password meet at least 3 requirements,
        False means it not.
    '''
    char_requirements = 3
    uppercase = False
    lowercase = False
    is_digit = False
    is_special_char = False
    for item in list_password:
        if item.isupper() is True:
            uppercase = True
        if item.islower() is True:
            lowercase = True
        if item.isdigit() is True:
            is_digit = True
        if item in special_chars:
            is_special_char = True

    total = uppercase + lowercase + is_digit + is_special_char
    return total >= char_requirements


def check_special_chars(list_password, special_chars):
    '''
    Function -- check_special_chars
        check if the password contain other special characters
        other than $, #, @, or !
    Parameters:
        list_password -- a list, contain all password characters
        special_chars -- a set, contain all valid special characters
    Returns:
        a boolean. False means the password has other special characters,
        False means it only contain $, #, @, or !
    '''
    for item in list_password:
        if item.isdigit() is False and item.isalpha() is False and \
                item not in special_chars:
            return False
    return True


def secure_password(password):
    '''
    Function -- secure_password
        validate if a password is valid or not according to
        several checking rules.
    Parameters:
        password --  a password
    Returns:
        a boolean, True if the password meets all the
        requirements, False if it not.
    '''
    special_chars = {"$", "#", "@", "!"}
    list_password = list(password)
    length_valid = check_length(password)
    char_valid = check_chars(list_password, special_chars)
    special_valid = check_special_chars(list_password, special_chars)
    return length_valid and char_valid and special_valid
