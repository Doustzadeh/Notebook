# region Iterators

# An iterator is an object that contains a countable number of values.
# Technically, in Python, an iterator is an object which implements the iterator protocol, 
# which consist of the methods __iter__() and __next__().


# ---------------------------------------------------------
# Iterator vs Iterable
# Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.

# %% Example
# Return an iterator from a tuple, and print each value:
mytuple = ("apple", "banana", "cherry")
myit = iter(mytuple)

print(next(myit))
# Out: apple
print(next(myit))
# Out: banana
print(next(myit))
# Out: cherry

# %% Example
# Strings are also iterable objects, containing a sequence of characters:
mystr = "banana"
myit = iter(mystr)

print(next(myit))
# Out: b
print(next(myit))
# Out: a
print(next(myit))
# Out: n
print(next(myit))
# Out: a
print(next(myit))
# Out: n
print(next(myit))
# Out: a


# ---------------------------------------------------------
# Looping Through an Iterator

# %% Example
# Iterate the values of a tuple:
mytuple = ("apple", "banana", "cherry")

for x in mytuple:
    print(x)
# Out: apple
#      banana
#      cherry

# %% Example
# Iterate the characters of a string:
mystr = "banana"

for x in mystr:
    print(x)
# Out: b
#      a
#      n
#      a
#      n
#      a


# ---------------------------------------------------------
# Create an Iterator

# %% Example
# Create an iterator that returns numbers, starting with 1, and each sequence will increase by one (returning 1,2,3,4,5 etc.):
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

myclass = MyNumbers()
myiter = iter(myclass)

print(next(myiter))
# Out: 1
print(next(myiter))
# Out: 2
print(next(myiter))
# Out: 3
print(next(myiter))
# Out: 4
print(next(myiter))
# Out: 5


# ---------------------------------------------------------
# StopIteration

# %% Example
# Stop after 20 iterations:
class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        if self.a <= 20:
            x = self.a
            self.a += 1
            return x
        else:
            raise StopIteration

myclass = MyNumbers()
myiter = iter(myclass)

for x in myiter:
    print(x)
# Out: 1
#      2
#      3
#      ....
#      18
#      19
#      20

# endregion
