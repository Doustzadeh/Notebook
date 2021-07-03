# region Strings

# Strings

# %% Example
print("Hello")
print('Hello')


# Assign String to a Variable

# %% Example
a = "Hello"
print(a)


# Multiline Strings

# %% Example
a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

# %% Example
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)


# Strings are Arrays

# %% Example
a = "Hello, World!"
print(a[1])


# Looping Through a String

# %% Example
for x in "banana":
    print(x)


# String Length

# %% Example
a = "Hello, World!"
print(len(a))


# Check String

# %% Example
txt = "The best things in life are free!"
print("free" in txt)

# %% Example
txt = "The best things in life are free!"
if "free" in txt:
    print("Yes, 'free' is present.")


# Check if NOT

# %% Example
txt = "The best things in life are free!"
print("expensive" not in txt)

# %% Example
txt = "The best things in life are free!"
if "expensive" not in txt:
    print("Yes, 'expensive' is NOT present.")

# endregion


# region Slicing Strings

# Slicing

# %% Example
b = "Hello, World!"
print(b[2:5])


# Slice From the Start

# %% Example
b = "Hello, World!"
print(b[:5])


# Slice To the End

# %% Example
b = "Hello, World!"
print(b[2:])


# Negative Indexing

# %% Example
b = "Hello, World!"
print(b[-5:-2])

# endregion


# region Modify Strings

# Upper Case

# %% Example
# The upper() method returns the string in upper case:
a = "Hello, World!"
print(a.upper())


# Lower Case

# %% Example
# The lower() method returns the string in lower case:
a = "Hello, World!"
print(a.lower())


# Remove Whitespace

# %% Example
# The strip() method removes any whitespace from the beginning or the end:
a = " Hello, World! "
print(a.strip()) # returns "Hello, World!"


# Replace String

# %% Example
# The replace() method replaces a string with another string:
a = "Hello, World!"
print(a.replace("H", "J"))


# Split String

# %% Example
# The split() method splits the string into substrings if it finds instances of the separator:
a = "Hello, World!"
print(a.split(",")) # returns ['Hello', ' World!']

# endregion


# region String Concatenation

# String Concatenation

# %% Example
a = "Hello"
b = "World"
c = a + b
print(c)

# %% Example
a = "Hello"
b = "World"
c = a + " " + b
print(c)

# endregion


# region Format - Strings

# String Format

# %% Example
age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))

# %% Example
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

# %% Example
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))

# endregion


# region Escape Characters

# Escape Characters

# %% Example
# The escape character allows you to use double quotes when you normally would not be allowed:
txt = "We are the so-called \"Vikings\" from the north."

# %% Example
# Code: \' , Result: Single Quote
txt = 'It\'s alright.'
print(txt)

# %% Example
# Code: \b , Result: Backslash
txt = "This will insert one \\ (backslash)."
print(txt)

# %% Example
# Code: \n , Result: New Line
txt = "Hello\nWorld!"
print(txt)

# %% Example
# Code: \r , Result: Carriage Return
txt = "Hello\rWorld!"
print(txt) 

# %% Example
# Code: \t , Result: Tab
txt = "Hello\tWorld!"
print(txt)

# %% Example
# Code: \b , Result: Backspace
# This example erases one character (backspace):
txt = "Hello \bWorld!"
print(txt)

# %% Example
# Code: \f , Result: Form Feed

# %% Example
# Code: \ooo , Result: Octal value
# A backslash followed by three integers will result in a octal value:
txt = "\110\145\154\154\157"
print(txt)

# %% Example
# Code: \xhh , Result: Hex value
# A backslash followed by an 'x' and a hex number represents a hex value:
txt = "\x48\x65\x6c\x6c\x6f"
print(txt) 

# endregion
