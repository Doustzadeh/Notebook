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

# endregion
