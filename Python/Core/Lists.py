# region Lists

# ---------------------------------------------------------
# List
# Lists are used to store multiple items in a single variable.

# %% Example
# Create a List:
thislist = ["apple", "banana", "cherry"]
print(thislist)
# Out: ['apple', 'banana', 'cherry']


# ---------------------------------------------------------
# Allow Duplicates
# Since lists are indexed, lists can have items with the same value:

# %% Example
# Lists allow duplicate values:
thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)
# Out: ['apple', 'banana', 'cherry', 'apple', 'cherry']


# ---------------------------------------------------------
# List Length
# To determine how many items a list has, use the len() function:

# %% Example
# Print the number of items in the list:
thislist = ["apple", "banana", "cherry"]
print(len(thislist))
# Out: 3


# ---------------------------------------------------------
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


# ---------------------------------------------------------
# The list() Constructor

# %% Example
# Using the list() constructor to make a List:
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)
# Out: ['apple', 'banana', 'cherry']

# endregion


# region Access List Items

# ---------------------------------------------------------
# Access Items
# Note: The first item has index 0.

# %% Example
# Print the second item of the list:
thislist = ["apple", "banana", "cherry"]
print(thislist[1])
# Out: banana


# ---------------------------------------------------------
# Negative Indexing
# Negative indexing means start from the end
# -1 refers to the last item, -2 refers to the second last item etc.

# %% Example
# Print the last item of the list:
thislist = ["apple", "banana", "cherry"]
print(thislist[-1])
# Out: cherry


# ---------------------------------------------------------
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


# ---------------------------------------------------------
# Range of Negative Indexes

# %% Example
# This example returns the items from "orange" (-4) to, but NOT including "mango" (-1):
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])
# Out: ['orange', 'kiwi', 'melon']


# ---------------------------------------------------------
# Check if Item Exists

# %% Example
# Check if "apple" is present in the list:
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
# Out: Yes, 'apple' is in the fruits list

# endregion


# region Change List Items

# ---------------------------------------------------------
# Change Item Value

# %% Example
# Change the second item:
thislist = ["apple", "banana", "cherry"]
thislist[1] = "blackcurrant"
print(thislist)
# Out: ['apple', 'blackcurrant', 'cherry']


# ---------------------------------------------------------
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


# ---------------------------------------------------------
# Insert Items

# %% Example
# Insert "watermelon" as the third item:
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)
# Out: ['apple', 'banana', 'watermelon', 'cherry']

# endregion


# region Add List Items

# ---------------------------------------------------------
# Append Items

# %% Example
# Using the append() method to append an item:
thislist = ["apple", "banana", "cherry"]
thislist.append("orange")
print(thislist)
# Out: ['apple', 'banana', 'cherry', 'orange']


# ---------------------------------------------------------
# Insert Items

# %% Example
# Insert an item as the second position:
thislist = ["apple", "banana", "cherry"]
thislist.insert(1, "orange")
print(thislist)
# Out: ['apple', 'orange', 'banana', 'cherry']


# ---------------------------------------------------------
# Extend List

# %% Example
# Add the elements of tropical to thislist:
thislist = ["apple", "banana", "cherry"]
tropical = ["mango", "pineapple", "papaya"]
thislist.extend(tropical)
print(thislist)
# Out: ['apple', 'banana', 'cherry', 'mango', 'pineapple', 'papaya']


# ---------------------------------------------------------
# Add Any Iterable

# %% Example
# Add elements of a tuple to a list:
thislist = ["apple", "banana", "cherry"]
thistuple = ("kiwi", "orange")
thislist.extend(thistuple)
print(thislist)
# Out: ['apple', 'banana', 'cherry', 'kiwi', 'orange']

# endregion


# region Remove List Items

# ---------------------------------------------------------
# Remove Specified Item

# %% Example
# Remove "banana":
thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)
# Out: ['apple', 'cherry']


# ---------------------------------------------------------
# Remove Specified Index

# %% Example
# Remove the second item:
thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)
# Out: ['apple', 'cherry']

# If you do not specify the index, the pop() method removes the last item.

# %% Example
# Remove the last item:
thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)
# Out: ['apple', 'banana']

# %% Example
# Remove the first item:
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
# Out: ['banana', 'cherry']

# %% Example
# Delete the entire list:
thislist = ["apple", "banana", "cherry"]
del thislist


# ---------------------------------------------------------
# Clear the List

# %% Example
# Clear the list content:
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)
# Out: []

# endregion


# region Loop Lists

# ---------------------------------------------------------
# Loop Through a List

# %% Example
# Print all items in the list, one by one:
thislist = ["apple", "banana", "cherry"]
for x in thislist:
    print(x)
# Out: apple
#      banana
#      cherry


# ---------------------------------------------------------
# Loop Through the Index Numbers

# %% Example
# Print all items by referring to their index number:
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])
# Out: apple
#      banana
#      cherry


# ---------------------------------------------------------
# Using a While Loop

# %% Example
# Print all items, using a while loop to go through all the index numbers
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
    print(thislist[i])
    i = i + 1
# Out: apple
#      banana
#      cherry


# ---------------------------------------------------------
# Looping Using List Comprehension

# %% Example
# A short hand for loop that will print all items in a list:
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]
# Out: apple
#      banana
#      cherry

# endregion


# region List Comprehension

# ---------------------------------------------------------
# List Comprehension

# %% Example
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)
# Out: ['apple', 'banana', 'mango']

# %% Example
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)
# Out: ['apple', 'banana', 'mango']


# ---------------------------------------------------------
# Condition

# %% Example
# Only accept items that are not "apple":
newlist = [x for x in fruits if x != "apple"]
print(newlist)
# Out: ['banana', 'cherry', 'kiwi', 'mango']

# %% Example
# With no if statement:
newlist = [x for x in fruits]
print(newlist)
# Out: ['apple', 'banana', 'cherry', 'kiwi', 'mango']


# ---------------------------------------------------------
# Iterable

# %% Example
# You can use the range() function to create an iterable:
newlist = [x for x in range(10)]
print(newlist)
# Out: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# %% Example
# Accept only numbers lower than 5:
newlist = [x for x in range(10) if x < 5]
print(newlist)
# Out: [0, 1, 2, 3, 4]


# ---------------------------------------------------------
# Expression

# %% Example
# Set the values in the new list to upper case:
newlist = [x.upper() for x in fruits]
print(newlist)
# Out: ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']

# %% Example
# Set all values in the new list to 'hello':
newlist = ['hello' for x in fruits]
print(newlist)
# Out: ['hello', 'hello', 'hello', 'hello', 'hello']

# %% Example
# Return "orange" instead of "banana":
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)
# Out: ['apple', 'orange', 'cherry', 'kiwi', 'mango']

# endregion


# region Sort Lists

# ---------------------------------------------------------
# Sort List Alphanumerically
# List objects have a sort() method that will sort the list alphanumerically, ascending, by default:

# %% Example
# Sort the list alphabetically:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)
# Out: ['banana', 'kiwi', 'mango', 'orange', 'pineapple']

# %% Example
# Sort the list numerically:
thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)
# Out: [23, 50, 65, 82, 100]


# ---------------------------------------------------------
# Sort Descending
# To sort descending, use the keyword argument reverse = True:

# %% Example
# Sort the list descending:
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)
# Out: ['pineapple', 'orange', 'mango', 'kiwi', 'banana']

# %% Example
# Sort the list descending:
thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)
# Out: [100, 82, 65, 50, 23]


# ---------------------------------------------------------
# Customize Sort Function
# You can also customize your own function by using the keyword argument key = function.

# %% Example
# Sort the list based on how close the number is to 50:
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)
# Out: [50, 65, 23, 82, 100]


# ---------------------------------------------------------
# Case Insensitive Sort
# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:

# %% Example
# Case sensitive sorting can give an unexpected result:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)
# Out: ['Kiwi', 'Orange', 'banana', 'cherry']

# %% Example
# Perform a case-insensitive sort of the list:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)
# Out: ['banana', 'cherry', 'Kiwi', 'Orange']


# ---------------------------------------------------------
# Reverse Order

# %% Example
# Reverse the order of the list items:
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
# Out: ['cherry', 'Kiwi', 'Orange', 'banana']

# endregion


# region Copy Lists

# ---------------------------------------------------------
# Copy a List

# %% Example
# Make a copy of a list with the copy() method:
thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)
# Out: ['apple', 'banana', 'cherry']

# %% Example
# Make a copy of a list with the list() method:
thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print(mylist)
# Out: ['apple', 'banana', 'cherry']

# endregion


# region Join Lists

# ---------------------------------------------------------
# Join Two Lists

# %% Example
# Join two list:
list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)
# Out: ['a', 'b', 'c', 1, 2, 3]

# %% Example
# Append list2 into list1:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)
# Out: ['a', 'b', 'c', 1, 2, 3]

# %% Example
# Use the extend() method to add list2 at the end of list1:
list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)
# Out: ['a', 'b', 'c', 1, 2, 3]

# endregion
