# region If ... Else

# ---------------------------------------------------------
# Conditions and If statements

# %% Example
# If statement:
a = 33
b = 200
if b > a:
    print("b is greater than a")
# Out: b is greater than a


# ---------------------------------------------------------
# Indentation

# %% Example
# If statement, without indentation (will raise an error):
a = 33
b = 200
if b > a:
print("b is greater than a") # you will get an error
# Out: IndentationError: expected an indented block


# ---------------------------------------------------------
# Elif

# %% Example
a = 33
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
# Out: a and b are equal


# ---------------------------------------------------------
# Else

# %% Example
a = 200
b = 33
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")
# Out: a is greater than b

# %% Example
a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")
# Out: b is not greater than a


# ---------------------------------------------------------
# Short Hand If

# %% Example
# One line if statement:
a = 200
b = 33
if a > b: print("a is greater than b")
# Out: a is greater than b


# ---------------------------------------------------------
# Short Hand If ... Else

# %% Example
# One line if else statement:
a = 2
b = 330
print("A") if a > b else print("B")
# Out: B

# %% Example
# One line if else statement, with 3 conditions:
a = 330
b = 330
print("A") if a > b else print("=") if a == b else print("B")
# Out: =


# ---------------------------------------------------------
# And

# %% Example
# Test if a is greater than b, AND if c is greater than a:
a = 200
b = 33
c = 500
if a > b and c > a:
    print("Both conditions are True")
# Out: Both conditions are True

# ---------------------------------------------------------
# Or

# %% Example
# Test if a is greater than b, OR if a is greater than c:
a = 200
b = 33
c = 500
if a > b or a > c:
    print("At least one of the conditions is True")
# Out: t least one of the conditions is True


# ---------------------------------------------------------
# Nested If

# %% Example
x = 41
if x > 10:
    print("Above ten,")
    if x > 20:
        print("and also above 20!")
    else:
        print("but not above 20.")
# Out: Above ten,
#      and also above 20!


# ---------------------------------------------------------
# The pass Statement

# %% Example
a = 33
b = 200
if b > a:
    pass

# endregion
