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
