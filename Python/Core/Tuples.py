# region Tuples

# ---------------------------------------------------------
# Tuple

# %% Example
# Create a Tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple)
# Out: ('apple', 'banana', 'cherry')

# %% Example
# Tuples allow duplicate values:
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)
# Out: ('apple', 'banana', 'cherry', 'apple', 'cherry')


# ---------------------------------------------------------
# Tuple Length

# %% Example
# Print the number of items in the tuple:
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))
# Out: 3


# ---------------------------------------------------------
# Create Tuple With One Item

# %% Example
# One item tuple, remember the comma:
thistuple = ("apple",)
print(type(thistuple))
# Out: <class 'tuple'>

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))
# Out: <class 'str'>


# ---------------------------------------------------------
# Tuple Items - Data Types

# %% Example
# String, int and boolean data types:
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

# %% Example
# A tuple with strings, integers and boolean values:
tuple1 = ("abc", 34, True, 40, "male")


# ---------------------------------------------------------
# The tuple() Constructor

# %% Example
# Using the tuple() method to make a tuple:
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
# Out: ('apple', 'banana', 'cherry')

# endregion


# region Access Tuple Items

# ---------------------------------------------------------
# Access Tuple Items
# Note: The first item has index 0.

# %% Example
# Print the second item in the tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple[1])
# Out: banana


# ---------------------------------------------------------
# Negative Indexing
# Negative indexing means start from the end.

# %% Example
# Print the last item of the tuple:
thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])
# Out: cherry


# ---------------------------------------------------------
# Range of Indexes

# %% Example
# Return the third, fourth, and fifth item:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])
# Out: ('cherry', 'orange', 'kiwi')

# %% Example
# This example returns the items from the beginning to, but NOT included, "kiwi":
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[:4])
# Out: ('apple', 'banana', 'cherry', 'orange')

# %% Example
# This example returns the items from "cherry" and to the end:
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:])
# Out: ('cherry', 'orange', 'kiwi', 'melon', 'mango')


# ---------------------------------------------------------
# Range of Negative Indexes

# %% Example
# This example returns the items from index -4 (included) to index -1 (excluded)
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[-4:-1])
# Out: ('orange', 'kiwi', 'melon')


# ---------------------------------------------------------
# Check if Item Exists

# %% Example
# Check if "apple" is present in the tuple:
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")
# Out: Yes, 'apple' is in the fruits tuple

# endregion
