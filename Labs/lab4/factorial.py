'''
Zengping Xu
CS 5001, Fall 2020

This program gets a positive integer n as input from user,
and calculate the factorial of n.
'''


def factorial(n):
    '''
    Function -- factorial
        calculate the product of n and all the non-negative,
        non-zero integers below it.
    Parameters:
        n -- an positive integer
    Returns:
        result -- an positive integer, the factorial of n
    '''
    # i = 1
    # result = 1
    # while i <= n:
    #     result = i * result
    #     i += 1
    # return result
    total = 1
    while n > 1:
        total *= n
        n -= 1
    return total


def main():
    n = int(input("Enter a positive integer: "))
    result = factorial(n)
    print("%d! = %d" % (n, result))


if __name__ == "__main__":
    main()
