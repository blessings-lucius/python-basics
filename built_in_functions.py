"""
built_in_functions.py

Author: Blessings Lucius
Created: 2026-01-04

A simple module demonstrating Python built-in functions.
"""


# Python has many built-in functions that are available for use without needing to import any modules
print("Hello, World!")  # This function prints a message to the console
len([1, 2, 3])  # This function returns the length of a list
max([1, 2, 3])  # This function returns the maximum value in a list
min([1, 2, 3])  # This function returns the minimum value in a list
sum([1, 2, 3])  # This function returns the sum of all values in a list
sorted([3, 1, 2])  # This function returns a sorted version of the list
abs(-5)  # This function returns the absolute value of a number
round(3.14159, 2)  # This function rounds a number to a specified number of decimal places

# Built-in functions can also be used with variables
number = -10
print("Absolute value of number:", abs(number))

# Built-in functions can also be used in expressions
numbers = [1, 2, 3, 4, 5]
average = sum(numbers) / len(numbers)
print("Average:", average)