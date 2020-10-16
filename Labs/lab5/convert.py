'''
Zengping
CS 5001 Fall 2020

This program will convert binary digit to decimal digit
'''


def convert_to_decimal(binary_digit):
    '''
    Function -- convert_to_decimal
        convert a binary digit to a decimal digit
    '''
    len_binary = len(binary_digit)
    sum = 0
    count = 0
    while count < len_binary:
        # started from rightmost character in the string to the leftmost
        digit_with_position = int(binary_digit[len_binary - count - 1])
        number = digit_with_position * (2**count)
        sum  = sum + number
        count += 1
    return sum


def main():
    binary_digit = input("Enter a binary digit: ")
    decimal_digit = convert_to_decimal(binary_digit)
    print(decimal_digit)


if __name__ == "__main__":
    main()
