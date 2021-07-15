# region Lambda

# ---------------------------------------------------------
# Syntax

# %% Example
# Add 10 to argument a, and return the result:
x = lambda a : a + 10
print(x(5))
# Out: 15

# %% Example
# Multiply argument a with argument b and return the result:
x = lambda a, b : a * b
print(x(5, 6))
# Out: 30

# %% Example
# Summarize argument a, b, and c and return the result:
x = lambda a, b, c : a + b + c
print(x(5, 6, 2))
# Out: 13

# %% Example
def myfunc(n):
    return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))
# Out: 22

# %% Example
def myfunc(n):
    return lambda a : a * n
mytripler = myfunc(3)
print(mytripler(11))
# Out: 33

# %% Example
def myfunc(n):
    return lambda a : a * n
mydoubler = myfunc(2)
mytripler = myfunc(3)
print(mydoubler(11))
# Out: 22
print(mytripler(11))
# Out: 33

# endregion
