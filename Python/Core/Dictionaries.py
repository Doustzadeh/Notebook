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


# region Add Dictionary Items

# ---------------------------------------------------------
# Adding Items

# %% Example
# Adding an item to the dictionary is done by using a new index key and assigning a value to it:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["color"] = "red"
print(thisdict)
# Out: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}


# ---------------------------------------------------------
# Update Dictionary

# %% Example
# Add a color item to the dictionary by using the update() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"color": "red"})
print(thisdict)
# Out: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964, 'color': 'red'}

# endregion


# region Remove Dictionary Items

# ---------------------------------------------------------
# Removing Items

# %% Example
# The pop() method removes the item with the specified key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)
# Out: {'brand': 'Ford', 'year': 1964}

# %% Example
# The popitem() method removes the last inserted item (in versions before 3.7, a random item is removed instead):
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)
# Out: {'brand': 'Ford', 'model': 'Mustang'}

# %% Example
# The del keyword removes the item with the specified key name:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)
# Out: {'brand': 'Ford', 'year': 1964}

# %% Example
# The del keyword can also delete the dictionary completely:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict
print(thisdict) #this will cause an error because "thisdict" no longer exists.
# Out: NameError: name 'thisdict' is not defined

# %% Example
# The clear() method empties the dictionary:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)
# Out: {}

# endregion


# region Loop Dictionaries

# ---------------------------------------------------------
# Loop Through a Dictionary

# %% Example
# Print all key names in the dictionary, one by one:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
    print(x)
# Out: brand
#      model
#      year

# %% Example
# Print all values in the dictionary, one by one:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict:
    print(thisdict[x])
# Out: Ford
#      Mustang
#      1964

# %% Example
# You can also use the values() method to return values of a dictionary:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.values():
   print(x)
# Out: Ford
#      Mustang
#      1964

# %% Example
# You can use the keys() method to return the keys of a dictionary:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x in thisdict.keys():
    print(x)
# Out: brand
#      model
#      year

# %% Example
# Loop through both keys and values, by using the items() method:
thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
    print(x, y)
# Out: brand Ford
#      model Mustang
#      year 1964

# endregion


# region Copy Dictionaries

# ---------------------------------------------------------
# Copy a Dictionary

# %% Example
# Make a copy of a dictionary with the copy() method:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)
# Out: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

# %% Example
# Make a copy of a dictionary with the dict() function:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)
# Out: {'brand': 'Ford', 'model': 'Mustang', 'year': 1964}

# endregion


# region Nested Dictionaries

# ---------------------------------------------------------
# Nested Dictionaries

# %% Example
# Create a dictionary that contain three dictionaries:
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
print(myfamily)
# Out: {'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}

# %% Example
# Create three dictionaries, then create one dictionary that will contain the other three dictionaries:
child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}
myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print(myfamily)
# Out: {'child1': {'name': 'Emil', 'year': 2004}, 'child2': {'name': 'Tobias', 'year': 2007}, 'child3': {'name': 'Linus', 'year': 2011}}

# endregion
