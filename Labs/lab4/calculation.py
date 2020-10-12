'''
Zengping Xu
CS 5001, Fall 2020

This program get inputs from user about a number, then
calculate the number according to the user's calculation step
'''


def calculation(a, b, op):
    '''
    Function -- calculation
        calculate number a and b through operation op
    Parameters:
        a -- the number a
        b -- the number b
        op -- the operation is +, -, * or /
    Returns a number, the calculation result after operate a and b
    '''
    total = eval(a + op + b)
    return total


def main():
    end_op = "q"
    start_number = input("Enter a number: ")
    next_step = input("Enter the next step in the calculation: ")
    while next_step != end_op:
        next_step_list = next_step.split(" ")
        op = next_step_list[0]
        number = next_step_list[1]
        subtotal = calculation(start_number, number, op)
        start_number = str(subtotal)
        print("Subtotal =", subtotal)
        next_step = input("Enter the next step in the calculation: ")
    total = subtotal
    print("Total =", total)


if __name__ == "__main__":
    main()
