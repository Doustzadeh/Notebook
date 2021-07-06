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


# region Access List Items

# Access Items
# Note: The first item has index 0.

# %% Example
# Print the second item of the list:
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
# Out: banana


# Negative Indexing
# Negative indexing means start from the end
# -1 refers to the last item, -2 refers to the second last item etc.

# %% Example
# Print the last item of the list:
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
# Out: cherry


# Range of Indexes

# %% Example
# Return the third, fourth, and fifth item:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
# Out: ['cherry', 'orange', 'kiwi']
# Note: The search will start at index 2 (included) and end at index 5 (not included).

# %% Example
# This example returns the items from the beginning to, but NOT including, "kiwi":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])
# Out: ['apple', 'banana', 'cherry', 'orange']

# %% Example
# This example returns the items from "cherry" to the end:
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])
# Out: ['cherry', 'orange', 'kiwi', 'melon', 'mango']


# Range of Negative Indexes

# %% Example
# This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
# Out: ['orange', 'kiwi', 'melon']


# Check if Item Exists

# %% Example
# Check if "apple" is present in the list:
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
# Out: Yes, 'apple' is in the fruits list

# endregion


# region Change List Items

# Change Item Value

# %% Example
# Change the second item:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
# Out: ['apple', 'blackcurrant', 'cherry']


# Change a Range of Item Values

# %% Example
# Change the values "banana" and "cherry" with the values "blackcurrant" and "watermelon":
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
thislist[1:3] = ["blackcurrant", "watermelon"]
print(thislist)
# Out: ['apple', 'blackcurrant', 'watermelon', 'orange', 'kiwi', 'mango']

# %% Example
# Change the second value by replacing it with two new values:
thislist = ["apple", "banana", "cherry"]
thislist[1:2] = ["blackcurrant", "watermelon"]
print(thislist)
# Out: ['apple', 'blackcurrant', 'watermelon', 'cherry']

# %% Example
# Change the second and third value by replacing it with one value:
thislist = ["apple", "banana", "cherry"]
thislist[1:3] = ["watermelon"]
print(thislist)
# Out: ['apple', 'watermelon']


# Insert Items

# %% Example
# Insert "watermelon" as the third item:
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
# Out: ['apple', 'banana', 'watermelon', 'cherry']

# endregion


# region Add List Items

# Append Items

# %% Example
# Using the append() method to append an item:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
# Out: ['apple', 'banana', 'cherry', 'orange']


# Insert Items

# %% Example
# Insert an item as the second position:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
# Out: ['apple', 'orange', 'banana', 'cherry']


# Extend List

# %% Example
# Add the elements of tropical to thislist:
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
# Out: ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']


# Add Any Iterable

# %% Example
# Add elements of a tuple to a list:
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
# Out: ['apple', 'banana', 'cherry', 'kiwi', 'orange']

# endregion
