# region Functions

# ---------------------------------------------------------
# Creating a Function

# %% Example
def my_function():
    print("Hello from a function")


# ---------------------------------------------------------
# Calling a Function

# %% Example
def my_function():
    print("Hello from a function")
my_function()
# Out: Hello from a function


# ---------------------------------------------------------
# Arguments

# %% Example
def my_function(fname):
    print(fname + " Refsnes")
my_function("Emil")
my_function("Tobias")
my_function("Linus")
# Out: Emil Refsnes
#      Tobias Refsnes
#      Linus Refsnes


# ---------------------------------------------------------
# Number of Arguments

# %% Example
# This function expects 2 arguments, and gets 2 arguments:
def my_function(fname, lname):
    print(fname + " " + lname)
my_function("Emil", "Refsnes")
# Out: Emil Refsnes

# %% Example
# This function expects 2 arguments, but gets only 1:
def my_function(fname, lname):
    print(fname + " " + lname)
my_function("Emil")
# Out: TypeError: my_function() missing 1 required positional argument: 'lname'


# ---------------------------------------------------------
# Arbitrary Arguments, *args

# %% Example
# If the number of arguments is unknown, add a * before the parameter name:
def my_function(*kids):
    print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")
# Out: The youngest child is Linus


# ---------------------------------------------------------
# Keyword Arguments

# %% Example
def my_function(child3, child2, child1):
    print("The youngest child is " + child3)
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
# Out: The youngest child is Linus


# ---------------------------------------------------------
# Arbitrary Keyword Arguments, **kwargs

# %% Example
# If the number of keyword arguments is unknown, add a double ** before the parameter name:
def my_function(**kid):
    print("His last name is " + kid["lname"])
my_function(fname = "Tobias", lname = "Refsnes")
# Out: His last name is Refsnes


# ---------------------------------------------------------
# Default Parameter Value

# %% Example
def my_function(country = "Norway"):
    print("I am from " + country)
my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")
# Out: I am from Sweden
#      I am from India
#      I am from Norway
#      I am from Brazil


# ---------------------------------------------------------
# Passing a List as an Argument

# %% Example
def my_function(food):
    for x in food:
        print(x)
fruits = ["apple", "banana", "cherry"]
my_function(fruits)
# Out: apple
#      banana
#      cherry


# ---------------------------------------------------------
# Return Values

# %% Example
def my_function(x):
    return 5 * x
print(my_function(3))
print(my_function(5))
print(my_function(9))
# Out: 15
#      25
#      45


# ---------------------------------------------------------
# The pass Statement

# %% Example
def myfunction():
    pass


# ---------------------------------------------------------
# Recursion

# %% Example
# Recursion Example
def tri_recursion(k):
    if(k > 0):
        result = k + tri_recursion(k - 1)
        print(result)
    else:
        result = 0
    return result
print("\n\nRecursion Example Results")
tri_recursion(6)
# Out: 
# 
# 
#      Recursion Example Results
#      1
#      3
#      6
#      10
#      15
#      21
# 
#      21

# endregion
