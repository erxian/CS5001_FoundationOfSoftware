'''
Zengping Xu
CS 5001, Fall 2020

This program gets a positive integer n as input from user,
and calculate the logarithm base 2, of n.
'''


def logarithm(n):
    """
    Function -- logarithm
        calculate the logarithm base 2
    Parameters:
        n --  a positive integer 
    Returns:
        i --  an positive integer, the logarithm base 2 of n
    """
    # i = 0
    # smallest = 1
    # index = n / 2
    # while index >= smallest:
    #     index = index / 2
    #     i += 1
    # return i
    i = 0
    while n % 2 == 0:
        n = n / 2
        i += 1
    return i


def main():
    n = int(input("Enter a positive power of 2: "))
    lg = logarithm(n)
    print("lg(%d) = %d" % (n, lg))


if __name__ == "__main__":
    main()
