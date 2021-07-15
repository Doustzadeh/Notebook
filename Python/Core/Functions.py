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

# endregion
