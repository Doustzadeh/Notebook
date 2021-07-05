# region Booleans

# Booleans represent one of two values: True or False.

# Boolean Values

# %% Example
print(10 > 9)
# Out: True
print(10 == 9)
# Out: False
print(10 < 9)
# Out: False

# %% Example
# Print a message based on whether the condition is True or False:
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")
# Out: b is not greater than a


# Evaluate Values and Variables

# %% Example
# Evaluate a string and a number:
print(bool("Hello"))
# Out: True
print(bool(15))
# Out: True

# %% Example
# Evaluate two variables:
x = "Hello"
y = 15

print(bool(x))
# Out: True
print(bool(y))
# Out: True


# Most Values are True
# Almost any value is evaluated to True if it has some sort of content.
# Any string is True, except empty strings.
# Any number is True, except 0.
# Any list, tuple, set, and dictionary are True, except empty ones.

# %% Example
# The following will return True:
print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))
# Out: True


# Some Values are False

# %% Example
# The following will return False:
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
# Out: False

# %% Example
class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))
# Out: False


# Functions can Return a Boolean

# %% Example
# Print the answer of a function:
def myFunction() :
  return True

print(myFunction())
# Out: True

# %% Example
# Print "YES!" if the function returns True, otherwise print "NO!":
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")
# Out: YES!

# %% Example
# Check if an object is an integer or not:
x = 200
print(isinstance(x, int))
# Out: True

# endregion
