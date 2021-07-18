# region Classes and Objects

# ---------------------------------------------------------
# Create a Class

# %% Example
# Create a class named MyClass, with a property named x:
class MyClass:
    x = 5
print(MyClass)
# Out: <class '__main__.MyClass'>


# ---------------------------------------------------------
# Create Object

# %% Example
# Create an object named p1, and print the value of x:
class MyClass:
    x = 5
p1 = MyClass()
print(p1.x)
# Out: 5


# ---------------------------------------------------------
# The __init__() Function

# %% Example
# Create a class named Person, use the __init__() function to assign values for name and age:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)
print(p1.name)
# Out: John
print(p1.age)
# Out: 36

# Note: The __init__() function is called automatically every time the class is being used to create a new object.

# ---------------------------------------------------------
# Object Methods

# %% Example
# Insert a function that prints a greeting, and execute it on the p1 object:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()
# Out: Hello my name is John

# Note: The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.


# ---------------------------------------------------------
# The self Parameter

# %% Example
# Use the words mysillyobject and abc instead of self:
class Person:
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age

    def myfunc(abc):
        print("Hello my name is " + abc.name)

p1 = Person("John", 36)
p1.myfunc()
# Out: Hello my name is John


# ---------------------------------------------------------
# Modify Object Properties

# %% Example
# Set the age of p1 to 40:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)
p1.age = 40
print(p1.age)
# Out: 40


# ---------------------------------------------------------
# Delete Object Properties

# %% Example
# Delete the age property from the p1 object:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)
del p1.age
print(p1.age)
# Out: AttributeError: 'Person' object has no attribute 'age'


# ---------------------------------------------------------
# Delete Objects

# %% Example
# Delete the p1 object:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("John", 36)
del p1
print(p1)
# Out: NameError: name 'p1' is not defined


# ---------------------------------------------------------
# The pass Statement

# %% Example
class Person:
    pass
# having an empty class definition like this, would raise an error without the pass statement

# endregion
