# # Strings -> Taking User Input
# # name = "Olamide"
# name = input("Enter Your Name here: ")
# birthyear = int(input("What year were you born? "))

# age = 2023 - birthyear

# next_age = 2024 - birthyear

# print(f"Your name is {name}")
# print(f'Wow! you are {age} years old')
# print(f"Your next age is {next_age}")

# Design a program that asks the user for the name of a product, its price, and the quantity they want to buy. Calculate the total cost and use a format string to display an invoice. For example:

name = "Olamide"
product = input("What is the name of the product? ")  # Macbook "Macbook"


# You are buying 4 Macbooks total price is 12000 dollars.

# str(), int(), bool(), float()
price = float(input("What is the price of the product? "))
quantity = int(input("How many product are you buying? "))
tt = price * quantity
print(f"You are buying {quantity} {product}. Total price is {tt} dollars")