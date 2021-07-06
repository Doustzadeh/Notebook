# region Lists

# List
# Lists are used to store multiple items in a single variable.

# %% Example
# Create a List:
thislist = ["apple", "banana", "cherry"]
print(thislist)
# Out: ['apple', 'banana', 'cherry']


# Allow Duplicates
# Since lists are indexed, lists can have items with the same value:

# %% Example
# Lists allow duplicate values:
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
# Out: ['apple', 'banana', 'cherry', 'apple', 'cherry']


# List Length
# To determine how many items a list has, use the len() function:

# %% Example
# Print the number of items in the list:
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
# Out: 3


# List Items - Data Types

# %% Example
list1 = ["apple", "banana", "cherry"]
list2 = [1, 5, 7, 9, 3]
list3 = [True, False, False]

# A list can contain different data types:

# %% Example
# A list with strings, integers and boolean values:
list1 = ["abc", 34, True, 40, "male"]

# %% Example
# What is the data type of a list?
mylist = ["apple", "banana", "cherry"]
print(type(mylist))
# Out: <class 'list'>


# The list() Constructor

# %% Example
# Using the list() constructor to make a List:
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
# Out: ['apple', 'banana', 'cherry']

# endregion
