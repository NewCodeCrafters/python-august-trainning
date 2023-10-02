firstname = input("what is your first name?")
lastname = input("what is your last name?")
email = input("what is your email address?")
print(f"Your email is {email}")


# lists and tuples

# strings ""
# Numbers int or float
# boolean True/False 1 0
# list indexing

names = ["Olamide", "Bello", "ibrahim"]
# len used to count numbers of items in our lists

trainee1 = ["Bukunmi", True, 45, 99999999999.99]
fruits = [
    'Date', 'Plum', "Kiwi", "Banana", "Pawpaw", "soursop", "Grape", "Guava"
]

# Second column in slicing is for steps
# negative number in steps slice from behind
print(fruits[-1])
print(fruits[::-2])
 get the minimum item in our list
print(min(names))
print(min(numbers))

print(ord('A'))

# get the maximum item in our list
print(max(names))
