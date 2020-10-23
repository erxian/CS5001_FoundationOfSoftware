'''
Zengping Xu
CS 5001 Fall 2020

This program get input from user about the current day,
and calculate the number of days untill Friday.
'''

def greeting(name):
    '''
    Function -- greeting
        print Hello <name> to the user
    Parameters:
        name -- the name of the user
    Returns a string, e.g. Hello <name> to the user
    '''
    greeting_words = "Hello, " + name
    return greeting_words


def day_convert_digit(day):
    '''
    Function -- day_convert_digit
        convert a week day to a digit by using dictionary, for example \
        M is represent by digit 2
    Parameters:
        day -- the day of week
    Return a digit which represents a week day
    '''
    dic = {'M': 2, 'Tu': 3, 'W': 4, 'Th': 5, 'F': 6, 'Sa': 0, 'Su': 1}
    digit = dic.get(day)
    return digit


def count(day):
    '''
    Function --  count
        count the day until Friday
    Parameters:
        day --  the day of week
    Return the number of days until friday
    '''
    friday_base = 6
    day_base = day_convert_digit(day)
    day_until_friday = friday_base - day_base
    return day_until_friday


def main():
    name = input("What's your name? ")
    greeting_words = greeting(name)
    print(greeting_words)
    day = input("Enter the current day(M, Tu, W, Th, F, Sa, Su): ").upper()
    valid_week_day = {"M", "Tu", "W", "Th", "F", "Sa", "Su"}
    if day not in valid_week_day:
        print("Invalid day! Please enter correct day format refer to the prompt")
    else:
        day_until_friday = count(day)
        print("The number of days until friday is", day_until_friday)


if __name__ == "__main__":
    main()
