# -*- coding: utf-8 -*
'''
Zengping Xu
CS 5001 Fall 2020

This program get input from user's choice and calculate business
trip driving expenses towards each choice
'''


def calculate_mileage(start, end):
    '''
    Function -- calculate_mileage
        Calculates miles driven using the start and end odometer values.
    Parameters:
        start -- The odometer reading at the start of the trip.
            Expecting a number greater than 0.
        end -- The odometer reading at the end of the trip. Expecting a
            number greater than 0 and greater than the start value.
    Returns:
        The miles driven, a number. If either parameter is invalid (e.g.
        either parameter is negative or end is less than start), returns 0.
    '''
    if start > 0 and end > 0 and end > start:
        mileage = end - start
    else:
        mileage = 0
    return mileage


def get_reimbursement_amount(mileage):
    '''
    Function -- get_reimbursement_amount
        Calculates the amount in dollars that the employee should be
        reimbursed based on their mileage and the standard rate per mile.
        The standard rate for 2020 is 57.5 cents per mile.
    Parameters:
        mileage -- The number of miles driven.
    Returns:
        The amount the employee should be reimbursed in dollars, a float
        rounded to 2 decimal places.
    '''
    cents_per_mile = 57.5
    dollar_to_cent = 100
    dollars_per_mile = cents_per_mile / dollar_to_cent
    reimbursement_amount = round(mileage * dollars_per_mile, 2)
    return reimbursement_amount


def get_actual_mileage_rate(mpg, fuel_price):
    '''
    Function -- get_actual_mileage_rate
        Calculates the actual trip cost per mile in dollars based on the
        car's MPG and the fuel price.
    Parameters:
        mpg -- The car's miles per gallon (MPG), an integer greater than 0.
        fuel_price -- The fuel cost in dollars per gallon, a non-negative
        float.
    Returns:
        The actual cost per mile in dollars, a float rounded to 4 decimal
        places. If supplied arguments are invalid, returns 0.0
    '''
    if mpg < 0 or mpg == 0 or fuel_price < 0:
        actual_cents_per_mile = 0.0
    else:
        actual_cents_per_mile = round(fuel_price / mpg, 4)
    return actual_cents_per_mile


def get_actual_trip_cost(start, end, mpg, fuel_price):
    '''
    Function -- get_actual_trip_cost
        Calculates the cost of a trip in dollars based on the miles driven,
        the MPG of the car, and the fuel price per gallon.
    Parameters:
        start -- The odometer reading at the start of the trip. Expecting a
            number greater than 0.
        end -- The odometer reading at the end of the trip. Expecting a
            number greater than 0 and greater than the start value.
        mpg -- The car's miles per gallon (MPG), an integer greater than 0.
        fuel_price -- The fuel price per gallon, a non-negative float.
    Returns:
        The cost of the drive in dollars, a float rounded to 2 decimal
        places. If any of the supplied arguments are invalid, returns 0.0
    '''
    mileage = calculate_mileage(start, end)
    actual_cents_per_mile = get_actual_mileage_rate(mpg, fuel_price)
    actual_trip_cost = round(mileage * actual_cents_per_mile, 2)
    return actual_trip_cost


def main():
    print("MILEAGE REIMBURSEMENT CALCULATOR\nOptions:\n\
1 - Calculate reimbursement amount from odometer readings\n\
2 - Calculate reimbursement amount from miles traveled\n\
3 - Calculate the actual cost of your trip")
    valid_choice = [1, 2, 3]
    choice = int(input("Enter your choice (1, 2, or 3): "))
    if choice not in valid_choice:
        print("Not a valid choice")
    else:
        if choice == 1:
            start = float(input("Enter your starting odometer reading: "))
            end = float(input("Enter your ending odometer reading: "))
            mileage = calculate_mileage(start, end)
            reimbursement_amount = get_reimbursement_amount(mileage)
            print("You will be reimbursed $%.2f" % reimbursement_amount)
        elif choice == 2:
            miles = float(input("Enter the number of miles traveled: "))
            reimbursement_amount = get_reimbursement_amount(miles)
            print("You will be reimbursed $%.2f" % reimbursement_amount)
        else:
            start = float(input("Enter your starting odometer reading: "))
            end = float(input("Enter your ending odometer reading: "))
            mpg = int(input("Enter your car's MPG: "))
            fuel_price = float(input("Enter the fuel price per gallon: "))
            trip_cost = get_actual_trip_cost(start, end, mpg, fuel_price)
            print("Your trip cost $%.2f" % trip_cost)


if __name__ == "__main__":
    main()
