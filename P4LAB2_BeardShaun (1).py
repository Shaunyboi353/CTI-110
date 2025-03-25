# Shaun Beard
# 3/20/2025
# P4LAB2
# write code that displays information to users using nested loops

int_loop = "yes"

while int_loop.lower() != "no":
    integer = int(input("Enter and integer: "))
    if integer >= 0:
        for mult in range(1,13):
            print(f"{integer} * {mult} = {integer * mult}")
    else:
        print("This program doesn't handle negative numbers")
    
    
    int_loop = input("Would you like to run this program again? ")

print("Thank you, Bye.")