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
