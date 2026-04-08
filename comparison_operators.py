"""
comparison_operators.py

Author: Blessings Lucius
Created: 2026-01-12

A simple module demonstrating Python comparison operators.
"""


# Comparison operators are used to compare two values and return a boolean result (True or False).
# The common comparison operators in Python are:
# == : Equal to
# != : Not equal to
# > : Greater than
# < : Less than
# >= : Greater than or equal to
# <= : Less than or equal to

# Example of using comparison operators
a = 10
b = 20

print(f"{a} == {b}: {a == b}")  # False
print(f"{a} != {b}: {a != b}")  # True

if a > b:
    print(f"{a} is greater than {b}")
elif a == b:
    print(f"{a} is equal to {b}")
else:
    print(f"{a} is less than {b}")