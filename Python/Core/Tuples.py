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


# region Update Tuples

# ---------------------------------------------------------
# Change Tuple Values
# Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called.

# %% Example
# Convert the tuple into a list to be able to change it:
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)
# Out: ('apple', 'kiwi', 'cherry')


# ---------------------------------------------------------
# Add Items
# Since tuples are immutable, they do not have a build-in append() method, but there are other ways to add items to a tuple.

# %% Example
# Convert the tuple into a list, add "orange", and convert it back into a tuple:
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)
# Out: ('apple', 'banana', 'cherry', 'orange')

# %% Example
# Create a new tuple with the value "orange", and add that tuple:
thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)
# Out: ('apple', 'banana', 'cherry', 'orange')


# ---------------------------------------------------------
# Remove Items
# Note: You cannot remove items in a tuple.

# %% Example
# Convert the tuple into a list, remove "apple", and convert it back into a tuple:

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)
# Out: ('banana', 'cherry')

# %% Example
# The del keyword can delete the tuple completely:
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists
# Out: NameError: name 'thistuple' is not defined

# endregion


# region Unpack Tuples

# ---------------------------------------------------------
# Unpacking a Tuple

# %% Example
# Packing a tuple:
fruits = ("apple", "banana", "cherry")
print(fruits)
# Out: ('apple', 'banana', 'cherry')

# %% Example
# Unpacking a tuple:
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
# Out: apple
print(yellow)
# Out: banana
print(red)
# Out: cherry


# ---------------------------------------------------------
# Using Asterisk*

# %% Example
# Assign the rest of the values as a list called "red":
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
# Out: apple
print(yellow)
# Out: banana
print(red)
# Out: ['cherry', 'strawberry', 'raspberry']

# %% Example
# Add a list of values the "tropic" variable:
fruits = ("apple", "mango", "papaya", "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
# Out: apple
print(tropic)
# Out: ['mango', 'papaya', 'pineapple']
print(red)
# Out: cherry

# endregion


# region Loop Tuples

# ---------------------------------------------------------
# Loop Through a Tuple

# %% Example
# Iterate through the items and print the values:
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
    print(x)
# Out: apple
#      banana
#      cherry


# ---------------------------------------------------------
# Loop Through the Index Numbers

# %% Example
# Print all items by referring to their index number:
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
   print(thistuple[i])
# Out: apple
#      banana
#      cherry


# ---------------------------------------------------------
# Using a While Loop

# %% Example
# Print all items, using a while loop to go through all the index numbers:
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1
# Out: apple
#      banana
#      cherry

# endregion
