'''
Zengping Xu
CS 5001 Fall 2020

This program gets input from customer about an UPC number,
and validate if the UPC number is valid or not.
'''


def is_valid_upc(upc):
    '''
    Function --  is_valid_upc
        validate if an UPC number is valid or not according
        to a summary calculation.
    Parameters:
        upc -- a string contains upc number
    Returns:
        a boolean, represent if the upc is valid or not
    '''
    if upc.isdigit() is False:
        return False

    sum = 0
    upc_list = list(upc)
    upc_list.reverse()
    for i in range(len(upc_list)):
        if (i % 2 == 1):
            item = int(upc_list[i])*3
        else:
            item = int(upc_list[i])
        sum += item
    print(sum)
    if (sum % 10 == 0):
        return True
    else:
        return False
