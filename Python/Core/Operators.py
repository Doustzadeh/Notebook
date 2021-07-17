# region Operators

# ---------------------------------------------------------
# Arithmetic Operators
# Arithmetic operators are used with numeric values to perform common mathematical operations:

# %% Example
x = 5
y = 3
print(x + y)
# Out: 8

# %% Example
x = 5
y = 3
print(x - y)
# Out: 2

# %% Example
x = 5
y = 3
print(x * y) 
# Out: 15

# %% Example
x = 12
y = 3
print(x / y)
# Out: 4.0

# %% Example
x = 5
y = 2
print(x % y)
# Out: 1

# %% Example
x = 2
y = 5
print(x ** y) #same as 2*2*2*2*2
# Out: 32

# %% Example
x = 15
y = 2
print(x // y)
# Out: 7


# ---------------------------------------------------------
# Assignment Operators
# Assignment operators are used to assign values to variables:

# %% Example
x = 5
print(x)
# Out: 5

# %% Example
x = 5
x += 3
print(x)
# Out: 8

# %% Example
x = 5
x -= 3
print(x)
# Out: 2

# %% Example
x = 5
x *= 3
print(x)
# Out: 15

# %% Example
x = 5
x /= 3
print(x)
# Out: 1.6666666666666667

# %% Example
x = 5
x%=3
print(x)
# Out: 2

# %% Example
x = 5
x//=3
print(x)
# Out: 1

# %% Example
x = 5
x **= 3
print(x)
# Out: 125

# %% Example
x = 5
x &= 3
print(x)
# Out: 1

# %% Example
x = 5
x |= 3
print(x)
# Out: 7

# %% Example
x = 5
x ^= 3
print(x)
# Out: 6

# %% Example
x = 5
x >>= 3
print(x)
# Out: 0

# %% Example
x = 5
x <<= 3
print(x)
# Out: 40


# ---------------------------------------------------------
# Comparison Operators
# Comparison operators are used to compare two values:

# %% Example
x = 5
y = 3
print(x == y)
# Out: False

# %% Example
x = 5
y = 3
print(x != y)
# Out: True

# %% Example
x = 5
y = 3
print(x > y)
# Out: True

# %% Example
x = 5
y = 3
print(x < y)
# Out: False

# %% Example
x = 5
y = 3
print(x >= y)
# Out: True

# %% Example
x = 5
y = 3
print(x <= y)
# Out: False


# ---------------------------------------------------------
# Logical Operators
# Logical operators are used to combine conditional statements:

# %% Example
x = 5
print(x > 3 and x < 10)
# Out: True

# %% Example
x = 5
print(x > 3 or x < 4)
# Out: True

# %% Example
x = 5
print(not(x > 3 and x < 10))
# Out: False


# ---------------------------------------------------------
# Identity Operators
# Identity operators are used to compare the objects, # not if they are equal, 
# but if they are actually the same object, # with the same memory location:

# %% Example
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
# Out: True
print(x is y)
# Out: False
print(x == y)
# Out: True

# %% Example
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z)
# Out: False
print(x is not y)
# Out: True
print(x != y)
# Out: False


# ---------------------------------------------------------
# Membership Operators
# Membership operators are used to test if a sequence is presented in an object:

# %% Example
# Returns True if a sequence with the specified value is present in the object
x = ["apple", "banana"]
print("banana" in x)
# Out: True

# %% Example
# Returns True if a sequence with the specified value is not present in the object
x = ["apple", "banana"]
print("pineapple" not in x)
# Out: True


# ---------------------------------------------------------
# Bitwise Operators
# Bitwise operators are used to compare (binary) numbers:
# Operator	Name	                Description
# & 	    AND	                    Sets each bit to 1 if both bits are 1
# |	        OR	                    Sets each bit to 1 if one of two bits is 1
# ^	        XOR	                    Sets each bit to 1 if only one of two bits is 1
# ~ 	    NOT	                    Inverts all the bits
# <<	    Zero fill left shift	Shift left by pushing zeros in from the right and let the leftmost bits fall off
# >>	    Signed right shift	    Shift right by pushing copies of the leftmost bit in from the left, and let the rightmost bits fall off

# endregion
