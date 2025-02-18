# get a name of a item from the user
product = input("What are you pruchaning? ")
cost = float(input(f"How much does the {product} cost? "))

# disply the data back to the user using a formatted string
print(f"You are buying {product} and it cost ${cost:.2f}")