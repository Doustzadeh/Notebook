# region Dictionaries

# ---------------------------------------------------------
# Dictionary
# Dictionaries are used to store data values in key:value pairs.

# %% Example
# Create and print a dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)
# Out: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}


# ---------------------------------------------------------
# Dictionary Items

# %% Example
# Print the "brand" value of the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
# Out: Ford


# ---------------------------------------------------------
# Duplicates Not Allowed

# %% Example
# Duplicate values will overwrite existing values:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)
# Out: {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}


# ---------------------------------------------------------
# Dictionary Length

# %% Example
# Print the number of items in the dictionary:
print(len(thisdict))
# Out: 3


# ---------------------------------------------------------
# Dictionary Items - Data Types

# %% Example
# String, int, boolean, and list data types:
thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}


# ---------------------------------------------------------
# type()

# %% Example
# Print the data type of a dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))
# Out: <class 'dict'>

# endregion
