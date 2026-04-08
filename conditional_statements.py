"""
conditional_statements.py

Author: Blessings Lucius
Created: 2026-01-10

A simple module demonstrating Python conditional statements.
"""


# Conditional statements allow you to execute different blocks of code based on certain conditions.
# The syntax of an if statement is:
# if condition:
#     # code to execute if the condition is true
# elif another_condition:
#     # code to execute if the another_condition is true
# else:
#     # code to execute if all conditions are false

# Example of an if statement that checks if a number is positive
number = 10
if number > 0:
    print(f"{number} is a positive number.")

# Example of an if-elif-else statement that checks if a number is positive, negative, or zero
number = -5
if number > 0:
    print(f"{number} is a positive number.")
elif number < 0:
    print(f"{number} is a negative number.")
else:
    print(f"{number} is zero.")