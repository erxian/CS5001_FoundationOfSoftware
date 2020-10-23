'''
Zengping Xu
CS 5001, Fall 2020

This program gets input from the users about the house buying plan and 
figure out how long a user can buy one.
'''

def main():
    cost = int(input("how much will the house cost? "))
    annual_salary = int(input("what is your annual salary of? "))
    monthly_saved_percent = float(input("how much money you can save from \
your monthly salary?(percent 0-1) "))

    down_payment_percent = 0.25
    months = 12
    down_payment = cost*down_payment_percent
    monthly_saved_money = annual_salary / months * monthly_saved_percent
    monthly_saved_money = float(format(monthly_saved_money, '.2f'))
    print("monthly_saved_money is:", monthly_saved_money)
    time_needed = down_payment / monthly_saved_money
    
    if type(time_needed) == "int":
       time_needed = time_needed
    else:
       time_needed =  int(time_needed) + 1 

    print("down_payment", down_payment)
    print("monthly_saved_money", monthly_saved_money)
    print("time_needed", time_needed)
    print("The amount to be saved per month is %.2f and the down payment amount is %d. If you save %.2f per month, \
    it will take %d month to save enough for the down payment" % (monthly_saved_money, down_payment, monthly_saved_money, time_needed))


if __name__ == "__main__":
    main()