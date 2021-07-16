# region Arrays

# Note: Python does not have built-in support for Arrays, but Python Lists can be used instead.

# ---------------------------------------------------------
# Arrays

# %% Example
# Create an array containing car names:
cars = ["Ford", "Volvo", "BMW"]
print(cars)
# Out: ['Ford', 'Volvo', 'BMW']


# ---------------------------------------------------------
# Access the Elements of an Array

# %% Example
# Get the value of the first array item:
cars = ["Ford", "Volvo", "BMW"]
x = cars[0]
print(x)
# Out: Ford

# %% Example
# Modify the value of the first array item:
cars = ["Ford", "Volvo", "BMW"]
cars[0] = "Toyota"
print(cars)
# Out: ['Toyota', 'Volvo', 'BMW']


# ---------------------------------------------------------
# The Length of an Array

# %% Example
# Return the number of elements in the cars array:
cars = ["Ford", "Volvo", "BMW"]
x = len(cars)
print(x)
# Out: 3


# ---------------------------------------------------------
# Looping Array Elements

# %% Example
# Print each item in the cars array:
cars = ["Ford", "Volvo", "BMW"]
for x in cars:
    print(x)
# Out: Ford
#      Volvo
#      BMW


# ---------------------------------------------------------
# Adding Array Elements

# %% Example
# Add one more element to the cars array:
cars = ["Ford", "Volvo", "BMW"]
cars.append("Honda")
print(cars)
# Out: ['Ford', 'Volvo', 'BMW', 'Honda']


# ---------------------------------------------------------
# Removing Array Elements

# %% Example
# Delete the second element of the cars array:
cars = ["Ford", "Volvo", "BMW"]
cars.pop(1)
print(cars)
# Out: ['Ford', 'BMW']

# %% Example
# Delete the element that has the value "Volvo":
cars = ["Ford", "Volvo", "BMW"]
cars.remove("Volvo")
print(cars)
# Out: ['Ford', 'BMW']

# endregion


# region Array Methods

# ---------------------------------------------------------
# List append() Method
# The append() method appends an element to the end of the list.

# %% Example
# Add an element to the fruits list:
fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")
print(fruits)
# Out: ['apple', 'banana', 'cherry', 'orange']

# %% Example
# Add a list to a list:
a = ["apple", "banana", "cherry"]
b = ["Ford", "BMW", "Volvo"]
a.append(b)
print(a)
# Out: ['apple', 'banana', 'cherry', ['Ford', 'BMW', 'Volvo']]


# ---------------------------------------------------------
# List clear() Method
# The clear() method removes all the elements from a list.

# %% Example
# Remove all elements from the fruits list:
fruits = ['apple', 'banana', 'cherry', 'orange']
fruits.clear()
print(fruits)
# Out: []


# ---------------------------------------------------------
# List copy() Method
# The copy() method returns a copy of the specified list.

# %% Example
# Copy the fruits list:
fruits = ['apple', 'banana', 'cherry', 'orange']
x = fruits.copy()
print(x)
# Out: ['apple', 'banana', 'cherry', 'orange']


# ---------------------------------------------------------
# List count() Method
# The count() method returns the number of elements with the specified value.

# %% Example
# Return the number of times the value "cherry" appears in the fruits list:
fruits = ['apple', 'banana', 'cherry']
x = fruits.count("cherry")
print(x)
# Out: 1

# %% Example
# Return the number of times the value 9 appears int the list:
points = [1, 4, 2, 9, 7, 8, 9, 3, 1]
x = points.count(9)
print(x)
# Out: 2


# ---------------------------------------------------------
# List extend() Method
# The extend() method adds the specified list elements (or any iterable) to the end of the current list.

# %% Example
# Add the elements of cars to the fruits list:
fruits = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']
fruits.extend(cars)
print(fruits)
# Out: ['apple', 'banana', 'cherry', 'Ford', 'BMW', 'Volvo']

# %% Example
# Add a tuple to the fruits list:
fruits = ['apple', 'banana', 'cherry']
points = (1, 4, 5, 9)
fruits.extend(points)
print(fruits)
# Out: ['apple', 'banana', 'cherry', 1, 4, 5, 9]


# ---------------------------------------------------------
# List index() Method
# The index() method returns the position at the first occurrence of the specified value.

# %% Example
# What is the position of the value "cherry":
fruits = ['apple', 'banana', 'cherry']
x = fruits.index("cherry")
print(x)
# Out: 2

# %% Example
# What is the position of the value 32:
fruits = [4, 55, 64, 32, 16, 32]
x = fruits.index(32)
print(x)
# Out: 3


# ---------------------------------------------------------
# List insert() Method
# The insert() method inserts the specified value at the specified position.

# %% Example
# Insert the value "orange" as the second element of the fruit list:
fruits = ['apple', 'banana', 'cherry']
fruits.insert(1, "orange")
print(fruits)
# Out: ['apple', 'orange', 'banana', 'cherry']


# ---------------------------------------------------------
# List pop() Method
# The pop() method removes the element at the specified position.

# %% Example
# Remove the second element of the fruit list:
fruits = ['apple', 'banana', 'cherry']
fruits.pop(1)
print(fruits)
# Out: ['apple', 'cherry']

# %% Example
# Return the removed element:
fruits = ['apple', 'banana', 'cherry']
x = fruits.pop(1)
print(x)
# Out: banana


# ---------------------------------------------------------
# List remove() Method
# The remove() method removes the first occurrence of the element with the specified value.

# %% Example
# Remove the "banana" element of the fruit list:
fruits = ['apple', 'banana', 'cherry']
fruits.remove("banana")
print(fruits)
# Out: ['apple', 'cherry']


# ---------------------------------------------------------
# List reverse() Method
# The reverse() method reverses the sorting order of the elements.

# %% Example
# Reverse the order of the fruit list:
fruits = ['apple', 'banana', 'cherry']
fruits.reverse()
print(fruits)
# Out: ['cherry', 'banana', 'apple']


# ---------------------------------------------------------
# List sort() Method
# The sort() method sorts the list ascending by default.

# %% Example
# Sort the list alphabetically:
cars = ['Ford', 'BMW', 'Volvo']
cars.sort()
print(cars)
# Out: ['BMW', 'Ford', 'Volvo']

# %% Example
# Sort the list descending:
cars = ['Ford', 'BMW', 'Volvo']
cars.sort(reverse=True)
print(cars)
# Out: ['Volvo', 'Ford', 'BMW']

# %% Example
# Sort the list by the length of the values:
# A function that returns the length of the value:
def myFunc(e):
    return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(key=myFunc)
print(cars)
# Out: ['VW', 'BMW', 'Ford', 'Mitsubishi']

# %% Example
# Sort a list of dictionaries based on the "year" value of the dictionaries:
# A function that returns the 'year' value:
def myFunc(e):
    return e['year']

cars = [
  {'car': 'Ford', 'year': 2005},
  {'car': 'Mitsubishi', 'year': 2000},
  {'car': 'BMW', 'year': 2019},
  {'car': 'VW', 'year': 2011}
]
cars.sort(key=myFunc)
print(cars)
# Out: [{'car': 'Mitsubishi', 'year': 2000}, {'car': 'Ford', 'year': 2005}, {'car': 'VW', 'year': 2011}, {'car': 'BMW', 'year': 2019}]

# %% Example
# Sort the list by the length of the values and reversed:
# A function that returns the length of the value:
def myFunc(e):
    return len(e)

cars = ['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(reverse=True, key=myFunc)
print(cars)
# Out: ['Mitsubishi', 'Ford', 'BMW', 'VW']

# endregion
