'''
Zengping
CS 5001 Fall 2020

This program will convert binary digit to decimal digit
'''


def convert_to_decimal(binary_digit):
    '''
    Function -- convert_to_decimal
        convert a binary digit to a decimal digit
    Parameters:
        binary_digit -- a binary
    Returns an integer

    '''
    if len(binary_digit) == 1:
        return int(binary_digit)
    else:
        decimal = int(binary_digit[0]) * 2**(len(binary_digit) -1)
        return decimal + convert_to_decimal(binary_digit[1:])
