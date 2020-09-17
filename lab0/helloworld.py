# if I plan to order 20 pizza for the parrty, each pizza have 8 slices, and each guest can eat 3 slices


#numbers_of_pizza = int(input("how many pizza you want to order? "))
numbers_of_pizza = 20
slices_of_each_pizza = 8
slices_of_each_guest_eaten = 3
numbers_of_guests = (numbers_of_pizza * slices_of_each_pizza) // slices_of_each_guest_eaten

print("The number of guests I can have", numbers_of_guests)

standard_pizza_price = 9.99
specialty_pizza_price = 12.99
numbers_of_specialty_pizza = 3
discount = 0.5
standard_pizza_with_discount = (numbers_of_pizza - numbers_of_specialty_pizza) // 2
numbers_of_standard_pizza_with_discount = standard_pizza_with_discount * 2
numbers_of_standard_pizza_without_discount = numbers_of_pizza - numbers_of_specialty_pizza - numbers_of_standard_pizza_with_discount
total_cost = numbers_of_specialty_pizza * specialty_pizza_price + (numbers_of_standard_pizza_with_discount * standard_pizza_price) * discount + \
             numbers_of_standard_pizza_without_discount * standard_pizza_price

print("The total cost of pizza order is", total_cost)

data = int(input("data is: "))
num = data // 2
rem = data % 2
print (num, rem)

