# region Modules

# ---------------------------------------------------------
# Use a Module

# %% Example
# Import the module named mymodule, and call the greeting function:
import mymodule
mymodule.greeting("Jonathan")
# Out: Hello, Jonathan


# ---------------------------------------------------------
# Variables in Module

# %% Example
# Import the module named mymodule, and access the person1 dictionary:
import mymodule
a = mymodule.person1["age"]
print(a)
# Out: 36

# endregion
