'''
Zengping Xu
CS 5002 Fall 2020

An recursively implementation of binary search.
'''


def binary_search(lst, item):
    '''
    Function -- binary_search
        Searches for the given item in the given list.
    Parameters:
        lst -- The list to search in.
        item -- The item to search for.
    Returns:
        True if item is in lst, False otherwise.
    '''
    found = False
    new_lst = []
    midpoint = (0 + len(lst)) // 2

    if len(lst) == 0:  # base case 1
        return False
    elif lst[midpoint] == item:  # base case 2
        found = True
    else:
        # recursive case
        if item < lst[midpoint]:
            new_lst = lst[:midpoint]
        else:
            new_lst = lst[midpoint + 1:]
    return found or binary_search(new_lst, item)


def main():
    desserts = ["apple", "banana", "carrot", "pecan", "pumpkin"]
    search1 = "pumpkin"
    search2 = "chocolate"
    search3 = "apple"

    print(binary_search(desserts, search1))
    print(binary_search(desserts, search2))
    print(binary_search(desserts, search3))


if __name__ == "__main__":
    main()