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


# region Access Dictionary Items

# ---------------------------------------------------------
# Accessing Items

# %% Example
# Get the value of the "model" key:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict["model"]
print(x)
# Out: Mustang

# %% Example
# Get the value of the "model" key:
x = thisdict.get("model")
print(x)
# Out: Mustang


# ---------------------------------------------------------
# Get Keys

# %% Example
# Get a list of the keys:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.keys()
print(x)
# Out: dict_keys(['brand', 'model', 'year'])

# %% Example
# Add a new item to the original dictionary, and see that the keys list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.keys()
print(x) # before the change
# Out: dict_keys(['brand', 'model', 'year'])
car["color"] = "white"
print(x) # after the change
# Out: dict_keys(['brand', 'model', 'year', 'color'])


# ---------------------------------------------------------
# Get Values

# %% Example
# Get a list of the values:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.values()
print(x)
# Out: dict_values(['Ford', 'Mustang', 1964])

# %% Example
# Make a change in the original dictionary, and see that the values list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) # before the change
# Out: dict_values(['Ford', 'Mustang', 1964])
car["year"] = 2020
print(x) # after the change
# Out: dict_values(['Ford', 'Mustang', 2020])

# %% Example
# Add a new item to the original dictionary, and see that the values list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.values()
print(x) #before the change
# Out: dict_values(['Ford', 'Mustang', 1964])
car["color"] = "red"
print(x) #after the change
# Out: dict_values(['Ford', 'Mustang', 1964, 'red'])


# ---------------------------------------------------------
# Get Items

# %% Example
# Get a list of the key:value pairs
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
x = thisdict.items()
print(x)
# Out: dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])

# %% Example
# Make a change in the original dictionary, and see that the items list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
print(x) #before the change
# Out: dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
car["year"] = 2020
print(x) #after the change
# Out: dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 2020)])

# %% Example
# Add a new item to the original dictionary, and see that the items list gets updated as well:
car = {
"brand": "Ford",
"model": "Mustang",
"year": 1964
}
x = car.items()
print(x) #before the change
# Out: dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964)])
car["color"] = "red"
print(x) #after the change
# Out: dict_items([('brand', 'Ford'), ('model', 'Mustang'), ('year', 1964), ('color', 'red')])


# ---------------------------------------------------------
# Check if Key Exists

# %% Example
# Check if "model" is present in the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")
# Out: Yes, 'model' is one of the keys in the thisdict dictionary

# endregion


# region Change Dictionary Items

# ---------------------------------------------------------
# Change Values

# %% Example
# Change the "year" to 2018:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
print(thisdict)
# Out: {'brand': 'Ford', 'model': 'Mustang', 'year': 2018}


# ---------------------------------------------------------
# Update Dictionary

# %% Example
# Update the "year" of the car by using the update() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})
print(thisdict)
# Out: {'brand': 'Ford', 'model': 'Mustang', 'year': 2020}

# endregion
