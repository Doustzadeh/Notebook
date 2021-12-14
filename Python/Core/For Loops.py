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


# ---------------------------------------------------------
# The continue Statement

# %% Example
# Do not print banana:
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)
# Out: apple
#      cherry


# ---------------------------------------------------------
# The range() Function

# %% Example
# Using the range() function:
for x in range(6):
    print(x)
# Out: 0
#      1
#      2
#      3
#      4
#      5

# %% Example
# Using the start parameter:
for x in range(2, 6):
    print(x)
# Out: 2
#      3
#      4
#      5

# %% Example
# Increment the sequence with 3 (default is 1):
for x in range(2, 30, 3):
    print(x)
# Out: 2
#      5
#      8
#      11
#      14
#      17
#      20
#      23
#      26
#      29


# ---------------------------------------------------------
# Else in For Loop

# %% Example
# Print all numbers from 0 to 5, and print a message when the loop has ended:
for x in range(6):
    print(x)
else:
    print("Finally finished!")
# Out: 0
#      1
#      2
#      3
#      4
#      5
#      Finally finished!

# Note: The else block will NOT be executed if the loop is stopped by a break statement.

# %% Example
# Break the loop when x is 3, and see what happens with the else block:
for x in range(6):
    if x == 3: break
    print(x)
else:
     print("Finally finished!")
# Out: 0
#      1
#      2


# ---------------------------------------------------------
# Nested Loops

# %% Example
# Print each adjective for every fruit:
adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]
for x in adj:
    for y in fruits:
        print(x, y)
# Out: red apple
#      red banana
#      red cherry
#      big apple
#      big banana
#      big cherry
#      tasty apple
#      tasty banana
#      tasty cherry


# ---------------------------------------------------------
# The pass Statement

# %% Example
for x in [0, 1, 2]:
    pass
# having an empty for loop like this, would raise an error without the pass statement.


# ---------------------------------------------------------

# %% Example
for number in range(3):
    print("Attempt", number + 1, (number + 1) * ".")
# Out: Attempt 1 .
#      Attempt 2 ..
#      Attempt 3 ...

for number in range(1, 4):
    print("Attempt", number, number * ".")
# Out: Attempt 1 .
#      Attempt 2 ..
#      Attempt 3 ...
for number in range(1, 10, 2):
    print("Attempt", number, number * ".")
# Out: Attempt 1 .
#      Attempt 3 ...
#      Attempt 5 .....
#      Attempt 7 .......
#      Attempt 9 .........

# endregion
