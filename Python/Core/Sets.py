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


# region Add Set Items

# ---------------------------------------------------------
# Add Items

# %% Example
# Add an item to a set, using the add() method:
thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)
# Out: {'banana', 'cherry', 'apple', 'orange'}


# ---------------------------------------------------------
# Add Sets

# %% Example
# Add elements from tropical into thisset:
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)
# Out: {'banana', 'pineapple', 'apple', 'papaya', 'cherry', 'mango'}


# ---------------------------------------------------------
# Add Any Iterable

# %% Example
# Add elements of a list to at set:
thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)
# Out: {'apple', 'cherry', 'kiwi', 'banana', 'orange'}

# endregion


# region Remove Set Items

# ---------------------------------------------------------
# Remove Item

# %% Example
# Remove "banana" by using the remove() method:
thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)
# Out: {'apple', 'cherry'}
# Note: If the item to remove does not exist, remove() will raise an error.

# %% Example
# Remove "banana" by using the discard() method:
thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)
# Out: {'apple', 'cherry'}
# Note: If the item to remove does not exist, discard() will NOT raise an error.

# %% Example
# Remove the last item by using the pop() method:
thisset = {"apple", "banana", "cherry"}
x = thisset.pop()
print(x)
# Out: apple
print(thisset)
# Out: {'banana', 'cherry'}
# Note: Sets are unordered, so when using the pop() method, you do not know which item that gets removed.

# %% Example
# The clear() method empties the set:
thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)
# Out: set()

# %% Example
# The del keyword will delete the set completely:
thisset = {"apple", "banana", "cherry"}
del thisset
print(thisset)
# Out: NameError: name 'thisset' is not defined

# endregion
