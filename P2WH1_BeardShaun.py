 # Shaun Beard
 # 2/25/2025
 # P2HW1
 # using string formatting to organize a program

# Header

print ("This program calculates and displays travel expenses")
print()

# Inputs

the_budget = int(input("Enter your budget: "))
print()
travel_dest = (input("Enter where you are going: "))
print()
gas_price = int(input("Enter how much you will spend on gas: "))
print()
accomodation_price = int(input("Enter How much you will spend for accommodation: "))
print()
food_price = int(input("Enter the amount you will spend on food: "))
print()

# calculations

the_expenses = gas_price + accomodation_price + food_price
the_amount = the_budget - the_expenses

# the display
#{circumference:.2f}")

print("--------------Travel Expenses-------------")
print(f"{'Location':<20}{travel_dest}")
print(f"{'Initial Budget':<20}${the_budget:.2f}")
print(f"{'Fuel':<20}${gas_price:.2f}")
print(f"{'Accomodation':<20}${accomodation_price:.2f}")
print(f"{'Food':<20}${food_price:.2f}")
print("------------------------------------------")
print()
print("Remaining Balance: ", the_amount)