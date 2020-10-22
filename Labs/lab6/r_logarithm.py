'''
Zengping Xu
CS 5001, Fall 2020

This program gets a positive integer n as input from user,
and calculate the logarithm base 2, of n.
'''


def r_logarithm(n):
    '''
    Function -- r_logarithm
        calculate the logarithm base 2
    Parameters:
        n --  a positive integer 
    Returns an positive integer, the logarithm base 2 of n
    '''
    count = 1
    if n == 1:
        return 0
    else:
        return count + r_logarithm(n/2)


def r_logarithm_all(n, m):
    '''
    Function -- r_logarithm_all
        calculate the logarithm of base m
    Parameters:
        n -- a positive integer
        m -- a positive integer bigger than 1
    Returns an positive integer, the logarithm base m of n
    '''
    count = 1
    if n == 1: # base case
        return 0
    else:
        # recursive case
        return count + r_logarithm_all(n/m, m)
