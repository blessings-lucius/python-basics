"""
memberships.py

Author: Blessings Lucius
Created: 2026-02-16

A simple module demonstrating Python membership operators.
"""


# Membership operators are used to test if a value is in a sequence (like a list, tuple, or string)
# Example of using the 'in' operator
fruits = ["apple", "banana", "cherry"]
print("banana" in fruits)  # This will print True because "banana" is in the list
# Checking if "grape" is in the list of fruits
if "grape" in fruits:
    print("Grape is in the list of fruits.")
else:
    print("Grape is not in the list of fruits.")


# Example of using the 'not in' operator
print("orange" not in fruits)  # This will print True because "orange" is not in the list
# Checking if "apple" is not in the list of fruits
if "apple" not in fruits:
    print("Apple is not in the list of fruits.")
else:
    print("Apple is in the list of fruits.")

# Membership operators can also be used with strings
greeting = "Hello, World!"
print("Hello" in greeting)  # This will print True because "Hello" is in the string
print("Hi" not in greeting)  # This will print True because "Hi" is not in the string