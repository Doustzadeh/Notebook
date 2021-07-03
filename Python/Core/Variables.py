# region Variables

# Creating Variables

# %% Example
x = 5
y = "John"
print(x)
print(y)

# %% Example
x = 4        # x is of type int
x = "Sally"  # x is now of type str
print(x)


# Casting

# %% Example
x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0


# Get the Type

# %% Example
x = 5
y = "John"
print(type(x))
print(type(y))


# Single or Double Quotes

# %% Example
x = "John"
# is the same as
x = 'John'


# Case-Sensitive
# Variable names are case-sensitive.

# %% Example
a = 4
A = "Sally"
# A will not overwrite a

# endregion


# region Variable Names

#  Variable Names

# %% Example
# Legal variable names:
myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


# Multi Words Variable Names

# Camel Case
# Each word, except the first, starts with a capital letter:
myVariableName = "John"

# Pascal Case
# Each word starts with a capital letter:
MyVariableName = "John"

# Snake Case
# Each word is separated by an underscore character:
my_variable_name = "John"

# endregion


# region Variables - Assign Multiple Values

# Many Values to Multiple Variables

# %% Example
x, y, z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)


# One Value to Multiple Variables

# %% Example
x = y = z = "Orange"
print(x)
print(y)
print(z)


# Unpack a Collection

# %% Example
# Unpack a list:
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

# endregion


# region Output Variables

# Output Variables

# %% Example
x = "awesome"
print("Python is " + x)

# %% Example
x = "Python is "
y = "awesome"
z = x + y
print(z)

# %% Example
x = 5
y = 10
print(x + y)

# endregion


# region Global Variables

# Global Variables

# %% Example
x = "awesome"

def myfunc():
    print("Python is " + x)

myfunc()

# %% Example
x = "awesome"

def myfunc():
    x = "fantastic"
    print("Python is " + x)

myfunc()

print("Python is " + x)


# The global Keyword

# %% Example
def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)

# %% Example
x = "awesome"

def myfunc():
    global x
    x = "fantastic"

myfunc()

print("Python is " + x)

# endregion
