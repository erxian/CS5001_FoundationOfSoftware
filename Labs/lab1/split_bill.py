'''
Zengping Xu
CS 5001, Fall 2020

This program gets input from the users about the payment plan for a group eating and 
calculate how much each person should contribute. 
'''

def main():
    amount = float(input("how much was the bill? "))
    percent = float(input("what percentage of tip would everyone prefer? (please enter 0-1): "))
    guests = int(input("how many people are in the group? "))

    total_fees = amount + amount*percent
    split_amount = total_fees/guests
    print("every group member should pay", split_amount)


if __name__ == "__main__":
    main()
