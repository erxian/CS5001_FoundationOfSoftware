'''
Zengping Xu
CS 5001 Fall 2020

This program will determine the greatest common divisor (GCD)
of two non-zero positive integers.
'''


def gcd_for_two(x, y):
    '''
    Function --  gcd_for_two
        determine the greates common divisor of two non-zero
        positive integers
    Parameters:
        x -- a non-zereo positive interger
        y -- another non-zereo positive interger
    Returns:
        a non-zero postive integer, the gcd of x and y
    '''
    # base case
    if x != 0 and y == 0:
        return x
    else:
        if x > y:
            remainder = x % y
            # recursive case
            return gcd_for_two(y, remainder)
        else:
            remainder = y % x
            # recursive case
            return gcd_for_two(x, remainder)


def gcd_for_n(lst_n):
    '''
    Function --  gcd_for_n
        determine the greates common divisor of n non-zero
        positive integers
    Parameters:
        lst_n -- a list, each element is positive interger
    Returns:
        a non-zero postive integer, the gcd of lst_n
    '''
    # base case, if len(lst_n) == 1
    if len(lst_n) == 1:
        return lst_n[0]
    else:
        gcd = gcd_for_two(lst_n[0], lst_n[1])
        # recursive case
        return gcd_for_n(lst_n[2:] + [gcd])
