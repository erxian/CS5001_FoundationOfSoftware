# -*- coding: utf-8 -*
'''
Zengping Xu
CS 5001, Fall 2020

This program gets input from guestes about their chest measurement in inches
and return the user’s size according to the T-shirt company.
'''


size_range = {0: 'S', 1: 'M', 2: 'L', 3: 'XL', 4: 'XXL', 5: 'XXL', 6: 'XXXL'}
category = ["Kids", "Womens", "Mens"]
chest_step = {'Kids': 2, 'Womens': 2, 'Mens': 3}
smallest_chest = {'Kids': 26, 'Womens': 30, 'Mens': 34}
largest_chest = {'Kids': 36, 'Womens': 42, 'Mens': 52}


def size_calculate(chest_inches, smallest, step):
    '''
    Function -- size_calculate
        calculate the matching size for the user according to the
        appropriate chart
    Parameters:
        chest_inches -- the value of the chest measurement in inches
        smallest -- the smallest chest of Kids, Womens, or Mens
        step --  the chest step of each size
    Returns:
        the size, is a string.
    '''
    quotient = (chest_inches - smallest) // step
    result = size_range.get(quotient)
    return result


def check_valid(chest_inches, smallest, largest):
    '''
    Function -- check_valid
        check if the chest_inches is within the valid chest range of
        Kids, Womens, or Mens
    Parameters:
        chest_inches -- the value of the chest measurement in inches
        smallest -- the smallest chest of Kids, Womens, or Mens
        largest -- the largest chest of Kids, Womens, or Mens
    '''
    if chest_inches < smallest or chest_inches >= largest:
        return False
    else:
        return True


def main():
    chest_inches = float(input("Chest measurement in inches: "))

    valid_smallest_chest = smallest_chest.get('Kids')
    valid_largerst_chest = largest_chest.get('Mens')
    if chest_inches < valid_smallest_chest or \
            chest_inches >= valid_largerst_chest:
        print("Sorry, we don't carry your size")
    else:
        print("Your size choices:")
        for c in category:
            smallest = smallest_chest[c]
            largest = largest_chest[c]
            category_size_vaild = check_valid(chest_inches, smallest, largest)
            if category_size_vaild is False:
                result = "not available"
            else:
                step = chest_step[c]
                result = size_calculate(chest_inches, smallest, step)
            print("%s size: %s" % (c, result))


if __name__ == "__main__":
    main()
