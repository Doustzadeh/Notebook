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


# region Loop Sets

# ---------------------------------------------------------
# Loop Items

# %% Example
# Loop through the set, and print the values:
thisset = {"apple", "banana", "cherry"}
for x in thisset:
    print(x)
# Out: apple
#      banana
#      cherry

# endregion


# region Join Sets

# ---------------------------------------------------------
# Join Two Sets

# %% Example
# The union() method returns a new set with all items from both sets:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)
# Out: {1, 2, 3, 'c', 'b', 'a'}

# %% Example
# The update() method inserts the items in set2 into set1:
set1 = {"a", "b" , "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)
# Out: {1, 2, 3, 'c', 'b', 'a'}

# Note: Both union() and update() will exclude any duplicate items.


# ---------------------------------------------------------
# Keep ONLY the Duplicates

# %% Example
# Keep the items that exist in both set x, and set y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)
# Out: {'apple'}

# The intersection() method will return a new set, that only contains the items that are present in both sets.

# %% Example
# Return a set that contains the items that exist in both set x, and set y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)
# Out: {'apple'}


# ---------------------------------------------------------
# Keep All, But NOT the Duplicates

# The symmetric_difference_update() method will keep only the elements that are NOT present in both sets.

# %% Example
# Keep the items that are not present in both sets:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y)
print(x)
# Out: {'microsoft', 'google', 'cherry', 'banana'}

# The symmetric_difference() method will return a new set, that contains only the elements that are NOT present in both sets.

# %% Example
# Return a set that contains all items from both sets, except items that are present in both:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.symmetric_difference(y)
print(z)
# Out: {'microsoft', 'google', 'cherry', 'banana'}

# endregion


# region Set Methods

# ---------------------------------------------------------
# Set add() Method
# The add() method adds an element to the set.
# If the element already exists, the add() method does not add the element.

# %% Example
# Add an element to the fruits set:
fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)
# Out: {'banana', 'cherry', 'orange', 'apple'}

# %% Example
# Try to add an element that already exists:
fruits = {"apple", "banana", "cherry"}
fruits.add("apple")
print(fruits)
# Out: {'banana', 'cherry', 'apple'}


# ---------------------------------------------------------
# Set clear() Method
# The clear() method removes all elements in a set.

# %% Example
# Remove all elements from the fruits set:
fruits = {"apple", "banana", "cherry"}
fruits.clear()
print(fruits)
# Out: set()


# ---------------------------------------------------------
# Set copy() Method
# The copy() method copies the set.

# %% Example
# Copy the fruits set:
fruits = {"apple", "banana", "cherry"}
x = fruits.copy()
print(x)
# Out: {'banana', 'cherry', 'apple'}


# ---------------------------------------------------------
# Set difference() Method
# The difference() method returns a set that contains the difference between two sets.
# Meaning: The returned set contains items that exist only in the first set, and not in both sets.

# %% Example
# Return a set that contains the items that only exist in set x, and not in set y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y)
print(z)
# Out: {'banana', 'cherry'}

# %% Example
# Return a set that contains the items that only exist in set y, and not in set x:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = y.difference(x)
print(z)
# Out: {'google', 'microsoft'}


# ---------------------------------------------------------
# Set difference_update() Method
# The difference_update() method removes the items that exist in both sets.
# The difference_update() method is different from the difference() method, 
# because the difference() method returns a new set, without the unwanted items, 
# and the difference_update() method removes the unwanted items from the original set.

# %% Example
# Remove the items that exist in both sets:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y)
print(x)
# Out: {'banana', 'cherry'}


# ---------------------------------------------------------
# Set discard() Method
# The discard() method removes the specified item from the set.
# This method is different from the remove() method, 
# because the remove() method will raise an error if the specified item does not exist, 
# and the discard() method will not.

# %% Example
# Remove "banana" from the set:
fruits = {"apple", "banana", "cherry"}
fruits.discard("banana")
print(fruits)
# Out: {'cherry', 'apple'}


# ---------------------------------------------------------
# Set intersection() Method
# The intersection() method returns a set that contains the similarity between two or more sets.
# Meaning: The returned set contains only items that exist in both sets, 
# or in all sets if the comparison is done with more than two sets.

# %% Example
# Return a set that contains the items that exist in both set x, and set y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.intersection(y)
print(z)
# Out: {'apple'}

# %% Example
# Compare 3 sets, and return a set with items that is present in all 3 sets:
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
result = x.intersection(y, z)
print(result)
# Out: {'c'}


# ---------------------------------------------------------
# Set intersection_update() Method
# The intersection_update() method removes the items that is not present in both sets 
# (or in all sets if the comparison is done between more than two sets).
# The intersection_update() method is different from the intersection() method, 
# because the intersection() method returns a new set, without the unwanted items, 
# and the intersection_update() method removes the unwanted items from the original set.

# %% Example
# Remove the items that is not present in both x and y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
print(x)
# Out: {'apple'}

# %% Example
# Compare 3 sets, and return a set with items that is present in all 3 sets:
x = {"a", "b", "c"}
y = {"c", "d", "e"}
z = {"f", "g", "c"}
x.intersection_update(y, z)
print(x)
# Out: {'c'}


# ---------------------------------------------------------
# Set isdisjoint() Method
# The isdisjoint() method returns True if none of the items are present in both sets, otherwise it returns False.

# %% Example
# Return True if no items in set x is present in set y:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y)
print(z)
# Out: True

# %% Example
# Return False if one ore more items are present in both sets:
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.isdisjoint(y)
print(z)
# Out: False

# endregion
