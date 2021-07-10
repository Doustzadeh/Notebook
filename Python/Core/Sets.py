# region Sets

# ---------------------------------------------------------
# Set
# Sets are used to store multiple items in a single variable.
# A set is a collection which is both unordered and unindexed.

# %% Example
# Create a Set:
thisset = {"apple", "banana", "cherry"}
print(thisset)
# Out: {'cherry', 'banana', 'apple'}


# ---------------------------------------------------------
# Duplicates Not Allowed
# Sets cannot have two items with the same value.

# %% Example
# Duplicate values will be ignored:
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)
# Out: {'cherry', 'banana', 'apple'}


# ---------------------------------------------------------
# Get the Length of a Set
# To determine how many items a set has, use the len() method.

# %% Example
# Get the number of items in a set:
thisset = {"apple", "banana", "cherry"}
print(len(thisset))
# Out: 3


# ---------------------------------------------------------
# Set Items - Data Types

# %% Example
# String, int and boolean data types:
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

# %% Example
# A set with strings, integers and boolean values:
set1 = {"abc", 34, True, 40, "male"}


# ---------------------------------------------------------
# type()

# %% Example
# What is the data type of a set?
myset = {"apple", "banana", "cherry"}
print(type(myset))
# Out: <class 'set'>


# ---------------------------------------------------------
# The set() Constructor

# %% Example
# Using the set() constructor to make a set:
thisset = set(("apple", "banana", "cherry")) # note the double round-brackets
print(thisset)
# Out: {'cherry', 'banana', 'apple'}

# endregion


# region Access Set Items

# ---------------------------------------------------------
# Access Items

# %% Example
# Loop through the set, and print the values:
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)
# Out: cherry
#      banana
#      apple

# %% Example
# Check if "banana" is present in the set:
thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)
# Out: True

# endregion
