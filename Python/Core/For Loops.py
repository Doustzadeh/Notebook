# region For Loops

# ---------------------------------------------------------
# For Loops

# %% Example
# Print each fruit in a fruit list:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
# Out: apple
#      banana
#      cherry


# ---------------------------------------------------------
# Looping Through a String

# %% Example
# Loop through the letters in the word "banana":
for x in "banana":
    print(x)
# Out: b
#      a
#      n
#      a
#      n
#      a


# ---------------------------------------------------------
# The break Statement

# %% Example
# Exit the loop when x is "banana":
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break
# Out: apple
#      banana

# %% Example
# Exit the loop when x is "banana", but this time the break comes before the print:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)
# Out: apple

# endregion
