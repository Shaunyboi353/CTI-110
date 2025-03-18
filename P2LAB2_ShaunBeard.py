# Shaun Beard
# 2/25/2025
# P2LAB2
# uses a dictionary to store user input and displays output to the user


cars = {"Camaro": 18.21, "Prius": 52.36, "Model S": 110, "Silverado": 26 }
print(dict.keys(cars))
car_name = input("Enter a vehicle to see it's mpg: ")
print(f"The {car_name} gets {cars[car_name]} mpg")
drive_miles = float(input(f"How many miles will you drive the {car_name}: "))
gallons_gas = drive_miles / cars[car_name]
print(f"{gallons_gas:.2f} gallon(s) of gas are needed to drive the {car_name} {drive_miles} miles")
