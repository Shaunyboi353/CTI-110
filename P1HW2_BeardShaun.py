# Shaun Beard 
# # 2/13/2025
# P1HW2
# Creating a progarm to do math to find a budget

# Header

print ("This program calculates and displays travel expenses")

# Inputs

the_budget = int(input("Enter your budget: "))
travel_dest = (input("Enter where you are going: "))
gas_price = int(input("Enter how much you will spend on gas: "))
accomodation_price = int(input("Enter How much you will spend for accommodation: "))
food_price = int(input("Enter the amount you will spend on food: "))

# calculations

the_expenses = gas_price + accomodation_price + food_price
the_amount = the_budget - the_expenses

# the display

print("--------------Travel Expenses-------------")
print("Location: ", travel_dest)
print("Initial Budget:", the_budget)
print()
print("Fuel: ", gas_price)
print("Accomodation: ", accomodation_price)
print("Food: ", food_price)
print()
print("Remaining Balance: ", the_amount)

# end