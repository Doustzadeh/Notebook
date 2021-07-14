# region While Loops

# ---------------------------------------------------------
# Loops

# %% Example
# Print i as long as i is less than 6:
i = 1
while i < 6:
    print(i)
    i += 1
# Out: 1
#      2
#      3
#      4
#      5


# ---------------------------------------------------------
# The break Statement

# %% Example
# Exit the loop when i is 3:
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1
# Out: 1
#      2
#      3


# ---------------------------------------------------------
# The continue Statement

# %% Example
# Continue to the next iteration if i is 3:
i = 0
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)
# Out: 1
#      2
#      4
#      5
#      6


# ---------------------------------------------------------
# The else Statement

# %% Example
# Print a message once the condition is false:
i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("i is no longer less than 6")
# Out: 1
#      2
#      3
#      4
#      5
#      i is no longer less than 6

# endregion
