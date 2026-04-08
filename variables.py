"""
variables.py

Author: Blessings Lucius
Created: 2026-02-02

A simple module demonstrating Python variables.
"""


# Variables are used to store data in Python
# They can hold different types of data such as numbers, strings, lists, etc.

# Example of creating and using variables

# Creating a variable to store a string
name = "Grace"

# Creating a variable to store an integer
age = 15

# Creating a variable to store a float
height = 1.22

# Creating a variable to store a list
hobbies = ["reading", "coding", "hiking"]

# Printing the variables to the console
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Hobbies:", hobbies)


# Variables can be reassigned to new values
name = "Favour"
age = 5
height = 0.5
hobbies.append("drawing")

# Printing the updated variables to the console
print("Updated Name:", name)
print("Updated Age:", age)
print("Updated Height:", height)
print("Updated Hobbies:", hobbies)

# Variables can also be used in expressions
age_next_year = age + 1
print("Age next year:", age_next_year)

# Variables can be of different types and can be used together in expressions
greeting = "Hello, " + name + "!"
print(greeting)
