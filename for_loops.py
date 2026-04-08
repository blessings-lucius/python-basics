"""
for_loops.py

Author: Blessings Lucius
Created: 2026-01-05

A simple module demonstrating Python for loops.
"""

# For loop go through a group of items and perform an action for each item in the group.
# The syntax of a for loop is:
# for variable in iterable:
#     # code to execute for each item in the iterable

# For loop to iterate over a list
my_list = [1, 2, 3, 4, 5]

print("Iterating over a list:")
for item in my_list:
    print(item)


# For loop to iterate over a string
my_string = "Hello"
print("\nIterating over a string:")

for character in my_string:
    print(character)


# For loop to iterate over a range of numbers
print("\nIterating over a range of numbers:")

for number in range(1, 6):
    print(number)


# For loop to iterate over a dictionary
my_dict = {
    "name": "Happiness", 
    "age": 10, 
    "city": "Zomba"
    }
print("\nIterating over a dictionary:")

for key, value in my_dict.items():
    print(f"{key}: {value}")