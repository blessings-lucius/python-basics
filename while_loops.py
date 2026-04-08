"""
while_loops.py

Author: Blessings Lucius
Created: 2026-01-06

A simple module demonstrating Python while loops.
"""


# A while loop repeatedly executes a block of code as long as a specified condition is true.

# The syntax of a while loop is:
# while condition:
#     # code to execute as long as the condition is true

# Example of a while loop that counts from 1 to 5
count = 1
print("Counting from 1 to 5:")

while count <= 5:
    print(count)
    count += 1  # Increment the count by 1


# Example of a while loop that calculates the factorial of a number
number = 5
factorial = 1
print(f"\nCalculating the factorial of {number}:")

while number > 1:
    factorial *= number  # Multiply the current factorial by the number
    number -= 1  # Decrement the number by 1

print(f"The factorial of {number} is {factorial}.")


# Example of a while loop that continues until the user enters 'exit'
user_input = ""
print("\nType 'exit' to stop the loop.")

while user_input.lower() != "exit":
    user_input = input("Enter something: ")
    print(f"You entered: {user_input}")
print("Loop has been exited.")
