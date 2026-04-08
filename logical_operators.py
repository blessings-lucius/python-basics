"""
logical_operators.py

Author: Blessings Lucius
Created: 2026-01-14

A simple module demonstrating Python logical operators.
"""


# Logical operators in Python include: and, or, not
# Example of using logical operators
a = True
b = False

# Using 'and' operator
result_and = a and b  # This will be False because both operands are not True

# Using 'or' operator
result_or = a or b  # This will be True because at least one operand is True

# Using 'not' operator
result_not_a = not a  # This will be False because a is True
result_not_b = not b  # This will be True because b is False

print(f"{a} and {b}: {result_and}")
print(f"{a} or {b}: {result_or}")
print(f"not {a}: {result_not_a}")
print(f"not {b}: {result_not_b}")

# Example of using logical operators in a conditional statement
if a and not b:
    print("Condition is True: a is True and b is False")
if a or b:
    print("Condition is True: at least one of a or b is True")