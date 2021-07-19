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


# region Naming a Module

# ---------------------------------------------------------
# Re-naming a Module

# %% Example
# Create an alias for mymodule called mx:
import mymodule as mx
a = mx.person1["age"]
print(a)
# Out: 36


# ---------------------------------------------------------
# Built-in Modules

# %% Example
# Import and use the platform module:
import platform
x = platform.system()
print(x)
# Out: Windows


# ---------------------------------------------------------
# Import From Module

# %% Example
# Import only the person1 dictionary from the module:
from mymodule import person1
print (person1["age"])
# Out: 36

# endregion
