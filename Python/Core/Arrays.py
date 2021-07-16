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

# endregion
