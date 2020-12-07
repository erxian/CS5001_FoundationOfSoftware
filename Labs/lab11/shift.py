'''
Sample Code
CS 5001, Fall 2020 - Lecture 11

An iterative implementation of binary search.
'''


def search_min(lst):
    '''
        Function -- search_min
            Perform a binary search for a given list,
            return the min number in the list
        Parameters:
            lst -- the list to search in.
        Returns:
            an integer
    '''
    left_index = 0
    right_index = len(lst) - 1
    middle = (left_index + right_index) // 2
    FOUND = False
    while not FOUND:
        # base case, when only two number waited sorting
        if right_index - left_index <= 1:
            minest = min(lst[left_index], lst[right_index])
            FOUND = True

        if lst[middle] > lst[middle - 1] and lst[middle] < lst[middle + 1]:
            # case 1, when middle number bigger than right-most number
            # and less than left-most number, means there is no shift
            # in this list, so the minest is the left-most number
            if lst[middle] > lst[left_index] and lst[middle] < lst[right_index]:
                minest = lst[left_index]
                FOUND = True
            # case 2, when middle number is less than both left-most and rihgt-most
            # number, means the minest is in the right side of middle
            if lst[middle] > lst[left_index] and lst[middle] > lst[right_index]:
                left_index = middle + 1     
            # case 3, when middle number is bigger than both left-most and rihgt-most
            # number, means the minest is in the lesf side of middle
            if lst[middle] < lst[left_index] and lst[middle] < lst[right_index]:
                right_index = middle - 1
        elif lst[middle] < lst[middle - 1] and lst[middle] < lst[middle + 1]:
            minest = lst[middle]
            FOUND = True
        else:
            minest = lst[middle + 1]
            FOUND = True    
        middle = (left_index + right_index) // 2
    return minest


def main():
    lst1 = [18, 25, 38, 45, 1, 12, 13]
    lst2 = [25, 38, 1, 12, 13, 18]
    lst3 = [1, 12, 13, 18, 25, 38]
    print(search_min(lst1))
    print(search_min(lst2))
    print(search_min(lst3))


if __name__ == "__main__":
    main()
