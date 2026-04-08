"""
data_structures.py

Author: Blessings Lucius
Created: 2026-02-19

A simple module demonstrating Python data structures.
"""

# There are several built-in data structures in Python, including lists, tuples, sets, and dictionaries.

# Lists are ordered, mutable collections of items
my_list = [1, 2, 3, 4, 5]
print("List:", my_list)
# Lists can contain items of different types
mixed_list = [1, "Hello", 3.14, True]
print("Mixed List:", mixed_list)
# Lists can be modified after creation
my_list.append(6)  # Adding an item to the end of the list
print("Updated List:", my_list)
# Lists can be accessed using indices
print("First item in the list:", my_list[0])  # Accessing the first item
# Lists can be sliced to get a subset of the list
print("Sliced List (first 3 items):", my_list[:3])  # Getting the first three items

# Tuples are ordered, immutable collections of items
my_tuple = (1, 2, 3, 4, 5)
print("Tuple:", my_tuple)
# Tuples can also contain items of different types
mixed_tuple = (1, "Hello", 3.14, True)
print("Mixed Tuple:", mixed_tuple)
# Tuples cannot be modified after creation, but they can be accessed using indices
print("First item in the tuple:", my_tuple[0])  # Accessing the first item
# Tuples can also be sliced to get a subset of the tuple
print("Sliced Tuple (first 3 items):", my_tuple[:3])  # Getting the first three items

# Sets are unordered collections of unique items
my_set = {1, 2, 3, 4, 5}
print("Set:", my_set)
# Sets can contain items of different types, but they must be immutable (not changeable)
mixed_set = {1, "Hello", 3.14, True}
print("Mixed Set:", mixed_set)
# Sets do not allow duplicate items
my_set.add(3)  # Trying to add a duplicate item (3) to the set
print("Set after trying to add a duplicate item:", my_set)
# Sets can be modified by adding or removing items
my_set.add(6)  # Adding a new item to the set
print("Set after adding a new item:", my_set)

# Dictionaries are unordered collections of key-value pairs
my_dict = {"name": "Grace", "age": 15, "city": "Lilongwe"}
print("Dictionary:", my_dict)
# Dictionaries can contain items of different types, but keys must be immutable (not changeable)
mixed_dict = {"name": "Grace", "age": 15, "is_student": True}
print("Mixed Dictionary:", mixed_dict)
# Dictionaries can be modified by adding or updating key-value pairs
my_dict["age"] = 16  # Updating the value associated with the key "age"
print("Updated Dictionary:", my_dict)
# Dictionaries can be accessed using keys
print("Name from the dictionary:", my_dict["name"])  # Accessing the value associated with the key "name"
# Dictionaries can also be accessed using the get() method, which returns None if the key is not found
print("City from the dictionary:", my_dict.get("city"))  # Accessing the value associated with the key "city"
print("Country from the dictionary (using get()):", my_dict.get("country"))  # Trying to access a non-existent key
print("Country from the dictionary (using get() with default):", my_dict.get("country", "Not Found"))  # Trying to access a non-existent key with a default value